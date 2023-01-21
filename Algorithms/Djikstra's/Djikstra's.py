from collections import defaultdict
from heapq import *

def dijkstra_revised(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    # dist records the min value of each node in heap.
    q, seen, dist = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 in seen: continue

        seen.add(v1)
        path += (v1,)
        if v1 == t: return (cost, path)

        for c, v2 in g.get(v1, ()):
            if v2 in seen: continue

            # Not every edge will be calculated. The edge which can improve the value of node in heap will be useful.
            if v2 not in dist or cost+c < dist[v2]:
                dist[v2] = cost+c
                heappush(q, (cost+c, v2, path))

    return None

if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

print("=== Dijkstra ===")
print(edges)
print("A -> E:")
print(dijkstra_revised(edges, "A", "E"))
print("F -> G:")
print(dijkstra_revised(edges, "F", "G"))