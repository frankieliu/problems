
Python: 7-line & 52ms (+ 1-liner for fun)

https://leetcode.com/problems/add-strings/discuss/90449

* Lang:    python3
* Author:  dalwise
* Votes:   12

```
def addStrings(self, num1, num2):
    z = itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0')
    res, carry, zero2 = [], 0, 2*ord('0')
    for i in z:
        cur_sum = ord(i[0]) + ord(i[1]) - zero2 + carry
        res.append(str(cur_sum % 10))
        carry = cur_sum // 10
    return ('1' if carry else '') + ''.join(res[::-1])
```

The above I think would be the expected answer in an interview. But just for fun based on a similar idea we can have a (rather long :-) one-liner. It technically satisfies the problem conditions, although it may warrant disqualification from the contest, depending on interpretation:
 - "You must not use any built-in BigInteger library" -> I don't use a library; I am just making use of the fact that Python's standard int supports arbitrarily large integers.
 - "or convert the inputs to integer directly" -> I don't; I sum them digit by digit. It is the result that I convert to integer and back.

Formated for added clarity, although everything can be put on the same line:
```
def addStrings(self, num1, num2):
     return str(
              reduce(lambda a, b: 10*a + b, 
                 map(lambda x: ord(x[0])+ord(x[1])-2*ord('0'),
                   list(itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0'))[::-1]
                 ) 
              )
            )
```

Would the one liner be acceptable in the contest?
