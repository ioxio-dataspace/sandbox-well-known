from typing import Literal

from pydantic import BaseModel, Field, HttpUrl

from settings import conf


class Header(BaseModel):
    v: Literal["0.2"] = Field(
        ...,
        description="The version of the Consent Request Token standard the token "
        "follows.",
        examples=["0.2"],
    )
    kid: str = Field(
        ...,
        description="The key ID used to sign the token. A key with the same kid must "
        "be found in the JWKS pointed to by the "
        "[party configuration](party-configuration.html).",
        examples=["2d149479-88a6-4141-ad4c-b14c92f430bc"],
    )
    alg: Literal["RS256"] = Field(
        ...,
        description="The algorithm the token is signed with.",
        examples=["RS256"],
    )


class Body(BaseModel):
    iss: HttpUrl = Field(
        ...,
        description="The issuer of the token. Must be the base URL "
        "(`https:// + domain`) on which the party configuration is hosted, with no "
        "trailing slash.",
        examples=["https://example.com"],
    )
    sub: str = Field(
        ...,
        description="The `sub` from the ID Token of the user.",
        examples=["debade8a-091d-42da-9b0c-e61f9471e2c3"],
    )
    subiss: str = Field(
        ...,
        description="The `iss` from the ID Token of the user.",
        examples=[conf.AUTHENTICATION_PROVIDER_URL],
    )
    acr: str = Field(
        ...,
        description="The `acr` from the ID Token of the user.",
        examples=[conf.ACR_VALUES],
    )
    app: str = Field(
        ...,
        description="The app identifier (OIDC Client ID of the app).",
        examples=["bb8c7f74-0855-42e1-ba09-70bb27103ded"],
    )
    appiss: str = Field(
        ...,
        description="The `iss` (OIDC issuer) at which the app is registered.",
        examples=[conf.AUTHENTICATION_PROVIDER_URL],
    )
    aud: str = Field(
        ...,
        description="The consent portal base URL.",
        examples=[conf.CONSENT_PROVIDER_URL],
    )
    exp: int = Field(
        ...,
        description="The unix timestamp at which the token expires. Must not be in the "
        "past.",
        examples=[1678492800],
    )
    iat: int = Field(
        ...,
        description="The unix timestamp at which the token was issued. It must not be "
        "in the future.",
        examples=[1678406400],
    )


class ConsentRequestToken(BaseModel):
    header: Header
    body: Body

    class Config:
        schema_extra = {
            "title": "Consent Request Token",
            "description": "The Consent Request Token is a "
            "[JWT](https://www.rfc-editor.org/rfc/rfc7519) used in the "
            "[Consent Protocol](https://miro.com/app/board/o9J_lC4tnfI=/) to "
            "authenticate the application when it is requesting a new consent or to "
            "get a consent token for an already given consent. The token is sent in "
            "the `X-Consent-Request-Token` header and signed with a key published by "
            "the application developer through the "
            "[party configuration](party-configuration.html). Below are details on "
            "fields or claims are required in the header and body of the token.",
            "examples": [
                {
                    "header": {
                        "v": "0.2",
                        "kid": "2d149479-88a6-4141-ad4c-b14c92f430bc",
                        "alg": "RS256",
                    },
                    "body": {
                        "iss": "https://example.com",
                        "sub": "debade8a-091d-42da-9b0c-e61f9471e2c3",
                        "subiss": conf.AUTHENTICATION_PROVIDER_URL,
                        "acr": conf.ACR_VALUES,
                        "app": "bb8c7f74-0855-42e1-ba09-70bb27103ded",
                        "appiss": conf.AUTHENTICATION_PROVIDER_URL,
                        "aud": conf.CONSENT_PROVIDER_URL,
                        "exp": 1678492800,
                        "iat": 1678406400,
                    },
                },
            ],
        }


ROOT = ConsentRequestToken
