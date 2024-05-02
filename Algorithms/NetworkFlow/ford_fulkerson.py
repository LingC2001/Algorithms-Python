"""
Ford-Fulkerson method complexity analysis:

Time complexity:
    Each DFS to find a augmenting path could take O(V+E), if using adj_list.
    Each augmenting path may only increase the flow by the minimum of 1 unit of flow.
    Therefore time complexity: O(E*max_flow)

Auxiliary Space complexity:
    If using adj_list:
        O(V+E) 
    If using adj_matrix or residual matrix:
        O(V^2)

"""
class edge:
    """
    note this could also be done using normal adj_list.
    each edge could be in the form of (v, cap, flow, back).
    The pointer to the back edge is crucial to avoid O(V) searching.
    """
    def __init__(self, v, cap, flow=0, back=None):
        self.next = v
        self.cap = cap
        self.flow = flow
        self.back = None

def ford_fulkerson(adj_list, source, sink):
    """
    Perfroms Ford-Fulkersons's method for determining maximum flow in a network

    Some definitions:
        Residual network: A graph G_f that has a forward edge and backward edge for
        each edge in the original graph G. The forward edge will be the residual capacity
        = edge capacity - current flow. And back edge will have negative flow of the forward edge.
        
        Augmenting paths: Paths from source (s) to sink (t) that consists of only non-full
        forward edges, or non-empty backward edges.

        Bottleneck: The maximum amount of extra flow we can push through the augmenting path

    Approach:
        1. Set initial flow of all edges to 0.
        2. Building residual graph:
            - two ways to do this, we can create an edge structure that has the following:
                    e.capacity (capacity of edge), where reverse edges have capacity = 0
                    e.flow (current flow value)
                    e.reverse (pointer to opposite edge),
                with this, the residual of any forward/reverse edge is just:
                    e.capacity - e.flow
                Whenever we find an augmenting path, we will do the following updates:
                    e.flow += augment amount
                    e.reverse.flow -= augment amount
                Aux space complexity: O(3E)
                We also only store the residual instead of cap and flow, so O(2E)
                    
            - The other way to store these information would be using adjacency matrix.
                We will have one adjacency matrix representing the capacity of all edges
                We will then have another adjacency matrix representing the flow of all edges.
                With this, the residual of any edge u->v would be:
                    cap[u][v] - flow[u][v]
                When augmenting path is found, we will do the following updates:
                    flow[u][v] += augment amount (this results in residual -= augment amount)
                    flow[v][u] -= augment amount (this results in residual += augment amount)
                Aux Space complexity: O(2V^2)

            - Third method, we can just keep a single residual adjacency matrix.
                Whenever we augment through an edge u->v
                    residual[u][v] -= augment
                    residual[v][u] += augment
                Aux Sapce complexity: O(V^2)
                However, note that using adj_matrix makes dfs traversal O(V^2)
        
        3. Repeatedily Use DFS or BFS to find an augmenting path from s->t.
            - Until no more augmenting paths are found
            - Using BFS instead of DFS is called the Edmonds-Karp algorithm,
            which has a better runtime complexity of O(VE^2), as it find the
            shortest augmenting path instead of a "random" one.
            
    """
    n = len(adj_list)
    
    # creating residual graph with custom edge structure for storing flow
    res_graph = [[] for i in range(n)]
    for u in range(n):
        for e in adj_list[u]:
            v = e[0]
            cap = e[1]
            new_edge = edge(v, cap, flow=0, back=None)
            back_edge = edge(u, 0, flow=0, back=new_edge)
            new_edge.back = back_edge

            res_graph[u].append(new_edge)
            res_graph[v].append(back_edge)

    # repeated augmenting path until max_flow cannot be increased
    max_flow = 0
    augment = 1
    while augment > 0:
        visited = [False]*n
        augment = dfs(res_graph, visited, source, sink, float('inf'))
        max_flow += augment
    
    return max_flow


def dfs(res_graph, visited, u, sink, bottleneck):
    if u == sink: # if sink found: augmenting path is found, return bottleneck for residual updating
        return bottleneck
    visited[u] = True

    for e in res_graph[u]:
        v = e.next
        residual = e.cap - e.flow
        
        # if edge still has residual and we have not visited yet, continue dfs this path
        if residual > 0 and not visited[v]: 
            # continue dfs, but notice bottleneck is updated, we keep the minimum residual of the path
            augment = dfs(res_graph, visited, v, sink, min(bottleneck, residual))

            # if augmenting path was found down this path:
            if augment > 0:
                e.flow += augment
                e.back.flow -= augment
                return augment
    
    # if no augmenting path was found down this path
    return 0