from gates import next_music1, next_music2, next_is_playing, next_transition

def parse_input(user_input):
    running = True
    previous, next, pause, play = 0, 0, 0, 0

    if user_input == "exit":
        running = False
    elif user_input == "previous":
        previous = 1
    elif user_input == "next":
        next = 1
    elif user_input == "pause":
        pause = 1
    elif user_input == "play":
        play = 1
    elif user_input != "no click":
        raise Exception("Invalid input. Please enter 'previous', 'next', 'pause', 'play' or 'no click'.")

    return previous, next, pause, play, running

def simulation_info():
    print("Welcome to the music player simulation!")
    print("You can control the music player with the following commands:")
    print("previous - go to the previous song")
    print("next - go to the next song")
    print("pause - pause the music")
    print("play - play the music")
    print("no click - do nothing")
    print("exit - exit the simulation")

def simulation():
    simulation_info()

    # memory
    music1 = 0
    music2 = 0
    is_playing = 0
    transition = 0

    # inputs
    previous = 0
    next = 0
    pause = 0
    play = 0

    running = True

    while running:
        print(f"\nCurrent state:")
        print(f"music2 = {music2}, music1 = {music1}, song = {music2}{music1}")
        print(f"music = {music2 << 1 | music1}")
        print(f"is playing: {bool(is_playing)}\n")

        user_input = input("Enter input (previous, next, pause, play, no click): ").strip().lower()

        try:
            previous, next, pause, play, running = parse_input(user_input)
        except Exception as e:
            print(e)
            continue

        print(f"Input: previous = {previous}, next = {next}, pause = {pause}, play = {play}")

        print(f"{music2}, {music1}, {transition}, {is_playing}, {previous}, {next}, {pause}, {play}")

        new_music1 = next_music1(music2, music1, transition, is_playing, previous, next, pause, play)
        new_music2 = next_music2(music2, music1, transition, is_playing, previous, next, pause, play)
        new_transition = next_transition(music2, music1, transition, is_playing, previous, next, pause, play)
        new_is_playing = next_is_playing(music2, music1, transition, is_playing, previous, next, pause, play)

        music1 = new_music1
        music2 = new_music2
        is_playing = new_is_playing
        transition = new_transition

        print(f"music2 = {music2}, music1 = {music1}, song = {music2}{music1}")

if __name__ == "__main__":
    simulation()
