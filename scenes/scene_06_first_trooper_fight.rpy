#Scene 06
#Power Cut & Next Mission

#contains labels:
    # trooper_attack
    # ignis leaves


# covers first Magitek Trooper fight, and Ignis leaving to go help Prompto and Gladio

label trooper_attack:

    show bg widestreet
    show trooper distance at SpriteLoc2(0.425, 0.3)
    with Dissolve(0.5)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    stop music fadeout 2.286
    play ambient clone_resonance fadein 2.286

    narrator1 "It's when you've just started crossing a particularly wide street that you encounter your first Magitek Trooper."

    narrator1 "The thing's waiting, zombie-like and menacing, at the end of the street and there's nowhere else to run. You're in the open."

    narrator1 "You ready your weapon, heart pounding."

    show ignis sidelong at left
    with dissolve

    narrator1 "But Ignis moves before you can do anything."

    show bluelightning at SpriteLoc2(-0.11, -0.01) behind ignis with Dissolve(1.5)

    hide bluelightning with Dissolve(1.5)

    narrator1 "The first step he takes is accompanied by a crackling blue light and the faint smell of ozone. Where there had been nothing in his hands before, now he grips a pair of brilliant and ornate daggers."

    ignis "Let's put a quick end to this."

    narrator1 "You don't have time to wonder how Ignis summoned those weapons."

    hide trooper distance
    show ignis sidelong openmouth
    #would be even better to have a shocked ignis here
    # sound effect magitek screech
    show trooper lunging at SpriteLoc2(0.325, 0.0)
    with hpunch

    narrator1 "The trooper lunges forward with a disturbing screech that you can't fully place as either mechanical or organic."

    narrator1 "It's all whirring limbs and strict, unexpressive movements, and everything about it makes you shiver."

    narrator1 "Ignis sidesteps its first attack, parries the next, and manages to land a hit."

    show bg widestreet with fastsoftflash
    # need another effect here... flash of blue light maybe, as when he summons his weapons
    # would be good if this was slightly different each time - randomised

    narrator1 "It somehow slips past him, and comes screaming straight for you."
    # scream sound effect

    narrator1 "You scream back, and draw back your sword rapidly, before stabbing forward in the swift motion you were taught during training."

    show trooper shortcircuit at SpriteLoc2(0.47, 0.0)
    with fastsoftflash
    show trooper shortcircuit at SpriteLoc2(0.47, 0.0)
    with hpunch

    narrator1 "The sword pierces what appears to be the trooper's core, and it falls to the ground, twitching and shrieking."

    show ignis smile
    with dissolve

    ignis "That was ... that was impressive, [your_name]."

    show trooper shortcircuit07 at SpriteLoc2(0.47, 0.0)
    with dissolve

    narrator1 "You barely manage a smile. You're breathless, and enraptured by the horrific sight of the dying trooper, whose body has begun to smoke."

    # start smoke effect around trooper - not sure how I'm gonna do this yet
    show trooper shortcircuit05 at SpriteLoc2(0.47, 0.0)
    with dissolve

    you "Is it ... is it evaporating?"

    ignis "Ah - they're infused with daemonic plasma. Rather unnerving the first time one sees it."

    you "Oh. That's ... pleasant."

    narrator1 "You watch the creature slip from uncanny-valley into nothing more than dust. Even some of the armour seems to disintegrate."

    hide trooper
    with fastdissolve

    stop ambient fadeout 2.286
    # sound effect - buzzing
    narrator1 "When the unnerving sight is over, a ping interrupts you both. Ignis draws out his mobile phone and answers it hurriedly."

    show ignis neutral openmouth
    with dissolve

    ignis "I'll be there as soon as I can, don't worry."

    show ignis neutral
    with dissolve

    you "Who was that?"

    ignis "Ah - my companions. The're in a spot of trouble. Or rather ... the Prince is."

    narrator1 "He sighs, and it's a shallow mask over his fear as he pinches the bridge of his nose. He's thinking hard."

    ignis "I'm afraid my imperative to keep the Crown Prince safe is going to override this mission."

    narrator1 "You understand, although you're a bit dejected."

    narrator1 "It was a bit odd for a diplomat to be pulled into an evacuation mission in the first place, and you suspect the First Secretary may have called for it as a purely symbolic measure."

    narrator1 "Not that Ignis wasn't incredibly capable..."

    narrator1 "You shove the thought of him moving so fluidly with those twin daggers far out of your mind. Luckily, you're already flushed from the fight."

    ignis "Right, I have to join up with the others now."

    narrator1 "He's looking a little apologetic, but at the same time, incredibly tense."

    narrator1 "What will you say?"

    menu:
        "Express disappointment that he has to leave":

            you "You're going to leave me here?"

            pause 1.0

            $ happiness -= 1

            show screen happiness_text(title="Happiness decreased")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            ignis "I'm afraid I must."

            you "I ... oh."

            narrator1 "Ignis seems to mistake your dejection for anxiety, because he pats your shoulder comfortingly."

            ignis "There's no need to fear. You have already shown yourself to be more than capable against the MTs."

            you "I, uh ... thanks."

            narrator1 "You don't really know what else to say."

            ignis "Okay. Best of luck with the remaining evacuees, [your_name]. I'll meet back with you as soon as I've assisted the others."

            jump ignis_leaving

        "Say you understand and wish him luck":

            you "Of course —  we can't let anything happen to the Prince. The risk is too great."

            pause 1.0

            $ happiness += 1

            show ignis smile
            with dissolve

            show screen happiness_text(title="Happiness increased!")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            ignis "I don't like to leave you here, but ... thank you."

            narrator1 "He pauses, studies the skyline, making the quickest of mental maps. Then back to you."

            ignis "Will you be okay?"

            you "I ... yes, I will."

            narrator1 "Ignis smiles."

            ignis "Good. Best of luck with the remaining evacuees, [your_name]. I'll meet back with you as soon as I've assisted the others."

            jump ignis_leaving



label ignis_leaving:

    you "Remember the security frequency!"

    ignis "4400 hertz, of course."

    narrator1 "Ignis summons the sparkling blue light again, and the daggers disappear into the ether. Then he's racing off towards the East Quarter."

    hide ignis
    with dissolve

    narrator1 "Damn. You had meant to ask him about that weird light."

    narrator1 "When he's vanished from sight round the corner of a municipal building, you reaffirm your grip on your dress sword and focus on the road ahead."

    narrator1 "You have a job to do."

    jump reaching_padore_boats
