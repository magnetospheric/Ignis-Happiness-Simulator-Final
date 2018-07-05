
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
define audio.bated_breath = "audio/bgmusic/Bated-Breath-gamever.wav"



# Chapter One - AWAKEN #
define audio.morning_coffee1 = "audio/bgmusic/Morning-Coffee-gamever-pt1.wav"
define audio.morning_coffee2 = "audio/bgmusic/Morning-Coffee-gamever-pt2.wav"

define audio.undercurrent = "audio/bgmusic/An-Undercurrent-gamever.wav"
define audio.shrinemaiden1 = "audio/bgmusic/Shrinemaidens-Calling-pt1.wav"
define audio.shrinemaiden2 = "audio/bgmusic/Shrinemaidens-Calling-pt2.wav"

define audio.lights_out_1 = "audio/bgmusic/Lights-Out-pt1.wav"
define audio.lights_out_2 = "audio/bgmusic/Lights-Out-pt2.wav"
define audio.lights_out_3 = "audio/bgmusic/Lights-Out-pt3.wav"

# Chapter Two - LIGHTNING STRIKES #
define audio.interloper = "audio/bgmusic/Interloper.wav"
define audio.clone_resonance = "audio/bgmusic/Clone-Resonance.wav"

define audio.stubborn_citizens = "audio/bgmusic/Is-This-Really-All-The-Help-We're-Gonna-Get-gamever.wav"
define audio.a_spot_of_lunch = "audio/bgmusic/A-Spot-Of-Lunch-gamever.wav"

# Chapter Three - MACHINE MESSIAH #
define audio.eggshell_walker_1 = "audio/bgmusic/Eggshell-Walker-pt1.wav"
define audio.eggshell_walker_2 = "audio/bgmusic/Eggshell-Walker-pt2.wav"
define audio.footsteps_in_the_dark = "audio/bgmusic/Footsteps-In-The-Dark-gamever.wav"
define audio.system_shocker = "audio/bgmusic/System-Shocker-gamever.wav"

# Chapter Four - YOUR MOVE #
define audio.home_blues = "audio/bgmusic/Home-Blues-gamever.wav"
define audio.andante = "audio/bgmusic/Andante-gamever.wav"
define audio.listro_fandango = "audio/bgmusic/Listro-Fandango-gamever.wav"
define audio.curious_encounter = "audio/bgmusic/A-Curious-Encounter-gamever.wav"

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

define audio.trooper_screech = "audio/soundeffects/screaming-trooper.wav"
define audio.trooper_screech2 = "audio/soundeffects/screaming-trooper2.wav"
define audio.trooper_screech3 = "audio/soundeffects/screaming-trooper3.wav"

define audio.mech_landing = "audio/soundeffects/mech-landing.wav"
define audio.mech_bass = "audio/soundeffects/mech-bass.wav"
define audio.mech_buzz = "audio/soundeffects/mech-buzz.wav"
define audio.mech_clang = "audio/soundeffects/mech-clang.wav"
