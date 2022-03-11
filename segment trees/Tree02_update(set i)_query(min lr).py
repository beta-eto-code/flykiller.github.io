# this segment tree will support two operations:
# 1. Set element i equal to v.
# 2. Find min of elements in range [r, l)
# difference from previous tree: replace sum with min and also replace 0 with inf in line 43

class SegmentTree:
    def __init__(self, n, arr):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.T = [0] * (2 * self.size - 1)
        self.arr = arr

    def _build(self, x, lx, rx):
        if rx - lx == 1:
            if lx < len(self.arr):
                self.T[x] = self.arr[lx]
        else:
            mx = (lx + rx)//2
            self._build(2*x+1, lx, mx)
            self._build(2*x+2, mx, rx)
            self.T[x] = min(self.T[2*x+1], self.T[2*x+2])

    def build(self):
        self._build(0, 0, self.size)

    def _set(self, i, v, x, lx, rx):
        if rx - lx == 1:
            self.T[x] = v
            return
        mx = (lx + rx) // 2
        if i < mx:
            self._set(i, v, 2 * x + 1, lx, mx)
        else:
            self._set(i, v, 2 * x + 2, mx, rx)
        self.T[x] = min(self.T[2 * x + 1], self.T[2 * x + 2])

    def set(self, i, v):
        self._set(i, v, 0, 0, self.size)

    def _min(self, l, r, x, lx, rx):
        if l >= rx or lx >= r:
            return float("inf")
        if lx >= l and rx <= r:
            return self.T[x]
        mx = (lx + rx) // 2
        s1 = self._min(l, r, 2 * x + 1, lx, mx)
        s2 = self._min(l, r, 2 * x + 2, mx, rx)
        return min(s1, s2)

    def min(self, l, r):
        return self._min(l, r, 0, 0, self.size)


if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    STree = SegmentTree(n, arr)
    STree.build()

    for i in range(m):
        t = [int(i) for i in input().split()]
        if t[0] == 1:
            STree.set(t[1], t[2])
        else:
            print(STree.min(t[1], t[2]))