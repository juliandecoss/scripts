import datetime
from dataclasses import dataclass

from marshmallow import Schema, fields, post_load


@dataclass
class NotificationTrace:
    trace: str


@dataclass
class Trace:
    user_id: str
    natural_person_id: str
    enterprise_id: str
    source: str
    domain: str
    stage: str
    screen: str
    action: str
    email: str
    phone: str
    first_name: str
    last_name: str
    last_name1: str
    last_name2: str
    timestamp: str
    enterprise_customer_type: str
    utm_source: float
    utm_medium: str
    utm_campaign: str
    utm_term: str
    utm_content: str


@dataclass
class TraceKey:
    id: str


class DataclassSchema(Schema):
    @post_load
    def make_object(self, data, **kwargs):
        return self.__model__(**data)


class NotificationTraceSchema(DataclassSchema):
    __model__ = NotificationTrace

    trace = fields.String(required=True)


class TraceSchema(DataclassSchema):
    __model__ = Trace

    user_id = fields.Integer()
    natural_person_id = fields.Integer()
    enterprise_id = fields.Integer()
    source = fields.String()
    domain = fields.String()
    stage = fields.String()
    screen = fields.String()
    action = fields.String()
    email = fields.String()
    phone = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    last_name1 = fields.String()
    last_name2 = fields.String()
    timestamp = fields.String()
    enterprise_customer_type = fields.String()
    utm_source = fields.String()
    utm_medium = fields.String()
    utm_campaign = fields.String()
    utm_term = fields.String()
    utm_content = fields.String()


class TraceKeySchema(DataclassSchema):
    __model__ = TraceKey

    id = fields.Integer()


obj = {
    "user_id": 10004,
    "natural_person_id": 10005,
    "enterprise_id": 4,
    "source": "server",
    "email": "juliandecoss@gmail.com",
    "phone": str("9611230729"),
    "first_name": "Julian David",
    "last_name": "Julian David",
    "last_name1": "De Coss",
    "last_name2": "Espinosa",
    "enterprise_customer_type": "",
    "timestamp": datetime.datetime.now().isoformat(),
    "screen": "https://konfio.mx/mi/login",
    "utm_source": "",
    "utm_medium": "",
    "utm_campaign": "",
    "utm_term": "",
    "utm_content": "",
    "domain": "",
    "stage": "",
    "action": "",
}
value_obj: Trace = TraceSchema().load(obj)
key_object = TraceKey(value_obj.user_id)
TraceKeySchema().dump(key_object)
TraceSchema().dump(value_obj)
breakpoint()
# lambda trace_key_obj, ctx: json.loads(obj),
