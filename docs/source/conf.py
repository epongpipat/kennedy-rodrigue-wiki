import datetime

# -- Project information

project = 'Kennedy-Rodrigue-Wiki'
copyright = '2022'
author = 'Pongpipat'

version = 'latest'
release = datetime.datetime.now().strftime('%Y-%m-%d')

# -- General configuration

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx_new_tab_link',
    'sphinx_copybutton',
    'sphinx_rtd_theme',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "colon_fence",
    "substitution",
]

import csv
import os

myst_substitutions = {}
_conf_dir = os.path.dirname(__file__)
_csv_path = os.path.join(_conf_dir, "abbreviations.csv")

if os.path.exists(_csv_path):
    with open(_csv_path, mode="r", encoding="utf-8") as _f:
        _reader = csv.DictReader(_f)
        for _row in _reader:
            _key = _row["Key"].strip()
            _term = _row["Term"].strip()
            _def = _row["Definition"].strip()
            myst_substitutions[_key] = f"{{abbr}}`{_term} ({_def})`"

myst_links_external_new_tab = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = ['**/._*', '._*']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

def generate_abbreviations_page(app):
    import csv
    import os

    conf_dir = app.srcdir
    csv_path = os.path.join(conf_dir, "abbreviations.csv")
    md_path = os.path.join(conf_dir, "abbreviations.md")

    if os.path.exists(csv_path):
        with open(csv_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Sort rows alphabetically by the Term column (case-insensitive)
        rows.sort(key=lambda r: r["Term"].strip().lower())

        # Generate the markdown table content
        content = [
            "(abbreviations)=",
            "",
            "# Abbreviations",
            "",
            "| Term | Definition |",
            "| --- | --- |",
        ]
        for row in rows:
            key = row["Key"].strip()
            term = row["Term"].strip()
            definition = row["Definition"].strip()
            content.append(f"| {{{{ {key} }}}} | {definition} |")

        content_str = "\n".join(content) + "\n"

        # Write to abbreviations.md
        os.makedirs(os.path.dirname(md_path), exist_ok=True)
        with open(md_path, mode="w", encoding="utf-8") as f:
            f.write(content_str)

def setup(app):
    app.connect("builder-inited", generate_abbreviations_page)

