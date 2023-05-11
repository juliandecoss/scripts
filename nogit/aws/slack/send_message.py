import os
from slack_sdk import WebClient,webhook, WebhookClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="xoxe.xoxp-1-Mi0yLTM2ODA1NjUyNDYtMTU4NTIwNjAwNDAxOC0zNDg2ODg1OTA0Njc3LTM0ODMxNTMxNDI4NTQtNWU3MTdlNWQzNDAwYWIxOWI5OTJlMzc3YWExZWRiNDU0Yjg1NTQwZTE0MWIyNDQzY2Y5YmU5MzAxMDQ0ZmVmZA")

try:
    response = client.chat_postMessage(channel="#platform-kli", text="Hello world!")
    #response = client.chat_meMessage(channel="julian.decoss@konfio.mx",text="prueba para julian")
    assert response["message"]["text"] == "Hello world!"
    print(response)
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
