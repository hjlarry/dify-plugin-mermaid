import base64
import logging
from collections.abc import Generator
from typing import Any
from urllib.parse import urlencode

import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.config.logger_format import plugin_logger_handler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(plugin_logger_handler)


class MermaidConverterTool(Tool):
    def _invoke(
        self, tool_parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        """
        Invoke the tool to convert Mermaid code to an image.
        """
        logger.info(f"Invoking MermaidConverterTool with parameters: {tool_parameters}")
        mermaid_code = tool_parameters.get("mermaid_code")
        if not mermaid_code:
            yield self.create_text_message("No Mermaid code provided.")
            return

        output_format = tool_parameters.get("format", "png")
        theme = tool_parameters.get("theme")
        bg_color = tool_parameters.get("bg_color")

        try:
            # 1. Base64 encode the mermaid code
            encoded_mermaid_code = base64.b64encode(
                mermaid_code.encode("utf-8")
            ).decode("utf-8")

            # 2. Construct the URL for mermaid.ink
            format_path = "img"
            if output_format == "svg":
                format_path = "svg"
            elif output_format == "pdf":
                format_path = "pdf"
            base_url = f"https://mermaid.ink/{format_path}/{encoded_mermaid_code}"
            params = {}
            if theme:
                params["theme"] = theme
            if bg_color:
                params["bg"] = bg_color

            if params:
                base_url += "?" + urlencode(params)

            logger.info(f"Constructed mermaid.ink URL: {base_url}")

            # 3. Fetch the image
            response = requests.get(base_url)
            response.raise_for_status()  # Raise an exception for bad status codes

            image_bytes = response.content

            # 4. Return the generated image file
            mime_type = "image/png"
            if output_format == "svg":
                mime_type = "image/svg+xml"
            elif output_format == "pdf":
                mime_type = "application/pdf"
            yield self.create_blob_message(
                blob=image_bytes, meta={"mime_type": mime_type}
            )

        except requests.RequestException as e:
            logger.error(f"Failed to fetch image from mermaid.ink: {e}", exc_info=True)
            yield self.create_text_message(
                f"Failed to fetch image from mermaid.ink: {e}"
            )
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}", exc_info=True)
            yield self.create_text_message(f"An error occurred: {e}")
