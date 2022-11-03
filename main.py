from pathlib import Path

import typer
from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

from src.consent_configuration import ConsentConfiguration
from src.dataspace_configuration import DataspaceConfiguration

app = typer.Typer()


@app.command()
def convert_src_to_json_schema():
    schemas_dir = Path("schemas")

    dataspace_configuration = DataspaceConfiguration.schema_json(indent=2)
    output = schemas_dir / "dataspace-configuration.json"
    output.write_text(dataspace_configuration)

    consent_configuration = ConsentConfiguration.schema_json(indent=2)
    output = schemas_dir / "consent-configuration.json"
    output.write_text(consent_configuration)


@app.command()
def convert_json_schema_to_html():
    schemas_dir = Path("schemas")
    html_dir = Path("html")

    config = GenerationConfiguration(
        collapse_long_examples=False,
        expand_buttons=True,
        footer_show_time=False,
        with_footer=True,
    )

    dataspace_file = schemas_dir / "dataspace-configuration.json"
    consent_file = schemas_dir / "consent-configuration.json"
    generate_from_filename(dataspace_file, html_dir, config=config)
    generate_from_filename(consent_file, html_dir, config=config)


@app.command()
def convert_src_to_html():
    convert_src_to_json_schema()
    convert_json_schema_to_html()


if __name__ == "__main__":
    app()
