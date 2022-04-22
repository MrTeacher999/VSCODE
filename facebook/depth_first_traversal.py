


from msilib.schema import Component
from turtle import distance, position


graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}





def dfs(node,visited,graph):
    if(node not in visited):
        visited.add(node)
        print(node)
        for neighbor in graph[node]:
            dfs(neighbor,visited,graph)





# Now lets try bfs


visiteda = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
    visiteda.append(node)
    queue.append(node)
    while queue:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visiteda.append(neighbor)
                queue.append(neighbor)





 # the iterative and queue approach

visitedlist = []
queue = []

       






# this is a recursive approach 

visited = set()

def dfs (node,visited,graph):
    if node not in visited:
        visited.add(node)
        print(node)
        for neighbor in graph[node]:
            dfs(neighbor,visited,graph)









visited = set()

def dfs_has_path(node,visited,graph,destination):
    if node == destination:
        return True
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == destination:
                return True
            return dfs_has_path(neighbor,visited,graph,destination)
    
    return False


print(dfs_has_path("A",visited,graph,"D"))



def convert_edges_to_adjacency(edges):
    mygraph ={}
    for edge in edges:
        a, b = edge
        if a not in mygraph:
            mygraph[a] = []
        if b not in mygraph :
            mygraph[b] = []
        mygraph[a].append(b)
        mygraph[b].append(a)
    return mygraph


print(convert_edges_to_adjacency(([1,3],[2,3],[3,6])))


visited = set()


  # iterative queue

visited = []
myqueue = []
def bfs(visited,node,graph):
    myqueue.append(node)
    while(myqueue):
        current = queue.pop(0)
        print(current)
        for neighbors in graph[current]:
            if neighbors not in visited:
                myqueue.append(neighbors)
                visited.append(neighbors)

# recursive


def dfs_has_path(node,visited,graph,destination):
    if node == destination:
        return True
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == destination:
                return True
            return dfs_has_path(neighbor,visited,graph,destination)
    
    return False



def convert_edges_to_adjacency(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    
    return graph 


def find_path_in_undirected(edges,start,destination):
    visited = set()
    ourgraph = convert_edges_to_adjacency(edges)
    return haspath(visited,graph,start,destination)


def haspath(visited,graph,source,destination):
    if source == destination:
        return True
    if source not in visited:
        for neighbor in graph[source]:
            if haspath(visited,graph,neighbor,destination) == True:
                return True
    return False



def connected_components(graph):
    visited = set()
    count = 0
    for keys in graph:
        if (explore(graph,keys,visited) == True):
            count +=1
        


def explore(graph,current,visited):

    if str(current) in visited:
        return False
    visited.add(str(current))
    for neighbors in graph[current]:
        explore(graph,neighbors)
    return True
    


def largestcomp(graph):
    size = 0
    for keys in graph:
        size = max(exploresize(graph,keys,size),size)
    return size


visited = set()
def exploresize(graph,node,visited):
    if(node in visited):
        return 0
    visited.add(node)
    size  = 1
    for neighbor in graph[node]:
        size += exploresize(graph,node,visited)
    return size






def connected_components(graph):
    visited = set()
    number_of_components = 0
    for keys in graph:
        number_of_components +=explore_component(graph,keys,visited)
    return number_of_components



def explore_component(graph,node,visited):
    if node in visited:
        return 0
    visited.add(node)
    for neighbor in graph[node]:
        explore_component(graph,neighbor,visited)
    return 1

mygraph = {
    0:[8,1,5],
    1:[0],
    2:[3,4],
    3:[2,4],
    4:[3,2],
    5 :[0,8],
    8: [0,5]
}
print(connected_components(mygraph))
    

def largest_components(graph):
    visited = set()
    max_component = 0
    for keys in graph:
        max_component = max(size_component(graph,keys,visited),max_component)
    return max_component



def size_component(graph,node,visited):

    if node in visited:
        return 0
    visited.add(node)
    size = 1
    for neighbor in graph[node]:
        size +=explore_component(graph,neighbor,visited)
    return size



myqueue = []
visited = set()

def bfs_shortest(graph,node,visited):
    queue.append(node)
    visited.append(node)
    if queue:
        current = queue.pop(0)
        visited.add(node)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                
                
def shortest_path(graph,start,end):
    visited = set()
    queue = [[start,0]]
    visited.add(start)
    while (queue):
        curr, distance = queue.pop(0)
        if curr == end:
            return distance
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor,distance+1])
    return -1

def convert_edges_to_adjacency(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


def Island_count(grid):
    visited = set()
    count = 0
    for row in grid:
        for column in grid[row]:
            if explore_island(grid,row,column,visited) == True:
                count +=1
    return count 




def explore_island(grid,row,column,visited):
    if (not (row >= 0 and row <= len(grid))) or (not(column>=0 and column<=len(grid[0]))):
        return False
    if grid[row][column]== 0:
        return False
    position = row,",",column
    if position in visited:
        return False
    visited.add(position)
    explore(grid,row-1,column,visited)
    explore(grid,row+1,column,visited)
    explore(grid,row,column+1,visited)
    explore(grid,row,column-1,visited)
    return True






    
