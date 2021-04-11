import networkx as nx
from networkx.algorithms.approximation import clique
from networkx.algorithms.approximation import independent_set
from networkx.algorithms.approximation import vertex_cover
from networkx.algorithms import covering
from networkx.algorithms import tournament
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

# b)
print("b) |V| = ", G_.number_of_nodes(), ", |E| = ", G_.number_of_edges(), ", min_degree(G) = ", min(val for (node, val) in G.degree()), ", max_degree(G) = ", max(val for (node, val) in G.degree()),", rad(G) = ", nx.radius(G), ", diam(G) = ", nx.diameter(G), ", girth(G) = ", len(min(nx.cycle_basis(G))), ", center(G) = ", nx.center(G), ", k_node_connectivity = ", nx.node_connectivity(G), ", k_edge_connectivity = ", nx.edge_connectivity(G))
print()

# c)
print("c) Colors:", max(nx.greedy_color(G).values()) + 1,", Z =", nx.greedy_color(G))
print()

# d)
print("d) Colors:", max(nx.greedy_color(nx.line_graph(G)).values()) + 1, ", E =", nx.greedy_color(nx.line_graph(G)))
print()

# e)
print("e) Q =", clique.max_clique(G))
print()

# f)
print("f) S =", independent_set.maximum_independent_set(G))
print()

# g)
print("g) M =", nx.max_weight_matching(G))
print()

# h)
print("h) R =", vertex_cover.min_weighted_vertex_cover(G))
print()

# i)
print("i) F =", covering.min_edge_cover(G))
print()

# j)
G.remove_nodes_from([u for v, u in G.edges() if len(G[u]) == 1]) #убираем висячие ребра
print(tournament.hamiltonian_path(G))#ищем гамильтонов путь и добавляем в него высячие ребра
