
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
    
    def union(self, x, y):
        """
        The union operartion using union by rank optimization.
        Joins the disjoint sets x and y into one set. 
        """
        x = self.find(x)
        y = self.find(y)
        if x != y: # if it is not the same disjoint set
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
            else:
                self.parent[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def find(self, x):
        """
        The find operartion with path compression optimization.
        Finds the representative of the disjoint set that 'x' is in 
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    