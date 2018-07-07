
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
image bg leville exterior = 'images/backgrounds/leville-exterior.png'
image bg leville corridor = 'images/backgrounds/leville-corridor.png'
image bg leville room = 'images/backgrounds/leville-room.png'
image bg leville alleyway = 'images/backgrounds/leville-alleyway.png'
image bg leville alleyway whiteout = 'images/backgrounds/leville-alleyway-whiteout.png'
image bg listropark = 'images/backgrounds/listropark.png'
image bg listroparkdark = 'images/backgrounds/listropark-dark.png'
image bg foodcart = 'images/backgrounds/food-cart.png'
image bg buskers = 'images/backgrounds/buskers.png'
image bg flowers = 'images/backgrounds/flowers.png'
image bg magisterialsquare = 'images/backgrounds/magisterial-plaza.png'
image bg restaurant = 'images/backgrounds/restaurant.png'
image bg gondola = 'images/backgrounds/gondola.png'
image bg leville exterior dark = 'images/backgrounds/leville-exterior-dark.png'

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

image bg credit_backgrounds:
    "images/credits/01.png"
    linear 6.858
    "images/credits/02.png"
    linear 6.858
    "images/credits/03.png"
    linear 6.858
    "images/credits/04.png"
    linear 6.858
    "images/credits/05.png"
    linear 6.858
    "images/credits/06.png"
    linear 6.858
    "images/credits/07.png"
    linear 6.858
    "images/credits/08.png"
    linear 6.858
    "images/credits/09.png"
    linear 6.858
    "images/credits/10.png"
    linear 6.858
    "images/credits/11.png"
    linear 6.858
    "images/credits/12.png"
    linear 6.858
    "images/credits/13.png"
    linear 6.858
    "images/credits/14.png"
    linear 6.858
    "images/credits/15.png"
    linear 6.858
    "images/credits/16.png"
    linear 6.858
    "images/credits/17.png"
    linear 6.858
    "images/credits/18.png"
    linear 6.858
    "images/credits/19.png"
    linear 6.858
    "images/credits/20.png"
    linear 6.858
    "images/credits/21.png"
    linear 6.858
    "images/credits/22.png"
    linear 6.858
    "images/credits/23.png"
    linear 6.858
    "images/credits/24.png"
    linear 6.858
    "images/credits/25.png"
    linear 6.858
    "images/credits/26.png"
    linear 6.858
    "images/credits/27.png"
    linear 6.858
    "images/credits/28.png"
    linear 6.858
    "images/credits/29.png"
    linear 6.858
    "images/credits/30.png"
    linear 6.858
    "images/credits/31.png"
    linear 6.858
    "images/credits/32.png"
    linear 6.858
    "images/credits/33.png"
    linear 6.858
    "images/credits/34.png"
    linear 6.858
    "images/credits/35.png"
    linear 6.858
    "images/credits/36.png"
    linear 6.858
    "images/credits/37.png"
    linear 6.858
    "images/credits/38.png"
    linear 6.858
    "images/credits/39.png"
    linear 6.858
    "images/credits/40.png"
    linear 6.858
    "images/credits/42.png"
    linear 6.858
    "images/credits/43.png"
    linear 6.858
    "images/credits/44.png"
    linear 6.858
    "images/credits/45.png"
    linear 6.858
