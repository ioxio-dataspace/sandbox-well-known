from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    SRC_PATH: Path = Path(__file__).parent / "src"
    SCHEMAS_PATH: Path = Path(__file__).parent / "schemas"
    HTML_PATH: Path = Path(__file__).parent / "html"


conf = Settings()
