
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
define ignis = DynamicCharacter('ignis_name', color="#fff2b5", ctc="ctc_blink", ctc_position="fixed")
define you = DynamicCharacter('your_name', color="#b2b1c4", ctc="ctc_blink", ctc_position="fixed")
define narrator = Character(ctc="ctc_blink", ctc_position="fixed")

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
image ignis neutral  = "images/characters/ignis-neutral.png"

#### Background Images ####
image bg altissia_alleyway = 'images/backgrounds/altissia-alleyway-night.jpg'
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
