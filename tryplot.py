import networkx as nx
import os
G = nx.MultiDiGraph()
# G.add_node(" ", shape="plaintext")
# G.add_edge(" ", "q0")
G.add_node("q0")
G.add_node("q1")
G.add_node("q2")
G.add_node("q3")
G.add_node("q4")
G.add_node("q5", peripheries=2)
G.add_edge("q0", "q1", label='Ɛ')
G.add_edge("q0", "q5", label='Ɛ')
G.add_edge("q1", "q2", label='Ɛ')
G.add_edge("q1", "q4", label='Ɛ')
G.add_edge("q2", "q3", label='a')
G.add_edge("q3", "q2", label='Ɛ')
G.add_edge("q3", "q4", label='Ɛ')
G.add_edge("q4", "q1", label='Ɛ')
G.add_edge("q4", "q5", label='Ɛ')
# print(list(G.nodes))
# print(list(G.edges(data="label")))
# for x in list(G.nodes(data="initial")):
#     if x[1]==True:
#         print(x[0])
nx.nx_agraph.write_dot(G, "dot1.gv")
os.system("dot dot1.gv -Tpng > dot1.png")
f = open("dot1.gv")
lines = f.readlines()
lines.insert(1, '\trankdir=LR\n')
lines.insert(2, '\t" " [shape=plaintext]\n')
lines.insert(3, '\t" " -> q0\n')
f = open("dot1.gv", "w")
for x in lines:
    print(x)
    f.write(x)
f.close()
os.system("dot dot1.gv -Tpng > dot1.png")
os.system("xdg-open dot1.png")
# labelloc = "t"
# label = "a**"
# name
# rankdir