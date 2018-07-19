import re

# Format is [(<string>, <expected output>), ...]
ss = [("apple-12.34 ba33na fanc-14.23e-2yapple+45e5+67.56E+3",
       ['-12.34', '33', '-14.23e-2', '+45e5', '+67.56E+3']),
      ('hello X42 I\'m a Y-32.35 string Z30',
       ['42', '-32.35', '30']),
      ('he33llo 42 I\'m a 32 string -30',
       ['33', '42', '32', '-30']),
      ('h3110 23 cat 444.4 rabbit 11 2 dog',
       ['3110', '23', '444.4', '11', '2']),
      ('hello 12 hi 89',
       ['12', '89']),
      ('4',
       ['4']),
      ('I like 74,600 commas not,500',
       ['74,600', '500']),
      ('I like bad math 1+2=.001',
       ['1', '+2', '.001'])]

for s, r in ss:
    rr = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s)
    if rr == r:
        print('GOOD')
    else:
        print('WRONG', rr, 'should be', r)
