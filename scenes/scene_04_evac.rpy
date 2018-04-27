#Scene 04
#Evac

#contains labels:
    # speech_and_evac
    # chaos_begins


# covers luna's speech and evac of those in the plaza, and reporting back to captain


label lunas_speech:

    show bg yureilplaza crowd with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "You and Ignis both make your way to the back of the plaza."

    # sound effect crowd buzzing

    narrator1 "The crowd is abuzz with conversation. Everyone's making small talk — it's much too big an event to get into deep conversation — and they all seem tense, hiding anticipation behind their smiling faces."

    show ignis neutral at left
    with dissolve

    narrator1 "You glance at Ignis. He seems calm enough, although you recognise the offhand gaze with which he scans the audience."

    narrator1 "He's checking for discrepancies and dissent as much as you are. His keen eyes rove the crowd, and he cuts quite the striking figure."

    ignis "It's a beautiful piece of architecture. Rather strategically-designed, too."

    you "How so?"

    ignis "The plaza itself is long and narrow - and it bottlenecks quite naturally before these points they've got us guarding. It's exceedingly good for crowd control."

    narrator1 "You had never thought of it that way before. But he's right."

    you "Should make our job much easier, then."

    ignis "Indeed."

    narrator1 "You turn back to the crowd. They're still restless, still chatty."

    narrator1 "Before long, you catch sight of a black-haired individual making his way through the crowd. He's moving irregularly, and as a guard, this is a cause for concern."

    narrator1 "But there's something about him that looks familiar..."

    narrator1 "And then you place it. It's a figure you've seen countless times on news reports before. The Crown Prince of Insomnia: Noctis Lucis Caelum. What's he doing here? It's odd to see him dressed so casually, and without bodyguards flanking him."

    narrator1 "Especially as, last you heard, the wedding between him and Lady Lunafreya had been called off."

    narrator1 "Ignis catches your gaze, and holds a finger to his lips softly. Oh. You should have guessed sooner."

    you "Is he with you?"

    ignis "Indeed he is."

    narrator1 "Ignis is watching the young Prince carefully, like a protective older brother would. You're itching to know more about why the Prince is here."

    menu:
        "Press Ignis about why the Prince is here":
            jump ask_about_prince
        "Nod in understanding and say no more":
            jump keep_quiet_about_prince
        "Steer the conversation tactfully away from the Prince":
            jump change_subject_from_prince



label ask_about_prince:

    you "I didn't expect to see the Lucian Prince here. I thought the... I thought the wedding was called off?"

    $ happiness -= 1

    show screen happiness_text(title="Happiness decreased")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    ignis "It has been, thanks to our friends from Niflheim."

    narrator1 "His tone is as stiff as his posture has suddenly become, and you get the sense you have put him on a back foot here. The way he talks, there's no love lost for the Empire."

    menu:
        "Press Ignis once again about Prince Noctis":
            jump ask_again_about_prince
        "Backtrack":
            you "Sorry. I shouldn't really be asking at a time like this."

            ignis "It's quite all right. Curiosity is natural, although I would prefer you kept your focus on the task at hand."

            jump niffs_arrive_on_the_scene



label ask_again_about_prince:

    narrator1 "But you've started now, so you continue, albeit hesitantly."

    you "So, uh, why {i}is{/i} he here?"

    $ happiness -= 1

    show screen happiness_text(title="Happiness decreased")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    ignis "Please, [your_name], some decorum. Lest our aforementioned friends take a shining to our conversation."

    jump niffs_arrive_on_the_scene



label keep_quiet_about_prince:

    narrator1 "You decide not to press him for details. It's not really the time nor the place, out in the open like this."

    narrator1 "You're just a guard, after all. You only get told things that are mission-critical."

    narrator1 "Ignis seems to appreciate your discretion."

    show ignis smile

    pause 1.0

    $ happiness += 1

    show screen happiness_text(title="Happiness increased!")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    jump niffs_arrive_on_the_scene



label change_subject_from_prince:

    narrator1 "While you desperately want to know, you are well aware that you only get told things that are mission-critical."
    narrator1 "And furthermore, you never know who might be listening in, in this busy place. So you change the subject, as casually as you can."

    you "" #architecture q


    show ignis smile

    pause 1.0

    $ happiness += 1

    show screen happiness_text(title="Happiness increased!")
    with dissolve

    pause 0.3

    hide screen happiness_text
    with dissolve

    jump niffs_arrive_on_the_scene


label niffs_arrive_on_the_scene:

    narrator1 "Gods above, "
    narrator1 "You're enjoying his company."

    # sound effect engine hum
    narrator1 "A distant hum interrupts your thoughts. A sort of revving, and it's getting closer."

    narrator1 "You look up to see Imperial dreadnoughts approaching."

    narrator1 "Altissia has had so many years of peace under Niflheim's rule that you've almost forgotten the sight of these monstrosities."


    narrator1 "A cheer rises. Up at the steps of the palace, Lady Lunafreya has appeared."

    narrator1 "Even from the back of the plaza, you can see how she walks proudly and confidently. The same stiff-backed, determined attitude your own Captain displays all-too-often. She doesn't want anyone to worry."

    show bg yureilplaza crowd dark with Dissolve(0.3)

    show ignis sidelong openmouth

    ignis "What they bloody hell do they think they're doing?"

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
