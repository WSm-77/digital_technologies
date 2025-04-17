def next_is_playing(music2, music1, transition, is_playing, previous, next, pause, play):
    res = not transition and \
          not previous and \
          not next and \
          not pause and \
         play or is_playing and \
          not previous and \
          not pause and \
          not play or is_playing and \
          not next and \
          not pause and \
          not play

    return int(res)

def next_transition(music2, music1, transition, is_playing, previous, next, pause, play):
    res = not previous and \
         next and \
          not pause and \
          not play or previous and \
          not next and \
          not pause and \
          not play

    return int(res)

def next_music1(music2, music1, transition, is_playing, previous, next, pause, play):
    res = not music1 and \
          not transition and \
          not previous and \
         next and \
          not pause and \
          not play or  not music1 and \
          not transition and \
         previous and \
          not next and \
          not pause and \
          not play or music1 and \
          not transition and \
          not previous and \
          not next and \
          not pause or music1 and \
          not transition and \
          not previous and \
          not next and \
          not play or music1 and \
         transition and \
          not previous and \
          not pause and \
          not play or music1 and \
         transition and \
          not next and \
          not pause and \
          not play

    return int(res)

def next_music2(music2, music1, transition, is_playing, previous, next, pause, play):
    res = not music2 and \
          not music1 and \
          not transition and \
         previous and \
          not next and \
          not pause and \
          not play or  not music2 and \
         music1 and \
          not transition and \
          not previous and \
         next and \
          not pause and \
          not play or music2 and \
          not music1 and \
          not previous and \
          not pause and \
          not play or music2 and \
          not transition and \
          not previous and \
          not next and \
          not pause or music2 and \
          not transition and \
          not previous and \
          not next and \
          not play or music2 and \
         transition and \
          not previous and \
          not pause and \
          not play or music2 and \
         transition and \
          not next and \
          not pause and \
          not play or music2 and \
         music1 and \
          not next and \
          not pause and \
          not play

    return int(res)
