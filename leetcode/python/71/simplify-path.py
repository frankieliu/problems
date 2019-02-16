"""71. Simplify Path
Medium

334

1011

Favorite

Share

Given an absolute path for a file (Unix-style), simplify it. Or in
other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current
directory. Furthermore, a double period .. moves the directory up a
level. For more information, see: Absolute path vs relative path in
Linux/Unix

Note that the returned canonical path must always begin with a slash
/, and there must be only a single slash / between two directory
names. The last directory name (if it exists) must not end with a
trailing /. Also, the canonical path must be the shortest string
representing the absolute path.



Example 1:

Input: "/home/"
Output: "/home"

Explanation: Note that there is no trailing slash after the last
directory name.

Example 2:

Input: "/../"
Output: "/"

Explanation: Going one level up from the root directory is a no-op, as
the root level is the highest level you can go.

Example 3:

Input: "/home//foo/"
Output: "/home/foo"

Explanation: In the canonical path, multiple consecutive slashes are
replaced by a single one.

Example 4:

Input: "/a/./b/../../c/"
Output: "/c"

Example 5:

Input: "/a/../../b/../c//.//"
Output: "/c"

Example 6:

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"

Accepted
137,350
Submissions
493,049
"""


from collections import deque

class Solution:
    def simplifyPath(self, p):
        """
        :type path: str
        :rtype: str
        """
        dq = deque()
        for a in p.split("/"):
            if a == "." or a == "":
                continue
            if a == "..":
                if dq:
                    dq.pop()
            else:
                dq.append(a)

        out = []
        while dq:
            el = dq.popleft()
            out.append(el)

        return "/" + "/".join(out)

s = Solution()

print(s.simplifyPath("/home/"))
print(s.simplifyPath("/../"))
print(s.simplifyPath("/home//foo/"))
print(s.simplifyPath("/a/./b/../../c/"))
print(s.simplifyPath("/a/../../b/../c//.//"))
print(s.simplifyPath("/a//b////c/d//././/.."))
