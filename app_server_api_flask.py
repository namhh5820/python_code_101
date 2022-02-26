# app_server_api_flask.py
from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.route("/")
def get_info():
    text1 =  '''
                API:

                1.GET /countries returns the list of countries
                2.POST /countries adds a new country to the list.
                3.SUM /sum?number1=a&number2=b .
             '''
    return text1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415


@app.get("/sum")
def sum():
   args = request.args
   a = args.get("number1")
   b = args.get("number2")
   sum = str(int(a) + int(b))

   return "Sum (a + b) = : " + sum

