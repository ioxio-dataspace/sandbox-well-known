import typer
from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

from settings import conf
from src.consent_configuration import ConsentConfiguration
from src.dataspace_configuration import DataspaceConfiguration

app = typer.Typer()


@app.command()
def convert_src_to_json_schema():
    dataspace_configuration = DataspaceConfiguration.schema_json(indent=2)
    output = conf.SCHEMAS_PATH / "dataspace-configuration.json"
    output.write_text(dataspace_configuration)

    consent_configuration = ConsentConfiguration.schema_json(indent=2)
    output = conf.SCHEMAS_PATH / "consent-configuration.json"
    output.write_text(consent_configuration)


@app.command()
def convert_json_schema_to_html():
    config = GenerationConfiguration(
        collapse_long_examples=False,
        expand_buttons=True,
        footer_show_time=False,
        with_footer=True,
    )

    for schema_file in conf.SCHEMAS_PATH.glob("*.json"):
        generate_from_filename(schema_file, conf.HTML_PATH, config=config)


@app.command()
def convert_src_to_html():
    convert_src_to_json_schema()
    convert_json_schema_to_html()


if __name__ == "__main__":
    app()
