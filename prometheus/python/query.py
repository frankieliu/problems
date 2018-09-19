import requests
import json


url = "http://localhost:9090/api/v1/query"
params = {'query': '{__name__=~".+"}'}
r = requests.get(url=url, params=params)
print(json.dumps(r.json(), indent=1))
