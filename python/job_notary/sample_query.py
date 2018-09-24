import time
import os
import json

def main():

    from_json = True
    if not from_json:
        rest_api = "http://localhost:9090/api/v1/query?query="
        query = "{__name__=~'[g]o.*'}"
        duration = "[1m]"
        atime = int(time.time()) - 10
        endtime = "&time={}".format(atime)
        outfile = "{}".format(atime)
    else:
        # can also read this from a json file
        with open("query.json") as file:
            d = json.load(file)
        rest_api = d["rest_api"]
        query = d["query"]
        duration = d["duration"]
        atime = d["atime"] if d["atime"] != "now" else int(time.time())
        endtime = d["endtime"].format(atime=atime)
        outfile = d["outfile"].format(atime=atime)

    os.system("curl -s --globoff -k \"{}{}{}{}\" | tee {}".format(
        rest_api, query, duration, endtime, outfile))
