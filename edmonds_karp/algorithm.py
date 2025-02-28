class EdmondsKarp:
    def __init__(self, capacity):
        # Validate that all capacities are non-negative
        for row in capacity:
            for value in row:
                if value < 0:
                    raise ValueError("Capacity cannot be negative")
        
        self.capacity = capacity  # Graph capacity (adjacency matrix)
        self.n = len(capacity)    # Number of nodes in the graph

    # BFS function to find an augmenting path
    def bfs(self, source, sink, parent):
        visited = [False] * self.n  # Visitation markers
        queue = [source]            # Queue for BFS
        visited[source] = True      # Mark source as visited

        while queue:
            u = queue.pop(0)  # Get the first node from the queue

            for v in range(self.n):
                # We can only traverse edges with positive residual capacity
                if not visited[v] and self.capacity[u][v] > 0:
                    queue.append(v)     # Add to the end of the queue
                    visited[v] = True   # Mark as visited
                    parent[v] = u       # Store the parent node to reconstruct the path

                    if v == sink:
                        return True  # If we reached the sink, stop the search

        return False  # No augmenting path found

    # Function to compute the maximum flow
    def find_max_flow(self, source, sink):
        parent = [-1] * self.n  # To reconstruct the path
        max_flow = 0

        # While there is an augmenting path
        while self.bfs(source, sink, parent):
            path_flow = float('Inf')  # Path flow (initialized as infinity)
            s = sink

            # Find the maximum possible flow in the found path
            while s != source:
                p = parent[s]
                path_flow = min(path_flow, self.capacity[p][s])  # Minimum capacity in the path
                s = p

            # Update the capacities of the edges in the path
            v = sink
            while v != source:
                u = parent[v]
                self.capacity[u][v] -= path_flow  # Reduce capacity of the original edge
                self.capacity[v][u] += path_flow  # Increase capacity of the reverse edge
                v = u

            max_flow += path_flow  # Add the found flow to the total flow

        return max_flow
