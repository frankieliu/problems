# Read and write JSON files with Python 2+3; works with unicode
# -*- coding: utf-8 -*-
import json

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Define data
data = {'a list': [1, 42, 3.141, 1337, 'help', u'€'],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42}}

# Write JSON file
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    Outfile.write(to_unicode(str_))

# Read JSON file
with open('data.json') as data_file:
    data_loaded = json.load(data_file)

print(data == data_loaded)

"""
Explanation of the parameters of json.dump:

indent:
 Use 4 spaces to indent each entry, e.g. when a new dict is started
 (otherwise all will be in one line),

sort_keys:
 sort the keys of dictionaries. This is useful if you want to compare
 json files with a diff tool / put them under version control.

separators:
 To prevent Python from adding trailing whitespaces


With a package

Have a look at my utility package mpu for a super simple and easy to
remember one:


import mpu.io
data = mpu.io.read('example.json')
mpu.io.write('example.json', data)

Created JSON file
{
    "a list":[
        1,
        42,
        3.141,
        1337,
        "help",
        "€"
    ],
    "a string":"bla",
    "another dict":{
        "foo":"bar",
        "key":"value",
        "the answer":42
    }
}

Common file endings
.json

Alternatives

CSV: Super simple format (read & write)
JSON: Nice for writing human-readable data; VERY commonly used (read & write)
YAML: YAML is a superset of JSON, but easier to read (read & write, comparison of JSON and YAML)
pickle: A Python serialization format (read & write)
MessagePack (Python package): More compact representation (read & write)
HDF5 (Python package): Nice for matrices (read & write)
XML: exists too *sigh* (read & write)

For your application, the following might be important:

Support by other programming languages
Reading / writing performance
Compactness (file size)

See also: Comparison of data serialization formats

In case you are rather looking for a way to make configuration files,
you might want to read my short article Configuration files in Python

https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
"""
