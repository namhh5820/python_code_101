
import requests
import json
import sys
import os

# Get CF API Key: https://support.cloudflare.com/hc/en-us/articles/200167836-Where-do-I-find-my-Cloudflare-API-key-
CF_API_KEY = 'xxx'
# Your cloudflare email address
CF_EMAIL = 'xxx'

RECORD_NAME = 'namhh.vinahost.vn'
RECORD_ID = 'f0e50df64978e355a396b0bb0910029c'
IP = '123.123.123.101'

resp = requests.get(
        'https://api.cloudflare.com/client/v4/zones/54e8b96734c473a6d34d55d104e1b650/dns_records?type=A&name={}'.format(RECORD_NAME),
        headers={
            'Content-Type':'application/json',
            'X-Auth-Key': CF_API_KEY,
            'X-Auth-Email': CF_EMAIL
        })

print(json.dumps(resp.json(), indent=4, sort_keys=True))
print('\nPlease find the DNS record ID you would like to update and entry the value into the script')


resp = requests.put(
    'https://api.cloudflare.com/client/v4/zones/54e8b96734c473a6d34d55d104e1b650/dns_records/{}'.format(RECORD_ID),
    json={
        'type': 'A',
        'name': 'namhh.vinahost.vn',
        'content': IP,
        'proxied': False
    },
    headers={
        'X-Auth-Key': CF_API_KEY,
        'X-Auth-Email': CF_EMAIL
    })
assert resp.status_code == 200

print('Updated dns record {} --> {}'.format(RECORD_NAME,IP))

