#Scene 04
#Evac

#contains labels:
    # speech_and_evac
    # chaos_begins


# covers luna's speech and evac of those in the plaza, and reporting back to captain


label lunas_speech:

    show bg yureilplaza crowd with Dissolve(0.3)

    narrator1 "You and Ignis both make your way to the back of the plaza."

    show ignis sidelong openmouth
    ignis "The Niffs have arrived..."

    # sound effect crowd buzzing

    narrator1 "You catch sight of a black-haired individual moving through the crowd. Your first thought is that he's moving irregularly, and as a guard, this is a cause for concern."

    narrator1 "But there's something about him that looks familiar. It's a figure you've seen countless times on news reports before. The Crown Prince of Lucis is here?"

    narrator1 "Ignis catches your gaze, and holds a finger to his lips softly."

    you "Is he with you?"

    ignis "Indeed he is."

    narrator1 "You're just a guard, after all. You only get told things that are mission-critical."

    # sound effect engine hum
    narrator1 "A distant hum interrupts your thoughts. A sort of revving, and it's getting closer."

    narrator1 "You look up to see Imperial dreadnoughts approaching."

    narrator1 "Altissia has had so many years of peace under Niflheim's rule that you've almost forgotten the sight of these monstrosities."

    jump power_cut



label power_cut:

    # captain gets you to search the room for the fuse switch before you head out.
    # this will teach you the 'flashlight' mechanic

    narrator1 "The lights flicker off, casting the room into darkness."
    # have a sort of flash effect as the room goes dark, if possible.
    # Could be achieved by a sort of inverted colouring of the current room bg

    you "A power cut?"

    captain "There's a flashlight on the table next to you. See if you can't find the fuse switch."

    # info box: FLASHLIGHT has been equipped You take the FLASHLIGHT

    # enter flashlight section

    captain "Take the torch with you, [your_name]. You might need it."

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
