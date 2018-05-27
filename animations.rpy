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
        choice (show_soot == True):
            Fixed(
                    SnowBlossom(im.Alpha("images/effects/big_soot.png",0.9), count=10, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/effects/medium_soot.png",0.9), count=20, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/effects/little-soot.png",0.9), count=30, start=10, yspeed=(40,80)) )

image snow:
        choice (show_snow == True):
            Fixed(
                    SnowBlossom(im.Alpha("images/sprites/big_snow.png",0.82), count=2, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/sprites/medium_snow.png",0.94), count=8, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/sprites/small_snow.png",0.97), count=12, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/sprites/tiny_snow.png",0.99), count=22, start=5, yspeed=(40,80)) )
        choice (show_snow == False):
            Fixed(
                    SnowBlossom(im.Alpha("images/sprites/big_snow.png",0.0), count=1, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/sprites/medium_snow.png",0.0), count=1, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/sprites/small_snow.png",0.0), count=1, start=10, yspeed=(40,80)),
                    SnowBlossom(im.Alpha("images/sprites/tiny_snow.png",0.0), count=1, start=5, yspeed=(40,80)) )
