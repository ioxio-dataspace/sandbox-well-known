# Documentation for .well-known endpoints on dataspaces

This repository is used to document the different .well-known URLs used on dataspaces
and to convert and host those as a human friendly web page.

## Structure

- [`./src/`](./src/) - Source files containing
  Python/[Pydantic](https://pydantic-docs.helpmanual.io/) models describing the
  different .well-known URLs and the data they contain.
- [`./schemas/`](./schemas/) - Intermediate JSON Schema files generated from the above
  by the tooling provided in this repo.
- [`./html/`](./html/) - Final static files generated by the tooling that are hosted
  using GitHub pages.
- [`./main.py`](./main.py) - The converter used to convert the source files to JSON
  Schema and HTML + CSS + JS.
- [`./.github/workflows/deploy.yaml`](./.github/workflows/deploy.yaml) - GitHub Action
  to build and deploy to GitHub Pages.

## Development

Generic pre-requisites for development

- [Pre-commit](https://pre-commit.com/#install)
- [Poetry](https://python-poetry.org/docs/#installation)

## Usage

These source files can be converted to HTML files by running:

```shell
poetry run python main.py convert-src-to-html
```
