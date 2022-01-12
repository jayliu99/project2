# write tests for bfs
import pytest
from search import graph
import networkx as nx

def bfs_nx(G, start):
    """
    A function that uses the networkx library to return a bfs traversal
    from a start node in a graph.

    This pathfinding function uses networkx's bfs method. 
    Documentation: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.traversal.breadth_first_search.bfs_edges.html#networkx.algorithms.traversal.breadth_first_search.bfs_edges
    """
    edges = nx.bfs_edges(G, start)
    nodes = [start] + [v for u, v in edges]
    return nodes

#@pytest.fixture
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    # Create an instance of my Graph class
    filename = "./data/tiny_network.adjlist"
    tiny_net = graph.Graph(filename)

    # Test my bfs traversal (by comparing my bfs output with networkx library's method)
    G = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")    # Create the same graph in networkx

    # Run bfs traversal using networkx and my library, compare outputs
    for n in G.nodes():
        assert (bfs_nx(G, n) == tiny_net.bfs(n))

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """

    filename = "./data/citation_network.adjlist"
    cite_net = graph.Graph(filename)

    # Test for nodes that are not connected which should return None. 
    # Case 1: Start node does not exist
    nonsense = "Jay Liu"
    assert(cite_net.bfs(nonsense) == None)
    assert(cite_net.bfs(nonsense, "Marina Sirota") == None)
    # Case 2: End node does not exist
    assert(cite_net.bfs("Marina Sirota", nonsense) == None)
    # Case 3: Both start and end exist, but no path exists between them
    assert(cite_net.bfs("31209381", "34953500") == None)

    # Create a dummy network to test for shortest path-finding ability
    dummy_net = graph.Graph("./data/dummy_net.adjlist")
    assert(dummy_net.bfs("A","G") == ["A", "C", "G"])

    # Test that bfs finds a shortest path between two actual nodes in the citation network
    # "Ground truth" = length of shortest path found by shortest_path function in networkx library
    # Documentation: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path.html#networkx.algorithms.shortest_paths.generic.shortest_path
    G = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")    # Create the same graph in networkx
    assert(len(cite_net.bfs("34413319", "34916529")) == len(nx.shortest_path(G, source="34413319", target="34916529")))
