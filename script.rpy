# script for Prompto Happiness Simulator 2k17
# authored by Olly Ferrie
# created 07-05-2017
#last edited 08-05-2017

### Character definitions ###
define ignis = Character("Ignis")
#### Character Images ####
image ignis neutral  = "images/ignis-neutral.png"
#### Background Images ####
image bg altissia_alleyway = 'images/altissia-alleyway-night.jpg'

#plan - first we need a simple scene where your mouse cursor hovering creates a flashlight effect
#second, we need the same scene, but the flashlight effect is only triggered when you click
#DONE
#now, we need an Awareness Counter that counts the seconds that go by while the flashlight is activated


# The game starts here.

label start:

    #shows the first background
    scene bg altissia_alleyway

    #shows the first character
    show ignis neutral
    with dissolve

    # These display lines of dialogue.

    "Altissia, on the day of the Covenant. Everything is going to hell."

    ignis "I've run into a bit of trouble. Would you care to help me?"

    ignis "Look around this room and see if there's anything useful."

    $ mouse_visible = False
    call screen flashlight

    hide ignis neutral
    with dissolve

    #return to title screen
    return
