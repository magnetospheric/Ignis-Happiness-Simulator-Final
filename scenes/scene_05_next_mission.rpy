#Scene 05
#Power Cut & Next Mission

#contains labels:
    # power_cut
    # find_fuse
    # leaving_palace
    # en_route_to_altar


# covers reporting back to the captain, flashlight test, and leaving on next mission



label power_cut:

    stop music fadeout 2.286
    play ambient lights_out_2 fadein 2.286

    stop foley2 fadeout 2.286
    $ renpy.music.set_volume(0.08, delay=1, channel='foley')

    $ show_happiness = False

    show bg yureilcorridor dark with Dissolve(0.3)

    show screen door_idle

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "When you arrive in the palace entrance hall, the Captain and a handful of guards are already there."

    show captain neutral at right with dissolve

    captain "Ah, [your_name], [ignis_name], good work."

    show ignis touching glasses at left with dissolve

    ignis "So, it's as we guessed."

    show ignis neutral at left with dissolve
    show captain neutral openmouth with dissolve

    captain "Right. The scale of the attack is larger than we predicted, though."

    show captain neutral sidelong with dissolve

    narrator1 "She seethes quietly for a moment."

    $ renpy.music.set_volume(0.09, delay=0, channel='foley4')

    play foley4 explosion04 noloop
    queue foley4 explosion03 noloop
    queue foley4 explosion02 noloop
    queue foley4 explosion03 noloop

    narrator1 "Outside, the sound of explosions and thrumming engines cut through to the palace hallway."

    narrator1 "It's hollow against the stone foundations, and every reverberation brings back the fact that, right now, you are under siege."

    narrator1 "You can't believe this is really happening."

    narrator1 "You've only been working here two months. You're not prepared for this."

    show captain neutral openmouth with dissolve
    captain "I got a report just now that dropships have landed in Padore District. The Magitek infantry are moving in."
    show captain neutral

    show ignis neutral openmouth
    ignis "Sounds like they're seeking to disrupt the ceremony from the west side."
    show ignis neutral

    show captain neutral openmouth with dissolve
    captain "Mm. So I'd like you to go ensure the citizens there are evacuated safely. That's first priority."
    show captain neutral

    you "Understood, Ma'am."

    show captain neutral openmouth
    captain "Second priority is finding a way to slow enemy movement. Although — Ignis, I understand your companions are already on that point?"
    show captain neutral

    show ignis neutral openmouth
    ignis "They are. A small complication, though — they're stationed on the east side, and we currently don't have a way to reach the dropships —"

    $ renpy.music.set_volume(0.6, delay=0, channel='foley3')
    $ renpy.music.set_volume(0.6, delay=0, channel='foley4')

    play foley3 "<from 1.5>audio/soundeffects/explosion02.wav" noloop
    play foley4 "<from 1.5>audio/soundeffects/explosion01.wav" noloop

    stop ambient fadeout 2.286
    $ renpy.music.set_volume(0.4, delay=0, channel='music')
    play music lights_out_3 fadein 2.286 loop

    show screen black_overlay
    with softflash

    narrator1 "There's a resounding crash from somewhere up above. The lights flicker off, casting the room into darkness." with vpunch

    you "A power cut?"

    captain "There's a flashlight on the table next to you. See if you can't find the fuse box."

    # info box: FLASHLIGHT has been equipped You take the FLASHLIGHT
    call screen infobubble(title="You take the FLASHLIGHT", content="Click your mouse button to use the flashlight and illuminate the room. Click again on anything of interest you uncover.", confirmation="Got it")

    hide screen infobubble

    # enter flashlight section
    hide screen black_overlay
    hide screen door_idle

    #call screen open_door
    call screen flashlight_palace_hallway

    jump find_fuse



label find_fuse:

    # show screen black_overlay
    show screen black_overlay
    show screen door_idle

    narrator1 "There's no sign of a fuse box in this central corridor, but that small door at the end looks like it might lead somewhere useful."

    narrator1 "You seem to remember the palace electricians taking that route, at least."

    hide screen door_idle
    hide ignis
    hide captain

    show bg yureilcorridor fuse idle with Dissolve(0.5)

    narrator1 "So you walk through to find a much narrower stairwell that looks far more promising."

    you "{i}Damn ... this place feels totally different with the lights out. It's ... kind of creepy.{/i}"

    you "{i}All right ... the fuse box has got to be in a place like this ...{/i}"

    call screen infobubble(title="You turn on the FLASHLIGHT", content="", confirmation="Begin to search")

    hide screen infobubble
    hide screen black_overlay

    show bg yureilcorridor fuse idle

    call screen flashlight_fuse

    show screen black_overlay
    show bg yureilcorridor fuse idle



label found_fuse:

    show screen black_overlay
    hide flashlight_fuse

    stop music fadeout 2.286

    you "Aha! Now that looks like a fuse box!"

    narrator1 "You flip the switches one by one, until eventually the lights flicker back to life."

    hide screen black_overlay
    with softflash
    play ambient undercurrent loop

    narrator1 "That's one small problem out of the way."

    narrator1 "You race back to your superior."

    jump leaving_palace



label leaving_palace:

    hide bg yureilcorridor fuse

    show bg yureilcorridor dark with Dissolve(0.3)

    show captain neutral
    with dissolve

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    show captain neutral openmouth
    captain "Ah, excellent job, [your_name]."
    captain "Now, there's no time to waste. Take the side exit when you leave, and remember to pick up your dress sword."
    show captain neutral

    narrator1 "Ah. The dress sword. A small rapier used mostly for show. You've had basic training, but you've never used it in proper combat."

    narrator1 "An uncomfortable thrill spreads through your nerves at the thought that today you might actually need to."

    show captain at left
    with move

    show ignis neutral at right
    with dissolve

    ignis "So, are you ready to go?"

    narrator1 "Padore District. Magitek Infantry. Save more citizens."

    narrator1 "You take a deep breath. You're not sure you're prepared for going up against the Empire's army, but you know you have to try."

    you "I'm ready."

    show ignis smile

    ignis "Lead onward, then."

    show captain neutral openmouth
    captain "Take the flashlight with you, [your_name]. You might need it."
    show captain neutral

    you "Thank you."

    captain "Good luck out there, both of you."

    hide ignis
    hide captain
    hide yureilcorridor dark
    with dissolve

    jump en_route_to_altar



label en_route_to_altar:

    $ renpy.music.set_volume(0.04, delay=1, channel='foley')
    stop ambient fadeout 2.286
    play music interloper fadein 2.286

    scene black with dissolve
    centered "{size=26}Chapter Two\n\n{/size}{size=36}Lightning Strikes{/size}"

    show bg fountaincourtyard with dissolve

    show ignis sidelong at center
    with dissolve

    narrator1 "You pick up your dress sword on the way out, marvelling at how light it feels beneath your grip."

    narrator1 "There's not much time to fasten it properly, so you just slide it into your belt and hope for the best. Your trainer would probably be appalled."

    narrator1 "You and Ignis make your way towards Padore District while the ships drone on above you."

    narrator1 "The roar of Leviathan's wrath fills the distance, and the dissonant sounds of fire crackling and water surging fills your ears."

    narrator1 "You both don't talk much; you're busy leading the way, leaping over balconies and down side alleys while Ignis is entirely focussed on keeping up."

    narrator1 "While he's agile enough, he lacks the knowledge of the area that you have, and he's not prepared for a lot of the shortcuts you're taking."

    hide ignis

    jump trooper_attack
