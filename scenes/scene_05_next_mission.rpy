#Scene 05
#Power Cut & Next Mission

#contains labels:
    # power_cut
    # en_route_to_altar


# covers reporting back to the captain, flashlight test, and leaving on next mission



label power_cut:

    $ show_happiness = False

    show bg yureilcorridor dark with Dissolve(0.3)

    show screen door_idle

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "When you arrive in the palace entrance hall, the Captain and a handful of guards are already there."

    show captain neutral at left
    with dissolve

    captain "Ah, [your_name], [ignis_name], good work."

    show ignis neutral at right #or maybe finger to glasses here?
    with dissolve

    ignis "So, it's as we guessed."

    # show captain neutral sidelook
    # with dissolve
    #
    # show captain neutral sidelook openmouth
    # with dissolve

    captain "Right. The scale of the attack is larger than we predicted, though."

    # show captain neutral sidelook
    # with dissolve

    narrator1 "She seethes quietly for a moment."

    narrator1 "Outside, the sound of explosions and thrumming engines cut through to the palace hallway. It's hollow against the stone foundations, and every reverberation brings back the fact that, right now, you are under siege."

    narrator1 "You can't believe this is really happening."

    narrator1 "You've only been working here two months. You're not prepared for this."

    # show captain neutral sidelook openmouth

    captain "I got a report just now that dropships have landed in Padore District. The Magitek infantry are moving in."

    ignis "Sounds like they're seeking to disrupt the ceremony from the west side."

    captain "Mm. So I'd like you to go ensure the citizens there are evacuated safely. That's first priority."

    you "Understood, Ma'am."

    captain "Second priority is finding a way to slow enemy movement. Although — Ignis, I understand your companions are already on that point?"

    ignis "They are. A small complication, though — they're stationed on the east side, and we currently don't have a way to reach the dropships —"

    narrator1 "There's a resounding crash from somewhere up above." with vpunch

    # show bg yureilcorridor dark with Dissolve(0.3)
    show screen black_overlay
    with softflash

    narrator1 "The lights flicker off, casting the room into darkness."
    # have a sort of flash effect as the room goes dark, if possible.
    # Could be achieved by a sort of inverted colouring of the current room bg

    you "A power cut?"

    # captain gets you to search the room for the fuse switch before you head out.
    # this will teach you the 'flashlight' mechanic

    captain "There's a flashlight on the table next to you. See if you can't find the fuse box."

    # info box: FLASHLIGHT has been equipped You take the FLASHLIGHT
    call screen infobubble(title="You take the FLASHLIGHT", content="Click your mouse button to use the flashlight and illuminate the room. Click again on anything of interest you uncover.", confirmation="Got it")

    hide screen infobubble

    # enter flashlight section
    hide screen black_overlay
    hide screen door_idle
    hide ignis
    hide captain

    #call screen open_door
    call screen flashlight_palace_hallway

    jump find_fuse

label find_fuse:

    # show screen black_overlay
    show screen black_overlay
    show screen door_idle

    narrator1 "There's no sign of a fuse box in this central corridor, but that small door at the end looks like it might lead somewhere useful. You seem to remember the palace electricians taking that route, at least."

    hide screen door_idle

    show bg yureilcorridor fuse idle with Dissolve(0.3)

    narrator1 "So you walk through to find a much narrower stairwell that looks far more promising."

    you "{i}Damn ... this place feels totally different with the lights out. It's ... kind of creepy.{/i}"

    you "{i}All right ... the fuse box has got to be in a place like this ...{/i}"

    call screen infobubble(title="You turn on the FLASHLIGHT", content="", confirmation="Begin to search")

    hide screen infobubble
    hide screen black_overlay

    show bg yureilcorridor fuse

    call screen flashlight_fuse

    show screen black_overlay
    show bg yureilcorridor fuse idle

    you "Aha! Now that looks like a fuse box!"

    narrator1 "You flip the switches one by one, until eventually the lights flicker back to life."

    hide screen black_overlay
    with softflash

    narrator1 "That's one small problem out of the way."

    narrator1 "You race back to your superior."

    jump leaving_palace

label leaving_palace:

    hide bg yureilcorridor fuse

    show bg yureilcorridor dark with Dissolve(0.3)

    show captain neutral
    with dissolve

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    captain "Ah, excellent job, [your_name]."

    captain "Now, there's no time to waste. Take the side exit when you leave, and remember to pick up your dress sword."

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

    captain "Take the flashlight with you, [your_name]. You might need it."

    you "Thank you."

    captain "Good luck out there, both of you."

    hide bg yureilcorridor dark

    jump en_route_to_altar



label en_route_to_altar:

    show bg fountaincourtyard
    # will probably have a different bg here, like, the random streets or suchlike

    show ignis sidelong at center
    with dissolve

    narrator1 "You pick up your dress sword on the way out, marvelling at how light it feels beneath your grip. There's not much time to fasten it properly, so you just slide it into your belt and hope for the best. Your trainer would probably be appalled."

    narrator1 "You and Ignis make your way towards Padore District while the ships drone on above you, while the roar of Leviathan's wrath fills the distance, while the dissonant sounds of fire crackling and water surging fills your ears."

    narrator1 "You both don't talk much; you're busy leading the way, leaping over balconies and down side alleys while Ignis is entirely focussed on keeping up. While he's agile enough, he lacks the knowledge of the area that you have, and he's not prepared for a lot of the shortcuts you're taking."

    narrator1 "It's when you've just started crossing a particularly wide street that you encounter your first Magitek Trooper. The thing's waiting, zombie-like and menacing, at the end of the street and there's nowhere else to run. You're in the open."

    narrator1 "You ready your weapon, heart pounding."

    narrator1 "But Ignis moves before you can do anything."

    narrator1 "The first step he takes is accompanied by a crackling blue light and the faint smell of ozone. Where there had been nothing in his hands before, now he grips a pair of brilliant and ornate daggers."

    ignis "Let's put a quick end to this."

    narrator1 "You don't have time to wonder how Ignis summoned those weapons. The trooper lunges forward with a disturbing screech that you're not quite sure is mechanical or organic. It's all whirring limbs and strict, unexpressive movements, and everything about it makes you shiver."

    narrator1 "Ignis sidesteps its first attack, parries the next, and manages to land a hit."

    narrator1 "It somehow slips past him, and comes screaming straight for you."

    narrator1 "You scream back, and draw back your sword rapidly, before stabbing forward in the swift motion you were taught during training."

    narrator1 "The sword pierces what appears to be the trooper's core, and it falls to the ground, twitching and shrieking."

    ignis "That was ... that was impressive, [your_name]."

    narrator1 "You barely manage a smile. You're breathless, and enraptured by the horrific sight of the dying trooper, whose body has begun to smoke. Is it ... is it evaporating?"

    ignis "They're infused with daemonic plasma."

    you "Oh. That's ... pleasant."

    narrator1 "f"
    # ignis shows you where to go on the map, then leaves after this

    ignis "Will you be okay?"

    narrator1 "Ignis has forgotten to turn his mic off, and you can hear everything that's happening."

    narrator1 "It's mostly muffled shouts and cries, accompanied by Ignis's breathing. He's clearly frantic, but doing an admirable job of stilling his own nerves."

    narrator1 "Then, an angry voice."

    unidentified_voice "The King's lapdog, eh?"

    narrator1 "And a sharp cry of pain. Ignis is hurt."

    narrator1 "You check your map. You're only a street away from the citizens you've been tasked with helping."

    menu:
        "Continue onward to help the citizens":
            "You can't abandon your duty. You know this as clear as day."
            # highlight current route on map
            "The citizens aren't far away. You'll help them first, then come to Ignis's aid."
        "Divert your route to help Ignis":
            "You simply can't leave him in pain like that. What if the Niffs kill him, after all?"
            #highlight new route on the map
            "If you take this route, you can come to his aid and still be close enough to double back for the citizens afterward."

    return
