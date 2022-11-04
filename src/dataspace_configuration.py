from typing import List

from pydantic import BaseModel, Field, HttpUrl


class AuthenticationProviders(BaseModel):
    base_url: HttpUrl = Field(..., examples=["https://login.testbed.fi"])


class ConsentProviders(BaseModel):
    base_url: HttpUrl = Field(..., examples=["https://consent.testbed.fi"])


class Definitions(BaseModel):
    git: HttpUrl = Field(
        ..., examples=["https://github.com/Virtual-Finland/definitions.git"]
    )
    web: HttpUrl = Field(
        ..., examples=["https://github.com/Virtual-Finland/definitions"]
    )


class DataspaceConfiguration(BaseModel):
    class Config:
        schema_extra = {
            "title": "/.well-known/dataspace/dataspace-configuration.json",
            "description": "Configuration details for a dataspace and critical URLs "
            "for it",
            "examples": [
                {
                    "dataspace_base_domain": "testbed.fi",
                    "product_gateway_url": "https://gateway.testbed.fi",
                    "developer_portal_url": "https://developer.testbed.fi",
                    "docs_url": "https://docs.testbed.fi",
                    "authentication_providers": [
                        {"base_url": "https://login.testbed.fi"}
                    ],
                    "content_providers": [{"base_url": "https://consent.testbed.fi"}],
                    "definitions": {
                        "git": "https://github.com/Virtual-Finland/definitions.git",
                        "web": "https://github.com/Virtual-Finland/definitions",
                    },
                }
            ],
        }

    dataspace_base_domain: str = Field(
        ...,
        description="The base domain for the whole dataspace, without any protocol. "
        "This is the domain at which for example the "
        "/.well-known/dataspace-configuration.json is expected to be found.",
        examples=["testbed.fi"],
    )

    product_gateway_url: HttpUrl = Field(
        ...,
        description="The URL at which the Product Gateway of the dataspace is hosted. "
        "Must use the https:// protocol",
        examples=["https://gateway.testbed.fi"],
    )
    developer_portal_url: HttpUrl = Field(
        ...,
        description="The URL where the Developer Portal for the dataspace can be "
        "found. This is where developers can register their own data sources and "
        "applications.",
        examples=["https://developer.testbed.fi"],
    )
    docs_url: HttpUrl = Field(
        ...,
        description="The URL at which the dataspace API documentation can be found.",
        examples=["https://docs.testbed.fi"],
    )
    authentication_providers: List[AuthenticationProviders]
    consent_providers: List[ConsentProviders]
    definitions: Definitions


ROOT = DataspaceConfiguration
