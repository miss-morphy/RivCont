import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from igraph import Graph

def generate_subgraph_by_value(percentile=80):
    # Read the graph table
    file_name = "financial_graph_2023-06.csv"  # Adjust the file name accordingly
    graph_table = pd.read_csv(file_name)
    
    # Determine the threshold based on percentile
    threshold = np.percentile(graph_table['transaction_volume'], percentile)

    # Filter the table based on the threshold
    filtered_table = graph_table[graph_table['transaction_volume'] >= threshold]

    # Create the subgraph from the filtered table
    subgraph = Graph.TupleList(edges=filtered_table[['origin_company_id', 'destiny_company_id']].itertuples(index=False), directed=True)
    
    # Plot the histogram and threshold line using Matplotlib and Seaborn
    plt.figure(figsize=(10, 6))
    sns.histplot(graph_table['transaction_volume'], bins=30, kde=False, color="#061727")
    plt.axvline(x=threshold, color='orange', linestyle='--', label=f'Threshold (percentile {percentile}): {threshold}')
    plt.xlabel('Transaction Value')
    plt.ylabel('Count')
    plt.title('Transaction Value Distribution with Threshold')
    plt.legend()
    plt.show()

    return subgraph

# Example usage
subgraph = generate_subgraph_by_value()


####

def calculate_distress_levels(subgraph, patient_zero_index, alpha=0.5):
    # Initialize distress levels
    distress_levels = [0] * len(subgraph.vs)
    distress_levels[patient_zero_index] = 1  # Patient zero is fully distressed

    # Track changes to avoid unnecessary iterations
    changes = True

    # Iteratively propagate distress
    while changes:
        changes = False
        for vertex in subgraph.vs:
            # Calculate cumulative distress from neighbors
            neighbor_distress = sum(
                distress_levels[neighbor.index] * subgraph[vertex.index, neighbor.index]
                for neighbor in vertex.neighbors()
            )

            # Calculate new distress level for the current vertex
            new_distress_level = alpha * neighbor_distress

            # Check if the distress level has changed
            if new_distress_level > distress_levels[vertex.index]:
                distress_levels[vertex.index] = new_distress_level
                changes = True

    return distress_levels

# Assuming the patient zero index is 5
patient_zero_index = 5
distress_levels = calculate_distress_levels(subgraph, patient_zero_index)
print(distress_levels)

#### 

def calculate_infection_levels(subgraph, patient_zero_index, beta=0.5, threshold=0.01):
    # Initialize infection levels
    infection_levels = [0] * len(subgraph.vs)
    infection_levels[patient_zero_index] = 1  # Patient zero is fully infected

    # Keep track of changes to avoid unnecessary iterations
    changes = True

    # Iteratively propagate infection
    while changes:
        changes = False
        for vertex in subgraph.vs:
            # Calculate cumulative infection from neighbors
            neighbor_infection = sum(
                infection_levels[neighbor.index] * beta * subgraph[vertex.index, neighbor.index]
                for neighbor in vertex.neighbors()
            )

            # Update infection level for the current vertex
            new_infection_level = infection_levels[vertex.index] + neighbor_infection

            # Check if the infection level has changed beyond the threshold
            if abs(new_infection_level - infection_levels[vertex.index]) > threshold:
                infection_levels[vertex.index] = new_infection_level
                changes = True

    return infection_levels

# Assuming the patient zero index is 5
patient_zero_index = 5
infection_levels = calculate_infection_levels(subgraph, patient_zero_index)
print(infection_levels)
