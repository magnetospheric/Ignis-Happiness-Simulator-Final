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
define softflash = Fade(.3, 0.0, .4, color="#ffffff99")
