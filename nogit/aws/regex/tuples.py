from ast import literal_eval


headers = "[('event_name', 'account_created')]"
headers = "['event_name', 'account_created']"
if isinstance(headers,str):
    headers = literal_eval(headers)
    if not isinstance(headers[0],tuple):
        raise Exception(f"Not valid format headers {type(headers[0])}")
print(headers)