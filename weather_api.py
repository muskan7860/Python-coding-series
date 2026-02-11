import requests
url = "http://api.weatherstack.com/current"   # 👈 http, not https
params = {
    "access_key": "15b9bc9441cc875d7e3fb26079f02788",
    "query": "London"
}
response = requests.get(url, params=params)
print(response.json())
==========================================================================================
You will create a Python script that:

Calls a public API (example: GitHub API, JSONPlaceholder) list
Fetches data using the requests library
Parses the JSON response
Extracts meaningful information from the response
Prints the processed output to the terminal
Saves the processed data into a JSON file
This task helps you understand how DevOps engineers work with APIs and structured data.

Expected Output
One Python script (example: api_data_fetcher.py)
One JSON output file (example: output.json)
Output should be visible:
In terminal
In the JSON file
