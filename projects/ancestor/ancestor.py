from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    #get unique vals for verts
    verts = set()
    for tup in ancestors:
        verts.add(tup[0])
        verts.add(tup[1])
    # create graph
    graph = Graph()
        #make vertex
    for val in verts:
        graph.add_vertex(val)
        #edges
    for conn in ancestors:
        graph.add_edge(conn[1],conn[0])


    #dfs
        #track longest path
    return graph.ancestor(starting_node)
    



#ancestors [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
