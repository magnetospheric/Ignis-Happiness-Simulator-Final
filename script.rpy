
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       Ignis Happiness Simulator
#       authored by Olly Ferrie
#       created 24-12-2017
#       last edited 26-12-2017
#
#       Main script file
#       Contains:
#               character definitions
#               character images
#               background images
#               extra images
#               start label
#
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

### Character definitions ###
define ignis = Character("Ignis")

#### Character Images ####
image ignis neutral  = "images/ignis-neutral.png"

#### Background Images ####
image bg altissia_alleyway = 'images/altissia-alleyway-night.jpg'


image countdown = DynamicDisplayable(countdown, length=10.0)

#plan - first we need a simple scene where your mouse cursor hovering creates a flashlight effect
#DONE

#second, we need the same scene, but the flashlight effect is only triggered when you click
#DONE

#now, we need an Awareness Counter that counts the seconds that go by while the flashlight is activated
#WE HAVE AN AWARENESS BAR THAT COUNTS EACH FLASHLIGHT TURN ON

#Now need to combine with a timer so that, instead of registering each turn on, it registers instead
#the seconds that pass

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

    # if $ show_countdown:
    #     # start awareness timer here
    #     show countdown
    #     ui.timer(9.0, ui.jumps("boom"))

    $ mouse_visible = True

    hide ignis neutral
    with dissolve

    #return to title screen
    return

# this will go in its own file eventually
label boom:

    return
