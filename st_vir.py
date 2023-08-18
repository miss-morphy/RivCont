import streamlit as st
import igraph as ig
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np

# Seed for reproducibility
seed = st.sidebar.number_input('Random seed', value=42)
random.seed(seed)
np.random.seed(seed)

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
    # Find the index of patient_zero within the subgraph
    patient_zero_subgraph_index = vertices_in_radius.index(patient_zero)
    return subgraph, patient_zero_subgraph_index

def threshold_model(graph, patient_zero, steps=10):
    distress = [0] * graph.vcount()
    distress[patient_zero] = 1
    for v in graph.vs:
        v['threshold'] = 0.3 # Example threshold
    for _ in range(steps):
        new_distress = distress.copy()
        for v in graph.vs:
            neighbor_distress = sum(distress[n] for n in graph.neighbors(v.index))
            if neighbor_distress >= v['threshold']:
                new_distress[v.index] = 1
        distress = new_distress
    return distress

def ising_model(graph, patient_zero, steps=10):
    spins = [1] * graph.vcount()
    spins[patient_zero] = -1
    for _ in range(steps):
        new_spins = spins.copy()
        for v in graph.vs:
            neighbor_spins = sum(spins[n] for n in graph.neighbors(v.index))
            if neighbor_spins > 0:
                new_spins[v.index] = 1
            else:
                new_spins[v.index] = -1
        spins = new_spins
    return spins

def plot_graph(subgraph, status, model_name):
    # Convert igraph to networkx for visualization
    nx_graph = nx.Graph([(e.source, e.target) for e in subgraph.es])
    colors = ['red' if s == 1 else 'green' for s in status]
    if model_name == "Ising Model":
        colors = ['red' if s == -1 else 'green' for s in status]
    pos = nx.spring_layout(nx_graph, seed=seed)
    nx.draw(nx_graph, pos, node_color=colors, with_labels=True)
    plt.show()

size = 1000
table = generate_data(size)
graph = create_graph_from_table(table)
patient_zero = random.randint(0, size-1) # Choose a random patient_zero
radius = 2
# Extract subgraph and find patient_zero's index in the vertices list
subgraph, patient_zero_in_subgraph = extract_subgraph(graph, patient_zero, radius=radius)

# Threshold Model
st.write("## Threshold Model")
distress_threshold = threshold_model(subgraph, patient_zero_in_subgraph)
st.pyplot(plot_graph(subgraph, distress_threshold, "Threshold Model"))
status_df_threshold = pd.DataFrame({'Node': range(len(distress_threshold)), 'Distress Status': distress_threshold})
st.write(status_df_threshold)


# Ising Model
st.write("## Ising Model")
spins_ising = ising_model(subgraph, patient_zero_in_subgraph)
st.pyplot(plot_graph(subgraph, spins_ising, "Ising Model"))
status_df_ising = pd.DataFrame({'Node': range(len(spins_ising)), 'Spin Status': spins_ising})
st.write(status_df_ising)
