def explore(graph,current,visited=set()):

    if current in visited:
        return 0

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph,neighbor,visited)
    
    return 1


graph = {
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]
}

visited = set()
count = 0
for i in graph:

    if(explore(graph,i,visited) == 1):
        count+=1

print(count)
    
