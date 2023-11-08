def bridges(G: 'graph represented by adjacency lists'):
    n = len(G)
    low = [0] * n
    times = [0] * n
    time = 0
    
    def dfs(u, parent):
        nonlocal time
        time += 1
        low[u] = times[u] = time
                
        for v in G[u]:
            # when there is no visit time, a vertex hasn't been yet visited
            if not times[v]:
                dfs(v, u)
                # If we have a cycle, we must update the low value of the parent vertex
                if low[v] < low[u]: low[u] = low[v]
            # v cannot be a parent of u as it's obvious it will always be visited before
            # and connected to the vertex u which doesn't imply that we have a trailing edge
            elif v != parent:  
                # We have a back edge (we try to enter a vertex which was entered before)
                if times[v] < low[u]: low[u] = times[v]
    
    # I assume that dwarfs' cave is in the 0 vertex
    dfs(0, -1)
            
    return times, low