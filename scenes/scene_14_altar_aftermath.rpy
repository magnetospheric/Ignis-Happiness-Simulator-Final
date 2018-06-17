#Scene 14
#Altar Aftermath

#contains labels:
    # altar_aftermath

# covers taking ignis back to the altar to Noct, and final conversation with Ravus, then going home


label altar_aftermath:

    show bg altar with dissolve

    show ignis neutral injured at right with move

    show ravus neutral at left with move

    ravus "Ah, the prodigal Advisor returns."

    ravus "You're a fool for taking him on, you know."

    ignis "And you're a bloody idiot for attempting the same."

    ignis "Is Noct here?"

    you "Yes. He's right beside you."

    narrator1 "Ignis tries to reach out, but falls back, exhaustion getting the better of him."

    you "Aah! Ignis!"

    ravus "I'm not surprised, with those wounds."

    you "Be strong, Ignis, be strong... Please... It'll be okay now..."

    narrator1 "Some of your words feel hollow, but you really, truly mean them. You stroke the wet hair off his forehead, gently pulling strands away from his inflamed wounds."

    you "You'll be okay. You will."

    narrator1 "Ignis tries to speak, but he's too exhausted."

    narrator1 "Moments later, he falls into unconsciousness. You watch his chest rise and fall, and tell yourself he's fine."

    narrator1 "Behind you, the Chancellor's airship takes off with a bassy rumble. He's leaving the area."

    you "I thought he was going to come after us."

    ravus "Either he doesn't realise Ignis not on the ship, or he doesn't care."

    you "He doesn't care? Why go to all the trouble if he doesn't care?"

    ravus "He was merely taking advantage of the opportunity."

    ravus "He'll just find someone else to play the role he desires."

    narrator1 "You don't quite know what this means, but it gives you a sickly feeling in the pit of your stomach."

    narrator1 "You look back to Ignis, breathing so softly as he rests on the ground, unconscious, vulnerable, unaware."

    narrator1 "How could anyone hurt him?"

    narrator1 "How could anyone seek to {i}use{/i} him?"

    narrator1 "The urge to protect him is so strong, you never thought it possible to feel this intensely."

    ravus "Ignis's companions are on their way. You are no longer needed."

    narrator1 "This makes you bristle; you feel like you've been pretty damn instrumental so far, and you don't enjoy the cold manner in which he says this."

    you "I want to stay with him."

    ravus "You have very limited choice. Ardyn is leaving, and I've ordered a full military retreat. Your superiors need to know about that."

    ravus "And ... about Luna."

    narrator1 "He bends down to touch Lunafreya's cheek softly, and you hate noticing how his fingers meet with the stiffness of her flesh. Rigor mortis has already set in."

    ravus "Would that I could stay with you, dear sister."

    narrator1 "Then he rises, and speaks to you once more."

    ravus "I can't be seen here when your superiors arrive. It shall be up to you to inform them of her passing."

    narrator1 "He turns to go."

    you "Hey, Ravus."

    menu:
        "Thank him, wish him well":

            you "Thank you. I hope you make it out okay."

            $ ravus_happiness += 1

            ravus "I appreciate that."

            ravus "I'm sorry about your city."

            narrator1 "And he leaves."

        "Just thank":

            you "Thank you."

            narrator1 "Ravus nods."

            ravus "Farewell."

            narrator1 "Then he leaves."

        "No thank, only farewell":

            you "Goodbye."

            narrator1 "Ravus gives only the briefest of nods, then leaves."

    narrator1 "In the stillness that follows, it feels like you're the only one left alive."

    narrator1 "You turn on your radio."

    you "Captain? I'm at the altar. The Empire's retreating but... We have some serious casualties."

    captain "{i}Okay - stay right where you are, [your_name]. A relief team is on their way.{/i}"

    narrator1 "You wait for them to arrive, sitting down on a broken pillar, not quite sure what to do with yourself."

    narrator1 "And around you, the dust and ash continues to swirl."

    #fade out, sounds of footsteps as people arrive, fading sound of engines.

    return
