import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None

        """
        ### BFS traversal
        G = self.graph
        visited = []
        queue = []
        backtrace = {} # keep track of parent nodes
        traversal = [] # keep track of order of traversal
        path_exists = False # keep track of whether end node is reached

        # Add start node to queue & mark as visited
        queue.append(start)
        visited.append(start)

        # Handle edge case: start node does not exist
        if start not in G.nodes():
            return None
            #print("Got here A")

        while len(queue) > 0:
            curr_node = queue[0]
            traversal.append(curr_node)
            if (end != None) and (curr_node == end): 
                path_exists = True # Turn on flag if end node has been reached

            #print(curr_node)

            # For each unvisited neighbors of current node:
            for n in G.neighbors(curr_node):
                if n not in visited:
                    queue.append(n)             # Add neighbor to queue
                    visited.append(n)           # Mark neighbor as visited
                    backtrace[n] = curr_node    # Set pointer from neighbor to current (parent) node 

            queue.remove(curr_node)

        # Backtracing
        path = []

        if end == None:
            return traversal
        else:
            if not path_exists:
                return None
                #print("Got here B")
            else:
                #print("Got here C")
                # Set end as current node & add end to path
                curr_node = end
                path.append(end)

                # While current node not start node:
                while curr_node != start:
                    #print("Got here D")
                    parent_node = backtrace[curr_node]  # Identify parent node
                    path.append(parent_node)            # Add parent node to path
                    curr_node = parent_node             # Set current node to parent node

                path.reverse()
                return path




