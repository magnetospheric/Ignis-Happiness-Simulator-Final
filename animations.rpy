## This file contains animations used to manipulate game elements.
##


## fades ######################################################################
define slowfade = Fade(2.0, 0.0, 2.0)
define mediumfade = Fade(3.0, 0.0, 3.0)
define fastfade = Fade(1.0, 0.0, 1.0)

## dissolves ##################################################################
define slowdissolve = Dissolve(8)
define mediumdissolve = Dissolve(5)
define fastdissolve = Dissolve(2)
define fastestdissolve = Dissolve(1)


## other effects ##############################################################
define flash = Fade(.25, 0.0, .75, color="#fff")
define hardflash = Fade(.25, 0.0, .35, color="#ffffffCC")
define softflash = Fade(.25, 0.0, .35, color="#ffffff99")
define fastsoftflash = Fade(.2, 0.0, .3, color="#ffffff99")
define fasthardflash = Fade(.2, 0.0, .3, color="#ffffffCC")
define fastesthardflash = Fade(.15, 0.0, .25, color="#ffffffCC")


## particles ##################################################################
image soot_particles:
        # choice (show_soot == True):
        Fixed(
            SnowBlossom(im.Alpha("images/effects/big-soot.png",0.7), border=10, xspeed=(-50, 50), yspeed=(50, -50), count=100, start=0, fast=True),
            SnowBlossom(im.Alpha("images/effects/medium-soot.png",0.8), border=10, xspeed=(-50, 50), yspeed=(50, -50), count=150, start=0, fast=True),
            SnowBlossom(im.Alpha("images/effects/little-soot.png",0.9), border=10, xspeed=(-50, 50), yspeed=(50, -50), count=380, start=0, fast=True),
            SnowBlossom(im.Alpha("images/effects/little-soot.png",0.6), border=10, xspeed=(-50, 50), yspeed=(50, -50), count=180, start=0, fast=True)
            )
# this one is designed to be shown above character images / only a few particles
image soot_particles_sparse:
        # choice (show_soot == True):
        Fixed(
            SnowBlossom(im.Alpha("images/effects/big-soot.png",0.3), border=10, xspeed=(-50, 50), yspeed=(50, -50), count=50, start=0, fast=True),
            SnowBlossom(im.Alpha("images/effects/medium-soot.png",0.3), border=10, xspeed=(-50, 50), yspeed=(50, -50), count=50, start=0, fast=True)
            )


image glow_particles:
        # choice (show_snow == True):
        Fixed(
            SnowBlossom(im.Alpha("images/effects/pink-glow-small.png",0.3), border=10, xspeed=(-30, 30), yspeed=(40, -40), count=12, start=0, fast=True),
            SnowBlossom(im.Alpha("images/effects/purple-glow-small.png",0.3), border=10, xspeed=(-30, 30), yspeed=(40, -40), count=12, start=0, fast=True),
            SnowBlossom(im.Alpha("images/effects/blue-glow-small.png",0.3), border=10, xspeed=(-30, 30), yspeed=(40, -40), count=12, start=0, fast=True),

            SnowBlossom(im.Alpha("images/effects/pink-glow-medium.png",0.2), border=10, xspeed=(-20, 20), yspeed=(40, -40), count=1, start=0, fast=True),
            SnowBlossom(im.Alpha("images/effects/purple-glow-medium.png",0.2), border=10, xspeed=(-20, 20), yspeed=(40, -30), count=1, start=0, fast=True),
            SnowBlossom(im.Alpha("images/effects/blue-glow-medium.png",0.2), border=10, xspeed=(-20, 20), yspeed=(40, -40), count=1, start=0, fast=True)
            )


### Glowing CTC button definition ###
image ctc_blink = LiveComposite(
    (65, 65),
    (1120, 635), "ctc_base",
    (1120, 635), "glow"
    )

image ctc_base:
    "images/ui/next_button_small.png"
    linear 0.8 alpha 1.0
    repeat

image glow:
    "images/ui/next_button_hover_small.png"
    linear 0.8 alpha 0.0
    "images/ui/next_button_hover_small.png"
    linear 0.8 alpha 0.8
    repeat



# AWARENESS BAR ANIMATIONS FOR MAGITEK TROOPERS #
image awareness20:
    "images/ui/awareness/awareness20.png"
    linear 0.5 alpha 0.5
    "images/ui/awareness/awareness20.png"
    linear 0.5 alpha 1.0
    repeat
image awareness40:
    "images/ui/awareness/awareness40.png"
    linear 0.5 alpha 0.5
    "images/ui/awareness/awareness40.png"
    linear 0.5 alpha 1.0
    repeat
image awareness60:
    "images/ui/awareness/awareness60.png"
    linear 0.5 alpha 0.5
    "images/ui/awareness/awareness60.png"
    linear 0.5 alpha 1.0
    repeat
image awareness80:
    "images/ui/awareness/awareness80.png"
    linear 0.5 alpha 0.5
    "images/ui/awareness/awareness80.png"
    linear 0.5 alpha 1.0
    repeat
image awareness100:
    "images/ui/awareness/awareness100.png"
    linear 0.5 alpha 0.5
    "images/ui/awareness/awareness100.png"
    linear 0.5 alpha 1.0
    repeat
image awarenesscrit:
    "images/ui/awareness/awarenesscrit.png"
    linear 0.5 alpha 0.8
    "images/ui/awareness/awarenesscrit.png"
    linear 0.5 alpha 1.0
    repeat
