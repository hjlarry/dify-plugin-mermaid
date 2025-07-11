## Mermaid Converter

**Author:** hjlarry  
**Version:** 0.0.1  
**Type:** tool  
**Repo:** https://github.com/hjlarry/dify-plugin-mermaid

### Description

A Dify plugin that converts Mermaid diagram code to images in multiple formats (PNG, JPG, PDF, SVG) using the mermaid.ink API service. This plugin enables users to generate visual diagrams programmatically within Dify workflows and agent interactions.

### Features

- **Multiple Output Formats**: Supports PNG, JPG, SVG, and PDF formats
- **Theme Support**: Choose from default, dark, neutral, or forest themes
- **Customization Options**: Configure background colors, image dimensions
- **Error Handling**: Graceful handling of invalid syntax and API failures
- **No API Key Required**: Uses the free mermaid.ink public service

### Supported Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `mermaid_code` | string | Yes | - | The Mermaid diagram syntax code |
| `output_format` | select | No | png | Output format: png, jpg, svg, pdf |
| `theme` | select | No | default | Visual theme: default, dark, neutral, forest |
| `background_color` | string | No | transparent | Background color (hex code or named color) |
| `width` | number | No | - | Image width in pixels |
| `height` | number | No | - | Image height in pixels |

### Usage Examples

The converter config:
![1](./_assets/1.png)

Here I create a workflow and ask the LLM to generate a git common operation mindmap by mermaid code:

![2](./_assets/2.png)

The final result:
![3](./_assets/3.png)

### Troubleshooting

#### Common Issues

1. **"Invalid Mermaid syntax"**
   - Check your Mermaid code syntax using [Mermaid Live Editor](https://mermaid.live/)
   - Ensure proper line breaks and spacing in diagram code

2. **"Conversion timeout"**
   - Simplify complex diagrams
   - Check network connectivity
   - Try again as the service may be temporarily slow

3. **"Diagram too large"**
   - Reduce the complexity of your diagram
   - Split large diagrams into smaller components

4. **Empty or corrupted output**
   - Verify Mermaid syntax is correct
   - Check if all required parameters are provided
   - Try with a simpler diagram first

### Limitations

- Maximum diagram size limited by mermaid.ink API
- Dependent on external service availability
- Some advanced Mermaid features may not be supported
- Internet connectivity required



