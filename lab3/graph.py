from __future__ import annotations

SONGS_COUNT = 4
TRANSITION_NEXT = 0b0100
TRANSITION_PREVIOUS = 0b1000
RESUME = 0b0001
PAUSE = 0b0010
NO_CLICK = 0b0000

class State:
    def __init__(self, song_no: int, is_transition_property: int, is_playing_property: int):
        self.song_no = song_no
        self.is_transition_property = is_transition_property
        self.is_playing_property = is_playing_property
        self.state = (song_no << 2) | (is_transition_property << 1) | is_playing_property

    def get_song_number(self):
        return self.song_no

    def is_transition(self):
        return self.is_transition_property

    def is_playing(self):
        return self.is_playing_property

    def get_state(self):
        return self.state

    def __eq__(self, value):
        if not isinstance(value, State):
            return False

        return self.song_no == value.song_no and \
                self.is_transition_property == value.is_transition_property and \
                self.is_playing_property == value.is_playing_property

    def __hash__(self):
        return hash(self.state)

    def __repr__(self):
        return f"{self.state:04b}"

    @staticmethod
    def value_to_state(value: int) -> State:
        return State(
            song_no = (value >> 2) & 0b11,
            is_transition_property = (value >> 1) & 0b1,
            is_playing_property = value & 0b1
        )

def create_graph():
    states_val = [val for val in range(2 ** 4)]

    # graph[state][input] = next_state
    graph: dict[State, dict[int, State]] = {State.value_to_state(state_val) : {} for state_val in states_val}

    for state in graph.keys():
        if state.is_transition():
            graph[state][TRANSITION_NEXT] = state
            graph[state][TRANSITION_PREVIOUS] = state
            graph[state][NO_CLICK] = State(
                song_no = state.get_song_number(),
                is_transition_property = 0,
                is_playing_property = state.is_playing()
            )
        else:
            graph[state][TRANSITION_NEXT] = State(
                song_no = (state.get_song_number() + 1) % SONGS_COUNT,
                is_transition_property = 1,
                is_playing_property = state.is_playing()
            )
            graph[state][TRANSITION_PREVIOUS] = State(
                song_no = (state.get_song_number() - 1) % SONGS_COUNT,
                is_transition_property = 1,
                is_playing_property = state.is_playing()
            )
            graph[state][NO_CLICK] = State(
                song_no = state.get_song_number(),
                is_transition_property = 0,
                is_playing_property = state.is_playing()
            )

            graph[state][RESUME] = State(
                song_no = state.get_song_number(),
                is_transition_property = 0,
                is_playing_property = 1
            )

            graph[state][PAUSE] = State(
                song_no = state.get_song_number(),
                is_transition_property = 0,
                is_playing_property = 0
            )

    return graph

if __name__ == "__main__":
    graph = create_graph()

    for state, transitions in graph.items():
        for transition, next_state in transitions.items():
            print(f"State: {state}, Transition: {transition:04b}, Next State: {next_state}")
