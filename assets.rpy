
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       Asset definitions
#
#       Contains:
#               character definitions
#               character images
#               background images
#               sprites
#
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


### Character definitions ###
define ignis = DynamicCharacter('ignis_name', color="#444176", ctc="ctc_blink", ctc_position="fixed")
define you = DynamicCharacter('your_name', color="#aa748d", ctc="ctc_blink", ctc_position="fixed")
define ravus = DynamicCharacter('ravus_name', color="#aa748d", ctc="ctc_blink", ctc_position="fixed")
define ardyn = DynamicCharacter('ardyn_name', color="#aa748d", ctc="ctc_blink", ctc_position="fixed")
define narrator = Character(ctc="ctc_blink", ctc_position="fixed")
define altissianguard = Character("Guard on Duty", ctc="ctc_blink", ctc_position="fixed")
define captain = Character("Captain", ctc="ctc_blink", ctc_position="fixed")
define magitektrooper = Character("Trooper", ctc="ctc_blink", ctc_position="fixed")
define caligo = Character("Caligo", ctc="ctc_blink", ctc_position="fixed")
define unidentified_voice = Character("Unidentified Voice", ctc="ctc_blink", ctc_position="fixed")

image ctc_blink = LiveComposite(
    (65, 65),
    (930, 685), "ctc_base",
    (930, 685), "glow",
    )

image ctc_base:
    "images/ui/next_button_small.png"
    linear 0.8 alpha 0.95
    repeat

image glow:
    "images/ui/next_button_hover_small.png"
    linear 0.8 alpha 0.0
    "images/ui/next_button_hover_small.png"
    linear 0.8 alpha 0.5
    repeat


#### Character Images ####
image ignis neutral  = "images/characters/ignis/ignis-neutral.png"

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
image black = "images/backgrounds/black_bg.png"



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
