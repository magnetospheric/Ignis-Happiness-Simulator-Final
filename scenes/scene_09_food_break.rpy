#Scene 09
#Stopping for a food break

#contains labels:
    # food_break
    # openup
    # ignis_opens_up
    # meet_prompto


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

    ignis "Well, dinner is served!"

    narrator1 "Just as well — you can't bear the tantalising smell any longer. You sit on one of the warehouse crates next to Ignis, and he hands you a bowl."

    show soup at SpriteLoc2(0.3, 0.11) with dissolve

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

    narrator1 "You both eat up eagerly. All your exertions so far have left you ravenous, and you wolf it down like there's no tomorrow."

    narrator1 "Potatoes are great enough as it is, but is it even {i}possible{/i} for them to taste this good?"

    show ignis neutral eyesclosed wet with dissolve

    show soup empty with dissolve

    narrator1 "When the plates lie empty, Ignis leans back against the stacks of crates, and sighs deeply."

    hide soup with dissolve

    show ignis neutral openmouth eyesclosed wet with dissolve

    ignis "This whole day is completely ridiculous. I expected {i}some{/i} trouble from the Empire — don't we always? — but this ... this is far above and beyond."

    you "It really is. I feel completely underprepared for this whole thing."

    show ignis neutral openmouth wet with dissolve

    ignis "Don't we all."

    you "So, you never did say what happened up there. Who was that man?"

    ignis "Oh, yes — Caligo Ulldor, he's called. Likes to think of himself as a big shot, but he's not."

    ignis "He was the one preventing Noctis getting to the altar, so I had to try and stop him."

    ignis "I ... let my guard down. He blew the bridge. I think he assumed the explosion killed me."

    you "Oh, gods... I'm glad you're okay."

    ignis "Well, a few bruises, but nothing to complain about."

    you "Is the Prince okay?"

    show ignis smile wet with dissolve

    ignis "He's not in immediate danger right now, thankfully. He's busy scouting for a way to the altar."

    you "Is it safe for him to be alone?"

    ignis "I assure you, he is quite capable."

    narrator1 "There's a wry upturn to his smile here, and you get the distinct impression there is more to this tale that he is not telling."

    narrator1 "For now, you leave it."

    show ignis unimpressed openmouth wet with dissolve

    ignis "I wish I knew what the Empire were thinking!"

    menu:
        "Lighten the mood":

            you "Hey, hey, you know what I want to know more than anything?"

            ignis "What's that?"

            you "Why there's so many weird pieces of artwork around this city."

            show ignis smile wet with dissolve

            $ show_happiness = True

            pause 0.5

            $ happiness += 1

            show screen happiness_text(title="Happiness increased!")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            narrator1 "Ignis laughs."

            ignis "I think I know the very person you mean."

            you "Yeah?"

            ignis "That street artist. Interesting lass, right enough. We bumped into her yesterday, you know."

            show ignis unimpressed wet with dissolve

            ignis "She made this ... doodle ... of the whole group of us. The Prince's entourage."

            you "Oh, yeah? You don't look like you liked it much."

            ignis "Yes, well. She made my forehead look massive."

            narrator1 "You giggle at this."

            you "Do you have it with you?"

            show ignis smile wet with dissolve

            ignis "Thankfully not."

            narrator1 "You've managed to make him smile, and you're all ready to congratulate yourself, but a moment later he falls back into thought."

            show ignis unimpressed wet with dissolve

        "Commiserate some more":

            you "Same. I just don't understand why they'd do this!"

            you "I mean, I understand there's a lot of political motivations, but — ugh, we'd had peace for a decade. What they're doing here now is overkill!"

            show ignis unimpressed wet with dissolve

            ignis "It's no fun to see one's home city be destroyed."

            narrator1 "This quells your words. You remember the news reports about the City of Insomnia."

            you "I'm sorry."

            show ignis neutral wet with dissolve

            ignis "Don't be. The Empire will stop at nothing to get what they want."

            you "Which is what, exactly? World domination?"

            you "There won't be any world left to rule if they keep this up."

            ignis "There's something else at play... It's not apparent to me yet, but... Something doesn't add up."

            $ ignis_revealed_suspicions = True

            narrator1 "And there, he's lost in thought again. You leave him to it."

    ignis "Agh — I have no idea how we're to get Noctis to the altar now."

    $ examined_harpoon = True

    if examined_harpoon == True:

        narrator1 "A memory sparks in your mind. Smooth chrome and the humorous image of an oversized hoverboard."

        you "Hey, I don't know if this is useful, but earlier I saw this ... {i}thing{/i} in the rubble. It looked like a giant harpoon, except ... more like one you could ride."

        show ignis smile wet with dissolve

        narrator1 "At this, Ignis's face lights up."

        ignis "A Magitek device?"

        narrator1 "You nod."

        you "The wires were short-circuited, but the components seemed intact. Maybe you could use it to get him to the altar?"

        $ show_happiness = True

        pause 0.5

        $ happiness += 1

        show screen happiness_text(title="Happiness increased!")
        with dissolve
        pause 0.3
        hide screen happiness_text
        with dissolve

        ignis "Yes... yes! That's perfect!"

    else:

        you "You'll think of something, Ignis."

        you "Shame we can't just fly over there."

        ignis "Wait ... that reminds me... I saw this curious piece of technology in the square. I wonder..."

    ignis "I need to make a call."

    narrator1 "It takes him a bit of fiddling with the dial before his radio will work again, but thankfully the ordeal with Caligo doesn't seem to have broken the device completely."

    ignis "Prompto, are you there?"

    ignis "..."

    ignis "Prompto?"

    narrator1 "A bright, youthful voice comes on over the radio static."

    prompto "{i}Oh, hey!{/i}"

    prompto "{i}Reading you loud and clear, Iggy!{/i}"

    ignis "Ah, good. Listen — we've found a way to get Noct to the altar."

    if examined_harpoon == True:
        ignis "There's a busted Niff harpoon in the square. My companion here thinks you can use it to get to Noct."
    else :
        ignis "There's a busted Niff harpoon in the square. I'm thinking you could use it to get to Noct."

    ignis "With your skills, it ought to be a cakewalk."

    prompto "{i}Aw, Iggy! Didn't expect you to be so interested in a piece of tech.{/i}"

    if examined_harpoon == True:
        if happiness > 8:
            ignis "Oh, no, I can't take the credit. It's all thanks to the guard I've teamed up with. [your_pronoun_subject] the one responsible for finding it."
        else:
            ignis "Oh, no, I can't take the credit. It's all thanks to the guard I'm travelling with. [your_pronoun_subject] the one responsible for finding it."
    else:
        ignis "A gentleman has his secrets."

    prompto "{i}Heheh. Okay, cool. Should I, uh, come meet you?{/i}"

    ignis "Please. We're in a warehouse cellar just across from the Tigiano bridge."

    prompto "{i}On it. Laters!{/i}"

    narrator1 "After switching off the dial, Ignis puts the radio aside and looks back at you."

    ignis "It ought to take him another ten minutes to get here."

    narrator1 "Seems you have some more time to rest up. You settle back against the wall, trying to ignore how scratchy the brick is against your uniform."

    you "Wow, I'm still kind of stuffed after that food, or I'd ask for more."

    show ignis neutral eyesclosed wet with dissolve

    ignis "If it had been a nice seafood paella, perhaps followed by some fluffy chiffon cake, I might say the same."

    ignis "But alas, this is no paella."

    narrator1 "The dust settles in the room. It's really quite calm here, despite the chaos you know is raging up above."

    narrator1 "There's the sense of being insulated, safe against a storm."

    show ignis neutral wet with dissolve

    if you_gender_nickname == "individual":
        ignis "So, [your_name], what made an [you_gender_nickname] such as yourself join the Municipal Guard?"
    else:
        ignis "So, [your_name], what made a [you_gender_nickname] such as yourself join the Municipal Guard?"

    you "Oh, wow, okay. Big question."

    show ignis neutral openmouth wet with dissolve

    ignis "The reasons are never easy to articulate, even to oneself."

    narrator1 "You really don't consider him a stranger at this point, but you don't want to say so."

    narrator1 "So why {i}did{/i} you sign up for this job?"

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

    narrator1 "So, that's your reason."

    narrator1 "Do you want to tell Ignis?"

    menu:
        "Tell Ignis your reason":
            if motivation == "help":

                you "I wanted to help people."

                $ show_happiness = True

                pause 0.5

                $ happiness += 1

                show screen happiness_text(title="Happiness increased!")
                with dissolve
                pause 0.3
                hide screen happiness_text
                with dissolve

                ignis "That's a good thing. The world could use more like you."


            if motivation == "protect":

                you "I wanted to protect people."

                $ show_happiness = True

                pause 0.5

                $ happiness += 1

                show screen happiness_text(title="Happiness increased!")
                with dissolve
                pause 0.3
                hide screen happiness_text
                with dissolve

                ignis "That's a good thing. The world could use more like you."

            if motivation == "survival":
                you "I needed a stable income."

                ignis "Well, that makes sense, in an unstable world like this."

                ignis "While it's good to have noble reasons, if one does not have a solid foundation to support their livelihood, it's all rather pointless, in my opinion."

            if motivation == "prestige":
                you "I, well, truthfully I wanted recognition. I think I can do well in a job like this."

                ignis "You certainly have the makings of a good security representative, I'll give you that."

                ignis "But do ensure that it does not blind you to other paths."

                ignis "That's easy enough to say for any reason, I suppose. But still, bear it in mind."

                you "Sure."

            if motivation == "education":
                you "Well, I've always liked learning. I always had an interest in this line of work."

                you "I joined because ... I wanted to know more."

                $ show_happiness = True

                pause 0.5

                $ happiness += 1

                show screen happiness_text(title="Happiness increased!")
                with dissolve
                pause 0.3
                hide screen happiness_text
                with dissolve

                ignis "I'm very happy to hear that. Never stop striving to learn."

            jump openup

        "Do not tell":
            you "The reasons are never easy to articulate, huh? Yeah, I guess so."

            ignis "Absolutely no pressure, [your_name]."

            you "Heh, maybe I'll tell you someday."

            ignis "It's important you follow the path that's right for you. Whatever your motivation, you ought to stay true to it."

            narrator1 "When did this get so much like an inspirational talk? You can't hide your wry smile, and Ignis chuckles."

            jump meet_prompto

label openup:

    ignis "Thank you for sharing with me."

    you "No problem. I, uh, don't usually expect anyone to be interested."

    ignis "That's a shame."

    narrator1 "It sounds like he really means that, and it makes you feel a little warm inside."

    you "So what about you? You haven't said much about yourself."

    ignis "Apologies — I don't usually get much chance to talk about myself."

    you "Kinda like me, huh?"

    ignis "I suppose so."

    you "I mean, me, I can understand. I'm not particularly important. But you —"

    you "You're a diplomat. It's clear you're intelligent. You must have so much to say."

    ignis "Well, It's more that... "

    ignis "There's never really been a need."

    you "Well, {i}I'm{/i} interested."

    ignis "So ... talking about myself, hmm?"

    narrator1 "He doesn't seem entirely convinced. What will you say?"

    menu:
        "It's good to open up":
            you "Yeah! It's good to open up."

            you "You never know what you might miss if you don't."

            you "Getting to know people... and not just for work or the like. It can be really rewarding."

            jump ignis_opens_up

        "Well, it's important to be cautious":

            you "I mean, I don't think it's a good idea to just overshare with everyone, of course..."

            you "It's important to be cautious."

            you "But ... maybe not {i}too{/i} cautious."

            narrator1 "You sigh. You're kind of making a pig's ear of this, huh?"

            ignis "Well, in an age of such political tension ... for someone like me, that makes sense."

            jump meet_prompto


label ignis_opens_up:

    ignis "It's good to open up ... hmm ... perhaps you are right."

    ignis "Truthfully, I never chose to become a Royal Advisor. I was more ... born into the role."

    you "Really? No say at all?"

    ignis "Well, they do things a little differently in Lucis, particularly where it comes to the Royal family."

    ignis "My family line has long been in the service of the Crown."

    you "Huh — that's really interesting. I mean, I don't know much about Lucis..."

    you "Even having a king at all is a foreign concept to me..."

    you "But are you satisfied with your job?"

    ignis "..."

    ignis "I've known Prince Noctis since I was six years old."

    you "Wow, that's pretty young."

    ignis "Indeed. I care deeply about his wellbeing."

    ignis "Protecting him has always been my top priority. It's more than a mere job for me. In a way, it's all I've known..."

    ignis "But I want to see him do well. For his own sake, as much as the kingdom's."

    ignis "So yes, I'd say I'm satisfied."

    you "That's good."

    you "If it's not something you had a choice in... I'm glad you don't hate it."

    ignis "Well, there's always some things..."

    you "Like what?"

    ignis "I — I admit, I ... never actually liked cooking."

    you "Really? But you're so good at it!" with vpunch

    ignis "I suppose I've learnt enough to get by, but — if I'm perfectly honest, it was only to make the Prince happy."

    ignis "He had this particular dish he liked, from his travels in Tenebrae as a youth. The Royal Chefs couldn't recreate it, and, with Tenebrae under Imperial rule, one couldn't exactly hop over and ask them for a recipe."

    ignis "So I learned. And over time I grew to enjoy the art of cooking, I suppose."

    narrator1 "He leans in a little, eyebrow quirking upward."

    ignis "I still haven't gotten the recipe quite right, however."

    menu:
        "Compliment his dedication":

            you "Y'know, it really says a lot that you'd go to such lengths for him. You're a really dedicated person, you know that?"

            ignis "Ah ... thank you, [your_name]."

            narrator1 "Wait... have you actually managed to make him shy?"

            narrator1 "You carry on regardless."

            you "Prince Noctis is lucky to have someone like you."

            $ show_happiness = True

            pause 0.5

            $ happiness += 1

            show screen happiness_text(title="Happiness increased!")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            show ignis smile wet with dissolve

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

            show ignis neutral wet with dissolve

            $ show_happiness = True

            pause 0.5

            $ happiness -= 1

            show screen happiness_text(title="Happiness decreased")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            show ignis unimpressed openmouth wet with dissolve

            ignis "It comes with the job description. Personal preference is not exactly something that plays a part in this."

            you "That seems ... kind of a shame."

            ignis "It's only a small sacrifice in the bigger picture."

            you "Still, I don't ... I don't like the thought of it."

            ignis "It's kind of you to be so concerned, but it's really not necessary."

            show ignis neutral wet with dissolve

    jump meet_prompto

label meet_prompto:

    ignis "Well, it must be about time - I suppose we should go out and meet him."

    you "Your friend?"

    ignis "Yes."

    you "Sounds good. At the least, we can check if the mechs have moved on."

    ignis "Indeed."

    narrator1 "Ignis starts to head up to ground level."

    # hide ignis with dissolve
    show ignis at SpriteLoc2(-0.5, 1.0) with move

    narrator1 "You spend a moment looking around before you do the same, just in case you miss anything."

    narrator1 "There's not enough time to grab much, so you..."

    menu:
        "Grab a bottle of water":
            $ extra_item = "water"
        "Stuff a pack of biscuits into your pocket":
            $ extra_item = "biscuits"
        "Stop wasting time and hurry outside":
            $ extra_item = "nothing"

    jump separation
