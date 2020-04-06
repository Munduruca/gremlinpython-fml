from gremlin_python.structure.graph import Graph
# creating the graph
graph = Graph()
# creating the traversal
g = graph.traversal()
# adding the vertex
g.addV("employee").property("name", "rico").property('position','data guy')
# running the query
my_stuff = g.V().has('name','rico').values()
# unfortunatelly, the result is not the same as the one gremlin-console provides...
# ??? how could we get simmilar result using python?