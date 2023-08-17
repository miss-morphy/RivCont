import networkx as nx
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_nx_graph_from_table(table):
    G = nx.DiGraph()
    for index, row in table.iterrows():
        origin = int(row['origin_node'])
        dest = int(row['destiny_node'])
        if origin != dest:
            G.add_edge(origin, dest, transaction_quantity=row['transaction_quantity'], transaction_volume=row['transaction_volume'])
    return G

def simulate_SI(graph, patient_zero, infection_probability, steps):
    states_history = []
    states = ['S'] * graph.number_of_nodes()
    states[patient_zero] = 'I'
    states_history.append(states.copy())
    for step in range(steps):
        infected_nodes = [node for node, state in enumerate(states) if state == 'I']
        for infected_node in infected_nodes:
            neighbors = list(graph.neighbors(infected_node))
            for neighbor in neighbors:
                if states[neighbor] == 'S' and random.random() < infection_probability:
                    states[neighbor] = 'I'
        states_history.append(states.copy())
    return states_history

def animate(graph, states_history):
    fig, ax = plt.subplots(figsize=(10, 10))

    def update(num):
        ax.clear()
        state_colors = ['g' if state == 'S' else 'r' for state in states_history[num]]
        nx.draw(graph, with_labels=True, node_color=state_colors, ax=ax)
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
graph = create_nx_graph_from_table(table)
patient_zero = random.randint(0, graph.number_of_nodes() - 1)
infection_probability = 0.1
steps = 10
states_history = simulate_SI(graph, patient_zero, infection_probability, steps)

# Animate
animate(graph, states_history)
