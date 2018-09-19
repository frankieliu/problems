
def findpath(graph, start, stop):
    print("visiting: ", start)

    if graph[start]['v'] != False:
        return graph[start]['v']

    if start == stop:
        print("Found stop: ", stop)
        return [[start]]

    neighbor = graph[start]['n']
    # DFS
    paths = []
    for n in neighbor:
        if n == stop:
            paths.append([start, n])
        else:
            p = findpath(graph, n, stop)
            if p:
                paths = paths + [[start] + x for x in p]
    graph[start]['v'] = paths
    return paths

graph = {'A': {'n': ['B', 'C'], 'v': False},
         'B': {'n': ['C', 'D'], 'v': False},
         'C': {'n': ['D'], 'v': False},
         'D': {'n': ['C'], 'v': False},
         'E': {'n': ['F'], 'v': False},
         'F': {'n': ['C'], 'v': False}}

# find all the paths from a to d
start = 'A'
stop = 'D'

print(findpath(graph, start, stop))
