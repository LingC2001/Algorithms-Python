"""
Union Find Disjoint Set Complexity analysis

Time complexity:
    Find operation:
        It keeps going up the parent until we reach the root node, which has parent equal to itself.
        In the worst case, when it is a straight line, it could be O(n)

        However with path compression optimisation, where whenever we perform a find operation,
        all nodes along the path is connected directly to the root, so that next time finding which set
        one of the nodes belongs to would be O(1). On average this makes m operations take O(mlog(n)) time,
        which means each operation taking O(log(n)) time.

    Union operation:
        Notice that in the union operation, we first perform 2 find operations.
        We can also optimise the union operation by doing "Union by Rank" where the set 
        with a smaller rank is connected to the root of the set with the bigger rank. A rank
        of a set is the upper bound of it height/depth, since we don't update the rank when doing
        path compression, that means the actual height may be smaller than its rank.
        This creates more balanced trees, which again makes m operations take O(mlog(n)) time, 
        which means each operation taking O(log(n)) time. 

        There is also "Union by size" where the set with smaller number of nodes in it is 
        connected with the larger set.
    
    Combined together:
        It can be proved that with both of the above optimisations, the worst case time complexity of
        a sequence of m operations is O(m*alpha(n)), where alpha(n) is the inverse Ackermann function,
        an extremely slow growing function. Functionally this means each operation is O(1), which is
        alot better than O(log(n)).
    
Space complexity:
    O(n) for the parent list, and rank list.
    Also the recursion depth of the find function, which was shown to be O(log(n))
"""


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

    