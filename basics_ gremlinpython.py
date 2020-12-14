# importing libs
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
import pandas as pd

# creating and instantiating connection with gremlin
connection = DriverRemoteConnection('ws://localhost:8182/gremlin', 'g')

# creating and instantiating graph
graph = Graph()
g = graph.traversal().withRemote(connection)

# (optional) clearing up graph
def wiping_out_graph():
  g.V().drop().iterate()
  g.E().drop().iterate()
  g.V().count().next()
  g.E().count().next()
  print("graph cleared!")
wiping_out_graph()

# adding dummy vertices
g.addV("person").property("name","macus").property("entity_id",1).next()
g.addV("person").property("name","jason").property("entity_id",2).next()
g.addV("person").property("name","jane").property("entity_id",3).next()

# querying the vertices we just added
g.V().hasLabel('person').valueMap().toList()

# adding edge
g.V(g.V().has('entity_id',1).next()).addE('knows').to(g.V().has('entity_id',2).next()).next()

# querying who jason knows
g.V().has('name','jason').out().valueMap().next()

# querying who knows jason
g.V().has('name','jason').in_().valueMap().next()
