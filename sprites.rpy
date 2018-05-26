## This file contains sprites used to create animated visuals
##


## blue armiger crackle ########################################################

image bluelightning1:
    alpha 0.3
    "images/effects/blue-lightning01.png"
    # This randomizes the time between blinking.
    choice:
        0.2
    choice:
        0.3
    alpha 0.2
    "images/effects/blue-lightning03.png"
    choice:
        0.2
    choice:
        0.3
    alpha 0.3
    "images/effects/blue-lightning02.png"
    choice:
        0.2
    choice:
        0.3
    alpha 0.2
    "images/effects/blue-lightning03.png"
    choice:
        0.2
    choice:
        0.3
    repeat


### CTC button definition ###
image bluelightning = LiveComposite(
    (865, 705),
    (0, 0), "bluelightning-base",
    (0, 0), "bluelightning-mid",
    (0, 0), "bluelightning-top",
    (0, 0), "bluelightning-mid"
    )

image bluelightning-base:
    "images/effects/blue-lightning01.png"
    linear 0.6 alpha 0.4
    "images/effects/blue-lightning01.png"
    linear 0.6 alpha 0.0
    "images/effects/blue-lightning01.png"
    linear 0.6 alpha 0.0
    "images/effects/blue-lightning01.png"
    linear 0.6 alpha 0.0
    repeat

image bluelightning-top:
    alpha 0.0
    "images/effects/blue-lightning02.png"
    linear 0.6 alpha 0.0
    "images/effects/blue-lightning02.png"
    linear 0.6 alpha 0.0
    "images/effects/blue-lightning02.png"
    linear 0.6 alpha 0.4
    "images/effects/blue-lightning02.png"
    linear 0.6 alpha 0.0
    repeat

image bluelightning-mid:
    alpha 0.0
    "images/effects/blue-lightning03.png"
    linear 0.6 alpha 0.0
    "images/effects/blue-lightning03.png"
    linear 0.6 alpha 0.05
    "images/effects/blue-lightning03.png"
    linear 0.6 alpha 0.0
    "images/effects/blue-lightning03.png"
    linear 0.6 alpha 0.05
    repeat
