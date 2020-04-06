# whats going on
Let's struggle together using gremlinpython <br/>

I'll have in this repo examples of things that I know how to do using pure gremlin (gremlin-console)<br/>
and I don't know how to do using gremlinpython.

Example:
I'll have a file called "find_user.py" and "find_user.txt". In the second file, I'll post everything I did <br/>
using gremlin-console. In the first, I'll show how I tried to do that but did not manage to succeed. <br/>
<br/>
"find_user.txt"<br/>
graph  = TinkerGraph.open()<br/>
g = graph.traversal()<br/>
g.addV('employee').property('name','rico').property('position','data guy')<br/>
g.V().has('name','rico').values().fold()<br/>
==> `[rico,data_guy]`<br/>


 
leaving some sample stuff with what I discovered by myself. <br/>
happy to receive help with the things I'm struggling with.<br/>

