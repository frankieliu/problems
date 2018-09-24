a = [{"id": 1, "data": 2},
   {"id": 3, "data": 4}]
b = {x["id"]: x["data"] for x in a}
d = {
    "done": {"file": 1,
             "data": {}
    },
    "todo": {"file": 2,
             "data": {}
    }
}
done = d["done"]["data"]
todo = d["todo"]["data"]
done["1"] = 3

print(d)
for k,v in d.items():
    print(k,v)
