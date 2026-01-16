# docs/conf.py

project = "Capybara"
author = "Capybara Project Authors"
copyright = "2026, Capybara Project Authors"

extensions = []

templates_path = ["_templates"]
exclude_patterns = []

import sphinx_rtd_theme
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
extensions = ['sphinx_rtd_theme']
html_theme = "sphinx_rtd_theme"
