#Scene 05
#Power Cut & Next Mission

#contains labels:
    # power_cut
    # en_route_to_altar


# covers reporting back to the captain, flashlight test, and leaving on next mission



label power_cut:

    show bg yureilcorridor dark with Dissolve(0.3)

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

    show bg yureilcorridor dark with Dissolve(0.3)

    narrator1 "The lights flicker off, casting the room into darkness."
    # have a sort of flash effect as the room goes dark, if possible.
    # Could be achieved by a sort of inverted colouring of the current room bg

    you "A power cut?"

    # captain gets you to search the room for the fuse switch before you head out.
    # this will teach you the 'flashlight' mechanic

    captain "There's a flashlight on the table next to you. See if you can't find the fuse switch."

    # info box: FLASHLIGHT has been equipped You take the FLASHLIGHT
    call screen infobubble(title="You take the FLASHLIGHT", content="Click your mouse button to use the flashlight and illuminate the room. Click again on anything of interest you uncover.")

    hide screen infobubble

    # enter flashlight section
    $ show_happiness = False
    call screen flashlight_no_timer

    captain "Take the flashlight with you, [your_name]. You might need it."

    you "Thank you."

    captain "Good luck out there, [your_name]." # captain says this after u go out with the flashlight to find the breaker room

    jump en_route_to_altar



label en_route_to_altar:

    # ignis shows you where to go on the map, then leaves after this

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
