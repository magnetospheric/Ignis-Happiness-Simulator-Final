## This file contains callbacks for sound effects
##


## typewriter click ##########################################################


init -1 python:
    def clicky_typewriter(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/click.wav", channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
