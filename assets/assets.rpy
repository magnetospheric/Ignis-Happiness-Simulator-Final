
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       Asset definitions
#
#       Contains:
#               sprites
#               character definitions
#               character images
#
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


# used to position images at specific x and y pos
transform SpriteLoc2(x, y):
    pos (x, y)


### Character definitions ###
# IGNIS IS IN HIS OWN FILE

define you = DynamicCharacter(
                            'your_name',
                            who_color="#ffeff6",
                            window_background="images/ui/dialog_bg02.png",
                            who_outlines=[ (7, "#0000004D", 0, 0), (4, "#ffffff59", 0, 0), (3, "#3b2831", 0, 0) ],
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            callback=clicky_typewriter
                        )

define altissianguard = Character(
                            "Guard on Duty",
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/dialog_bg02.png",
                            callback=clicky_typewriter
                        )
define captain = Character(
                            "Captain",
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/dialog_bg02.png",
                            callback=clicky_typewriter
                        )

# niffs
define ravus = DynamicCharacter('ravus_name', who_color="#e0e0e0", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg02.png")
define ardyn = DynamicCharacter('ardyn_name', who_color="#d0c3bf", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg02.png")
#MAKE SURE to use a robot sound for the typewriter noise for the trooper!
define magitektrooper = Character("Trooper", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg02.png")
define caligo = Character("Caligo", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg02.png")
define unidentified_voice = Character("Unidentified Voice", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg02.png")

#other chocobros
define prompto = Character("Prompto", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg02.png")
define noctis = Character("Noctis", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg02.png")

#citizens
define citizen1 = Character("Scared Citizen", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg02.png")
define citizen2 = Character("Reasonable Citizen", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg02.png")
define citizen3 = Character("Sceptical Citizen", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg02.png")

define friend = Character("Friend", ctc="ctc_blink", ctc_position="fixed", window_background="images/ui/dialog_bg02.png")

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

image ravus neutral:
    "images/characters/ravus-neutral.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ravus-neutral-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ravus neutral openmouth:
    "images/characters/ravus-neutral-openmouth.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ravus-neutral-openmouth-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ravus smile:
    "images/characters/ravus-smile.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ravus-smile-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ravus smile openmouth:
    "images/characters/ravus-smile-openmouth.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ravus-smile-openmouth-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat


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

image trooper dropship = "images/characters/mt-dropship01.png"
image trooper dropship silhouette  = "images/characters/mt-dropship-silhouette.png"

### trooper short circuiting animation definition ###
image trooper dropship shortcircuit = LiveComposite(
    (728, 720),
    (0, 0), "dropshipshortcircuit0"
    )

image dropshipshortcircuit0:
    alpha 1.0
    "images/characters/mt-dropship-shortcircuit01.png"
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
    "images/characters/mt-dropship-shortcircuit02.png"
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
    "images/characters/mt-dropship-shortcircuit01.png"
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
    "images/characters/mt-dropship-shortcircuit03.png"
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


image noctis neutral:
    "images/characters/noctis-neutral.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/noctis-neutral-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image noctis neutral openmouth:
    "images/characters/noctis-neutral-openmouth.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/noctis-neutral-openmouth-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image noctis smile:
    "images/characters/noctis-smile.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/noctis-smile-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image noctis smile openmouth:
    "images/characters/noctis-smile-openmouth.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/noctis-smile-openmouth-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat


# ITEMS #
# those not defined in screens
image soup = "images/items/soup1.png"
image soup empty = "images/items/empty-soup1.png"
