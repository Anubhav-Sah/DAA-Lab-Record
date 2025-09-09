from matrix_graph import *
from collections import deque



def BFS(matrix, root_node):
    visited = set()
    queue = deque([root_node])
    visited.add(root_node)

    while queue:
        node = queue.popleft()
        print(node + 1, end=" ")

        for i, j in enumerate(matrix[node]):
            if j == 1 and i not in visited:
                visited.add(i)
                queue.append(i)




if __name__=="__main__":
    nodes=int(input("Enter the number of nodes : "))
    edges = int(input("Enter the number of edges: "))

    matrix=[[0]*nodes for _ in range(nodes)]

    for i in range(edges):
        node1=int(input("Enter index of node1 : "))
        node2=int(input("Enter index of node2 : "))
        print("Node succesfully added\n\nAdd the next node : ")

        add_node(matrix,node1-1,node2-1)
    
    root_node=int(input("Enter the root node : "))-1

    graph_displayer(matrix)
    print("DFS trversel : \n")
    BFS(matrix,root_node)
    print("\n")