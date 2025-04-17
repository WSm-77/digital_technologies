from graph import create_graph, State
import logicmin
import csv

def get_states_transition_table(graph: dict[State, dict[int, State]]) -> tuple[list[str], list[str]]:
    states_inputs = []
    next_states = []

    for state, transitions in graph.items():
        for transition, next_state in transitions.items():
            states_inputs.append(f"{state}{transition:04b}")
            next_states.append(f"{next_state}")

    return states_inputs, next_states

def minimize_table(variables: list[str], outputs: list[str], variables_names: list[str], outputs_names: list[str]) -> None:
    assert len(variables[0]) == len(variables_names), "Number of variables must match number of names in variables_names list"
    assert len(outputs[0]) == len(outputs_names), "Number of outputs must match number of names in outputs_names list"

    truth_table = logicmin.TT(len(variables_names), len(outputs_names))

    for state_input, next_state in zip(variables, outputs):
        truth_table.add(state_input, next_state)

    solution = truth_table.solve()
    print(solution.printN(variables_names, outputs_names, syntax='VHDL'))
    # print(solution.printN(states_inputs_names, next_states_names))

if __name__ == "__main__":
    # states_inputs_names = ["Music1", "Music2", "Transition", "IsPlaying", "Previous", "Next", "Pause", "Play"]
    states_inputs_names = ["M1", "M2", "T", "P", "<|", "|>", "||", ">"]
    # next_states_names = ["NextMusic1", "NextMusic2", "NextTransition", "NextIsPlaying"]
    next_states_names = ["NM1", "NM2", "NT", "NP"]
    graph = create_graph()
    states_inputs, next_states = get_states_transition_table(graph)

    print("Transition table minimalization:\n")

    minimize_table(states_inputs, next_states, states_inputs_names, next_states_names)

    with open("truth_table_state_transitions.csv", mode="w", newline="") as file:
        csv_writer = csv.writer(file, delimiter=",")
        csv_writer.writerow(states_inputs_names + next_states_names)
        for state_input, next_state in zip(states_inputs, next_states):
            csv_writer.writerow(list(map(int, state_input + next_state)))

    output_names = ["NM1", "NM2", "NP"]
    states = [state[:4] for state in states_inputs]
    outputs = [state[:2] + state[3] for state in states_inputs]

    print("\nOutput values table minimalization:\n")
    minimize_table(states, outputs, states_inputs_names[:4], output_names)

    with open("truth_table_output.csv", mode="w", newline="") as file:
        csv_writer = csv.writer(file, delimiter=",")
        csv_writer.writerow(states_inputs_names[:4] + output_names)
        for state_input in states_inputs:
            state_output = state_input[:2] + state_input[3]
            csv_writer.writerow(list(map(int, state_input[:4] + state_output)))
