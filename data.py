import requests


para = {
    "amount": 10,
    "type": "boolean"
}
api = requests.get(url="https://opentdb.com/api.php", params=para)

question_data = api.json()["results"]

