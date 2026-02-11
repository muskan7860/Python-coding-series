import requests
url = "http://api.weatherstack.com/current"   # 👈 http, not https
params = {
    "access_key": "15b9bc9441cc875d7e3fb26079f02788",
    "query": "London"
}
response = requests.get(url, params=params)
print(response.json())
