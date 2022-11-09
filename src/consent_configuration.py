from pydantic import BaseModel, Field, HttpUrl

from settings import conf


class ConsentConfiguration(BaseModel):
    class Config:
        schema_extra = {
            "title": "/.well-known/dataspace/consent-configuration.json",
            "description": "Configuration details for a consent provider on a "
            "dataspace. This is hosted by the consent provider on the dataspace and is "
            f"thus available at for example `{conf.CONSENT_PROVIDER_URL}/.well-known/"
            "dataspace/consent-configuration.json`.",
            "examples": [
                {
                    "issuer": conf.CONSENT_PROVIDER_URL,
                    "jwks_uri": f"{conf.CONSENT_PROVIDER_URL}/.well-known/jwks.json",
                    "consent_request_uri": f"{conf.CONSENT_PROVIDER_URL}/Consent/"
                    "Request",
                }
            ],
        }

    issuer: HttpUrl = Field(
        ...,
        description="The issuer used by the consent provider in the JWT based consent "
        "tokens.",
        examples=[conf.CONSENT_PROVIDER_URL],
    )

    jwks_uri: HttpUrl = Field(
        ...,
        description="The URI for the JWKs used by the consent provider when signing "
        "tokens.",
        examples=[f"{conf.CONSENT_PROVIDER_URL}/.well-known/jwks.json"],
    )
    consent_request_uri: HttpUrl = Field(
        ...,
        description="The URI at which a consent can be requested.",
        examples=[f"{conf.CONSENT_PROVIDER_URL}/Consent/Request"],
    )


ROOT = ConsentConfiguration
