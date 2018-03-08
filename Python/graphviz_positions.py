import networkx as nx

def setup_europe():
    G = nx.Graph()

    G.add_edge("Portugal", "Spain")
    G.add_edge("Spain","France")
    G.add_edge("France","Belgium")
    G.add_edge("France","Germany")
    G.add_edge("France","Italy")
    G.add_edge("Belgium","Netherlands")
    G.add_edge("Germany","Belgium")
    G.add_edge("Germany","Netherlands")
    G.add_edge("England","Wales")
    G.add_edge("England","Scotland")
    G.add_edge("Scotland","Wales")
    G.add_edge("Switzerland","Austria")
    G.add_edge("Switzerland","Germany")
    G.add_edge("Switzerland","France")
    G.add_edge("Switzerland","Italy")
    G.add_edge("Austria","Germany")
    G.add_edge("Austria","Italy")
    G.add_edge("Austria","Czech Republic")
    G.add_edge("Austria","Slovakia")
    G.add_edge("Austria","Hungary")
    G.add_edge("Denmark","Germany")
    G.add_edge("Poland","Czech Republic")
    G.add_edge("Poland","Slovakia")
    G.add_edge("Poland","Germany")
    G.add_edge("Czech Republic","Slovakia")
    G.add_edge("Czech Republic","Germany")
    G.add_edge("Slovakia","Hungary")
    return G

G = setup_europe()
nx.nx_pydot.write_dot(G, '/tmp/out.dot')

pos = nx.nx_pydot.pydot_layout(G, prog = 'dot')
print(pos)

agraph = nx.nx_agraph.to_agraph(G)
agraph.draw("/tmp/europe.png", format = 'png', prog = 'dot')
