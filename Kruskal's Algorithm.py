def find(parent, i):  # this recursive function is used to find the parent of a node
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]
    # if the condition returned true, it means that the specific node is not its own parent anymore because it was, initially
    # its parent is a different node now
    # the use of the statement below is to check if the parent of the node that was inserted before the recursion have a parent or not
    # observe that the argument that was passed is the parent of the node known as 'parent[i]', that was inserted before the recursion which is 'i'
    # using this recursion we can find the respective parents OR parents of parents OR... of the nodes in our graph


graph = [  # inserting edges with weights
    [0, 6, 51],
    [0, 1, 32],
    [0, 2, 29],
    [4, 3, 34],
    [5, 3, 18],
    [7, 4, 46],
    [5, 4, 40],
    [0, 5, 60],
    [6, 4, 51],
    [7, 0, 31],
    [7, 6, 25],
    [7, 1, 21]
]
MST = []
parent = []
rank = []
cost = 0
V = []  # creating a list for vertices/nodes

for edge in graph:  # counting every unique edges in the graph
    if not edge[0] in V:
        V.append(edge[0])
    if not edge[1] in V:
        V.append(edge[1])

V.sort()
print(V)

graph = sorted(graph, key=lambda item: item[2])  # function to sort the list of edges by weight
print(graph)

for node in range(len(V)):
    parent.append(node)  # listing the parent in a list
    rank.append(0)  # assigning parents to the nodes which is initially their parents are themselves

i = 0
j = 0
while i < len(V) - 1:
    u, v, w = graph[j]  # getting the inputs one by one

    x = find(parent, u)  # finding the parent of the source node using recursion
    y = find(parent, v)  # finding the parent of the destination node using recursion
    # see information above

    #  finding their respective parents is essential because it will tell us if the edge that we picked will create a loop
    #  so, nodes MUST have different parent, otherwise the edge will be omitted
    if x != y:
        i += 1
        MST.append([u, v, w])
        if rank[x] < rank[y]:  # performing union by rank to decide who will be the parent of who
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
    j += 1

for u, v, weight in MST:
    cost += weight
    print("%d -- %d == %d" % (u, v, weight))
print("Total Weight of Edges", cost)
