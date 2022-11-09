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
    ] = "https://miro.com/app/board/uXjVO8VCjGA=/"

    DATASPACE_BASE_DOMAIN: str = "testbed.fi"
    AUTHENTICATION_PROVIDER_URL: HttpUrl = "https://login.testbed.fi"
    CONSENT_PROVIDER_URL: HttpUrl = "https://consent.testbed.fi"
    WEBSITE_URL: HttpUrl = "https://testbed.fi"
    DATASPACE_DOCS_URL: HttpUrl = "https://docs.testbed.fi"
    DEFINITIONS_VIEWER_URL: HttpUrl = "https://definitions.testbed.fi"
    DEVELOPER_PORTAL_URL: HttpUrl = "https://developer.testbed.fi"
    PRODUCT_GATEWAY_URL: HttpUrl = "https://gateway.testbed.fi"
    DEFINITIONS_GIT_URL: HttpUrl = (
        "https://github.com/Virtual-Finland/definitions.git"
    )
    DEFINITIONS_WEB_URL: HttpUrl = (
        "https://github.com/Virtual-Finland/definitions"
    )


conf = Settings()
