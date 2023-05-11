import json
from pprint import pprint

from aws_service import glue_client


class Glue:
    def __init__(self) -> None:
        self.client = glue_client()

    def create_schema(
        self,
        schema_str_value: str,
        schema_name: str,
        registry_name: str,
        description: str,
        tags: dict,
    ):
        response = self.client.create_schema(
            RegistryId={
                "RegistryName": registry_name,
            },
            SchemaName=schema_name,
            DataFormat="AVRO",
            Compatibility="FULL_ALL",
            Description=description,
            Tags=tags,
            SchemaDefinition=schema_str_value,
        )
        return response

    def get_schema(self, schema_name: str, registry_name: str):
        response = self.client.get_schema(
            SchemaId={
                "SchemaName": schema_name,
                "RegistryName": registry_name,
            }
        )
        return response

    def get_schema2(self, schema_name: str, registry_name: str, schema_definition: str):
        # this method returns the schemaVersionId but needs the definition
        response = self.client.get_schema_by_definition(
            SchemaId={"SchemaName": schema_name, "RegistryName": registry_name},
            SchemaDefinition=schema_definition,
        )
        return response

    def get_schema_definition(self, schema_name: str, registry_name: str):
        response = self.client.get_schema_version(
            SchemaId={"SchemaName": schema_name, "RegistryName": registry_name},
            SchemaVersionNumber={"LatestVersion": True},
        )
        return response


glue_service = Glue()

schema = glue_service.get_schema_definition("k-auth-account-created-value", "auth")
schema_json = json.loads(schema["SchemaDefinition"])
print(type(schema_json))
pprint(schema_json)
