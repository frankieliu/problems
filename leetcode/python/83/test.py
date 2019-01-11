from solution import Solution, ListNode

s = Solution()
ln = ListNode(1)
a = ListNode(1)
ln.next = a
b = ListNode(2)
a.next = b
b.next = None

s.deleteDuplicates(ln)
m = ln
while m:
    print(m.val)
    m = m.next
