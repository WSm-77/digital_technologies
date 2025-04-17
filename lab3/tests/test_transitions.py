from lab3.graph import create_graph, State, TRANSITION_NEXT, TRANSITION_PREVIOUS, RESUME, PAUSE, NO_CLICK, SONGS_COUNT
from lab3.gates import next_music1, next_music2, next_is_playing, next_transition

def get_bit(value: int, bit_position: int) -> int:
    """
    Returns the value of a specific bit in an integer.
    """
    return (value >> bit_position) & 0b1

class TestTransitions:
    def test_transitions(self):
        checked_states_cnt = 0

        graph = create_graph()

        for song_no in range(SONGS_COUNT):
            for transition in range(2):
                for is_playing in range(2):
                    for transition_type in [TRANSITION_NEXT, TRANSITION_PREVIOUS, RESUME, PAUSE, NO_CLICK]:
                        curr_state = State(
                            song_no = song_no,
                            is_transition_property=transition,
                            is_playing_property=is_playing
                        )

                        if transition_type not in graph[curr_state]:
                            continue

                        checked_states_cnt += 1

                        music1 = get_bit(song_no, 0)
                        music2 = get_bit(song_no, 1)

                        previous = get_bit(transition_type, 3)
                        next = get_bit(transition_type, 2)
                        pause = get_bit(transition_type, 1)
                        play = get_bit(transition_type, 0)

                        new_music1 = next_music1(music2, music1, transition, is_playing, previous, next, pause, play)
                        new_music2 = next_music2(music2, music1, transition, is_playing, previous, next, pause, play)
                        new_transition = next_transition(music2, music1, transition, is_playing, previous, next, pause, play)
                        new_is_playing = next_is_playing(music2, music1, transition, is_playing, previous, next, pause, play)

                        new_state = State(
                            song_no = new_music2 << 1 | new_music1,
                            is_transition_property = new_transition,
                            is_playing_property = new_is_playing
                        )

                        print(f"{curr_state} -> {transition_type:04b} -> {new_state}")

                        assert graph[curr_state][transition_type] == new_state, f"{curr_state} -> {transition_type:04b} -> {new_state} is not valid transition"

        assert checked_states_cnt == sum(len(transition_dict) for transition_dict in graph.values()), "Checked states count does not match the expected value"
