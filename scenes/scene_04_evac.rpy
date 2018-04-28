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

    narrator1 "He's checking for discrepancies and dissent as much as you are. His keen eyes rove the crowd, before settling on the multi-spired, domed towers of the palace."

    ignis "It's a beautiful piece of architecture. Rather strategically-designed, too."

    you "How so?"

    ignis "The domed structures are a good shape to protect against assault or natural disaster. And the plaza itself is long and narrow - see where it bottlenecks quite naturally before these points they've got us guarding? It's exceedingly good for crowd control."

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

    narrator1 "Ignis is watching the young Prince carefully, like a protective older brother would. You're itching to know more, because it feels like there's a part of this plan you're missing."

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

    narrator1 "His tone is as stiff as his posture has suddenly become, and you get the sense you have put him on a back foot here. The way he talks, there's no love lost for the Empire. But more than that — he seems uncomfortable discussing this in such a public space."

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

    ignis "Please, [your_name], some decorum. Lest our aforementioned 'friends' take a shining to our conversation."

    jump niffs_arrive_on_the_scene



label keep_quiet_about_prince:

    narrator1 "You decide not to press him for details. It's not really the time nor the place, out in the open like this where anyone could be listening."

    narrator1 "Is it really necessary for you to know, anyway? You're just a guard, after all. You only get told things that are mission-critical."

    narrator1 "So you nod, and return to watching the crowd."

    show ignis smile

    narrator1 "Ignis seems to appreciate your discretion."

    pause 1.0

    $ happiness += 1

    show screen happiness_text(title="Happiness increased!")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    ignis ""

    jump niffs_arrive_on_the_scene



label change_subject_from_prince:

    narrator1 "While you desperately want to know, you are well aware that you only get told things that are mission-critical for a reason."

    narrator1 "And furthermore, you never know who might be listening in, in this busy place. So you change the subject, as casually as you can."

    you "You know, the palace is actually a lot newer than the rest of Altissia."

    ignis "Oh?"

    narrator1 "He seems to appreciate the distraction."

    you "Yeah. I mean, the Altar of the Tidemother is still older than most things here, but there used to be a different shrine around it. It got destroyed a couple of hundred years ago, during a flood."

    ignis "Did it now? Mm, I don't suppose it was built from the same material as the altar, then?"

    narrator1 "You shake your head."

    you "Just regular limestone. Not a great idea."

    ignis "Indeed."

    you "But yeah — a lot of people don't know that, about the palace. People have terrible memories when it comes to floods, though. We forget our histories too quickly."

    show ignis smile

    pause 1.0

    $ happiness += 1

    show screen happiness_text(title="Happiness increased!")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    ignis "True enough."

    ignis "Well, I certainly didn't expect to get a personal tour guide on this assignment. But — you ought to know — you do a fine job."

    narrator1 "His smile is broad and genuine, and you realise he's not simply humouring you for the sake of distracting any would-be eavesdroppers. You're glowing with his compliment, too — people are usually telling you to shut up around now."

    jump niffs_arrive_on_the_scene


label niffs_arrive_on_the_scene:

    show ignis neutral

    # these next few lines you only get if you haven't seriously pissed him off so far.
    if happiness > 4:

        narrator1 "Ignis turns back to survey the scene. Gods above, he cuts a sharp profile against the pastel morning light. You're staring but you don't care. Do all Lucians look this good?"

        narrator1 "One thing stands out above all others. You're enjoying his company."

    elif happiness > 3:

        narrator1 "Ignis turns back to survey the scene. You watch him for a short moment — he cuts a striking figure — but you soon turn back yourself and focus on your job."

    elif happiness <= 3:

        narrator1 "You try to think of something to say to fill the gap, but nothing comes."

    narrator1 "Then, a cheer rises. Up at the steps of the palace, Lady Lunafreya has appeared."

    narrator1 "Even from the back of the plaza, you can see how she walks proudly and confidently. The same stiff-backed, determined attitude your own Captain displays all-too-often. She doesn't want anyone to worry."


    narrator1 "Ignis activates his receiver."

    ignis "{i}Don't forget the plan.{/i}"

    narrator1 "Somewhere further in the crowd, a black head of hair shifts as the call is answered. It sounds like the Prince says something sarcastic then, because Ignis smiles wryly."

    show ignis smile

    ignis "Of course."

    narrator1 "Up at the gates of the palace, Lunafreya begins to speak."

    show ignis neutral
    with dissolve

    narrator1 "Her voice carries far, for someone so slight. She speaks of the coming darkness, of the scourge that plagues the world, and it sounds so foreboding, such mentions of horror and despair from someone so pure."

    narrator1 "But then, she turns to talk of hope. {i}The Gods have not abandoned us,{/i} she says. And she speaks with such gravitas, you want to believe it. You {i}do{/i} believe it."

    narrator1 "Lunafreya, too, makes no mention of Prince Noctis, although her eyes scan the crowd just before she leaves. You get the impression her plea to Leviathan will not be made alone, and you can only hope that the Empire does not catch wind of Noctis's presence."

    narrator1 "Then Lady Lunafreya is gone, vanished back into the palace to make her petitions at the Altar of the Tidemother."

    narrator1 "It's time for action."

    you "Okay, everyone, please make your way to the back of the plaza. The boats here will take you to Finangia District, out of the flooding zone."

    narrator1 "You wave the bemused citizens forward."

    you "Please, exit this way."

    narrator1 "You and Ignis both guide them towards the boats. You get a few questions — {i}why do we have to evacuate?{/i}, and {i}we want to support the Oracle{/i}, and {i}you can't tell us what to do in our own home{/i} — but for the most part, everyone is solemn enough to not cause any trouble."

    # sound effect engine hum
    narrator1 "A distant hum interrupts your work. A sort of revving, and it's getting closer."

    narrator1 "You look up to see Imperial dreadnoughts approaching."

    narrator1 "Altissia has had so many years of peace under Niflheim's rule that you've almost forgotten the sight of these monstrosities. It's always been there, that low-rumbling threat in the back of your mind, and it's a shock now to see so many of the massive machines, fencing the city in like this."

    ignis "Don't draw too much attention to them."

    narrator1 "You nod. You don't want to panic the crowd. You continue herding them as before, hoping the Empire won't be foolish enough to start anything before the citizens reach safety."

    narrator1 "Ignis has taken to his receiver once again, and is speaking in hushed tones."

    ignis "{i}Noct, do you read me? ... Good. Listen — the Empire has arrived.{/i}"

    ignis "{i}Dropships are closing in on the port. You need to reach the altar before —{/i}"

    hide ignis

    show bg yureilplaza crowd dark with Dissolve(0.3)

    narrator1 "With a burst of frenetic energy, the airships hovering above you open fire." with vpunch

    narrator1 "Their focus seems to be on the altar beyond the palace, but they don't seem particularly bothered about catching people in the crossfire, and stray bursts of explosions from small missiles and gunfire erupt in the plaza."

    narrator1 "The few people left in the plaza, and those still being transported away on the boats, begin to scream." with vpunch

    show ignis sidelong openmouth at left
    with dissolve

    ignis "What they bloody hell do they think they're doing?"

    show ignis sidelong
    with dissolve

    narrator1 "Now both your receivers crackle into life."

    captain "{i}Everyone in the South sector of the plaza, report back to the palace immediately once the citizens have boarded the boats! I repeat: Report back to the palace immediately once the citizens have boarded.{/i}"

    show ignis sidelong direct
    with dissolve

    narrator1 "The crackling cuts off, and you and Ignis share a worried glance before ushering the last few stragglers onto the boats. You tell the last citizens that everything will be okay, then Ignis claps you briefly on the shoulder and together you race back to the palace."

    you "what's going on?"

    narrator1 "The two of you are running as fast as humanly possible, and Ignis's reply comes in sharp bursts."

    show ignis sidelong direct openmouth
    with dissolve

    ignis "The empire ... seeks to disrupt ... the ceremony."

    you "And you knew this was going to happen?"

    ignis "Yes."

    narrator1 "You would have liked to have known this beforehand. But there's little point in making a fuss now. You need to focus."

    jump power_cut



label power_cut:

    narrator1 "When you arrive in the palace entrance hall, the Captain and a handful of guards are already there."

    captain "Ah, [your_name], [ignis_name], good work."

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
