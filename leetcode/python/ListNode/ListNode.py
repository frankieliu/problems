# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __repr__(self):
        out = []
        out.append(str(self.val))
        head = self.next
        while head:
            out.append(str(head.val))
            head = head.next
        return "->".join(out)

    def make(h):
        ll = []
        first = True
        for el in h:
            ll.append(ListNode(el))
        for i in range(0, len(ll)-1):
            ll[i].next = ll[i+1]
        if len(ll) == 0:
            return None
        return ll[0]


if __name__ == "__main__":
    ll = ListNode.make([1, 2, 3, 4, 5])
    print(ll)
