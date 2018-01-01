# The game starts here.
label start:

    #starting variables

    $ ignis_name = "Blargh"
    $ your_name = "Meee"

    #shows the first background
    scene bg altissia_alleyway

    #shows the first character
    show ignis neutral
    with dissolve

    # These display lines of dialogue.

    "Altissia, on the day of the Covenant. Everything is going to hell."

    you "Hi."

    ignis "I've run into a bit of trouble. Would you care to help me?"

    # $ renpy.ui.timer(5.0, renpy.ui.jumps("boom"))

    ignis "Look around this room and see if there's anything useful."

    # $ mouse_visible = False

    call screen flashlight

    # $ mouse_visible = True

    hide ignis neutral
    with dissolve

    #return to title screen
    return
