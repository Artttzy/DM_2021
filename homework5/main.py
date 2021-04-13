import networkx as nx
from networkx.algorithms.approximation import clique
from networkx.algorithms.approximation import independent_set
from networkx.algorithms.approximation import vertex_cover
from networkx.algorithms import covering
from networkx.algorithms import tournament
from networkx.algorithms.tree import mst
from networkx.algorithms import euler
from networkx.algorithms.connectivity import edge_kcomponents
# G*
fin = open('europe.txt', 'r')
mas = [[0] * 3 for i in range(90)]
for i in range(90):
    s = fin.readline()
    k = s.split()
    for j in range(2):
        mas[i][j] = k[j]
    mas[i][2] = int(k[2])
G_ = nx.Graph()
G_.add_weighted_edges_from(mas)

# G
fin = open('connected.txt', 'r')
mas = [[0] * 3 for i in range(85)]
for i in range(85):
    s = fin.readline()
    k = s.split()
    for j in range(2):
        mas[i][j] = k[j]
    mas[i][2] = int(k[2])
G = nx.Graph()
G.add_weighted_edges_from(mas)

# D
fin = open('digraph.txt', 'r')
mas = [[0] * 3 for i in range(170)]
for i in range(90):
    s = fin.readline()
    k = s.split()
    for j in range(2):
        mas[i][j] = k[j]
    mas[i][2] = int(k[2])
D = nx.DiGraph()
D.add_weighted_edges_from(mas)

# b)
print("b) |V| = ", G_.number_of_nodes(), ", |E| = ", G_.number_of_edges(), ", min_degree(G) = ", min(val for (node, val) in G.degree()), ", max_degree(G) = ", max(val for (node, val) in G.degree()),", rad(G) = ", nx.radius(G), ", diam(G) = ", nx.diameter(G), ", girth(G) = ", len(min(nx.cycle_basis(G))), ", center(G) = ", nx.center(G), ", k_node_connectivity = ", nx.node_connectivity(G), ", k_edge_connectivity = ", nx.edge_connectivity(G))
print()

# c) Minimum vertex coloring
print("c) Colors:", max(nx.greedy_color(G).values()) + 1,", Z =", nx.greedy_color(G))
print()

# d) Minimum edge coloring
print("d) Colors:", max(nx.greedy_color(nx.line_graph(G)).values()) + 1, ", E =", nx.greedy_color(nx.line_graph(G)))
print()

# e) Maximum clique
print("e) Q =", clique.max_clique(G))
print()

# f) Maximum stable set
print("f) S =", independent_set.maximum_independent_set(G))
print()

# g) Maximum matching
print("g) M =", nx.max_weight_matching(G))
print()

# h) Minimum vertex cover
print("h) R =", vertex_cover.min_weighted_vertex_cover(G))
print()

# i) Minimum edge cover
print("i) F =", covering.min_edge_cover(G))
print()

# j) Shortest closed path (circuit) that visits every vertex
print("j) W =", end=" ")
for i in range(len(tournament.hamiltonian_path(D))):
    print(tournament.hamiltonian_path(D)[i], "-", end=" ")
print(tournament.hamiltonian_path(D)[0])
print()

# k) Shortest closed path (circuit) that visits every edge
H = nx.eulerize(G)
c = list(n for (n, d) in nx.eulerian_circuit(H))
print("k) U =", end=" ")
for i in range (len(c)):
    print(c[i], "-", end=" ")
print(c[0])
print()

# m) 2-edge-connected components
print("m) ", list(edge_kcomponents.bridge_components(G)))
print()

# o) MST
MST=nx.Graph(mst.minimum_spanning_tree(G))
print("o) MST = ", MST.nodes)
print("Weight =", sum(c for (a,b,c) in (MST.edges.data('weight'))))
print()
