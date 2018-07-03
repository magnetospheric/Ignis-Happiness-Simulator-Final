
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


#### FILES USED ####
# -- settings.rpy
# -- scene_01_start.rpy
# -- credits.rpy


#### SPLASHSCREEN ####

# image producer = "images/logos/producer.png"
# image author = "images/logos/author.png"
# image title = "images/logos/title.png"

label splashscreen:

    # python:
    #
    #     if not persistent.set_volumes:
    #         persistent.set_volumes = True
    #
    #         _preferences.volumes['music'] = .70
    #         _preferences.volumes['sounds'] = .80
    #
    # play music "sound/Voglio_La_Pace-Snippet.wav" fadein 1.0

    # scene black
    # with Pause(5)
    #
    # show producer with dissolve
    # with Pause(2)
    #
    #
    # scene author with dissolve
    # with Pause(2)


    # scene title with dissolve
    # with Pause(1)
    # stop music fadeout 0.5
    # pause 0.5
    #
    return

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
# list made and ref images compiled

#Next, work out background images required
# list made of all b images necessary for starting scene

#Next we will need to set up a starting-choices menu for the player
# DONE
