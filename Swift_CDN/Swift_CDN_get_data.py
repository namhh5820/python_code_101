#coding=utf-8
# Author namhh.vinahost.vn 
import hashlib
import hmac
import random
import time
import json
import requests


###Configure APP SERVER### 
api_server = "https://base-api.swiftfederation.com" 
###Paste your access key id!!!
access_key_id=""    
###Paste your access key secret!!!###    
access_key_secret=""     

request_method = "GET"
uri = "/v1.1/customer"
request_timestamp = time.strftime("%Y%m%dT%H%M%SZ", time.localtime(time.time() + time.timezone))
nonce = 56789
request_body = ''

def signature(request_method, request_body):             
    #request_body = '{"domains":["cycdnml.yuanzhanapp.com"],"startTime":"2018-12-16T00:00:00Z","endTime":"2018-12-16T00:20:00Z"}'     
    request_method = request_method
    request_body = request_body
    #'''Caculate signature'''    
    signing_string = "%s\n%s\n%s\n%s\n%s\n%s" % (request_method.upper(), uri, request_timestamp, nonce, access_key_id, request_body)    
    #print (signing_string)
    signature = hex_hmac_sha256(access_key_secret, signing_string)    
    #'''Assemble Authroization value'''    
    authorization_val = "HMAC-SHA256 " + access_key_id + ":" + signature     
    #print "================ Signature ==================="    
    #print("signature: %s" % signature)    
    print("") 
    #'''hex hamc sha256 algorithm''' 
    return authorization_val

def hex_hmac_sha256(sign_key, signing_string):    
    signed_bytes = hmac.new(sign_key, signing_string, digestmod=hashlib.sha256).digest()    
    return signed_bytes.encode('hex') 


authorization_val = signature(request_method, request_body)

resp = requests.get(
        'https://base-api.swiftfederation.com/v1.1/customer',
        headers={
            'Authorization':authorization_val,
            'Content-Type':'application/json; charset=utf-8',
            'X-SFD-Date': request_timestamp,
            'X-SFD-Nonce': nonce
        })
print('Information of VNH:\n')
print(json.dumps(resp.json(), indent=4, sort_keys=True))


###Get Customer Children
#"id": 31745
#"name": "VINAHOST PARTNER"
print('\n\nGet list Customer of VNH:\n')
uri = "/v1.2/customerChildren/31745"
authorization_val = signature(request_method, request_body)

resp = requests.get(
        'https://base-api.swiftfederation.com/v1.2/customerChildren/31745',
        headers={
            'Authorization':authorization_val,
            'Content-Type':'application/json; charset=utf-8',
            'X-SFD-Date': request_timestamp,
            'X-SFD-Nonce': nonce
        })

print(json.dumps(resp.json(), indent=4, sort_keys=True))

###Get Customer Volume
customerId = "31845"
print('\nGet Customer Volume Usage (month): Huy Tran-{}\n', customerId)
request_method = "POST"
uri = "/v1.1/report/customers/31845/volume"
request_body = '{"startTime":"2022-02-01T00:00:00Z","endTime":"2022-03-01T00:00:00Z"}'
authorization_val = signature(request_method, request_body)

resp = requests.post(
        'https://base-api.swiftfederation.com/v1.1/report/customers/31845/volume',
        headers={
            'Authorization':authorization_val,
            'Content-Type':'application/json; charset=utf-8',
            'X-SFD-Date': request_timestamp,
            'X-SFD-Nonce': nonce
        },
        data=request_body
        )

volume = resp.json()
#print('Type volume: ', type(volume))
#print('Type volume[0]', type(volume[0]))
sum = 0
for i in range(len(volume)):
    data = volume[i].get('value', i)
    sum = sum + int(data)
    #print('Data values= ' , data)

print('Total volume (Gb): ', sum/(1024*1024*1024))
#print(json.dumps(resp.json(), indent=4, sort_keys=True))