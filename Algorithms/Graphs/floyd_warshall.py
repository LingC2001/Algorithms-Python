"""
Floyd Warshall complexity analysis:

Time complexity:
    Simply 3 nested for loops each iterating V times, hence O(V^3)
    The post processing step to find negative cycle also is O(V^3)
    Hence: O(V^3)

    In comparison to other methods for all-pairs shortest paths:
        - For unweighted graphs, we could do BFS for every node.
            = O(V(V+E)) = O(VE) = O(V^2) for sparse, O(V^3) for dense
        - For weighted graphs (no negative weights), we could do Dijkstra's for every node.
            = O(VELog(V)) = O(V^2Log(V)) for sparse, O(V^3Log(V)) for dense
        - For weighted graphs with negative weights, we can do repreated Bellman-Ford
            = O(V^2 E) = O(V^3) for sparse, O(V^4) for dense
    Hence Floyd-Warshall is very good for dense graphs in all situations, 
    but repeated BFS or repeated Dijkstra's is better for sparse graphs
            
Auxiliary Space complexity:
    The DP memo table of dist and succ are both O(V^2)
    This is the space saving version.
    O(V^2)

"""


def floyd_warshall(adj_list):
    """
    Performs floyd warshall algorithm on the given graph to find the
    all-pairs shortest paths. The shortest path from any node to any other node
    is calculated.

    Idea:
        - Similar to Bellman-Ford, where we first considered paths with at most 1 edge, then
        paths with at most 2... until V-1 edges.
        - Instead this algorithm finds the shortest distance using only intermediate node v1, then
        finds shortest paths using only intermediate nodes v1,v2 etc.
            - By the end of the algorithm, we will have the shortest distances from any node i 
            to any node j, using any intermediate nodes. (which is the answer)

    The idea is that we can utilise dynamic programming where dp[k][u][v] stores the
    shortest path from u to v routing from nodes 0-k.
    Therefore the recurrence relation for next value of k would be:
        dp[k][u][v] = min(dp[k-1][u][v], dp[k-1][u][k] + dp[k-1][k][v])
            - the first element is if the minimum doesn't use the edge k->v.
                if routing through node k to go to v does not give a shorter path, then we just stay
                with the path we had routing through any nodes in {1, 2, .., k-1}
            - the second element is if the minimum uses the edge k->v
                if routing through node k to go v DOES give a shorter path than what we previous found
                using only nodes {1, 2, .., k-1}, then update the distance/path
            
    
    Negative cyles just means we can get from vertex v to v itself again with a negative value.
    Therefore we just check the diagonal of the matrix to see if any nodes have negative distance value
    to itself.            

    The path can be reconstructed by keeping a VxV successor matrix succ, 
        where succ[u][v] = next node after u on the shortest path to v
    
    Upadating successors/paths:
        Consider a case where path from u->v was u->x->y->v
            and shortest u->k was u->z->k
        During the iteration where we consider k as an intermediate node, if we find that
        routing through k (u->z->k->v) was shorter than not routing through k (u->x->y->v),
        then we would need to update the sucessors.
        We can do this by simply setting succ[u][v] = succ[u][k]
            in this case it would set succ[u][v] = z,
            and then the path is found by now getting the value succ[z][v], which is k in this case
        

    We notice that each k value only uses values from previous value of k, therefore
    instead of keeping a whoel 3D VxVxV memo table, we can just keep a constantly updating
    2D table. 

    :param adj_list: Adjacency list representation of the graph.

    Note that this algorithm consructs a NxN dist matrix. This has the same initial
    elements as an adjacency matrix, except non-exitent edges must be represented as +inf.
    
    """
    # initialise a nxn dist matrix. 
    inf = float('inf')
    n = len(adj_list)
    dist = [[inf]*n for i in range(n)]
    succ = [[None]*n for i in range(n)] # succ[u][v] = successor/next node of u on shortest path to v

    # initialising initial values
    for u in range(n):
        dist[u][u] = 0 # dist to itself = 0
        succ[u][u] = u # succ to itself
        for e in adj_list[u]:
            v = e[0]
            w = e[1]
            dist[u][v] = w # initial dist from u->v = edge weight
            succ[u][v] = v # initially assume shortest path is from u->v for every edge


    # Floyd-Warshall
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if dist[u][k]+dist[k][v] < dist[u][v]:
                    dist[u][v] = dist[u][k]+dist[k][v]
                    succ[u][v] = succ[u][k]
    

    # detecting negative cycles:
    # if the distance to itself is negative, then it must have been affect by a negative cycle.
    # therefore consider any intermediate node k.
    # if the shortest distance from k->k is negative, then it must be part of a negative cycle
    # hence if there is a path that goes from u->v through k, then the min dist of u->v = -inf
    # to check this we, just check if dist[u][k] = inf or dist[k][v] = inf

    for k in range(n):
        if dist[k][k] < 0: # node k is apart of a negative cycle
            for u in range(n):
                for v in range(n):
                    if dist[u][k] != inf and dist[k][v] != inf:
                        dist[u][v] = -inf

    return dist, succ

def get_path(dist, succ, u, v):
    inf = float('inf')
    if dist[u][v] == inf: # not connected
        return None
    elif dist[u][v] == -inf: # affected by negative cycle, hence invalid path
        return -1
    else:
        path = [u]
        while u != v:
            u = succ[u][v]
            path.append(u)
        return path
