## This file contains callbacks for sound effects
##


## typewriter click ##########################################################


init -1 python:

    def clicky_typewriter(event, **kwargs):
        if event == "show":
            renpy.music.play(renpy.random.choice([
                "<from 0.0>audio/typewriters/typewriter-narrator.wav",
                "<from 2.0>audio/typewriters/typewriter-narrator.wav",
                "<from 8.0>audio/typewriters/typewriter-narrator.wav",
                "<from 12.0>audio/typewriters/typewriter-narrator.wav",
                "<from 15.0>audio/typewriters/typewriter-narrator.wav",
                "<from 18.0>audio/typewriters/typewriter-narrator.wav",
                "<from 20.0>audio/typewriters/typewriter-narrator.wav",
                "<from 22.0>audio/typewriters/typewriter-narrator.wav",
                "<from 26.0>audio/typewriters/typewriter-narrator.wav"
            ]), channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def clicky_typewriter_titles(event, **kwargs):
        if event == "show":
            renpy.music.play(renpy.random.choice([
                "<from 0.0>audio/typewriters/typewriter-titles.wav",
                "<from 2.0>audio/typewriters/typewriter-titles.wav",
                "<from 8.0>audio/typewriters/typewriter-titles.wav",
                "<from 12.0>audio/typewriters/typewriter-titles.wav",
                "<from 15.0>audio/typewriters/typewriter-titles.wav",
                "<from 18.0>audio/typewriters/typewriter-titles.wav",
                "<from 20.0>audio/typewriters/typewriter-titles.wav",
                "<from 22.0>audio/typewriters/typewriter-titles.wav"
            ]), channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
