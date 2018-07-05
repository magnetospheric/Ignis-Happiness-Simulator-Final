#Scene 14
#Altar Aftermath

#contains labels:
    # altar_aftermath

# covers taking ignis back to the altar to Noct, and final conversation with Ravus, then going home


label altar_aftermath:

    show bg altar with dissolve

    show ignis neutral injured at right with move

    show ravus neutral at left with Dissolve(0.5)

    show ravus neutral openmouth
    ravus "Ah, the prodigal Advisor returns."
    ravus "You're a fool for taking him on, you know."
    show ravus neutral

    show ignis neutral openmouth injured
    ignis "And you're a bloody idiot for attempting the same."
    ignis "Is Noct here?"
    show ignis neutral injured

    you "Yes. He's right beside you."

    narrator1 "Ignis tries to reach out, but falls back, exhaustion getting the better of him." with vpunch

    you "Aah! Ignis!"

    show ravus neutral openmouth
    ravus "I'm not surprised, with those wounds."
    show ravus neutral

    you "Be strong, Ignis, be strong... Please... It'll be okay now..."

    narrator1 "Some of your words feel hollow, but you really, truly mean them. You stroke the wet hair off his forehead, gently pulling strands away from his inflamed wounds."

    you "You'll be okay. You will."

    narrator1 "Ignis tries to speak, but he's too exhausted."

    hide ignis with Dissolve(0.5)
    $ show_happiness = False
    show ravus at center with move

    narrator1 "Moments later, he falls into unconsciousness. You watch his chest rise and fall, and tell yourself he's fine."

    narrator1 "Behind you, the Chancellor's airship takes off with a bassy rumble. He's leaving the area."

    if deactivated_generator == True:
        narrator1 "It lilts to the side as it gains altitude, sparks issuing from the engine."
        you "Hah! I thought killing that generator would help."
        narrator1 "It's not quite enough to fell the ship, however. It only slows it down, but still, it's satisfying to see."

        show ravus neutral openmouth
        ravus "{i}You{/i} killed one of the generators?"
        show ravus smile with dissolve

        you "Yep!"

        $ ravus_happiness += 1

        show ravus smile openmouth with dissolve
        ravus "Well, fancy that."
        show ravus smile

    you "I thought he was going to come after us."

    show ravus neutral openmouth with dissolve
    ravus "Either he doesn't realise Ignis is not on the ship, or he doesn't care."
    show ravus neutral

    you "He doesn't care? Why go to all the trouble if he doesn't care?"

    show ravus neutral openmouth
    ravus "This {i}is{/i} the Chancellor we're talking about."
    ravus "He was merely taking advantage of the opportunity."
    ravus "He'll just find someone else to play the role he desires..."
    show ravus neutral

    narrator1 "You don't quite know what this means, but it gives you a sickly feeling in the pit of your stomach."

    narrator1 "You look back to Ignis, breathing so softly as he rests on the ground, unconscious, vulnerable, unaware."

    narrator1 "How could anyone hurt him?"

    narrator1 "How could anyone seek to {i}use{/i} him?"

    narrator1 "The urge to protect him is so strong, you never thought it possible to feel this intensely."

    show ravus neutral openmouth
    ravus "Ignis's companions are on their way. You are no longer needed."
    show ravus neutral

    narrator1 "This makes you bristle; you feel like you've been pretty damn instrumental so far, and you don't enjoy the cold manner in which he says this."

    you "I want to stay with him."

    show ravus neutral openmouth
    ravus "You have very limited choice. Ardyn is leaving, and I've ordered a full military retreat. Your superiors need to know about that."
    ravus "And ... about Luna."
    show ravus neutral

    narrator1 "He bends down to touch Lunafreya's cheek softly, and you hate noticing how his fingers meet with the stiffness of her flesh. Rigor mortis has already set in."

    show ravus neutral openmouth
    ravus "Would that I could stay with you, dear sister."
    show ravus neutral

    narrator1 "Then he rises, and speaks to you once more."

    show ravus neutral openmouth
    ravus "I can't be seen here when your superiors arrive. It shall be up to you to inform them of her passing."
    show ravus neutral

    narrator1 "He turns to go."

    you "Hey, Ravus."

    menu:
        "Thank him, wish him well":

            you "Thank you. I hope you make it out okay."

            $ ravus_happiness += 2

            show ravus neutral openmouth
            ravus "I appreciate that."
            ravus "I'm sorry about your home."
            show ravus neutral

            narrator1 "And he leaves."

        "Just thank":

            you "Thank you."

            $ ravus_happiness += 1
            narrator1 "Ravus nods."

            show ravus neutral openmouth
            ravus "Farewell."
            show ravus neutral

            narrator1 "Then he leaves."

        "No thank, only farewell":

            you "Goodbye."

            narrator1 "Ravus gives only the briefest of nods, then leaves."


    hide ravus with Dissolve(0.5)

    narrator1 "In the stillness that follows, it feels like you're the only one left alive."

    narrator1 "You turn on your radio."

    you "Captain? I'm at the altar. The Empire's retreating but ... we have some serious casualties."

    captain "{i}Okay - stay right where you are, [your_name]. A relief team is on their way.{/i}"

    narrator1 "You wait for them to arrive, sitting down on a broken pillar, not quite sure what to do with yourself."

    narrator1 "And around you, the dust and ash continues to swirl."

    #fade out, sounds of footsteps as people arrive, fading sound of engines.

    jump going_home
