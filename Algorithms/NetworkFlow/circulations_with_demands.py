"""
Circulation with Demands and Lower bounds Complexity Analysis

Time complexity:
    Constructing graphs takes O(V^2)
    Therefore time complexity is domianted by Ford-Fulkerson's O(E*max_flow)
    Unless max_flow is low and graph is sparse, then domianted by O(V^2)

Space complexity:
    Dominated by constructing new graph G* O(V + E)
    and output solution circ_graph. O(V^2)
"""


from ford_fulkerson import ford_fulkerson
def circulations_with_demands(graph, demands):

    """
    Solves the Circulation with demands and lower bounds problem.


    param Graph: A NxN matrix each containing tuples representing edges in
                    the network flow graph. In the form of (lower, cap), None = No edge
    param demands: A list representing the demands of every vertex
    
    
    returns:
        False if there is no solution that meet the constraints
        The resulting flow graph that meets the demands of every node.
    
    # Approach:
        1. Assume the graph starts with every edge with the lower bound flow, and
        construct new graph G* with no lower bounds but demands and edge capacity changed:
            d* = d - incoming_flow + outgoing_flow
            cap* = cap - lower bound flow
        
        2. Solve circulations with demands on this new graph G* by 
        connecting all nodes with positive demand to a super sink with the demand as the edge cap.
        connecting all nodes with negative demand to a super source with -demand as the edge cap.
        Perform Ford-Fulkerson's to find max flow.
        
        3. Check if all outgoing edges of super source or all incoming edges of super sink
        are saturated. If saturated delete super sink and super source and you have the solution.
        If not all saturated, then return False as no solutions exist.
        
    """
    # checking initial demand constriants
    total_demand = 0
    for i in range(len(demands)):
        total_demand += demands[i]
    if total_demand != 0:
        return False

    # Construct new G* graph
    n = len(graph)
    demands_star = [x for x in demands]
    G_star = [[] for _ in range(n)]
    
    # update capacities and demands
    for u in range(n):
        for v in range(n):
            if graph[u][v] is not None:
                e = graph[u][v]
                lower = e[0]
                cap = e[1]
                G_star[u].append((v, cap-lower))
                demands_star[u] += lower
                demands_star[v] -= lower
    # Add a new node for super source and super sink at the end as vertex n and vertex n+1
    G_star.append([])
    G_star.append([])
    source = n
    sink = n+1
    # Add new edges with demand values
    for u in range(n):
        if demands_star[u] < 0:
            G_star[source].append((u, -demands_star[u]))
        elif demands_star[u] > 0:
            G_star[u].append((sink, demands_star[u]))
    # Solve maximum flow with Ford-Fulkerson's
    max_flow, res_graph = ford_fulkerson(G_star, source, sink)

    # check all outgoing edges of source are saturated
    for e in res_graph[source]:
        if e.flow != e.cap:
            return False
    # Remove super sink and super and create final solution cirulation graph
    circ_graph = [[None]*n for _ in range(n)]

    for u in range(n):
        for e in res_graph[u]:
            v = e.v
            if v < n and not e.is_back_edge and graph[u][v] is not None:
                lb_flow = graph[u][v][0]
                circ_graph[u][v] = (e.flow+ lb_flow, e.cap + lb_flow)
    
    return circ_graph



