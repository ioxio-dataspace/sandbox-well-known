from typing import Literal

from pydantic import AnyUrl, BaseModel, Field, HttpUrl

from settings import conf


class Header(BaseModel):
    v: Literal["0.2"] = Field(
        ...,
        description="The version of the Consent Token standard the token follows.",
        examples=["0.2"],
    )
    tid: str = Field(
        ...,
        description="A consent token ID, It is unique for each consent the user has "
        "granted to some app. Multiple consent token JWTs can however be issued for "
        "the same consent with for example different `iat` and `exp`, but sharing the "
        "same `tid`.",
        examples=["36bd899b-8b43-484c-ac58-a4da7e32273d"],
    )
    kid: str = Field(
        ...,
        description="The key ID used to sign the token. A key with the same kid must "
        "be found in the JWKS pointed to by the "
        "[consent configuration](consent-configuration.html).",
        examples=["0fcf0244-69fa-454d-a124-0bd8bc05430"],
    )
    alg: Literal["RS256"] = Field(
        ...,
        description="The algorithm the token is signed with.",
        examples=["RS256"],
    )
    typ: Literal["JWT"] = Field(
        ...,
        description="The algorithm the token is signed with, must be `RS256`",
        examples=["JWT"],
    )
    jku: HttpUrl = Field(
        ...,
        description="JWK Set URL where the key the token was signed with can be found. "
        "Note that apps or productizers that validate the token must not trust this "
        "header alone, as that would allow bypassing the validation. If the key is "
        "loaded based on this, the URL must be validated to match the `jwks_uri` in "
        "the [consent-configuration](consent-configuration.html). If that is done, "
        "this can be used in libraries or online services like for example "
        "[JWT.io](https://jwt.io/) to quickly and easily validate the token.",
        examples=[f"{conf.CONSENT_PROVIDER_URL}/.well-known/jwks.json"],
    )


class Body(BaseModel):
    iss: HttpUrl = Field(
        ...,
        description="The issuer of the token. This is the base URL for the consent "
        "provider.",
        examples=[conf.CONSENT_PROVIDER_URL],
    )
    sub: str = Field(
        ...,
        description="The `sub` from the ID Token of the user.",
        examples=["debade8a-091d-42da-9b0c-e61f9471e2c3"],
    )
    subiss: str = Field(
        ...,
        description="The `iss` from the ID Token of the user.",
        examples=[conf.AUTHENTICATION_PROVIDER_END_USER_URL],
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
        examples=[conf.AUTHENTICATION_PROVIDER_END_USER_URL],
    )
    dsi: AnyUrl = Field(
        ...,
        description="Data source identifier for which the token proves consent.",
        examples=[
            f"dpp://source@{conf.DATASPACE_BASE_DOMAIN}/draft/Weather/Current/"
            f"Metric"
        ],
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


class ConsentToken(BaseModel):
    header: Header
    body: Body

    class Config:
        schema_extra = {
            "title": "Consent Token",
            "description": "The Consent Token is a "
            "[JWT](https://www.rfc-editor.org/rfc/rfc7519) used in the "
            "[Consent Protocol](https://miro.com/app/board/o9J_lC4tnfI=/) to prove a "
            "user has granted their consent for an application to access the data "
            "provided by a data source. When the user has granted the consent, the "
            "consent provider can issue a consent token to the app. The application "
            "includes the consent token in the `X-Consent-Token` header in the "
            "requests it makes to the product gateway, which forwards the header to "
            "the productizer. The productizer is responsible for validating the token "
            "and handling access control to the data it provides. Below are details on "
            "fields or claims included in the header and body of the token.",
            "examples": [
                {
                    "header": {
                        "v": "0.2",
                        "tid": "36bd899b-8b43-484c-ac58-a4da7e32273d",
                        "kid": "0fcf0244-69fa-454d-a124-0bd8bc05430",
                        "alg": "RS256",
                        "typ": "JWT",
                        "jku": f"{conf.CONSENT_PROVIDER_URL}/.well-known/jwks.json",
                    },
                    "body": {
                        "iss": conf.CONSENT_PROVIDER_URL,
                        "sub": "debade8a-091d-42da-9b0c-e61f9471e2c3",
                        "subiss": conf.AUTHENTICATION_PROVIDER_END_USER_URL,
                        "acr": conf.ACR_VALUES,
                        "app": "bb8c7f74-0855-42e1-ba09-70bb27103ded",
                        "appiss": conf.AUTHENTICATION_PROVIDER_END_USER_URL,
                        "dsi": f"dpp://source@{conf.DATASPACE_BASE_DOMAIN}/"
                        "draft/Weather/Current/Metric",
                        "exp": 1678492800,
                        "iat": 1678406400,
                    },
                },
            ],
        }


ROOT = ConsentToken
