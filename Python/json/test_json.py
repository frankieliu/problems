import json
s = '{"a": 1, "b": 2}'
d = json.loads(s)
print(d)
print(
    json.dumps(
        ['foo',{'bar': ('baz', None, 1.0, 2)}],
        indent=4))
