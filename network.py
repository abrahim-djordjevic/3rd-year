import networkx as nx
from matplotlib.backends.backend_pgf import PdfPages
import matplotlib.pyplot as plt
G = nx.Graph()
red_nodes =([
    '])

blue_nodes=([
    ])
G.add_edges_from([
    ])

plt.figure(figsize=(18,18))
pos=nx.kamada_kawai_layout(G)
nx.draw_networkx_nodes(G,pos,nodelist=blue_nodes, node_color='cyan')
nx.draw_networkx_nodes(G,pos,nodelist=red_nodes, node_color='red')
nx.draw_networkx_edges(G,pos)
labels=nx.draw_networkx_labels(G,pos,font_size=10,font_color='black')
limits=plt.axis('off')

print(nx.degree(G))
