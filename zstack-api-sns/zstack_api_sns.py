# app_server_api_flask.py
import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

list = [
    {"text": "msg1"},
    {"text": "msg2"},
    {"text": "msg3"},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.route("/")
def get_info():
    home_text = '''
                API:
                1.GET / List of API 
                2.POST /slack Send msg to Slack
                3.POST /telegram Send mgs to Telegram
                '''
    return home_text


@app.post("/slack")
def send_msg_to_slack():
    webhook_url = "https://hooks.slack.com/services/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"
    if request.is_json:
        msg = request.get_json()
        ALARM_UUID = msg.get('ALARM_UUID', '')
        ALARM_NAME = msg.get('ALARM_NAME', '')
        ALARM_RESOURCE_NAME = msg.get('ALARM_RESOURCE_NAME', '')
        ALARM_METRIC = msg.get('ALARM_METRIC', '')
        ALARM_CURRENT_VALUE = msg.get('ALARM_CURRENT_VALUE', '')

        sns_msg = "VINAHOST ALARM: " + ALARM_NAME + ": " + ALARM_RESOURCE_NAME +": "+ ALARM_METRIC + ": " + ALARM_CURRENT_VALUE
        data = {"text":sns_msg}
        headers =  {"Content-Type":"application/json"}
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

        return msg, 201
    return {"error": "Request must be JSON"}, 415


@app.post("/telegram")
def send_msg_to_telegram():
    #ADD CODE HERE

   return "VINAHOST ALARM"

