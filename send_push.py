# -*- coding:utf-8 -*-

# send push notification via nifty cloud mobile backend
# cf https://wp.sakaki333.com/2017/02/21/post-967/

import hmac
import hashlib
import base64
from datetime import datetime
import requests
import json

fqdn = "mb.api.cloud.nifty.com"
sig_method = "HmacSHA256"
sig_ver = "2"
app_key = "xxxxxxxxxxxxxxxxxxxxxx"
client_key = b"xxxxxxxxxxxxxxxxxxx"


def encode_signature(secret, message):
    signature = hmac.new(secret, message, hashlib.sha256).digest()
    decoded = base64.b64encode(signature)
    return decoded


def gen_signature(method, api_path, timestamp):
    keys = "&".join([
        "SignatureMethod=" + sig_method,
        "SignatureVersion=" + sig_ver,
        "X-NCMB-Application-Key=" + app_key,
        "X-NCMB-Timestamp=" + timestamp
    ])
    message = "\n".join([
        method,
        fqdn,
        api_path,
        keys
    ]).encode()
    signature = encode_signature(client_key, message)
    return signature


def send_request(method, api_path, params):
    timestamp = datetime.utcnow().isoformat()[:-3]
    signature = gen_signature(method, api_path, timestamp)
    headers = {
        "X-NCMB-Application-Key": app_key,
        "X-NCMB-Signature": signature,
        "X-NCMB-Timestamp": timestamp,
        "Content-Type": "application/json"
    }
    if method == "POST":
        res = requests.post(
            "https://{0}{1}".format(fqdn, api_path),
            headers=headers,
            data=json.dumps(params)
        )
        print(res.text)


def test_push():
    method = "POST"
    api_path = "/2013-09-01/push"
    params = {
        "immediateDeliveryFlag": True,
        "target": ["android"],
        "message": "Test Message from raspberry pi!",
        "deliveryExpirationTime": "3 day"
    }
    send_request(method, api_path, params)


if __name__ == "__main__":
    test_push()
