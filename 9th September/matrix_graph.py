def add_node(matrix,node1,node2):
    matrix[node1][node2] = 1
    matrix[node2][node1] = 1
    #undirected graph

def graph_displayer(matrix):
    for i in matrix:
        print(" ".join(map(str,i)))


if __name__=="__main__":

    nodes=int(input("Enter the number of nodes : "))
    edges = int(input("Enter the number of edges: "))

    matrix=[[0]*nodes for _ in range(nodes)]

    for i in range(edges):
        node1=int(input("Enter index of node1 : "))
        node2=int(input("Enter index of node2 : "))
        print("Node succesfully added\n\nAdd the next node : ")

        add_node(matrix,node1-1,node2-1)

    graph_displayer(matrix)



