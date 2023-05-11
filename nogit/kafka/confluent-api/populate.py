from csv import reader
from pprint import pprint
from json import loads,load,dump,dumps
import numpy as np


ejemplo = [{'name': 'idTransaction', 'type': 'long', 'doc': 'Transaction id'}, {'name': 'idUser', 'type': 'long', 'doc': 'Transaction user'}, {'name': 'transactionTimestamp', 'type': ['null', 'string'], 'doc': 'Timestamp on which the transaction was born', 'default': None}, {'name': 'paymentAttemptTimestamp', 'type': ['null', 'string'], 'doc': 'Timestamp on which the payment is attempted', 'default': None}, {'name': 'idPaymentTransaction', 'type': 'long', 'doc': 'Transaction payment id'}, {'name': 'paymentTransactionTimestamp', 'type': ['null', 'string'], 'doc': 'Timestamp on which the payment was approved', 'default': None}, {'name': 'transactionType', 'type': 'string', 'doc': 'Transaction type ()'}, {'name': 'paymentMethod', 'type': 'string', 'doc': 'Payment method ()'}, {'name': 'totalAmount', 'type': 'string', 'doc': 'Total amount in transaction'}, {'name': 'cardNumber', 'type': 'string', 'doc': 'Bank card number used in transaction. It has a mask for PCI purposes'}, {'name': 'cardType', 'type': ['null', 'string'], 'doc': 'Card type (Visa, Mastercard, etc)', 'default': None}, {'name': 'reference', 'type': ['null', 'string'], 'doc': 'Should contain information regarding transaction', 'default': None}, {'name': 'cardHolderName', 'type': 'string', 'doc': 'Card holder name'}, {'name': 'merchantNumber', 'type': 'long', 'doc': 'Merchant number associated in the transaction'}, {'name': 'operationKey', 'type': ['null', 'string'], 'doc': 'Operation key associated with PROSA or other institution', 'default': None}, {'name': 'authorizationCode', 'type': ['null', 'string'], 'doc': 'Authorization code in the transaction. It could be received from different sources. It will depend on transaction type', 'default': None}, {'name': 'tipService', 'type': ['null', 'string'], 'doc': 'If transaction was performed in restaurant context, tip will be fill in this field. In other case, always should be null', 'default': None}, {'name': 'paymentAvailableDate', 'type': ['null', 'string'], 'doc': 'Date when money should be available for merchant', 'default': None}, {'name': 'idOperationAffected', 'type': ['null', 'long'], 'doc': 'Id in original transaction that was affected with this devolution', 'default': None}, {'name': 'commissions', 'type': ['null', {'type': 'array', 'items': {'type': 'record', 'name': 'CommissionEvent', 'fields': [{'name': 'idCommission', 'type': 'long', 'doc': 'Commission id'}, {'name': 'commissionDate', 'type': 'string', 'doc': 'Date of the commission'}, {'name': 'commissionPercentage', 'type': 'string', 'doc': 'Commission percentage'}, {'name': 'commissionType', 'type': 'string', 'doc': 'Commission rate (can be fixed or variable)'}, {'name': 'commissionAmount', 'type': 'string', 'doc': 'Commission amount'}, {'name': 'ivaPercentage', 'type': 'string', 'doc': 'Iva percentage'}, {'name': 'ivaAmount', 'type': 'string', 'doc': 'Iva amount'}, {'name': 'commissionTotal', 'type': 'string', 'doc': 'Commission total amount'}]}}], 'doc': 'List of commissions in transaction', 'default': None}, {'name': 'antiFraudEvents', 'type': ['null', {'type': 'array', 'items': {'type': 'record', 'name': 'AntiFraudEvent', 'fields': [{'name': 'idAntiFraudEvent', 'type': 'long', 'doc': 'Anti fraud event id'}, {'name': 'recommendationCode', 'type': ['null', 'string'], 'doc': 'Response from anti fraud vendor. This response will be used to determine the transaction status later', 'default': None}, {'name': 'totalScore', 'type': 'double', 'doc': 'Score from anti fraud vendor'}, {'name': 'antiFraudCreatedDateEvent', 'type': ['null', 'string'], 'doc': 'Date on which the anti fraud event was created', 'default': None}]}}], 'doc': 'List of anti-fraud events in transaction', 'default': None}, {'name': 'secure3DEvents', 'type': ['null', {'type': 'array', 'items': {'type': 'record', 'name': 'Secure3DEvent', 'fields': [{'name': 'id3DSEvent', 'type': 'long', 'doc': '3DS event id'}, {'name': 'enrollmentStatus', 'type': ['null', 'string'], 'default': None, ',doc': 'First response from 3DS vendor. This response could be null and is not considered as a final decision'}, {'name': 'validationStatus', 'type': ['null', 'string'], 'doc': 'Second response from 3DS vendor. It could be considered as final decision.', 'default': None}, {'name': 'secure3DSCreatedAt', 'type': ['null', 'string'], 'doc': 'Date on which the 3DS event was created', 'default': None}]}}], 'doc': 'List of 3DS events in transaction', 'default': None}]

with open("/Users/intern/projects/nogit/kafka/confluent-api/schemas_list.csv") as schemas_file:
    schemas = reader(schemas_file)
    fields_len = 0
    errors = 0
    for pos,schema in enumerate(schemas):
        if pos >0:
            try:
                fields = schema[2]
                fields = fields.replace('\t','')
                fields = fields.replace('\n','')
                fields = fields.replace(',}','}')
                fields = fields.replace(',]',']')
                fields = loads(fields.replace("\'", "\""))
            except:
                breakpoint()
                errors += 1
            if len(fields)>fields_len:
                fields_len = len(fields)
                pprint(schema)
                print(pos)
    print(f"Errors {errors}")