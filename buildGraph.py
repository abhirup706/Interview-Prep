def buildGraph(edges):
    graph = {}

    for i in edges:
        a,b = i

        if(a not in graph):
            graph[a] = []
        if(b not in graph):
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


def hasPath(graph,src,dest,visitedNodes=set()):

    #print(src)
    if (src==dest):
        #print('1')
        return 1
    #if src in visitedNodes:
    #    return 0
    
    visitedNodes.add(src)

    for neighbours in graph[src]:
        #print(neighbours)
        if neighbours not in visitedNodes:
            #visitedNodes.add(neighbours)
            if(hasPath(graph,neighbours,dest,visitedNodes) == 1):
                return 1

    return 0


edges = [('i','j'),('k','i'),('m','k'),('k','l'),('o','n')]

print(buildGraph(edges))

print(hasPath(buildGraph(edges),'i','o'))