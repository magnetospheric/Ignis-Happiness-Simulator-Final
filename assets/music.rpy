
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       Assets: Music
#
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


# MUSIC #

#music plan:


# FOR IN THE MORNING #
# an undercurrent
# Morning Coffee
# the ceremony - Shrinemaidens Calling


# FOR IN THE STREETS / CEREMONY GOING WRONG #
# bated breath
# tension
# tension 2
# double beat tension
# really fast tension
# is this really all the help we're gonna get?
# a spot of lunch


# FOR ABOARD THE DROPSHIP #

# Footsteps in the Dark
# Eggshell Walker
# System Shocker


# FOR AFTER #
# home blues
# A Natural Rise / A Natural Lull
# (gonna need that guitar piece for the plaza)


# Menu and Credit Music
define config.main_menu_music = "audio/bgmusic/menu-screen-music.wav"
define audio.main_credit_music = "audio/Palinopsia.wav"

define audio.reverse_guitar = "audio/reverse-guitar-clip.wav"

define audio.tense_morning = "audio/tense-morning.wav"
define audio.tense_morning_2 = "audio/tense-morning-2.wav"



# Chapter One - AWAKEN #
define audio.morning_coffee1 = "audio/bgmusic/Morning-Coffee-gamever-pt1.wav"
define audio.morning_coffee2 = "audio/bgmusic/Morning-Coffee-gamever-pt2.wav"

define audio.undercurrent = "audio/bgmusic/An-Undercurrent-gamever.wav"
define audio.shrinemaiden1 = "audio/bgmusic/Shrinemaidens-Calling-pt1.wav"
define audio.shrinemaiden2 = "audio/bgmusic/Shrinemaidens-Calling-pt2.wav"

define audio.lights_out_1 = "audio/bgmusic/Lights-Out-pt1.wav"
define audio.lights_out_2 = "audio/bgmusic/Lights-Out-pt2.wav"
define audio.lights_out_3 = "audio/bgmusic/Lights-Out-pt3.wav"

define audio.interloper = "audio/bgmusic/Interloper.wav"
define audio.clone_resonance = "audio/bgmusic/Clone-Resonance.wav"

define audio.stubborn_citizens = "audio/is_this_all_the_help_were_gonna_get.wav"

define audio.a_spot_of_lunch = "audio/a-spot-of-lunch.wav"
define audio.a_spot_of_lunch_2 = "audio/a-spot-of-lunch2.wav"


# define audio.breath_in = "sound/breath_in.wav"
# define audio.thunder = "sound/thunder.wav"
# define audio.thunder_distant = "sound/thunder_distant.wav"
# define audio.magitek = "sound/magitek.wav"
init python:
    renpy.music.register_channel("ambient", "music", True, tight=True)
    renpy.music.register_channel("foley", "music", True, tight=True)
    renpy.music.register_channel("foley2", "music", True, tight=True)
    renpy.music.register_channel("foley3", "music", True, tight=True)
    renpy.music.register_channel("foley4", "music", True, tight=True)


# sound effects
define audio.birdsong1 = "audio/soundeffects/birdsong1.wav"
define audio.birdsong2 = "audio/soundeffects/birdsong2.wav"
define audio.altissian_morning_streets = "audio/soundeffects/altissian-morning-streets.wav"
define audio.out_of_bed = "audio/soundeffects/out-of-bed.wav"
define audio.keys_rustling = "audio/soundeffects/keys-rustling.wav"
define audio.locking_up_your_house = "audio/soundeffects/locking-up-your-house.wav"

define audio.bells_chiming = "audio/soundeffects/bells-chiming.wav"
define audio.plaza_crowd = "audio/soundeffects/plazacrowd.wav"
define audio.cheering1 = "audio/soundeffects/cheering01.wav"
define audio.cheering2 = "audio/soundeffects/cheering02.wav"

define audio.dropships_approaching = "audio/soundeffects/dropships-approaching.wav"
define audio.engine_bassline = "audio/soundeffects/engine-bassline.wav"
define audio.explosion01 = "audio/soundeffects/explosion01.wav"
define audio.explosion02 = "audio/soundeffects/explosion02.wav"
define audio.explosion03 = "audio/soundeffects/explosion03.wav"
define audio.explosion04 = "audio/soundeffects/explosion04.wav"
define audio.gunfire = "audio/soundeffects/gunfire.wav"
define audio.airship_zoom = "audio/soundeffects/airship-zoom.wav"
