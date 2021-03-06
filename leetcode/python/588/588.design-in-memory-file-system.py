#
# @lc app=leetcode id=588 lang=python3
#
# [588] Design In-Memory File System
#
# https://leetcode.com/problems/design-in-memory-file-system/description/
#
# algorithms
# Hard (38.24%)
# Total Accepted:    4.8K
# Total Submissions: 12.5K
# Testcase Example:  '["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]\n[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]'
#
# Design an in-memory file system to simulate the following functions:
#
# ls: Given a path in string format. If it is a file path, return a list that
# only contains this file's name. If it is a directory path, return the list of
# file and directory names in this directory. Your output (file and directory
# names together) should in lexicographic order.
#
# mkdir: Given a directory path that does not exist, you should make a new
# directory according to the path. If the middle directories in the path don't
# exist either, you should create them as well. This function has void return
# type.
#
# addContentToFile: Given a file path and file content in string format. If the
# file doesn't exist, you need to create that file containing given content. If
# the file already exists, you need to append given content to original
# content. This function has void return type.
#
# readContentFromFile: Given a file path, return its content in string
# format.
#
#
#
# Example:
#
#
# Input:
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
#
# Output:
# [null,[],null,null,["a"],"hello"]
#
# Explanation:
#
#
#
#
#
# Note:
#
#
# You can assume all file or directory paths are absolute paths which begin
# with / and do not end with / except that the path is just "/".
# You can assume that all operations will be passed valid parameters and users
# will not attempt to retrieve file content or list a directory or file that
# does not exist.
# You can assume that all directory names and file names only contain
# lower-case letters, and same names won't exist in the same directory.
#
#
#
from typing import List
from pprint import PrettyPrinter

class FileSystem:
    """
    a directory is not a file
    a directory contains files and other directories
    a file is a file
    """
    def __init__(self):
        # filesystem
        # with root directory

        self.root = {
            'name': '/',
            'isFile': False,
            'content': {}
        }

    def descend(self, path):
        """
        returns the 'leaf'
        """
        if path == '/':
            return self.root, []
        p = self.root
        sub = path.split('/')[1:]
        nprev = self.root
        for i, el in enumerate(sub):
            if el in p['content']:
                if p['content'][el]['isFile']:
                    return p['content'][el], []
                else:
                    nprev = p
                    p = p['content'][el]
            else:  # did not find
                return p, sub[i:]
        return p, []

    def ls(self, path: str) -> List[str]:
        cur, rem = self.descend(path)
        if cur['isFile']:
            return [cur['name']]
        else:
            return list(sorted(cur['content'].keys()))

    def mkdir(self, path: str) -> None:
        cur, rem = self.descend(path)
        for x in rem:
            cur['content'][x] = {
                'name': x,
                'isFile': False,
                'content': {}
            }
            cur = cur['content'][x]

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur, rem = self.descend(filePath)
        # print("cur:{} rem:{}".format(cur,rem))
        if len(rem) == 0:   # file exists
            cur['content']['text'] += content
        elif len(rem) == 1:  # file does not exist
            cur['content'][rem[0]] = {
                'name': rem[0],
                'isFile': True,
                'content': {
                    'text': content
                }
            }
        else:
            print("Non-existing path: {}".format(filePath))

    def readContentFromFile(self, filePath: str) -> str:
        cur, rem = self.descend(filePath)
        # print("cur:{} rem:{}".format(cur,rem))
        if len(rem) == 0:
            return cur['content']['text']
        print("Non-existing path: {}".format(filePath))
        return ""

test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*1
    if case[0]:
        obj = FileSystem()
        print(obj.ls('/'))
        obj.mkdir('/a/b/c')
        print(obj.ls('/'))
        print(obj.ls('/a'))
        print(obj.ls('/a/b'))
        print(obj.ls('/a/b/c'))
        obj.addContentToFile('/a/b/c/d', 'hello ')
        obj.addContentToFile('/a/b/c/d', 'good bye ')
        print(obj.readContentFromFile('/a/b/c/d'))
        pp = PrettyPrinter(depth=10)
        # pp.pprint(obj.root)
        # print(obj.descend('/a/b/c'))
        # param_1 = obj.ls('/')
        # obj.mkdir('/a/b/c')
        # obj.addContentToFile('/a/b/c/d','hello')

        # print(param_1, param_4)
