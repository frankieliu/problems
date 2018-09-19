import requests
from pprint import pprint as pp
import json

url = "http://keybridge-vm4.us.oracle.com:9091/api/v1/query"
# params = {'query': 'request_processing_seconds_count{group="canary"}[1m]',
#           'time': '1536785901.152'}

# params = {'query': 'request_processing_seconds_count[1m]',
#           'time': '1536785901.152'}

params = {'query': 'ifInPacketsPerSecond{ad="phx3",device="phx3-apex1",instance="localhost:9112",interface="Ethernet3/1/1",job="snmp-poller",role="ROLE-MISSING"}[10m]',
          'time': '1536773362.000'}
# params = {'query': 'ifInPacketsPerSecond'}

r0 = requests.get(url=url, params=params).json()
# print(r0)
if True:
    r = r0["data"]["result"]
    y = [x["values"] for x in r]
    pp(y)
    # print(r.keys()) # result resultType
    # print(json.dumps(r["result"], indent=1))
