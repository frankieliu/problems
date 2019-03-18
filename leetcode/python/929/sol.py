
Python ~10 lines ~ easy to understand

https://leetcode.com/problems/unique-email-addresses/discuss/254862

* Lang:    python3
* Author:  nicolime
* Votes:   1

```
class Solution:
    def numUniqueEmails(self, emails):
        uniques = set() # A set can not contain duplicates
        for email in emails:
            name, domain = email.split("@")
            if "+" in name:
                name = name.split("+")[0].replace(".", "") # grab everything before "+", remove "."
            else:
                name = name.replace(\'.\', "") # remove "."
            cleanEmail = name + "@" + domain # reassemble emails
            uniques.add(cleanEmail) # add cleanEmail to set, which will not accept duplicates
        return len(uniques) # return length of uniques to get number of uniques
```
