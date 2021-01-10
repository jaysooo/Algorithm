

class UnionFind():
    parent = []
    friend_idx = dict()
    childCnt = []
    friend_seq = 1

    def __init__(self):
        self.parent = [i for i in range(0, 1000000)]
        self.childCnt = [i for i in range(0, 1000000)]

    def friend_idx_get(self, name=''):

        if name not in self.friend_idx:
            self.friend_idx[name] = self.friend_seq
            idx = self.friend_seq
            self.friend_seq += 1
        else:
            idx = self.friend_idx[name]
        return idx

    def getParent(self, p):

        if self.parent[p] == p:
            return p

        self.parent[p] = self.getParent(self.parent[p])
        return self.parent[p]

    def unionParent(self, a, b):
        unionSum = self.getParentCnt(a)+self.getParentCnt(b)
        a = self.getParent(a)
        b = self.getParent(b)

        if (a < b):
            self.parent[b] = a
            self.childCnt[a] = unionSum
        else:
            self.parent[a] = b
            self.childCnt[b] = unionSum
          #  self.childCnt[b] = self.getParentCnt(b)

    def findTotalFriendCnt(self, a):
        a = self.getParent(a)
        return self.childCnt[a]

    def getParentCnt(self, a):
        a = self.getParent(a)
        cnt = 0
        for i in (self.parent):
            if i == a:
                cnt += 1

        return cnt


def main():
    T = int(input())

   # uf = UnionFind()
    for i in range(0, T):
      F = int(input())
      uf = UnionFind()
      for j in range(0, F):
        fr = input().split(' ')
        #    print(fr)
        a = uf.friend_idx_get(fr[0])
        b = uf.friend_idx_get(fr[1])
        uf.unionParent(a, b)
        print(uf.findTotalFriendCnt(a))

    # uf.unionParent(1, 2)
    # uf.unionParent(3, 4)
    # uf.unionParent(2, 3)
    # print(uf.findTotalFriendCnt(2))


if __name__ == '__main__':
    main()
