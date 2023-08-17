import igraph as ig
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


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

def simulate_SI(graph, patient_zero, infection_probability, steps):
    states_history = []
    states = ['S'] * graph.vcount()
    states[patient_zero] = 'I'
    states_history.append(states.copy())

    for step in range(steps):
        infected_nodes = [v.index for v in graph.vs if states[v.index] == 'I']

        for infected_node in infected_nodes:
            neighbors = graph.neighbors(infected_node)
            for neighbor in neighbors:
                if states[neighbor] == 'S' and random.random() < infection_probability:
                    states[neighbor] = 'I'
        states_history.append(states.copy())

    return states_history

def animate(graph, states_history):
    fig, ax = plt.subplots(figsize=(10, 10))

    layout = graph.layout('kk')
    coords = np.array(layout.coords)

    def update(num):
        ax.clear()
        state_colors = ['g' if state == 'S' else 'r' for state in states_history[num]]
        ax.scatter(coords[:, 0], coords[:, 1], c=state_colors)
        for edge in graph.es:
            start, end = edge.tuple
            ax.plot([coords[start, 0], coords[end, 0]], [coords[start, 1], coords[end, 1]], c='gray')
        ax.set_title(f"Step {num + 1}")

    ani = animation.FuncAnimation(fig, update, frames=len(states_history), repeat=False)

    # Show the animation
    plt.show()

# Example data
data = {
    'origin_node': [0, 1, 2, 3],
    'destiny_node': [1, 2, 3, 0],
    'transaction_quantity': [100, 200, 300, 400],
    'transaction_volume': [1000, 2000, 3000, 4000]
}

table = pd.DataFrame(data)
graph = create_graph_from_table(table)
patient_zero = random.randint(0, graph.vcount() - 1)
radius = 2
infection_probability = 0.1
steps = 100
states_history = simulate_SI(graph, patient_zero, infection_probability, steps)

# Animate
animate(graph, states_history)
