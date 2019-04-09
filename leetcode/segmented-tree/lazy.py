class node_ap:

    def __init__(self, val=0):
        self.sum = val
        self.lazy = 0
        self.lazy_ap = 0

    def __repr__(self):
        if self.lazy and self.lazy_ap:
            return "[{}/{}/{}]".format(self.sum, self.lazy, self.lazy_ap)
        if self.lazy:
            return "[{}/{}]".format(self.sum, self.lazy)
        if self.lazy_ap:
            return "[{}/A{}]".format(self.sum, self.lazy_ap)
        return "[{}]".format(self.sum)


def merge(ln, rn):
    return node_ap(ln.sum + rn.sum)


class segment_tree_ap:
    def __init__(self, n, a):
        self.tr = [0] * (2*len(a) - 1)
        self.a = a

    def __repr__(self):
        # return str(self.tr[0])
        out = str(self.tr[0])
        ll, rr = 0, 0
        while True:
            ll = 2*ll+1
            rr = min(2*rr+2, len(self.tr)-1)
            out += "\n"
            out += ",".join([str(x) for x in self.tr[ll:(rr+1)]])
            if rr == len(self.tr)-1:
                break
        return out

    def update(self, ll, rr, idx):
        print("update l{} r{} i{} lst{}".format(ll, rr, idx, len(self.tr)))
        # constant factor
        if self.tr[idx].lazy:

            # add the constant amount
            self.tr[idx].sum += (rr-ll+1) * self.tr[idx].lazy

            # propagate down
            if ll != rr:
                self.tr[2*idx+1].lazy += self.tr[idx].lazy
                self.tr[2*idx+2].lazy += self.tr[idx].lazy

            # done with this level
            self.tr[idx].lazy = 0

        if self.tr[idx].lazy_ap:
            mid = (ll + rr) >> 1
            self.tr[idx].sum += ((rr-ll+1)*(rr-ll+2)/2)*self.tr[idx].lazy_ap
            if ll != rr:
                self.tr[2*idx+1].lazy_ap += self.tr[idx].lazy_ap
                self.tr[2*idx+2].lazy_ap += self.tr[idx].lazy_ap
                self.tr[2*idx+2].lazy += self.tr[idx].lazy_ap*(mid-ll+1)
            self.tr[idx].lazy_ap = 0

    def init(self, ll, rr, idx):
        # creates node repr range [ll, rr] at idx
        if ll == rr:
            self.tr[idx] = node_ap(self.a[ll])
            return
        mid = (ll + rr) >> 1
        self.init(ll, mid, 2*idx+1)
        self.init(mid+1, rr, 2*idx+2)
        self.tr[idx] = merge(self.tr[2*idx+1], self.tr[2*idx+2])

    def update_range(self, qL, qR, val, prog, ll, rr, idx):
        print("updater ql{} qr{} v{} p{} l{} r{} i{}".format(
            qL, qR, val, prog, ll, rr, idx))
        # update anyway
        self.update(ll, rr, idx)

        # range not touched
        if qL > rr or ll > qR:
            return

        # completely in range
        if qL <= ll and rr <= qR:
            self.tr[idx].lazy += val + (ll - qL) * prog
            self.tr[idx].lazy_ap += prog
            self.update(ll, rr, idx)
            return

        # partially in range
        mid = (ll + rr) >> 1
        self.update_range(qL, qR, val, prog, ll, mid, 2*idx+1)
        self.update_range(qL, qR, val, prog, mid+1, rr, 2*idx+2)
        self.tr[idx] = merge(self.tr[2*idx+1], self.tr[2*idx+2])

    def query(self, qL, qR, ll, rr, idx):
        '''
        [qL, qR] is the query range
        [ll, rr] is a range in the tree repr by a particular idx
        '''
        # [qL, qR] outside of the node's range
        if ll > qR or rr < qL:
            return node_ap()

        # partial overlap, requires update
        self.update(ll, rr, idx)

        # [ll, rr] completely covered by the range
        if qL <= ll and rr <= qR:
            return self.tr[idx]

        # partial overlap, need to look further down the tree
        mid = (ll + rr) >> 1
        return merge(
            self.query(qL, qR, ll, mid, 2*idx+1),
            self.query(qL, qR, mid+1, rr, 2*idx+2))


def main():
    n = 8
    t = segment_tree_ap(n, [0, 1, 2, 3, 4, 5, 6, 7])
    t.init(0, n-1, 0)
    t.update_range(2, 6, 1, 0, 0, len(t.tr)-1, 0)
    print(str(t.query(2, 6, 0, 7, 0)))


if __name__ == '__main__':
    main()
