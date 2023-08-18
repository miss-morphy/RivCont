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


def threshold_model(graph, patient_zero, steps=10):
    distress = [0] * graph.vcount()
    distress[patient_zero] = 1
    for v in graph.vs:
        v['threshold'] = random.uniform(0.1, 1) # Example threshold
    for _ in range(steps):
        new_distress = distress.copy()
        for v in graph.vs:
            neighbor_distress = sum(distress[n] * graph[v.index, n] for n in graph.neighbors(v.index))
            if neighbor_distress >= v['threshold']:
                new_distress[v.index] = 1
        distress = new_distress
    return distress

# Example data
size = 1000
table = generate_data(size)
graph = create_graph_from_table(table)
patient_zero = 1
radius = 2

subgraph = extract_subgraph(graph, patient_zero, radius=radius)
distress = threshold_model(subgraph, patient_zero)

# Visualization
layout = subgraph.layout("kk")
colors = ["red" if d == 1 else "green" for d in distress]
ig.plot(subgraph, vertex_color=colors, layout=layout)
