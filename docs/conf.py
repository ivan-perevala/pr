from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    "image/svg+xml",
    "image/gif",
    "image/png",
    "image/jpeg",
]

project = u'PR PR PR PR PR PR PR PR PR PR'
copyright = '2020, BHQ'
author = 'BHQ'

release = '0.1'
version = '0.1.0'

source_suffix = '.rst'
master_doc = 'index'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

html_theme = "sphinx_rtd_theme"
html_logo = "bhq_logo_color_v1.svg"
html_show_sourcelink = True
html_templates_path = ["_templates"]
html_theme_options = {
    'logo_only': True,
    "display_version": False,
    'navigation_depth': 5,
}
