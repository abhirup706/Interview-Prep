def explore(graph,current,visited,nodeCnt=0):
    if current in visited:
        return 0
    
    visited.add(current)
    nodeCnt = 1
    for neighbor in graph[current]:
        #nodeCnt = nodeCnt+1
        nodeCnt += explore(graph,neighbor,visited,nodeCnt)
        
    return nodeCnt

graph = {
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]
}


nodeCnt = 0
visited=set()
largest = 0
for i in graph:
    nodeCnt = 0
    nodeCnt= explore(graph,i,visited,nodeCnt)
    largest=max(largest,nodeCnt)


print(largest)
        




