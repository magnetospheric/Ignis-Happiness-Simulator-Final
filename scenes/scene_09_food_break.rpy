#Scene 09
#Stopping for a food break

#contains labels:
    # food_break


# covers stopping for food & supplies and restocking before he's dragged away again

label food_break:

    show bg cellar with Dissolve(0.3)

    show ignis touching glasses wet at left
    with move

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "Inside the cellar it's damp and airy. There's stacks of boxes everywhere — merchandise, most likely, discarded amid the chaos."

    narrator1 "You turn over a box to reveal a sign saying 'LEIDEN POTATOES — IMPORT'."

    you "I think this is a grocery warehouse."

    ignis "It does seem that way."

    narrator1 "He pauses, considers."

    ignis "We need to replenish our strength ... but let's take only what we need."

    show ignis neutral wet with dissolve

    narrator1 "You root around for something suitable to eat. Maybe a chocolate bar, or some fruit..."

    narrator1 "By the time you've turned around, Ignis has already found a small portable stove, and has grabbed some Leiden potatoes, peppers and herbs."

    show bluelightning at SpriteLoc2(-0.11, -0.01) behind ignis with Dissolve(1.5)

    hide bluelightning with Dissolve(1.5)

    narrator1 "Did you spy a crackle of blue light there?"

    narrator1 "You really should ask him about that. But right now you're staring at the sparse ingredients, wondering how he's going to cook them up with the meagre tools available."

    you "Need any help?"

    ignis "Oh, no, I'm quite all right. Thank you, though."

    narrator1 "You don't really know what to do, so you take to standing guard while he rustles up something to eat. Within minutes the appetising smell is teasing your senses."

    show ignis neutral openmouth wet with dissolve

    # bit with cooking here
    ignis "Well, dinner is served!"

    narrator1 "Just as well — you can't bear the tantalising smell any longer. You sit on one of the warehouse crates next to Ignis, and he hands you a bowl."

    narrator1 "It looks like some kind of potato stew."

    ignis "It's a bit of a slapdash recipe, but I hope it tastes adequate."

    narrator1 "You take a bite."

    narrator1 "A rush of flavour floods your senses: you feel warm, comforted, even nostalgic. Your mouth is watering even while you're eating."

    you "Oh wow. Okay. Ignis, this is amazing!"

    ignis "Well, I do try my best."

    you "No, but seriously. This is a whole other level!"

    show ignis smile wet with dissolve

    ignis "I'll have to consider that very high praise indeed, coming from a citizen of Altissia."

    you "Where on earth did you learn to cook like this?"

    ignis "Ah, it was something I picked up in my line of work. When one takes care of a prince, one must learn to make food worthy for a king."

    you "Heh — lucky Prince."

    narrator1 "You both eat up eagerly. All your exertions so far have left you ravenous"

    show ignis neutral eyesclosed wet with dissolve

    narrator1 "When the plates lie empty, Ignis leans back against the stacks of crates, and sighs deeply."

    show ignis neutral openmouth eyesclosed wet with dissolve

    ignis "This whole day is completely ridiculous. I expected {i}some{/i} trouble from the Empire — don't we always? — but this ... this is far above and beyond."

    you "It really is. I feel completely underprepared for this whole thing."

    show ignis neutral openmouth wet with dissolve

    ignis "Don't we all."

    # narrator1 "Then he focusses hard on the floor in front of him."

    ignis "I wish I knew what the Empire were thinking!"

    menu:
        "Lighten the mood":

            you "You know what I want to know more than anything? Why there's so many weird pieces of artwork around this city."

            narrator1 "Ignis laughs."

            narrator1 "But a moment later he falls back into thought."

            narrator1 "You don't enjoy that expression. He seems sad, frustrated."

        "Commiserate some more":

            you "Same. I just don't understand why they'd do this!"

            you "I mean, I understand there's a lot of political motivations, but — ugh, we'd had peace for a decade. What they're doing here now is overkill!"

            ignis "It's no fun to see one's home city be destroyed."

            narrator1 "This quells your words. You remember the news reports about the City of Insomnia."

            you ""

            ignis "Don't be. The Empire will stop at nothing to get what they want."

            you "Which is what, exactly? There won't be any world left to rule if they keep this up."

            ignis "There's something else at play... It's not apparent to me yet, but...sSomething doesn't add up."

            narrator1 "And there, he's lost in thought again. You leave him to it."

    narrator1 "After a while, he lets out a frustrated sigh."

    ignis "Agh — I have no idea how we're to get Noctis to the altar."

    if examined_harpoon == True:

        narrator1 "A memory sparks in your mind. Smooth chrome and the humorous image of an oversized hoverboard."

        you "Hey, I don't know if this is useful, but earlier I saw this ... {i}thing{/i} in the rubble. It looked like a giant harpoon, except ... more like one you could ride."

        narrator1 "At this, Ignis's face lights up."

        ignis "A Magitek device?"

        narrator1 "You nod."

        ignis "Yes... yes! That's perfect!"

    else:

        you "You'll think of something"

        you "Shame we can't just fly over there."

        ignis "Wait ... that reminds me... I saw this curious piece of technology in the square. I wonder..."

    ignis "I need to make a call."

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

    narrator1 "After switching off the dial, Ignis puts the radio aside and looks back at you."

    ignis "It ought to take him another ten minutes to get here."

    narrator1 "Seems you have some more time to rest up. You settle back against the wall, trying to ignore how scratchy the brick is against your uniform."

    you "Wow, I'm still kind of stuffed after that food, or I'd ask for more."

    show ignis neutral eyesclosed wet with dissolve

    ignis "Now, if it had been a nice seafood paella, followed by some fluffy chiffon cake, I might say the same."

    ignis "But alas, this is no paella."

    show ignis neutral wet with dissolve

    if you_gender_nickname == "individual":
        ignis "So, [your_name], what made an [you_gender_nickname] such as yourself join the Municipal Guard?"
    else:
        ignis "So, [your_name], what made a [you_gender_nickname] such as yourself join the Municipal Guard?"

    you "Oh, wow, okay. Big question."

    show ignis smile wet

    ignis "The reasons are never easy to articulate, even to oneself."

    narrator1 "You really don't consider him a stranger at this point, but you don't want to say so."

    narrator1 "So why did you sign up for this job?"

    narrator1 "You don't need to tell Ignis your reason. But it's important to be honest with yourself."

    menu:
        "I wanted to help people in times of need":
            $ motivation = "help"
        "I wanted to protect people from threats":
            $ motivation = "protect"
        "I just wanted to get paid regularly":
            $ motivation = "survival"
        "I wanted the prestige that comes with the position":
            $ motivation = "prestige"
        "I wanted to learn more about security":
            $ motivation = "education"

    narrator1 "Will you tell Ignis?"

    menu:
        "Tell Ignis your reason":
            if $ motivation = "help":
                you "I wanted to help people."
            if $ motivation = "protect":
                you "I wanted to protect people."
            if $ motivation = "survival":
                you "I needed a stable income."
            if $ motivation = "prestige":
                you "I needed a stable income."
            if $ motivation = "education":
                you "I wanted to learn about "

            jump openup

        "Do not tell":
            you "Yeah, I guess so. Heh, maybe someday."

            ignis "It's important you follow the path that's right for you. Whatever your motivation, you ought to stay true to it."

            narrator1 "When did this get so much like an inspirational talk? You can't hide your wry smile, and Ignis chuckles."

            jump meet_prompto

label openup:
    menu:
        "It's good to open up":
            you "tell"
            # if you say yes it's good to open up, he will then open up about his stuff
        "It's important to be cautious":
            you "Do not"

    ignis "It's good to open up ... hmm ... perhaps you are right."

    ignis "I — I admit, I ... never actually liked cooking."

    you "Really? But you're so good at it"

    ignis "I suppose I've learnt enough to get by, but — if I'm perfectly honest, it was only to make "

    ignis "He had this particular dish he liked, from his travels in Tenebrae as a youth. The Royal Chefs couldn't recreate it, and, with Tenebrae under Imperial rule, one couldn't exactly hop over and ask them for a recipe."

    ignis "So I learned. And over time I grew to enjoy the art of cooking, I suppose."

    narrator1 "He leans in a little, eyebrow quirking upward."

    ignis "I still haven't gotten the recipe quite right, however."

    # he reveals he was never into cooking until noctis. +1H if you say this shows his dedication and quality of character. -1H if you question why he would do something he doesn't like.

    menu:
        "Compliment his dedication":

            you "Y'know, it really says a lot that you'd go to such lengths for him. You're a really dedicated person, you know that?"

            ignis "Ah ... thank you, [your_name]."

            narrator1 "Have you actually managed to make him shy?"

            narrator1 "You carry on regardless."

            you "Prince Noctis is lucky to have someone like you."

            narrator1 "The dimples that cross his cheeks are incredibly cute, and you're happy you've managed to make him feel better, despite the stress, despite the awful situation you're both in."

            ignis "Ah ... one can only hope."

            you "I'm certain of it."

            # this only happens if happiness is above a certain number, otherwise he says a simpler flattery and stops there

            ignis "Well, in return, I have to say I'm lucky to have met someone like you."

            you "Me?"

            narrator1 "Ignis nods."

            ignis "Of all the guards I could have been assigned on duty with, I'm exceedingly glad it was you. Your care for your fellow man is ... well, heartening, to say the least."

            ignis "You've lifted my spirits, that's for sure."

            narrator1 "There's a blush hitting your cheeks — you can feel it rising. It must be so obvious."

            you "I'm really glad to hear that."

        "Question why he would do something he doesn't enjoy":

            you "Why would you put so much energy into doing something you don't like?"

            show ignis neutral wet

            ignis "It comes with the job description. Personal preference is not exactly something that plays a part in this."

            you "That seems ... kind of a shame."

            ignis "It's only a small sacrifice in the bigger picture."

            you "Still, I don't ... I don't like the thought of you never getting to "

            ignis "It's kind of you to be so concerned, but it's really not necessary."

    jump meet_prompto

label meet_prompto:

    ignis "Well, I suppose we should go out and meet him."

    you "Or at least check if the mechs have moved on."

    ignis "Indeed."

    narrator1 "Ignis starts to head up to ground level."

    narrator1 "You spend a moment looking around before you do the same, just in case you miss anything."

    narrator1 "There's not enough time to grab much, so you..."

    menu:
        "Grab a bottle of water":
            $ extra_item = "water"
        "Stuff a pack of biscuits into your pocket":
            $ extra_item = "biscuits"
        "Stop wasting time and hurry outside":
            $ extra_item = "nothing"

    # call screen choose_warehouse_goods

    return
# conversation with ignis.... for later
