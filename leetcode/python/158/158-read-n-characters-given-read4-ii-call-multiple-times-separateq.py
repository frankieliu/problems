#
# @lc app=leetcode id=158 lang=python3
#
# [158] Read N Characters Given Read4 II - Call multiple times
#
# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/description/
#
# algorithms
# Hard (25.31%)
# Total Accepted:    61.6K
# Total Submissions: 243.3K
# Testcase Example:  '"abc"\n[1,2,1]'
#
# Given a file and assume that you can only read the file using a given method
# read4, implement a method read to read n characters. Your method read may be
# called multiple times.
#
#
#
# Method read4:
#
# The API read4 reads 4 consecutive characters from the file, then writes those
# characters into the buffer array buf.
#
# The return value is the number of actual characters read.
#
# Note that read4() has its own file pointer, much like FILE *fp in C.
#
# Definition of read4:
#
#
# ⁠   Parameter:  char[] buf
# ⁠   Returns:    int
#
# Note: buf[] is destination not source, the results from read4 will be copied
# to buf[]
#
#
# Below is a high level example of how read4 works:
#
#
# File file("abcdefghijk"); // File is "abcdefghijk", initially file pointer
# (fp) points to 'a'
# char[] buf = new char[4]; // Create buffer with enough space to store
# characters
# read4(buf); // read4 returns 4. Now buf = "abcd", fp points to 'e'
# read4(buf); // read4 returns 4. Now buf = "efgh", fp points to 'i'
# read4(buf); // read4 returns 3. Now buf = "ijk", fp points to end of
# file
#
#
#
#
# Method read:
#
# By using the read4 method, implement the method read that reads n characters
# from the file and store it in the buffer array buf. Consider that you cannot
# manipulate the file directly.
#
# The return value is the number of actual characters read.
#
# Definition of read:
#
#
# ⁠   Parameters:    char[] buf, int n
# ⁠   Returns:    int
#
# Note: buf[] is destination not source, you will need to write the results to
# buf[]
#
#
#
#
# Example 1:
#
#
# File file("abc");
# Solution sol;
# // Assume buf is allocated and guaranteed to have enough space for storing
# all characters from the file.
# sol.read(buf, 1); // After calling your read method, buf should contain "a".
# We read a total of 1 character from the file, so return 1.
# sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2
# characters from the file, so return 2.
# sol.read(buf, 1); // We have reached the end of file, no more characters can
# be read. So return 0.
#
#
# Example 2:
#
#
# File file("abc");
# Solution sol;
# sol.read(buf, 4); // After calling your read method, buf should contain
# "abc". We read a total of 3 characters from the file, so return 3.
# sol.read(buf, 1); // We have reached the end of file, no more characters can
# be read. So return 0.
#
#
#
#
# Note:
#
#
# Consider that you cannot manipulate the file directly, the file is only
# accesible for read4 but not for read.
# The read function may be called multiple times.
# Please remember to RESET your class variables declared in Solution, as
# static/class variables are persisted across multiple test cases. Please see
# here for more details.
# You may assume the destination buffer array, buf, is guaranteed to have
# enough space for storing n characters.
# It is guaranteed that in a given test case the same buffer buf is called by
# read.
#
#
#
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.q = []
        self.is_end = False

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)

        The point is that you are requesting 'n' reads
        and you may either:
        1. read more than 'n' then you need to store
        2. if you read less than 'n' (end-of-file)
           need to return how much you've read

        read4       internal Q
        xxxx   --->

        internalQ        buf[] (output buffer)
        qqqqq      --->  bbbb
        """
        idx = 0
        old_n = n
        while n>0:
            if self.is_end:
                s = 0                  # s is the number of characters read
            else:
                buf4 =[""]*4
                s = read4(buf4)
                if s < 4:              # if you read less than 4 at end
                    self.is_end = True
                for i in range(s):     # add what you read to q
                    self.q.append(buf4[i])

            while self.q:
                t = self.q.pop(0)
                buf[idx] =  t          # add what you read to buf[]
                idx += 1
                n -= 1
                if n == 0:             # if you have read enough
                    return old_n       # exit

            if self.is_end:
                return idx             # if reached end of file return what was read

        return old_n
