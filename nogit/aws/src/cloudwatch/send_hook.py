from slack_sdk.webhook import WebhookClient
from datetime import datetime
url = "https://hooks.slack.com/services/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" #HOOK DE PRUEBA
url_pruebas = "https://hooks.slack.com/services/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"
url_acct_mgmt = "https://hooks.slack.com/services/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"
def send_hook_to_prueba(message):
    webhook = WebhookClient(url_pruebas)
    response = webhook.send(text=message)
    assert response.status_code == 200
    assert response.body == "ok"
    return

def send_hook_to_act_mgmmt(message):
    webhook = WebhookClient(url_acct_mgmt)
    response = webhook.send(text=message)
    assert response.status_code == 200
    assert response.body == "ok"
    return
