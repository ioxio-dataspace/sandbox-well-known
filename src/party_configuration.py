from pydantic import BaseModel, Field, HttpUrl


class PartyConfiguration(BaseModel):
    class Config:
        schema_extra = {
            "title": "/.well-known/dataspace/party-configuration.json",
            "description": "This configuration should be provided by each party "
            "creating applications or productizers on the dataspace and will provide "
            "details of for example where keys used to sign different payloads can be "
            "found. Typically this would be found on something like "
            "`https://example.com/.well-known/dataspace/party-configuration.json`. "
            "This must be served over https and it's highly recommended to set up the "
            'domain with <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/'
            'Headers/Strict-Transport-Security" target="_blank">HSTS</a>.',
            "examples": [
                {
                    "jwks_uri": "https://example.com/.well-known/jwks.json",
                }
            ],
        }

    jwks_uri: HttpUrl = Field(
        ...,
        description='The URI at which the <a href="https://auth0.com/docs/secure/'
        'tokens/json-web-tokens/json-web-key-set-properties" target="_blank">JWKS'
        "</a> for the party can be found. For now the following values must be used in "
        "the keys that are defined in the JWKS: <br />"
        '`"alg": "RS256",`<br />'
        '`"kty": "RSA",`<br />'
        '`"use": "sig",`<br />',
        examples=["https://example.com/.well-known/jwks.json"],
    )


ROOT = PartyConfiguration
