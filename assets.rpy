
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       Asset definitions
#
#       Contains:
#               narrator definitions
#               character definitions
#               ctc button
#               character images
#               background images
#               sprites
#               music?
#
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

### Narrator definitions ###
define centered = Character(
                            None,
                            what_size=20,
                            what_outlines=[(2, "#ffffff33", 0, 0)],
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.5,
                            window_yalign=0.32
                        )
define top_narrator = Character(
                            '',
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/transparent.png",
                            what_outlines=[(2, "#ffffff33", 0, 0)],
                            callback=clicky_typewriter,
                            window_yalign=0.1,
                            window_xalign=0,
                            window_xsize=800
                        )
define topcentre_narrator = Character(
                            '',
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/transparent.png",
                            what_outlines=[(2, "#ffffff33", 0, 0)],
                            callback=clicky_typewriter,
                            window_yalign=0.3,
                            window_xalign=0.2,
                            window_xsize=800
                        )
define centre_narrator = Character(
                            '',
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/transparent.png",
                            callback=clicky_typewriter,
                            window_yalign=0.5,
                            window_xalign=0.45,
                            window_xsize=900
                        )
define centrebottomright_narrator = Character('',
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/transparent.png",
                            callback=clicky_typewriter,
                            window_yalign=0.85,
                            window_xalign=0.7,
                            window_xsize=500
                        )
define narrator1 = Character(
                            '',
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            callback=clicky_typewriter,
                            window_background="images/ui/dialog_bg01.png",
                        )
define narrator1_nosound = Character(
                            '',
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/dialog_bg01.png"
                        )


### Character definitions ###
# IGNIS IS IN HIS OWN FILE

define you = DynamicCharacter(
                            'your_name',
                            who_color="#ffeff6",
                            window_background="images/ui/dialog_bg01.png",
                            who_outlines=[ (7, "#0000004D", 0, 0), (4, "#ffffff59", 0, 0), (3, "#3b2831", 0, 0) ],
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            callback=clicky_typewriter
                        )

define altissianguard = Character(
                            "Guard on Duty",
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/dialog_bg01.png",
                            callback=clicky_typewriter
                        )
define captain = Character(
                            "Captain",
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/dialog_bg01.png",
                            callback=clicky_typewriter
                        )

# niffs
define ravus = DynamicCharacter('ravus_name', who_color="#e0e0e0", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg01.png")
define ardyn = DynamicCharacter('ardyn_name', who_color="#d0c3bf", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg01.png")
#MAKE SURE to use a robot sound for the typewriter noise for the trooper!
define magitektrooper = Character("Trooper", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg01.png")
define caligo = Character("Caligo", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg01.png")
define unidentified_voice = Character("Unidentified Voice", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg01.png")

#other chocobros
define prompto = Character("Prompto", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg01.png")

#citizens
define citizen1 = Character("Scared Citizen", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg01.png")
define citizen2 = Character("Reasonable Citizen", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg01.png")
define citizen3 = Character("Sceptical Citizen", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg01.png")
# define citizen1 = Character("Pondering Citizen", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg01.png")
# define citizen2 = Character("Reasonable Citizen", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg01.png")
# define citizen3 = Character("Excited Citizen", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg01.png")

### CTC button definition ###
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


#### Character Images ####
# IGNIS IS IN HIS OWN FILE

image altissianguard neutral  = "images/characters/altissianguard-neutral.png"
image altissianguard smile  = "images/characters/altissianguard-smile.png"

image captain neutral = "images/characters/captain-neutral.png"
image captain smile = "images/characters/captain-smile.png"
image captain neutral openmouth = "images/characters/captain-neutral-openmouth.png"
image captain looking around = "images/characters/captain-looking-around.png"

image citizens dark = "images/characters/citizens-dark.png"
image citizens scared = "images/characters/citizens-dark-scared.png"
image citizens reasonable = "images/characters/citizens-dark-reasonable.png"
image citizens sceptical = "images/characters/citizens-dark-sceptical.png"

image ardyn trashbags = "images/characters/ardyn.png"
image ardyn neon = "images/characters/ardyn-neon.png"
image ardyn silhouette = "images/characters/ardyn-silhouette.png"

image trooper distance = "images/characters/trooper-distance.png"
image trooper lunging = "images/characters/trooper-lunging.png"

### trooper short circuiting animation definition ###
image trooper shortcircuit = LiveComposite(
    (758, 720),
    (0, 0), "shortcircuit0"
    )

image shortcircuit0:
    alpha 1.0
    "images/characters/trooper-short-circuit-0.png"
    choice:
        0.07
    choice:
        0.1
    choice:
        0.2
    choice:
        0.3
    choice:
        0.4
    # This randomizes the time between blinking.
    "images/characters/trooper-short-circuit-1.png"
    choice:
        0.07
    choice:
        0.1
    choice:
        0.2
    choice:
        0.3
    choice:
        0.4
    "images/characters/trooper-short-circuit-0.png"
    choice:
        0.07
    choice:
        0.1
    choice:
        0.2
    choice:
        0.3
    choice:
        0.4
    "images/characters/trooper-short-circuit-2.png"
    choice:
        0.07
    choice:
        0.1
    choice:
        0.2
    choice:
        0.3
    choice:
        0.4
    repeat


### trooper short circuiting animation definition ###
image trooper shortcircuit07 = LiveComposite(
    (758, 720),
    (0, 0), "shortcircuit1"
    )

image shortcircuit1:
    alpha 0.7
    "images/characters/trooper-short-circuit-0.png"
    choice:
        0.1
    choice:
        0.2
    choice:
        0.3
    choice:
        0.4
    # This randomizes the time between blinking.
    "images/characters/trooper-short-circuit-1.png"
    choice:
        0.1
    choice:
        0.2
    choice:
        0.3
    choice:
        0.4
    "images/characters/trooper-short-circuit-0.png"
    choice:
        0.1
    choice:
        0.2
    choice:
        0.3
    choice:
        0.4
    "images/characters/trooper-short-circuit-2.png"
    choice:
        0.1
    choice:
        0.2
    choice:
        0.3
    choice:
        0.4
    repeat

### trooper short circuiting animation definition ###
image trooper shortcircuit05 = LiveComposite(
    (758, 720),
    (0, 0), "shortcircuit2"
    )

image shortcircuit2:
    alpha 0.5
    "images/characters/trooper-short-circuit-0.png"
    choice:
        0.2
    choice:
        0.3
    choice:
        0.4
    choice:
        0.5
    # This randomizes the time between blinking.
    "images/characters/trooper-short-circuit-1.png"
    choice:
        0.2
    choice:
        0.3
    choice:
        0.4
    choice:
        0.5
    "images/characters/trooper-short-circuit-0.png"
    choice:
        0.2
    choice:
        0.3
    choice:
        0.4
    choice:
        0.5
    "images/characters/trooper-short-circuit-2.png"
    choice:
        0.2
    choice:
        0.3
    choice:
        0.4
    choice:
        0.5
    repeat


# used to position images at specific x and y pos
transform SpriteLoc2(x, y):
    pos (x, y)

#ignis raised eyes
#ignis skeptical
#ignis calm
#ignis angry
#ignis smiling
#ignis smiling widely
#ignis laughing
#ignis eyes closed (pain)
#ignis eyes closed (calm)
#ignis distraught / pained (eyes open)
#ignis looking off to the side
#ignis looking upward
#ignis propping his glasses up
#ignis shocked (open-mouthed)
#ignis scared
#ignis sad (mouth closed)
#ignis determined

#(and all of these with blind iggy AND with ringhand Iggy too)

#### Background Images ####
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

image bg leviathan = 'images/backgrounds/leviathan.png'
image bg altar = 'images/backgrounds/altar01.png'
image bg altar whiteout static = 'images/backgrounds/altar-whiteout.png'

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

# ITEMS #
# those not defined in screens
image soup = "images/items/soup1.png"
image soup empty = "images/items/empty-soup1.png"


# MUSIC #

# define config.main_menu_music = "sound/Voglio_La_Pace-Menu_version.wav"
# define audio.menu = "sound/Voglio_La_Pace-Menu_version.wav"
# define audio.credits = "sound/Voglio_La_Pace.wav"
# define audio.snowplains = "sound/Ruscello_Nella_Neve.wav"
# define audio.footsteps = "sound/footsteps.wav"
# define audio.breath_in = "sound/breath_in.wav"
# define audio.thunder = "sound/thunder.wav"
# define audio.thunder_distant = "sound/thunder_distant.wav"
# define audio.magitek = "sound/magitek.wav"
