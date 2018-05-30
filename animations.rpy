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
define softflash = Fade(.25, 0.0, .35, color="#ffffff99")
define fastsoftflash = Fade(.2, 0.0, .3, color="#ffffff99")


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
