import re

print([int(s) for s in re.findall(r'\d+', 'hello 42 I\'m a 32 string 30')])
# ['42', '32', '30']
