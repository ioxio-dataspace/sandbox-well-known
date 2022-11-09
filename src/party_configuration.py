from pydantic import BaseModel, Field, HttpUrl


class PartyConfiguration(BaseModel):
    class Config:
        schema_extra = {
            "title": "/.well-known/dataspace/party-configuration.json",
            "description": "This configuration should be provided by each party "
            "creating applications or productizers on the dataspace and will provide "
            "details of for example where keys used to sign different payloads can be "
            "found. Typically this would be found on something like "
            "`https://example.com/.well-known/dataspace/party-configuration.json`.",
            "examples": [
                {
                    "jwks_uri": "https://example.com/.well-known/jwks.json",
                }
            ],
        }

    jwks_uri: HttpUrl = Field(
        ...,
        description="The URI at which the JWKs for the party can be found.",
        examples=["https://example.com/.well-known/jwks.json"],
    )


ROOT = PartyConfiguration
