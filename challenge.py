
class Challenge:
    def __init__(self, adj_matrix):
        self.num_nodes = len(adj_matrix)
        self.nodes = [i for i in range(self.num_nodes)]
        self.adj_matrix = adj_matrix

    def are_adj(self, n1, n2): return self.adj_matrix[n1][n2] != 0

    def input_node(self, name):
        n = input(f"{name} Node -> ")
        try:
            n = int(n)
        except:
            print('Node invalid')
            return self.input_node(name)
        if n in self.nodes:
            return n
        else:
            print('Node invalid')
            return self.input_node(name)

    def console(self):
        while(True):
            print(f"Our graph has: {self.nodes} nodes")
            print("Enter two nodes:")
            n1 = self.input_node('First')
            n2 = self.input_node('Second')
            result = self.are_adj(n1, n2)
            print(30*"-")
            print(f"{n1} is adj to {n2}? {result}")
            print(30*"-")


if __name__ == "__main__":
    adj_matrix1 = [
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0]
    ]
    adj_matrix2 = [
        [0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0]
    ]
    # Examples
    example1 = Challenge(adj_matrix1) 
    assert(example1.are_adj(0,1)==True)
    assert(example1.are_adj(0,2)==False)

    example2 = Challenge(adj_matrix2) 
    assert(example2.are_adj(0,3)==True)
    assert(example2.are_adj(1,4)==False)

    # Para usar la consola 
    # Challenge(adj_matrix1).console() 
    # Challenge(adj_matrix2).console() 
