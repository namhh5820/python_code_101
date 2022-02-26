import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)

print response.json()
print "Status code: " + str(response.status_code)
