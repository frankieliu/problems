
Python 3 solution beats 94% speed, 78% space

https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/256180

* Lang:    python3
* Author:  csush
* Votes:   0

Thoughts: This code is not very scalable, but it works well within the scope of this problem ;). It generates a random 6 character string and checks if it exists in dict values. But once the dict becomes extremely large our while loop in encode will become very slow. This may be improved by dynamically increasing the string length returned by generate_shortUrl as it detects the number of values in our dict.

```
import string
import random

class Codec:
    
    def __init__(self):
		# dict to store all longUrl to shortUrl mappings
        self.long_to_short = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
		# Test if mapping already exists
        if longUrl in self.long_to_short.keys():
            return self.long_to_short[longUrl]
        
		# Generate random 6 character string for tinyUrl
        def generate_shortUrl():
            all_chars = string.ascii_letters + string.digits
            shortUrl = "".join(random.choice(all_chars) for x in range(6))
            return shortUrl
        
		# Keep generating new shortUrl till it finds one that doesn\'t exist in our dict
        shortUrl = generate_shortUrl()
        while shortUrl in self.long_to_short.values():
            shortUrl = generate_shortUrl()
        
		# map
        self.long_to_short[longUrl] = shortUrl
        
        return shortUrl
                

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
		# Simple mapping
        for k, v in self.long_to_short.items():
            if v == shortUrl:
                return k
        return None
```
