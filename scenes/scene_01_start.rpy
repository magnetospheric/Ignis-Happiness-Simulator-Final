#starting scene
#contains labels:
    # start
    # mc_room
    # to_work

# covers scene setup, location fn tutorial


# use this start label to test things
label startn:

    #starting variables

    $ ignis_name = "Stranger"
    $ your_name = "You"

    #shows the first background
    scene bg altissia_alleyway

    #shows the first character
    show ignis neutral
    with dissolve

    "Altissia, on the day of the Covenant. Everything is going to hell."

    ignis "I've run into a bit of trouble. Would you care to help me?"

    ignis "Look around this room and see if there's anything useful."

    call screen flashlight

# The game starts here.
label start:

    # start scene needs to introduce the hunting-around mechanic for later
    # maybe protag is looking for their keys or something that'll be useful later

    #starting variables
    $ ignis_name = "Stranger"
    $ your_name = "You"
    $ ravus_name = "White-haired man"
    $ ardyn_name = "Sinister man"

    #scene dawns on an overview of altissia
    scene bg altissian_skyline

    "Altissia, on the day of the Covenant."

    "The sky is a pale pastel glow, but despite this, the atmosphere is tense. You can feel it around you, thick as syrup."

    "Today is the day that the Oracle, Lady Lunafreya, summons a goddess."
    "Leviathan. The stuff of legends."
    "You remember the stories. The prayers. You never thought you would see this in the flesh."

    "An important day, indeed."

    "So it really doesn't help that today, of all days, you are late to work."

    jump mc_room

label mc_room:

    scene bg mc_room

    you "Ah, where did I put my keys?"

    # look up to left
    # look to right
    # main room view

    you "Y'know, it would be {i}really{/i} useful if I could just ... find them ..."

    # this will teach you the 'find things' mechanic
    show screen infobubble(who="meeee", what="yoouuuuu")

    # call screen focus
    # call screen flashlight
    # imagebutton "continue" xpos 300 ypos 300 action Return()

    you "Found 'em!"

    jump to_work
