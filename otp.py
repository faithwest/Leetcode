import http.client
import json

conn = http.client.HTTPSConnection("5y2v5g.api.infobip.com")
payload = json.dumps({
    "messages": [
        {
            "destinations": [{"to":"254705780000"},{"to":"254712764067"},{"to":"254721601031"},{"to":"254710224989"}],
            "from": "ServiceSMS",
            "text": "Hello,\n\nThis is a test message from AgriSoko Team. "
        }
    ]
})
("utf-8"))