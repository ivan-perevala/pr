from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    "image/svg+xml",
    "image/gif",
    "image/png",
    "image/jpeg",
]

html_theme = "sphinx_rtd_theme"
html_logo = "bhq_logo_color_v1.svg"
html_theme_options = {
    "display_version": True,
    "style_external_links": True,
}
