from marshmallow import Schema, fields, post_load, pre_load
from re import sub
from typing import List
from pprint import pprint
LAST_NAMES = ["paternal_last_name", "maternal_last_name"]
class CreateSsoUserSchema(Schema):
    country_code = fields.String(allow_none=True, data_key="countryCode")
    email = fields.Email(required=True)
    name = fields.String(required=True)
    maternal_last_name = fields.String(data_key="maternalLastName")
    paternal_last_name = fields.String(data_key="paternalLastName", required=True)
    phone_number = fields.String(data_key="mobilePhone")

    @pre_load
    def before_deserialize(self, data, **kwargs):
        if isinstance(data.get("mobilePhone"), int):
            data["mobilePhone"] = str(data["mobilePhone"])
        return data

    @post_load
    def after_deserialize(self, data, **kwargs):
        country_code = data.pop("country_code", None) or "+52"
        phone_number = data.get("phone_number") or "5555555555"
        data["phone_number"] = country_code + sub(r"[^0-9]", "", phone_number)
        return data

def get_cognito_user_attributes_list(
    sso_user_schema: dict, ignored_fields: List
) -> List[dict]:
    new_user_data = []
    for key, value in sso_user_schema.items():
        if key in LAST_NAMES:
            key = f"custom:{key}"
        if value and key not in ignored_fields:
            new_user_data.append({"Name": key, "Value": value})
    return new_user_data
json = {"email":"juligan_2911@hotmail.com",
        "name":"Paulito",
        "paternalLastName":"LasCurain",
        "mobilePhone":961230729,
        "countryCode":"+123"
}
sso_user_data = CreateSsoUserSchema().load(json, unknown="exclude")
breakpoint()
user_data = get_cognito_user_attributes_list(sso_user_data,[])
pprint(user_data)