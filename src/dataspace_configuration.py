from typing import List

from pydantic import BaseModel, Field, HttpUrl

from settings import conf


class AuthenticationProviderDetailsDeveloper(BaseModel):
    base_url: HttpUrl = Field(
        ...,
        examples=[conf.AUTHENTICATION_PROVIDER_DEVELOPER_URL],
        description="Base URL for the authentication provider. Appending "
        "`/.well-known/openid-configuration` will give the full URL to the "
        "openid-configuration.",
    )


class AuthenticationProviderDetailsEndUser(BaseModel):
    base_url: HttpUrl = Field(
        ...,
        examples=[conf.AUTHENTICATION_PROVIDER_END_USER_URL],
        description="Base URL for the authentication provider. Appending "
        "`/.well-known/openid-configuration` will give the full URL to the "
        "openid-configuration.",
    )


class AuthenticationProviders(BaseModel):
    developer: AuthenticationProviderDetailsDeveloper = Field(
        ...,
        examples=[{"base_url": conf.AUTHENTICATION_PROVIDER_DEVELOPER_URL}],
        description="Details about authentication provider used to identify developers "
        "on the dataspace.",
    )
    end_user: AuthenticationProviderDetailsEndUser = Field(
        ...,
        examples=[{"base_url": conf.AUTHENTICATION_PROVIDER_END_USER_URL}],
        description="Details about authentication provider used to identify end users "
        "on the dataspace.",
    )


class ConsentProviders(BaseModel):
    base_url: HttpUrl = Field(
        ...,
        examples=[conf.CONSENT_PROVIDER_URL],
        description="Base URL for the consent provider. Appending "
        "`/.well-known/dataspace/consent-configuration.json` will give the full URL to "
        "the consent configuration.",
    )


class Definitions(BaseModel):
    git: HttpUrl = Field(
        ...,
        examples=[conf.DEFINITIONS_GIT_URL],
        description="The URL to the git repository of the definitions used on the "
        "dataspace.",
    )
    web: HttpUrl = Field(
        ...,
        examples=[conf.DEFINITIONS_WEB_URL],
        description="The URL to a human friendly view of the definitions git "
        "repository used on the dataspace.",
    )


class DataspaceConfiguration(BaseModel):
    class Config:
        schema_extra = {
            "title": "/.well-known/dataspace/dataspace-configuration.json",
            "description": "This configuration is found on the dataspace base domain, "
            f"for example at `{conf.WEBSITE_URL}/.well-known/"
            "dataspace/dataspace-configuration.json`. It lists all the relevant "
            "configuration of the dataspace, such as endpoints for different dataspace "
            "components.",
            "examples": [
                {
                    "dataspace_base_domain": conf.DATASPACE_BASE_DOMAIN,
                    "product_gateway_url": conf.PRODUCT_GATEWAY_URL,
                    "developer_portal_url": conf.DEVELOPER_PORTAL_URL,
                    "docs_url": conf.DATASPACE_DOCS_URL,
                    "dataspace_name": conf.DATASPACE_NAME,
                    "authentication_providers": {
                        "developer": {
                            "base_url": conf.AUTHENTICATION_PROVIDER_DEVELOPER_URL
                        },
                        "end_user": {
                            "base_url": conf.AUTHENTICATION_PROVIDER_END_USER_URL
                        },
                    },
                    "consent_providers": [{"base_url": conf.CONSENT_PROVIDER_URL}],
                    "definitions": {
                        "git": conf.DEFINITIONS_GIT_URL,
                        "web": conf.DEFINITIONS_WEB_URL,
                    },
                }
            ],
        }

    dataspace_base_domain: str = Field(
        ...,
        description="The base domain for the whole dataspace, without any protocol. "
        "This is the domain at which for example the "
        "`/.well-known/dataspace/dataspace-configuration.json` is found.",
        examples=[conf.DATASPACE_BASE_DOMAIN],
    )

    product_gateway_url: HttpUrl = Field(
        ...,
        description="The URL at which the Product Gateway of the dataspace is hosted "
        "and on which all the data products are accessed.",
        examples=[conf.PRODUCT_GATEWAY_URL],
    )
    developer_portal_url: HttpUrl = Field(
        ...,
        description="The URL where the Developer Portal for the dataspace is hosted. "
        "This is where developers can register their own data sources and "
        "applications.",
        examples=[conf.DEVELOPER_PORTAL_URL],
    )
    docs_url: HttpUrl = Field(
        ...,
        description="The URL at which the API documentation is hosted.",
        examples=[conf.DATASPACE_DOCS_URL],
    )
    dataspace_name: str = Field(
        ...,
        description="A human readable name for the dataspace",
        examples=[conf.DATASPACE_NAME],
    )
    authentication_providers: AuthenticationProviders
    consent_providers: List[ConsentProviders]
    definitions: Definitions


ROOT = DataspaceConfiguration
