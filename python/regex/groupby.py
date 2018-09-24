from itertools import groupby
my_str = "hello 12 hi 89"

l = [int(''.join(i)) for is_digit, i in groupby(my_str, str.isdigit) if is_digit]

str = "h3110 23 cat 444.4 rabbit 11 2 dog"
[int(s) for s in str.split() if s.isdigit()]
# [23, 11, 2]
