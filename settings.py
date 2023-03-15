from pathlib import Path
from typing import List, Optional

from pydantic import BaseSettings, HttpUrl


class Settings(BaseSettings):
    SRC_PATH: Path = Path(__file__).parent / "src"
    SCHEMAS_PATH: Path = Path(__file__).parent / "schemas"
    HTML_PATH: Path = Path(__file__).parent / "html"
    TEMPLATE_PATH: Optional[Path] = (
        Path(__file__).parent / "templates" / "js" / "base.html"
    )
    EXTRA_TEMPLATE_FILES_TO_COPY: List[str] = [
        "bootstrap-4.3.1.min.css",
        "bootstrap-4.3.1.min.js",
        "favicon.ico",
        "jquery-3.4.1.min.js",
    ]

    DOCUMENTATION_HUB_URL: Optional[
        HttpUrl
    ] = "https://miro.com/app/board/uXjVO7VL5jc=/"

    DATASPACE_BASE_DOMAIN: str = "sandbox.ioxio-dataspace.com"
    AUTHENTICATION_PROVIDER_URL: HttpUrl = "https://login.sandbox.ioxio-dataspace.com"
    CONSENT_PROVIDER_URL: HttpUrl = "https://consent.sandbox.ioxio-dataspace.com"
    WEBSITE_URL: HttpUrl = "https://sandbox.ioxio-dataspace.com"
    DATASPACE_DOCS_URL: HttpUrl = "https://docs.sandbox.ioxio-dataspace.com"
    DEFINITIONS_VIEWER_URL: HttpUrl = "https://definitions.sandbox.ioxio-dataspace.com"
    DEVELOPER_PORTAL_URL: HttpUrl = "https://developer.sandbox.ioxio-dataspace.com"
    PRODUCT_GATEWAY_URL: HttpUrl = "https://gateway.sandbox.ioxio-dataspace.com"
    DEFINITIONS_GIT_URL: HttpUrl = (
        "https://github.com/ioxio-dataspace/sandbox-definitions.git"
    )
    DEFINITIONS_WEB_URL: HttpUrl = (
        "https://github.com/ioxio-dataspace/sandbox-definitions"
    )
    ACR_VALUES: str = "fake-auth"


conf = Settings()
