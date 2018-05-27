#Scene 11
#Altar

#contains labels:
    # head_to_altar
    # ardyn_appears
    # ravus_conversation

# covers heading to the altar, reaching it and seeing ardyn take ignis away, and talking to ravus for the first time

label head_to_altar:

    show bg jettynearcellar with Dissolve(0.3)

    narrator1 "It takes some effort to swim back over the canal, but you manage."

    narrator1 "This is the fastest way to the altar, now that the bridge is gone, after all."

    narrator1 "You race down the street, past the cellar, past the warehouse block, and on to new streets, new territories."

    show bg leviathan with Dissolve(0.3)

    you "Whoa!"

    narrator1 "The next street you turn down gives you an apocalyptic view."

    you "{i}Leviathan{/i}"

    you "I can't belive I'm really seeing this."

    jump ardyn_appears

label ardyn_appears:

    show bg altar with dissolve

    jump ravus_conversation

label ravus_conversation:

    you "Where did that man take Ignis?"

    you "What did you do to him?"

    ravus "Calm down, brat. I didn't—"

    you "Look, I know you're with the Empire!"

    narrator1 "At this, the man laughs."

    ravus "Oh, I'm not just 'with' the Empire. Ravus Nox Fleuret — Commander of the Nilfheim Military."

    narrator1 "So {i}this{/i} is Ravus. Brother of the Oracle. You've heard of him, for sure, but in person, you never expected him to look so ... young."

    narrator1 "You dimly wonder if the grey is natural."

    ravus "But I've absconded from my duties."

    ravus "I was only trying to protect my sister. And they... they..."

    menu:
        "Show anger":
            you "I don't care!"
            ravus "I don't expect you to. But she's... "
            narrator1 "He cuts off. He's so close to crying, and that's when you spot her."
            narrator1 "She's lying a few metres off, next to another, darker shape."
            narrator1 "Prince Noctis."

        "Show empathy":
            you "Oh. I..."
            narrator1 "You cut yourself off, unsure how to finish."
            narrator1 "He's so close to crying, and that's when you spot her."
            narrator1 "Lady Lunafreya. She's lying a few metres off, next to another, darker shape."
            narrator1 "Prince Noctis."

    you "Oh my gosh, are they both —"
    ravus "No. Only Luna."
    narrator1 "The silence is awkward."
    you "I'm sorry."
    narrator1 "Ravus acts like he hasn't heard you. He's probably hurting too much to acknowledge it."
    ravus "I'm staying with them. If you want to rescue your friend, you'll need to head to the dropship over there."



    return
