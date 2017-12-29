
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

#plan - first we need a simple scene where your mouse cursor hovering creates a flashlight effect
#DONE

#second, we need the same scene, but the flashlight effect is only triggered when you click
#DONE

#now, we need an Awareness Counter that counts the seconds that go by while the flashlight is activated
#WE HAVE AN AWARENESS BAR THAT COUNTS EACH FLASHLIGHT TURN ON

#Now need to combine with a timer so that, instead of registering each turn on, it registers instead
#the seconds that pass
#DONE

#Now we need to animate the awareness bar

#Now we need to log and display the amount of battery left in the torch

#Need to have a failsafe for what happens when the flashlight runs out. don't frustrate the player toooo much,
#and can't kill them.

#Next we will need to work out what Ignis expressions we need

#Next we will need to set up a starting-choices menu for the player

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

    # $ renpy.ui.timer(5.0, renpy.ui.jumps("boom"))

    ignis "Look around this room and see if there's anything useful."

    # $ mouse_visible = False

    call screen flashlight

    # $ mouse_visible = True

    hide ignis neutral
    with dissolve

    #return to title screen
    return
