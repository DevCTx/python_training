import matplotlib.pyplot as plt
import networkx as nx

# Create the Graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3)])

# Create the DiGraph
D = nx.DiGraph()
D.add_edges_from([(4, 2), (2, 5)])

# Create the MultiGraph
MG = nx.MultiGraph()
# Add edges from the Graph (undirected)
MG.add_edges_from(G.edges(), label='Graph', orientation='undirected')
# Add edges from the DiGraph (directed)
MG.add_edges_from(D.edges(), label='DiGraph', orientation='directed')

# Create the MultiGraph
MD = nx.MultiDiGraph()
# Add edges from the Graph (undirected)
MD.add_edges_from(G.edges(), label='Graph', orientation='undirected')
# Add edges from the DiGraph (directed)
MD.add_edges_from(D.edges(), label='DiGraph', orientation='directed')

# Draw and display the Graph
plt.subplot(141)
nx.draw(G, with_labels=True)
plt.title("Graph")

# Draw and display the DiGraph
plt.subplot(142)
nx.draw(D, with_labels=True)
plt.title("DiGraph")

# Draw and display the MultiGraph
plt.subplot(143)
nx.draw(MG, with_labels=True)
plt.title("MultiGraph")

# Draw and display the MultiGraph
plt.subplot(144)
nx.draw(MD, with_labels=True)
plt.title("MultiDiGraph")

plt.tight_layout()
plt.show()
