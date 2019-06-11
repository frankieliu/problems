from collections import Counter

class Solution:
  def numUniqueEmails(self, emails):
    a = [x.split('@') for x in emails]
    b = [[x[0].split('+')[0].replace('.',''), x[1]] for x in a]
    c = Counter(["@".join(x) for x in b])
    return len(c)

a = ["test.email+alex@leetcode.com",
     "test.e.mail+bob.cathy@leetcode.com",
     "testemail+david@lee.tcode.com"]

s = Solution()
print(s.numUniqueEmails(a))
