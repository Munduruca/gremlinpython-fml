# whats going on
Let's struggle together using gremlinpython <br/>


### how to install it<br/>
pip install gremlinpython<br/>


For the super beginners, I'll leave simple stuff that I know how to do. Those files will have the prefix "OK_" in the name. <br/>
What I mean by simple stuff is how to create vertices and edges as well as how to run queries.<br/>

I'll have in this repo examples of things that I know how to do using pure gremlin (gremlin-console)<br/>
and I don't know how to do using gremlinpython.<br/>

Example:<br/>
I'll have a file called "_finding_one_simple_query.py" and "_finding_one_simple_query.txt". In the second file, I'll post everything I did <br/>
using gremlin-console. In the first, I'll show how I tried to do that but did not manage to succeed. <br/>
<br/>
"_finding_one_simple_query.txt"<br/>
graph  = TinkerGraph.open()<br/>
g = graph.traversal()<br/>
g.addV('employee').property('name','rico').property('position','data guy')<br/>
g.V().has('name','rico').values().fold()<br/>
==> `[rico,data_guy]`<br/>

"_finding_one_simple_query.py"<br/>
from gremlin_python.structure.graph import Graph<br/>
graph = Graph()<br/>
g = graph.traversal()<br/>
g.addV("employee").property("name", "rico").property('position','data guy')<br/>
my_stuff = g.V().has('name','rico').values()<br/>
In `[39]`: my_stuff<br/>
Out`[39]`: `[['V'], ['has', 'name', 'rico'], ['values'], ['values', '_ipython_display_']]`<br/>

^^^^<br/>
As we can see above the result is not the same :(<br/>
My first attempt was to get thiings from this object that looks like a list<br/>
using index position e.g. `my_stuff[0]`<br/>
After trying that, I've go this error: `TypeError: NoneType object is not an iterator`<br/>


 
leaving some sample stuff with what I discovered by myself. <br/>
happy to receive help with the things I'm struggling with.<br/>

