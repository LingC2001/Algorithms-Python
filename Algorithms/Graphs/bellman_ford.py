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
