import random
import numpy as np
import networkx as nx
import igraph as ig
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Fixing random seed for reproducibility
random_seed = st.sidebar.number_input("Set random seed:", value=42)
random.seed(random_seed)
np.random.seed(random_seed)

def generate_data(size):
    # ... same as before ...

def create_graph_from_table(table):
    # ... same as before ...

def extract_subgraph(graph, patient_zero, radius=2):
    # ... same as before ...

def initialize_spins(graph, patient_zero):
    # ... same as before ...

def energy(graph, spins):
    # ... same as before ...

def metropolis(graph, spins, n_steps=1000, T=1.0):
    # ... same as before ...

def threshold_model(graph, patient_zero, steps=10):
    # ... same as before ...

def plot_igraph(graph, colors):
    nx_graph = nx.Graph()
    for edge in graph.es:
        nx_graph.add_edge(edge.source, edge.target)
    pos = nx.kamada_kawai_layout(nx_graph)
    nx.draw_networkx_nodes(nx_graph, pos, node_color=colors, node_size=100)
    nx.draw_networkx_edges(nx_graph, pos)
    plt.show()

size = 1000
table = generate_data(size)
graph = create_graph_from_table(table)
radius = 2
subgraph = extract_subgraph(graph, random.randint(0, graph.vcount() - 1), radius=radius)
patient_zero = random.randint(0, subgraph.vcount() - 1)

model_selection = st.sidebar.selectbox("Select a model:", ["Ising", "Modified Ising", "Threshold"])

if model_selection == "Ising":
    spins = initialize_spins(subgraph, patient_zero)
    final_spins = metropolis(subgraph, spins)
    colors = ["red" if spin == -1 else "green" for spin in final_spins]
    plot_igraph(subgraph, colors)
elif model_selection == "Modified Ising":
    spins = initialize_spins(subgraph, patient_zero)
    final_spins = metropolis(subgraph, spins, T=0.5)  # Modify temperature as needed
    colors = ["red" if spin == -1 else "green" for spin in final_spins]
    plot_igraph(subgraph, colors)
elif model_selection == "Threshold":
    distress_threshold = threshold_model(subgraph, patient_zero)
    colors = ["red" if d == 1 else "green" for d in distress_threshold]
    plot_igraph(subgraph, colors)
