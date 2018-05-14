#Scene 08
#Reuniting with Ignis and stopping for a food break

#contains labels:
    # meeting_ignis_again
    # food_break


# covers meeting back up with ignis again and stopping for food & supplies and restocking before he's dragged away again


label meeting_ignis_again:

    show bg mediumstreet with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "Back down the same streets, and it's starting to feel like deja-vu."

    narrator1 "You don't turn your radio back on. Yes, it would let Ignis know you're coming to his aid, but there's no way of knowing if it will incite his assailant, make him hurt Ignis more."

    narrator1 "Better to surprise them all, anyway, if it comes to that."

    narrator1 "So there's nothing to do but keep going, and trust that he'll still be there, in Tigiano District."

    show bg rubblestreet with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "When you reach Tigiano, the square is empty. Nothing but mech debris and the smoking remnants of Magitek armour scattered about."

    narrator1 "There's certainly no sign of human life."

    you "Ignis?"

    narrator1 "No response."

    narrator1 "You explore the square, shouting out at intervals. You don't even care if any Magitek Troopers hear you, you'll fight."

    narrator1 "Or so you tell yourself."

    you "Ignis? Ignis — come on, please be here!"

    narrator1 "A scrabbling amid the rubble to your right catches your attention."

    show ignis wet neutral
    with dissolve

    ignis "[your_name] ... Ah!"

    narrator1 "He stumbles, and you rush to support him."

    ignis "Th-thank you."

    narrator1 "It's a shock to see Ignis looking so dishevelled. You bite your lip as you steady him, thinking this is all your fault for being late."

    you "I — I heard over the radio. Who was that man? Are you okay?"

    ignis "Before I go into it, tell me — did you manage to save the citizens?"

    if citizens_first == True:
        you "Yes"
    else:
        menu:
            "(Lie)":
                "Yes"
            "Say you haven't yet but you will":
                you "Not yet, but I'm planning on going back as soon as I know you're okay."
            "Tell him he was more important":
                you "I couldn't leave you!"

    jump food_break



label food_break:

    return



# conversation with ignis.... for later


# ignis "You wanted to save as many people as possible, right?"
#
# narrator1 "Is that why you became a guard?"
#
# narrator1 "You don't need to tell Ignis your reason why. But it's important to be honest with yourself."
#
# menu:
#     "I wanted to help people in times of need":
#         $ motivation = "help"
#     "I wanted to protect people from threats":
#         $ motivation = "protect"
#     "I just wanted to get paid regularly":
#         $ motivation = "survival"
#     "I wanted the prestige that comes with the position":
#         $ motivation = "prestige"
#     "I wanted to learn more about security":
#         $ motivation = "education"
