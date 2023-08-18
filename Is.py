import igraph as ig
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def generate_data(size):
    data = {
        'origin_node': [random.randint(0, size-1) for _ in range(size*2)],
        'destiny_node': [random.randint(0, size-1) for _ in range(size*2)],
        'transaction_quantity': [random.randint(100, 1000) for _ in range(size*2)],
        'transaction_volume': [random.randint(1000, 10000) for _ in range(size*2)]
    }
    return pd.DataFrame(data)

def create_graph_from_table(table):
    g = ig.Graph(directed=True)
    n_nodes = max(table['origin_node'].max(), table['destiny_node'].max()) + 1
    g.add_vertices(n_nodes)

    for index, row in table.iterrows():
        origin = int(row['origin_node'])
        dest = int(row['destiny_node'])
        if origin != dest:
            g.add_edge(origin, dest)
            g.es[-1]['transaction_quantity'] = row['transaction_quantity']
            g.es[-1]['transaction_volume'] = row['transaction_volume']

    return g

def extract_subgraph(graph, patient_zero, radius=2):
    vertices_in_radius = graph.neighborhood(patient_zero, order=radius)
    subgraph = graph.subgraph(vertices_in_radius)
    return subgraph


size = 1000
table = generate_data(size)
graph = create_graph_from_table(table)
radius = 2
def initialize_spins(graph, patient_zero):
    spins = [-1 if v.index == patient_zero else 1 for v in graph.vs]
    return spins

def energy(graph, spins):
    E = 0
    for edge in graph.es:
        E -= edge['transaction_quantity'] * spins[edge.source] * spins[edge.target]
        if spins[edge.source] == -1:
            E -= edge['transaction_quantity']  # Favoring distressed state
    return E

def metropolis(graph, spins, n_steps=1000, T=1.0):
    N = graph.vcount()
    E1 = energy(graph, spins)
    for _ in range(n_steps):
        i = random.randint(0, N - 1)
        spins[i] *= -1
        E2 = energy(graph, spins)
        dE = E2 - E1
        if dE > 0 and random.uniform(0, 1) >= np.exp(-dE / T):
            spins[i] *= -1  # Revert change
        else:
            E1 = E2
    return spins

subgraph = extract_subgraph(graph, patient_zero, radius=radius)
patient_zero = random.randint(0, subgraph.vcount() - 1)
spins = initialize_spins(subgraph, patient_zero)
final_spins = metropolis(subgraph, spins)

# Visualization
layout = subgraph.layout("kk")
colors = ["red" if spin == -1 else "green" for spin in final_spins]
ig.plot(subgraph, vertex_color=colors, layout=layout)
