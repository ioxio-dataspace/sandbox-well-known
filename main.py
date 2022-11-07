import importlib.util
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import typer
from dataclasses_json import dataclass_json
from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration
from pydantic import BaseModel
from stringcase import spinalcase

from settings import conf

app = typer.Typer()


def get_schema_path(src_path: Path) -> Path:
    """
    Get the path to the JSON Schema file corresponding to the given Python source file.

    :param src_path: The path to the source Python file.
    :return: The Path to the JSON schema file.
    """
    relative_path = src_path.relative_to(conf.SRC_PATH)
    path = conf.SCHEMAS_PATH / relative_path
    path = path.with_stem(spinalcase(path.stem)).with_suffix(".json")
    return path


@app.command()
def convert_src_to_json_schema() -> None:
    """
    Convert Python/Pydantic source files to JSON Schema files.

    :return:
    """
    python_files = (
        py_file
        for py_file in conf.SRC_PATH.glob("*.py")
        if not (py_file.name.startswith("__") and py_file.name.endswith("__.py"))
    )
    for p in python_files:
        spec = importlib.util.spec_from_file_location(name=str(p), location=str(p))
        if not spec.loader:
            raise RuntimeError(f"Failed to import {p} module")

        module = spec.loader.load_module(str(p))
        root: BaseModel = getattr(module, "ROOT")
        if not root:
            raise ValueError(f"Error finding ROOT variable in {p}")

        json_schema = root.schema_json(indent=2)
        schema_file = get_schema_path(p)
        schema_file.write_text(json_schema)


@dataclass_json
@dataclass
class CustomGenerationConfiguration(GenerationConfiguration):
    """
    Custom version of the GenerationConfiguration that allows specifying extra files to
    copy from the template to the destination and adding a documentation hub URL.
    """

    documentation_hub_url: Optional[str] = None
    extra_files_to_copy: Optional[List[str]] = None

    @property
    def files_to_copy(self) -> List[str]:
        files = super().files_to_copy
        return [*files, *self.extra_files_to_copy]


@app.command()
def convert_json_schema_to_html() -> None:
    """
    Convert JSON Schema files to HTML.

    :return:
    """
    config = CustomGenerationConfiguration(
        collapse_long_examples=False,
        expand_buttons=True,
        footer_show_time=False,
        with_footer=True,
        custom_template_path=conf.TEMPLATE_PATH,
        documentation_hub_url=conf.DOCUMENTATION_HUB_URL,
        extra_files_to_copy=[
            "bootstrap-4.3.1.min.css",
            "bootstrap-4.3.1.min.js",
            "jquery-3.4.1.min.js",
        ],
    )

    for schema_file in conf.SCHEMAS_PATH.glob("*.json"):
        generate_from_filename(schema_file, conf.HTML_PATH, config=config)


@app.command()
def convert_src_to_html() -> None:
    """
    Convert Python/Pydantic source files first to JSON Schema and then those to HTML.

    :return:
    """
    convert_src_to_json_schema()
    convert_json_schema_to_html()


if __name__ == "__main__":
    app()
