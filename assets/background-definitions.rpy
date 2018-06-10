
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       Assets: Backgrounds
#
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


#### Background Images ####

# CHAPTER 1 - BEGINNINGS #
image bg altissia_alleyway = 'images/backgrounds/altissia-alleyway-night.jpg'
image bg altissian_skyline = 'images/backgrounds/altissian_skyline.png'

image bg mc_home = 'images/backgrounds/mc_home.png'
image bg mc_room = 'images/backgrounds/mc_room.png'

image bg yureilplaza = 'images/backgrounds/yureil_plaza.png'
image bg yureilplazadark = 'images/backgrounds/yureil_plaza_dark.png'
image bg yureilplaza crowd = 'images/backgrounds/yureil_plaza_crowd.png'
image bg yureilplaza crowd dark = 'images/backgrounds/yureil_plaza_crowd_dark.png'

image bg yureilcorridor = 'images/backgrounds/yureil_corridor-2.png'
image bg yureilcorridor dark = 'images/backgrounds/yureil_corridor_dark.png'
image bg yureilcorridor fuse = 'images/backgrounds/yureil-fusebox-hallway.png'
image bg yureilcorridor fuse idle = 'images/backgrounds/yureil-fusebox-hallway-idle.png'

# CHAPTER 2 - EVACUATION #

image bg padore jetty = 'images/backgrounds/padore_jetty.png'
image bg evacuee hideout = 'images/backgrounds/evacuee_hideout.png'
image bg evacuee hideout dark = 'images/backgrounds/evacuee_hideout_dark.png'

image bg fountaincourtyard = 'images/backgrounds/fountain_courtyard.png'
image bg widestreet = 'images/backgrounds/wide_garden_street.png'
image bg mediumstreet = 'images/backgrounds/medium_street.png'
image bg rubblestreet = 'images/backgrounds/rubble_street.png'
image bg rubblestreet dark = 'images/backgrounds/rubble_street_dark.png'
image bg jettynearcellar = 'images/backgrounds/jetty-near-cellar2.png'
image bg cellar = 'images/backgrounds/cellar2.png'

# CHAPTER 3 - RESCUE #

image bg leviathan = 'images/backgrounds/leviathan.png'
image bg altar = 'images/backgrounds/altar01.png'
image bg altar whiteout static = 'images/backgrounds/altar-whiteout.png'
image bg dropship exterior = 'images/backgrounds/dropship/dropship-exterior.png'
image bg dropship exterior door = 'images/backgrounds/dropship/dropship-exterior-door.png'
image bg dropship loading bay = 'images/backgrounds/dropship/loading-bay.png'
image bg dropship corridor1 = 'images/backgrounds/dropship/interior-corridor-01.png'
image bg dropship corridor2 = 'images/backgrounds/dropship/interior-corridor-02.png'
image bg dropship corridor3 = 'images/backgrounds/dropship/interior-corridor-03.png'
image bg dropship corridor4 = 'images/backgrounds/dropship/interior-corridor-04.png'
image bg dropship room1 = 'images/backgrounds/dropship/dropship-room01.png'
image bg dropship room2 = 'images/backgrounds/dropship/dropship-room02.png'
image bg dropship room2 active = 'images/backgrounds/dropship/dropship-room02-active.png'
image bg dropship cell = 'images/backgrounds/dropship/ignis-cell.png'
image bg dropship loading bay exit = 'images/backgrounds/dropship/loading-bay-exit.png'
image cell bars = 'images/backgrounds/dropship/cell-bars.png'

# CHAPTER 4 - DATE #

image bg magisterialsquare = 'images/backgrounds/magisterial_square.png'

image black = "images/black.png"
image blackoverlay = Image("ui/black-layer.png", xalign=0.5, yalign=0.5)


### CTC button definition ###
image bg altar whiteout = LiveComposite(
    (1280, 720),
    (0, 0), "altar_base",
    (0, 0), "altar_glow"
    )

image altar_base:
    "images/backgrounds/altar01.png"
    linear 0.8 alpha 1.0
    repeat

image altar_glow:
    "images/backgrounds/altar-whiteout.png"
    linear 0.8 alpha 0.0
    choice:
        0.5
    choice:
        1
    choice:
        2
    choice:
        3
    choice:
        3
    choice:
        4
    choice:
        4
    choice:
        4.5
    choice:
        5
    "images/backgrounds/altar-whiteout.png"
    alpha 0.8
    repeat
