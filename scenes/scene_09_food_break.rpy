#Scene 09
#Stopping for a food break

#contains labels:
    # food_break


# covers stopping for food & supplies and restocking before he's dragged away again

label food_break:

    show bg cellar with Dissolve(0.3)

    show ignis at left
    with move

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "Inside the cellar it's damp and airy. There's stacks of boxes everywhere — merchandise, most likely, discarded amid the chaos."

    narrator1 "You turn over a box to reveal a sign saying 'LEIDEN POTATOES — IMPORT'."

    you "I think this is a grocery warehouse."

    ignis "It does seem that way."

    narrator1 "He pauses, considers."

    ignis "We need to replenish our strength ... but let's take only what we need."

    you "You know what I want to know more than anything? Why there's so many weird pieces of artwork around this city."

    narrator1 "Ignis laughs"

    narrator1 "But a moment later he falls back into thought."

    narrator1 "You don't enjoy that expression. He seems sad, frustrated."

    ignis "Agh — I have no idea how we're to get Noctis to the altar."

    if examined_harpoon == True:

        you "Hey, I don't know if this is useful, but earlier I saw this"

        narrator1 "At this, Ignis's face lights up. You can practically see the cogs turning in his brain."

        ignis "Yes... yes! That's perfect! "

    else:

        ignis ""

    narrator1 "It takes him a bit of fiddling with the dial before his radio will work again, but thankfully the ordeal with Caligo doesn't seem to have broken the device completely."

    ignis "Prompto, are you there?"

    ignis "..."

    prompto "{i}Reading you loud and clear, Iggy!{/i}"

    ignis "Ah, good. Listen — we've found a way to get Noct to the altar."

    prompto "{i}Aw, Iggy! Didn't expect you to be so interested in a piece of tech.{/i}"

    if examined_harpoon == True:
        if happiness > 8:
            ignis "Oh, no, I can't take the credit. It's all thanks to the guard I've teamed up with. [your_pronoun_subject] the one responsible for finding it."
        else:
            ignis "Oh, no, I can't take the credit. It's all thanks to the guard I'm travelling with. [your_pronoun_subject] the one responsible for finding it."
    else:
        ignis "A gentleman has his secrets."

    prompto "{i}Heheh. Okay, cool. Should I, uh, come meet you?{/i}"

    ignis "Please. We're in a warehouse cellar just across from the Tigiano bridge. There's a harpoon in the square."

    prompto "{i}On it. Laters!{/i}"

    narrator1 "You rest back against the wall. There's still time to kill while Ignis's companion heads this way."

    ignis "Well, I suppose we should go out and meet him."

    you "Or at least check if the mechs have moved on."

    ignis "Indeed."

    narrator1 "Ignis starts to head up to ground level."

    narrator1 "You spend a moment looking around before you do the same, just in case you miss anything."

    # call screen choose_warehouse_goods

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
