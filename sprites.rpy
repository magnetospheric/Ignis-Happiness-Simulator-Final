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





### CTC button definition ###
image smoke = LiveComposite(
    (1280, 720),
    (0, 0), "smoke1a",
    (0, 0), "smoke1b",
    (0, 0), "smoke2a",
    (0, 0), "smoke2b",
    (0, 0), "smoke3a",
    (0, 0), "smoke3b"
    )

image smoke1a:
    im.Alpha("images/effects/smoke1a.png",0.4)
    linear 3.0 alpha 1.0
    im.Alpha("images/effects/smoke1a.png",0.4)
    linear 3.0 alpha 0.0
    repeat

image smoke1b:
    im.Alpha("images/effects/smoke1b.png",0.4)
    linear 3.0 alpha 0.0
    im.Alpha("images/effects/smoke1b.png",0.4)
    linear 3.0 alpha 1.0
    repeat

image smoke2a:
    im.Alpha("images/effects/smoke2a.png",0.4)
    linear 2.0 alpha 1.0
    im.Alpha("images/effects/smoke2a.png",0.4)
    linear 2.0 alpha 0.0
    repeat

image smoke2b:
    im.Alpha("images/effects/smoke2b.png",0.4)
    linear 2.0 alpha 0.0
    im.Alpha("images/effects/smoke2b.png",0.4)
    linear 2.0 alpha 1.0
    repeat

image smoke3a:
    im.Alpha("images/effects/smoke3a.png",0.6)
    linear 2.0 alpha 1.0
    im.Alpha("images/effects/smoke3a.png",0.6)
    linear 2.0 alpha 0.0
    repeat

image smoke3b:
    im.Alpha("images/effects/smoke3b.png",0.6)
    linear 2.0 alpha 0.0
    im.Alpha("images/effects/smoke3b.png",0.6)
    linear 2.0 alpha 1.0
    repeat
