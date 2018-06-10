# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       Asset definitions for IGNIS ONLY
#
#       Contains:
#               character definitions
#               character images
#               sprites
#
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


define ignis = DynamicCharacter(
                            'ignis_name',
                            who_color="#eae9ff",
                            window_background="images/ui/dialog_bg02.png",
                            who_outlines=[ (7, "#0000004D", 0, 0), (5, "#ffffffd9", 0, 0), (4, "#282645", 0, 0) ],
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            callback=clicky_typewriter
                            )


# CHAPTER 1 - BEGINNINGS #
# CONTAINS:
#           Ignis neutral
#           Ignis neutral openmouth
#           Ignis smile
#           Ignis touching glasses
#           Ignis unimpressed
#           Ignis unimpressed openmouth

#           Ignis sidelong
#           Ignis sidelong openmouth
#           Ignis sidelong direct
#           Ignis sidelong openmouth direct

image ignis neutral:
    "images/characters/ignis/ignis-neutral.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ignis/ignis-neutral-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ignis neutral openmouth:
    "images/characters/ignis/ignis-neutral-openmouth.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ignis/ignis-neutral-openmouth-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ignis smile:
    "images/characters/ignis/ignis-smile.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ignis/ignis-smile-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ignis touching glasses:
    "images/characters/ignis/ignis-touching-glasses.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ignis/ignis-touching-glasses-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ignis unimpressed:
    "images/characters/ignis/ignis-unimpressed.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ignis/ignis-unimpressed-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ignis unimpressed openmouth:
    "images/characters/ignis/ignis-unimpressed-openmouth.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ignis/ignis-unimpressed-openmouth-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ignis neutral eyesclosed = "images/characters/ignis/ignis-neutral-blink.png"
image ignis neutral openmouth eyesclosed = "images/characters/ignis/ignis-neutral-openmouth-blink.png"
image ignis smile eyesclosed = "images/characters/ignis/ignis-smile-blink.png"
image ignis touching glasses eyesclosed = "images/characters/ignis/ignis-touching-glasses-blink.png"
image ignis unimpressed eyesclosed = "images/characters/ignis/ignis-unimpressed-blink.png"
image ignis unimpressed openmouth eyesclosed = "images/characters/ignis/ignis-unimpressed-openmouth-blink.png"

image ignis sidelong = "images/characters/ignis/ignis-sidelong.png"
image ignis sidelong openmouth = "images/characters/ignis/ignis-sidelong-openmouth.png"
image ignis sidelong direct = "images/characters/ignis/ignis-sidelong-direct.png"
image ignis sidelong direct openmouth = "images/characters/ignis/ignis-sidelong-direct-openmouth.png"



# CHAPTER 2 - EVACUATION #
# CONTAINS:
#           Ignis neutral WET
#           Ignis neutral openmouth WET
#           Ignis smile WET
#           Ignis touching glasses WET
#           Ignis unimpressed WET
#           Ignis unimpressed openmouth WET

#           Ignis sidelong WET
#           Ignis sidelong openmouth WET
#           Ignis sidelong direct WET
#           Ignis sidelong openmouth direct WET

image ignis neutral wet:
    "images/characters/ignis/ignis-neutral-wet.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ignis/ignis-neutral-wet-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ignis neutral openmouth wet:
    "images/characters/ignis/ignis-neutral-openmouth-wet.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ignis/ignis-neutral-openmouth-wet-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ignis smile wet:
    "images/characters/ignis/ignis-smile-wet.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ignis/ignis-smile-wet-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ignis touching glasses wet:
    "images/characters/ignis/ignis-touching-glasses-wet.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ignis/ignis-touching-glasses-wet-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ignis unimpressed wet:
    "images/characters/ignis/ignis-unimpressed-wet.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ignis/ignis-unimpressed-wet-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ignis unimpressed openmouth wet:
    "images/characters/ignis/ignis-unimpressed-openmouth-wet.png"
    choice:
        4
    choice:
        5
    choice:
        6
    choice:
        7
    # This randomizes the time between blinking.
    "images/characters/ignis/ignis-unimpressed-openmouth-wet-blink.png"
    choice:
        0.09
    choice:
        0.11
    repeat

image ignis neutral eyesclosed wet = "images/characters/ignis/ignis-neutral-wet-blink.png"
image ignis neutral openmouth eyesclosed wet = "images/characters/ignis/ignis-neutral-openmouth-wet-blink.png"
image ignis smile eyesclosed wet = "images/characters/ignis/ignis-smile-wet-blink.png"
image ignis touching glasses eyesclosed wet = "images/characters/ignis/ignis-touching-glasses-wet-blink.png"
image ignis unimpressed eyesclosed wet = "images/characters/ignis/ignis-unimpressed-wet-blink.png"
image ignis unimpressed openmouth eyesclosed wet = "images/characters/ignis/ignis-unimpressed-openmouth-wet-blink.png"
image ignis wet silhouette = "images/characters/ignis/ignis-wet-silhouette.png"

# the no-blinks
image ignis unimpressed openmouth wet noblink = "images/characters/ignis/ignis-unimpressed-openmouth-wet.png"


image ignis sidelong wet = "images/characters/ignis/ignis-sidelong-wet.png"
image ignis sidelong openmouth wet = "images/characters/ignis/ignis-sidelong-openmouth-wet.png"
image ignis sidelong direct wet = "images/characters/ignis/ignis-sidelong-direct-wet.png"
image ignis sidelong direct openmouth wet = "images/characters/ignis/ignis-sidelong-direct-openmouth-wet.png"



# CHAPTER 3 - RESCUE #
# CONTAINS:
#           NOTHING YET

image ignis neutral injured = "images/characters/ignis/ignis-neutral-injured.png"
image ignis neutral openmouth injured = "images/characters/ignis/ignis-neutral-openmouth-injured.png"
image ignis smile injured = "images/characters/ignis/ignis-smile-injured.png"
# image ignis touching glasses blind = "images/characters/ignis/ignis-touching-glasses-blind.png"
image ignis unimpressed injured = "images/characters/ignis/ignis-unimpressed-injured.png"
image ignis unimpressed openmouth injured = "images/characters/ignis/ignis-unimpressed-openmouth-injured.png"



# CHAPTER 4 - DATE #
# CONTAINS:
#           Ignis neutral BLIND
#           Ignis neutral openmouth BLIND
#           Ignis smile BLIND
#           Ignis unimpressed BLIND
#           Ignis unimpressed openmouth BLIND
#           Ignis pain BLIND
#           Ignis pain openmouth BLIND

image ignis neutral blind = "images/characters/ignis/ignis-neutral-blind.png"
image ignis neutral openmouth blind = "images/characters/ignis/ignis-neutral-openmouth-blind.png"
image ignis smile blind = "images/characters/ignis/ignis-smile-blind.png"
# image ignis touching glasses blind = "images/characters/ignis/ignis-touching-glasses-blind.png"
image ignis unimpressed blind = "images/characters/ignis/ignis-unimpressed-blind.png"
image ignis unimpressed openmouth blind = "images/characters/ignis/ignis-unimpressed-openmouth-blind.png"
image ignis pain blind = "images/characters/ignis/ignis-pain-blind.png"
image ignis pain openmouth blind = "images/characters/ignis/ignis-pain-openmouth-blind.png"
image ignis happy blind = "images/characters/ignis/ignis-happy-blind.png"
