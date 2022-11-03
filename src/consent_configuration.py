from pydantic import BaseModel, Field, HttpUrl


class ConsentConfiguration(BaseModel):
    class Config:
        schema_extra = {
            "title": "/.well-known/dataspace/consent-configuration.json",
            "description": "Configuration details for a consent provider on a "
            "dataspace",
            "examples": [
                {
                    "issuer": "https://consent.testbed.fi",
                    "jwks_uri": "https://consent.testbed.fi/.well-known/jwks.json",
                    "consent_request_uri": "https://consent.testbed.fi/Consent/Request",
                }
            ],
        }

    issuer: HttpUrl = Field(
        ...,
        description="",
        examples=["https://consent.testbed.fi"],
    )

    jwks_uri: HttpUrl = Field(
        ...,
        description="",
        examples=["https://consent.testbed.fi/.well-known/jwks.json"],
    )
    consent_request_uri: HttpUrl = Field(
        ...,
        description="",
        examples=["https://consent.testbed.fi/Consent/Request"],
    )
