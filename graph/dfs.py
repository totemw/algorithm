parent = {s: None}
def DFS_visit(V, Adj, s):
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            DFS_visit(V, Adj, v)

def DFS(V, Adj):
    parent = {}
    for s in V:
        if s not in parent:
            parent[s] = None
            DFS_visit(V, Adj, s)