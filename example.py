from search import graph
import networkx as nx
import random


def bfs_nx(G, start, end=None):
	"""
	A function that uses the networkx library to return the shortest path from start to end 
	between nodes in a graph(returns None if no path exists and path
	of traversal if end == None).

	This pathfinding function uses networkx's bfs method. 
	Documentation: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.traversal.breadth_first_search.bfs_edges.html#networkx.algorithms.traversal.breadth_first_search.bfs_edges
	"""
	edges = nx.bfs_edges(G, start)
	nodes = [start] + [v for u, v in edges]
	if end == None: 
		return nodes
	else:
		try: 
			target_index = nodes.index(end)
		except ValueError: # End node was not reached or does not exist in the graph (no path exists)
			return None
		return nodes[:target_index+1] # Return only up to the end node, if one exists

def main():
	"""
	The main function

	TODO: Write your unit test for a breadth-first
	traversal here. Create an instance of your Graph class 
	using the 'tiny_network.adjlist' file and assert 
	that all nodes are being traversed (ie. returns 
	the right number of nodes, in the right order, etc.)
	"""

	# Create an instance of my Graph class
	filename = "./data/tiny_network.adjlist"
	tiny_net = graph.Graph(filename)

	# Test my bfs traversal (by comparing my bfs output with networkx library's bfs method)
	G = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")    # Create the same graph in networkx

	# Run bfs traversal using networkx and my library, compare outputs
	for n in G.nodes():
		assert bfs_nx(G, n) == tiny_net.bfs(n)
	#-----------

	"""
	TODO: Write your unit test for your breadth-first 
	search here. You should generate an instance of a Graph
	class using the 'citation_network.adjlist' file 
	and assert that nodes that are connected return 
	a (shortest) path between them.
	
	Include an additional test for nodes that are not connected 
	which should return None. 
	"""

	# # Create an instance of my Graph class
	filename = "./data/citation_network.adjlist"
	cite_net = graph.Graph(filename)

	# Test my bfs pathfinding (by comparing my bfs output with networkx library's shortest path)
	G = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")    # Create the same graph in networkx
	num_tests = 5 # Number of tests to run
	while num_tests != 0:
		n1 = random.choice(G.nodes())
		n2 = random.choice(G.nodes())
		if nx.has_path(G, source=n1, target=n2): # Check only if a path exists (see below for edge case handling)
			print(n1, n2)
			my_path = cite_net.bfs(n1, n2)
			nx_path = nx.shortest_path(G, source=n1, target=n2)
			print(my_path)
			print(nx_path)
			assert(len(my_path) == len(nx_path))
			num_tests -= 1
	


	# Test for nodes that are not connected which should return None. 
	# Case 1: Start node does not exist
	path = []
	nonsense = "Jay Liu"
	try:
		path = bfs_nx(G,nonsense)
	except nx.exception.NetworkXError:
		path = None # This test should end up triggering the exception
	assert(path == cite_net.bfs(nonsense))

	# Test for nodes that are not connected which should return None. 
	# Case 2: End node does not exist
	path = []
	start = "Marina Sirota"
	nonsense = "Jay Liu"
	try:
		path = bfs_nx(G,start, nonsense) # This test should end up returning path = None
	except nx.exception.NetworkXError:
		pass
	assert(path == cite_net.bfs(start, nonsense))




"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
	main()
