from graph import create_graph, State
import graphviz

def visualize_graph(graph: dict[State, dict[int, State]], output_file: str = "graph"):
    """
    Visualizes the state transition graph using graphviz.

    Args:
        graph (dict[State, dict[int, State]]): The state transition graph.
        output_file (str): The name of the output file (without extension).
    """
    dot = graphviz.Digraph(format="png")
    # dot.attr(rankdir="UD")  # Left-to-right layout
    dot.attr(layout="dot")  # Use dot layout engine

    # Add nodes and edges
    for state, transitions in graph.items():
        dot.node(str(state), label=f"State: {state}")

        for transition, next_state in transitions.items():
            dot.edge(str(state), str(next_state), label=f"{transition:04b}")

    # Render the graph to a file
    dot.render(output_file, cleanup=True)
    print(f"Graph visualization saved as {output_file}.png")

if __name__ == "__main__":
    graph = create_graph()

    # Visualize the graph
    visualize_graph(graph, output_file="state_transition_graph_dot")

    for state, transitions in graph.items():
        for transition, next_state in transitions.items():
            print(f"State: {state}, Transition: {transition:04b}, Next State: {next_state}")
