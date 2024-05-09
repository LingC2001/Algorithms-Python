"""
Bellman Ford Complexity Analysis:

Time Complexity:
    We must perform V-1 iterations of checking all edges to guarantee correctness.
    Therefore time complexity is worst case: O(VE)
    We introducing early stopping for when no nodes gets distance improved.

Auxiliary Space complexity:
    O(V) for the dist/pred arrays

"""
import math

def bellman_ford(adj_list, start_node):
    """
    Performs Bellman-Ford algorithm to find the single source shortest path problem.
    Finds the shortest path to all nodes from a starting node.
    Slower than Dijkstra's but works for graphs with negative edges or negative cycles.

    Approach:
        We start by realising that a simple (no cycles) shortest path in a graph
        has at most V-1 edges.
        Therefore we can consider the following recurrrence relation:
            dp[i, v] = min(dp[i-1, v], dp[i-1, u] + w(u, v))
            - shortest path using AT MOST i edges is either:
                - the same as the shortest path using at most i-1 edges, or
                - if an incoming edge relaxation causes the shortest path/dist to reduce.
        
        Therefore if we perform V-1 iterations where we attempt to relax all edges,
        then we are guaranteed to find the shortest path to all nodes from source.
            - Note that we can stop the algorithm early if no more edges were updating during
            an iteration. 
        
            
        How to find negative cycles?
            - Since the above default Bellman-Ford algorthm can only find REACHABLE negative cycles from source,
                then we create a new source, and connect it with zero weight to all nodes in the graph, then
                perform bellman-ford from new source for V iterations, since we just added a node. 
                Now all nodes are reachable hence, all negative cycles can be detected.
                    - This is simplified to just doing bellman-ford again for V-1 iterations on the distances that
                    we got after the first V-1 iterations. Essentially done the first iteration with zero weights already.
        
            Since the shortest path is guaranteed to be found after V-1 iterations, if any
            distance values can be reduced after that then it must be affected by a negative cycle.
            Hence we perform V-1 iterations of edge relaxation again so that any negative cycle is guaranteed
            to propogate to all nodes it can reach. We change the distance of any nodes whose distance was
            reduced, to -inf/Error. And predecessor to None/Error. This marks any nodes that are affected
            by a negative cycle since there is no valid path.

        Space compelxity wise if we keep the whole DP memo table, then it would be O(V^2).
        However, since every row is only dependent on the previous row, then we only need to
        keep the last row in memory to do the alogrithm, hence O(V).
            - Note dist[v] during iteration i is not guaranteed to have the same value as dp[i, v]
            - This is because since we are only using a single dist array, and modifying it during the iterations,
            theres a chance that an edge relaxation uses a newly updated distance instead of the old i-1 distance.
            - Therefore iteration i's dist[v] <= dp[i, v]
            - Our answer does not get affected, since eventually we reach the same value of minimum dist,
                unless affected by negative cycle
        
        Reconstruction is done by keeping a decision/predecessor array.

    """
    num_nodes = len(adj_list)
    distance = [math.inf] * num_nodes
    predecessor = [None] * num_nodes
    distance[start_node] = 0

    def relax_edges(negative_cycle_detection=False):
        improved = False
        for u in range(num_nodes):
            for v, weight in adj_list[u]:
                # relax
                if distance[u] + weight < distance[v]:
                    if not negative_cycle_detection:
                        distance[v] = distance[u] + weight
                        predecessor[v] = u
                        improved = True
                    else:
                        # any edges that can be relaxed must be reachable from a negative cycle
                        distance[v] = -math.inf
                        predecessor[v] = None
                        improved = True

        return improved

    # perform V-1 iterations to guarantee correctness
    for _ in range(num_nodes - 1):
        if not relax_edges():
            break

    # second iteration of Bellman-Ford to detect negative cycles
    for _ in range(num_nodes - 1):
        if not relax_edges(True):
            break

    return distance, predecessor
