#Scene 06
#Power Cut & Next Mission

#contains labels:
    # trooper_attack
    # ignis leaves


# covers first Magitek Trooper fight, and Ignis leaving to go help Prompto and Gladio

label trooper_attack:

    show bg widestreet
    show trooper distance at SpriteLoc2(0.425, 0.3)
    with Dissolve(1.0)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    stop music fadeout 4.572
    play ambient clone_resonance fadein 4.572

    narrator1 "It's when you've just started crossing a particularly wide street that you encounter your first Magitek Trooper."

    you "Is ... is that ..."

    show ignis neutral openmouth
    ignis "A Magitek Trooper. Indeed it is."
    show ignis neutral

    narrator1 "The thing's waiting, zombie-like and menacing, at the end of the street and there's nowhere else to run. You're in the open."

    narrator1 "You ready your weapon, heart pounding."

    show ignis sidelong at left
    with dissolve

    narrator1 "But Ignis moves before you can do anything."

    show bluelightning at SpriteLoc2(-0.11, -0.01) behind ignis with Dissolve(1.0)
    pause 1.0
    hide bluelightning with Dissolve(1.0)

    narrator1 "The first step he takes is accompanied by a crackling blue light and the faint smell of ozone. Where there had been nothing in his hands before, now he grips a pair of brilliant and ornate daggers."

    show ignis sidelong openmouth
    ignis "Let's put a quick end to this."
    show ignis sidelong

    narrator1 "You don't have time to wonder how Ignis summoned those weapons."

    play foley2 trooper_screech noloop
    pause 0.3

    hide trooper distance
    show ignis sidelong openmouth
    show trooper lunging at SpriteLoc2(0.325, 0.0)
    with hpunch

    narrator1 "The trooper lunges forward with a disturbing screech that you can't fully place as either mechanical or organic."

    narrator1 "It's all whirring limbs and strict, unexpressive movements, and everything about it makes you shiver."

    narrator1 "Ignis sidesteps its first attack, parries the next, and manages to land a hit."

    show bg widestreet with fastsoftflash

    play foley2 trooper_screech noloop
    narrator1 "It somehow slips past him, and comes screaming straight for you."

    narrator1 "You scream back, and draw back your sword rapidly, before stabbing forward in the swift motion you were taught during training."

    narrator1 "The sword pierces what appears to be the trooper's core."

    play foley2 trooper_screech2 noloop
    show trooper shortcircuit at SpriteLoc2(0.47, 0.0)
    with fastsoftflash
    show trooper shortcircuit at SpriteLoc2(0.47, 0.0)
    with hpunch

    narrator1 "It falls to the ground, twitching and shrieking."

    show ignis smile with dissolve
    show trooper shortcircuit07 at SpriteLoc2(0.47, 0.0)
    with dissolve

    you "What the ... Is it ... is it evaporating?"

    ignis "Ah - they're infused with daemonic plasma. Rather unnerving the first time one sees it."

    you "Oh. That's ... pleasant."

    hide trooper with fastdissolve

    show ignis neutral openmouth
    ignis "That was very impressive, [your_name]."
    show ignis smile

    narrator1 "You barely manage a smile. You're enraptured watching the dying trooper slip from uncanny-valley into nothing more than dust. Even some of the armour seems to disintegrate."

    stop ambient fadeout 2.286
    play music undercurrent loop

    # sound effect - buzzing
    narrator1 "When the unnerving sight is over, a ping interrupts you both. Ignis draws out his mobile phone and answers it hurriedly."

    show ignis neutral openmouth
    ignis "I'll be there as soon as I can, don't worry."
    show ignis neutral with dissolve

    you "Who was that?"

    show ignis neutral openmouth
    ignis "Ah - my companions. The're in a spot of trouble. Or rather ... the Prince is."

    narrator1 "He sighs, and it's a shallow mask over his fear as he pinches the bridge of his nose. He's thinking hard."

    ignis "I'm afraid my imperative to keep the Crown Prince safe is going to override this mission."
    show ignis neutral

    narrator1 "You understand, although you're a bit dejected."

    narrator1 "It was a bit odd for a diplomat to be pulled into an evacuation mission in the first place, and you suspect the First Secretary may have called for it as a purely symbolic measure."

    narrator1 "Not that Ignis wasn't incredibly capable..."

    narrator1 "You shove the thought of him moving so fluidly with those twin daggers far out of your mind. Luckily, you're already flushed from the fight."

    show ignis neutral openmouth
    ignis "Right, I have to join up with the others now."
    show ignis neutral

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

            show ignis unimpressed openmouth
            ignis "I'm afraid I must."
            show ignis unimpressed

            you "I ... oh."

            narrator1 "Ignis seems to mistake your dejection for anxiety, because he pats your shoulder comfortingly."

            show ignis neutral openmouth
            ignis "There's no need to fear. You have already shown yourself to be more than capable against the MTs."
            show ignis neutral

            you "I, uh ... thanks."

            narrator1 "You don't really know what else to say."

            show ignis neutral openmouth
            ignis "Okay. Best of luck with the remaining evacuees, [your_name]. I'll meet back with you as soon as I've assisted the others."
            show ignis neutral

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

            show ignis neutral openmouth
            ignis "Will you be okay?"
            show ignis neutral

            you "I ... yes, I will."

            show ignis smile with dissolve
            pause 0.5
            show ignis neutral openmouth with dissolve
            ignis "Good. Best of luck with the remaining evacuees, [your_name]. I'll meet back with you as soon as I've assisted the others."
            show ignis smile

            jump ignis_leaving



label ignis_leaving:

    you "Remember the security frequency!"

    show ignis neutral openmouth
    ignis "4400 hertz, of course."
    show ignis neutral

    show bluelightning at SpriteLoc2(-0.11, -0.01) behind ignis with Dissolve(1.0)
    pause 1.0
    hide bluelightning with Dissolve(1.0)

    narrator1 "Ignis summons the sparkling blue light again, and the daggers disappear into the ether."

    narrator1 "Then he's racing off towards the East Quarter."

    hide ignis with Dissolve(0.8)

    narrator1 "Damn. You had meant to ask him about that weird light."

    narrator1 "When he's vanished from sight round the corner of a municipal building, you reaffirm your grip on your dress sword and focus on the road ahead."

    narrator1 "You have a job to do."

    scene black with Dissolve(1.5)

    jump reaching_padore_boats
