#Scene 15
#Recovery

#contains labels:
    # altar_aftermath

# covers the days following the ceremony,




label going_home:

    scene black
    with dissolve

    centered "The cavalry arrives, and you get sent home."

    pause 0.3

    if reached_chapter_three == False:
        scene black with dissolve
        centered "{cps=15}{size=26}Chapter Three\n\n{/size}{p=0.5}{size=36}Your Move{/size}{/cps}"
    else:
        scene black with dissolve
        centered "{cps=15}{size=26}Chapter Four\n\n{/size}{p=0.5}{size=36}Your Move{/size}{/cps}"

    scene bg mc_room
    with dissolve

    narrator1 "Everything feels hollow back in your lonely little room."

    narrator1 "You did a good job, right? You {i}helped.{/i}"

    narrator1 "So why does everything feel so awful?"

    narrator1 "You potter around idly for a while, before falling into listless dreams filled with ships and explosions and lights."

    narrator1 "In your head, you save Ignis over and over again."

    narrator1 "But when you wake up in the morning, the world outside the window is still broken and in ruins."

    narrator1 "What will you do?"

    menu:
        "Report into work":
            jump report_in_post_ceremony
        "Stay at home to recuperate some more":
            jump cabin_fever
    hide screen black_overlay



label report_in_post_ceremony:

    scene bg yureilplaza
    with dissolve

    narrator1 "The Palace is abuzz with activity."

    narrator1 "People rushing to and fro, busy fixing the place up. Your ID card is scanned, but nobody really has the time to speak to you."

    narrator1 "You don't get very far before the Captain stops you."

    show captain neutral at left with dissolve

    captain "[your_name]! I thought I told you to get some rest."

    captain "Look, I appreciate that you want to help, but you were right at the centre of the storm yesterday."

    captain "You've been through a lot. We can't have you burning out."

    you "But - there has to be something I can do!"

    captain "We have more than enough people right now."

    captain "You can help us by resting up. Next week we'll need you back and at the ready."

    narrator1 "It seems your help is not needed."

    narrator1 "Time to go home."

    jump cabin_fever



label cabin_fever:

    scene black

    centered "Some days later ..."

    scene bg mc_room
    with dissolve

    friend "{i}...{/i}"

    friend "{i}[your_name], are you even listening to me?{/i}"

    you "Oh! Yeah ... sorry."

    narrator1 "You grip the phone more firmly against your ear."

    you "Listening."

    friend "{i}Right — so, like, I was asking how you were doing?{/i}"

    friend "{i}You haven't said that much since the ceremony.{/i}"

    menu:
        "I don't really want to talk about it":
            you "Look, I really don't want to talk about it right now."
            friend "Okay. I'm just concerned, is all."
            you "Yeah, I get it."
            friend "I'm here if you need me."
            you "..."
            you "Thanks."
            narrator1 "You say your goodbyes - there's no point dragging this conversation out any longer - and hang up."
        "Leave me alone!":
            you "Look, can you get off my case already?"
            you "Leave me alone!"
            friend "Sheesh, I'm only trying to help..."
            you "..."
            you "Yeah, well ..."
            narrator1 "You know your friend means well. But it doesn't stop you being irritated."
            narrator1 "And now they're annoyed, and you're annoyed, and everything's kind of awful."
            narrator1 "You hang up."
        "... It was awful":
            you "It was ... honestly, it was awful."
            narrator1 "Somehow, you can't bring yourself to talk about Ignis. So instead, you talk about the Empire."
            you "Imperial troops were everywhere ... it was chaos. And then ... the Chancellor, up near the Altar ..."
            friend "The Chancellor? As in, of Niflheim?"
            you "Yeah."
            friend "Gods ... You really were right up there, huh?"
            you "Mm."
            friend "Did you see the Oracle?"
            you "Yeah. I did."
            friend "..."
            friend "I'm so sorry."
            narrator1 "There's not really much more to say."
            narrator1 "You make your excuses, and hang up."

    if ignis_opened_up == True:
        narrator1 "So much for 'opening up to others'."
        narrator1 "Even if you did, you're not sure how they could understand, to be honest."
    else:
        narrator1 "You're not sure how they could understand, to be honest."

    narrator1 "Maybe you just need more time."

    narrator1 "Or a distraction ... something to occupy your mind."

    narrator1 "You glance to your side. The cup of tea you made earlier is stone cold."

    narrator1 "Someone once told you drinking tea made things better, in times of crisis."

    narrator1 "So far, you're not sure it's helping. But, at least it tastes good."

    menu:
        "Make another cup of tea":
            narrator1 "You potter into the kitchen, and put the kettle on."
            narrator1 "Hot tea, extra sugar, and loads of milk. It doesn't matter if it's not your usual: it'll do the trick for now."
            narrator1 "The next few minutes are spent with you slowly sipping at the hot drink, and for a while, that's enough."
            narrator1 "But only for a while."
            $ chose_tea = True

        "Stare out the window":
            narrator1 "You draw back the curtains and peek out onto the street."
            narrator1 "Below you, the world goes on as best it can. An old woman, watering her plants. A group of friends, strolling by."
            narrator1 "Neighbours helping each other fix broken masonry."
            narrator1 "There's still some smoke in the sky as the debris from the attack is cleared away. But otherwise, the sky is as it was yesterday - all calm, rosy pastels."
            narrator1 "For a while, that's enough."
            narrator1 "But only for a while."
            $ chose_window = True

        "Try to fall asleep":
            narrator1 "You lay on the bed, burying your face into the pillow."
            narrator1 "You try and try, but sleep isn't coming."
            narrator1 "So you're left staring at the patterns on the ceiling, just focussing on enjoying the soft feel of the covers beneath you."
            narrator1 "For a while, that's enough."
            narrator1 "But only for a while."
            $ chose_sleep = True

    jump next_house_decision



label next_house_decision:

    narrator1 "What now?"

    if chose_tea == True:
        menu:
            "Stare out the window":
                narrator1 "You draw back the curtains and peek out onto the street."
                narrator1 "Below you, the world goes on as best it can. An old woman, watering her plants. A group of friends, strolling by."
                narrator1 "Neighbours helping each other fix broken masonry."
                narrator1 "There's still some smoke in the sky as the debris from the attack is cleared away. But otherwise, the sky is as it was on the morning of the ceremony - all calm, rosy pastels."
                narrator1 "It kind of makes you feel sick."
                narrator1 "You turn away."
                $ chose_window = True
                jump second_house_decision
            "Try to fall asleep":
                narrator1 "You lay on the bed, burying your face into the pillow."
                narrator1 "You try and try, but sleep isn't coming."
                narrator1 "So you're left staring at the patterns on the ceiling, just focussing on enjoying the soft feel of the covers beneath you."
                narrator1 "There's too much space to think, here."
                $ chose_sleep = True
                jump second_house_decision
            "Give up":
                $ chose_tea = True
                jump give_up

    elif chose_window == True:
        menu:
            "Make another cup of tea":
                narrator1 "You potter into the kitchen, and put the kettle on."
                narrator1 "Hot tea, extra sugar, and loads of milk. It doesn't matter if it's not your usual: it'll do the trick for now."
                narrator1 "The next few minutes are spent with you slowly sipping at the hot drink."
                narrator1 "But it's not enough to calm you."
                $ chose_tea = True
                jump second_house_decision

            "Try to fall asleep":
                narrator1 "You lay on the bed, burying your face into the pillow."
                narrator1 "You try and try, but sleep isn't coming."
                narrator1 "So you're left staring at the patterns on the ceiling, just focussing on enjoying the soft feel of the covers beneath you."
                narrator1 "There's too much space to think, here."
                $ chose_sleep = True
                jump second_house_decision

            "Give up":
                $ chose_tea = True
                jump give_up

    else:
        menu:
            "Make another cup of tea":
                narrator1 "You potter into the kitchen, and put the kettle on."
                narrator1 "Hot tea, extra sugar, and loads of milk. It doesn't matter if it's not your usual: it'll do the trick for now."
                narrator1 "The next few minutes are spent with you slowly sipping at the hot drink."
                narrator1 "But it's not enough to calm you."
                $ chose_tea = True
                jump second_house_decision
            "Stare out the window":
                narrator1 "You draw back the curtains and peek out onto the street."
                narrator1 "Below you, the world goes on as best it can. An old woman, watering her plants. A group of friends, strolling by."
                narrator1 "Neighbours helping each other fix broken masonry."
                narrator1 "There's still some smoke in the sky as the debris from the attack is cleared away. But otherwise, the sky is as it was on the morning of the ceremony - all calm, rosy pastels."
                narrator1 "It kind of makes you feel sick."
                narrator1 "You turn away."
                $ chose_window = True
                jump second_house_decision
            "Give up":
                $ chose_tea = True
                jump give_up



label second_house_decision:

    narrator1 "What now?"

    if chose_tea == True and chose_window == True:
        menu:
            "Try to fall asleep":
                narrator1 "You lay on the bed, burying your face into the pillow."
                narrator1 "You try and try, but sleep isn't coming."
                narrator1 "So you're left staring at the patterns on the ceiling, just focussing on enjoying the soft feel of the covers beneath you."
                narrator1 "There's too much space to think, here."
                $ chose_sleep = True
                jump final_house_decision
            "Give up":
                jump give_up
    elif chose_sleep == True and chose_window == True:
        menu:
            "Make another cup of tea":
                narrator1 "You potter into the kitchen, and put the kettle on."
                narrator1 "Hot tea, extra sugar, and loads of milk. It doesn't matter if it's not your usual: it'll do the trick for now."
                narrator1 "The next few minutes are spent with you slowly sipping at the hot drink."
                narrator1 "But it's not enough to calm you."
                $ chose_tea = True
                jump final_house_decision
            "Give up":
                jump give_up

    elif chose_sleep == True and chose_tea == True:
        menu:
            "Stare out the window":
                narrator1 "You draw back the curtains and peek out onto the street."
                narrator1 "Below you, the world goes on as best it can. An old woman, watering her plants. A group of friends, strolling by."
                narrator1 "Neighbours helping each other fix broken masonry."
                narrator1 "There's still some smoke in the sky as the debris from the attack is cleared away. But otherwise, the sky is as it was on the morning of the ceremony - all calm, rosy pastels."
                narrator1 "It kind of makes you feel sick."
                narrator1 "You turn away."
                $ chose_window = True
                jump final_house_decision
            "Give up":
                jump give_up


label final_house_decision:

    narrator1 "Nothing's working."
    narrator1 "You're still feeling irritable."
    narrator1 "Listless."
    narrator1 "Fenced in."
    narrator1 "Yeah, it seems stupid, but there's no getting round it."
    narrator1 "You're at a loss."
    menu:
        "Give up":
            jump give_up



label give_up:
    narrator1 "You give up with a sigh."

    you "What's the use? Nothing's helping."

    you "I ... no, I need to know if Ignis is okay."

    narrator1 "You may have only met the diplomat for a brief time, but he left quite the impression."

    narrator1 "Was he doing okay?"

    you "I can't bear not knowing!"

    narrator1 "You jump up from the bed."

    narrator1 "There seems little other choice. You need to see how he's doing."

    you "Where did they say he was staying again?"

    you "Oh. The Leville." with vpunch

    narrator1 "The hotel's a half hour away, in the tourist district."

    you "Right, time to get going."

    pause 0.2

    scene black
    with Dissolve(0.5)

    pause 0.2

    jump leville


label leville:

    scene bg leville exterior
    with Dissolve(0.5)

    narrator1 "The Leville lies sandwiched between restaurants and cafés on the waterfront."

    narrator1 "It all seems so idyllic here, in this sector, where the gunfire didn't reach so intensely."

    narrator1 "There's far more people in the tourist district than you expected."

    narrator1 "Chatting in cafés, watching the boats in the bay, sipping their tea and soda and acting for all the world like nothing's wrong."

    narrator1 "Someone nearby mentions the Totomostro games have started up again already."

    narrator1 "It's only been a day, and it seems a little soon, but you suppose the attractions are sorely needed."

    narrator1 "But you've dallied outside the hotel for long enough."

    narrator1 "Without further ado, you walk into the Leville and tell the steward you're here to see Ignis."

    narrator1 "A flash of your ID and he doesn't ask questions, just tells you the room number."

    narrator1 "27. Top floor. Okay, this shouldn't be so hard. You can't back out now."

    scene bg leville corridor
    with dissolve

    show noctis neutral at center
    with dissolve

    narrator1 "Outside the room, a black-haired youth stands waiting. He turns, and you recognise him immediately."

    menu:
        "Prince Noctis?":
            you "Prince Noctis?"
            noctis "Uh ... "
            noctis "Can you, uh, not..."
            you "Huh?"
            show noctis neutral openmouth with dissolve
            noctis "You shouldn't say that so loud."
            show noctis neutral with dissolve
            you "Oh! Um, sorry. So. Is this where Ignis Scientia is staying?"
            show noctis neutral openmouth with dissolve
            noctis "Yeah, it is."
            show noctis neutral with dissolve

        "Pretend you don't recognise him":
            $ noctis_friendly = True
            you "Hi."
            show noctis neutral openmouth with dissolve
            noctis "Heya."
            show noctis neutral
            you "Is, uh, is this where Ignis Scientia is staying?"
            narrator1 "It's clear that he knows that you know he's the Prince."
            narrator1 "And he seems to appreciate your subtlety."
            show noctis smile with dissolve
            noctis "Sure is."

    show noctis neutral openmouth with dissolve
    noctis "You must be the [you_gender_nicename] he told us about. You helped him, back there."

    show noctis neutral with dissolve

    you "Yeah, I... I tried, anyways."

    narrator1 "You stare at each other a little awkwardly, because even your best efforts hadn't stopped him from being injured."

    if noctis_friendly == True:
        show noctis smile with dissolve
    else:
        show noctis neutral openmouth with dissolve

    noctis "I'll let him know you've popped by."

    hide noctis with moveoutright

    pause 1.0

    show noctis neutral at center with moveinright
    show noctis neutral openmouth

    noctis "Go on ahead."

    show noctis neutral

    you "Thanks."

    hide noctis with moveoutleft

    scene black
    with Dissolve(0.5)

    scene bg leville room
    with Dissolve(0.5)

    narrator1 "Inside, the room's colours are all muted, and a pale light shines in from the window."

    narrator1 "There's a scent like rosewater in the air. Fresh flowers on the bedside stand. A lot of them."

    show ignis silhouette blind at center with Dissolve(0.5)

    narrator1 "Ignis is sitting in one of the velvety chairs by the window."

    narrator1 "There's a cup of coffee on the table beside him, but it's long since cooled."

    narrator1 "You step forward, and he turns to meet you."

    show ignis neutral blind at center with dissolve

    narrator1 "Ignis is dressed much as you last saw him, only now he sports thick black glasses which barely cover the raw burn marks that still decorate his face."

    narrator1 "It looks so painful, and it makes you wince."

    ignis "Is that ... "

    you "It's me, [your_name]."

    show ignis smile blind with dissolve

    ignis "You came to see me?"

    you "Of course I did!"

    ignis "Oh, where are my manners? Come and sit down - I'll get some biscuits."

    ignis "I'd offer tea, but I'm not entirely comfortable handling hot water just yet."

    you "Oh - that's really okay, you don't need to worry about that."

    ignis "The biscuits are rather delicious, though."

    narrator1 "You take one out of politeness."

    you "Mm - you're right!"

    ignis "I have yet to thank your First Secretary, she's been most accommodating of us since the ceremony ended."

    narrator1 "The mere mention of the ceremony brings a brief stillness over you both."

    narrator1 "You finish eating the biscuit and force yourself out of the rut."

    you "You've ... got everything you need, right?"

    ignis "I believe so."

    you "Well, just let me know if not. I don't mind running errands. If I can get you anything - anything at all ..."

    ignis "I wouldn't want you to worry. And besides, haven't you got a lot to do, what with the recovery effort?"

    you "The Captain told me to stay at home until next week."

    you "I think right now I'd only get in their way. But I was going stir-crazy cooped up at home."

    ignis "Mm. I know the feeling."

    narrator1 "You smile, and he hears the quickness of your breath, and smiles too."

    if citizens_first == False and said_you_saved_citizens == True:

        ignis "I heard from the Palace yesterday. A number of citizens in Padore district didn't make it to safety."

        ignis "Apparently they were waiting for a guard escort who never came."

        you "..."

        ignis "You told me you had rescued them."

        $ show_happiness = True

        pause 0.5

        $ happiness -= 5

        show screen happiness_text(title="Happiness decreased a lot")
        with dissolve
        pause 0.3
        hide screen happiness_text
        with dissolve

        narrator1 "You wish the floor would swallow you up."

        you "I ... I didn't rescue them."

        ignis "So back then? You were just telling me what I wanted to hear?"

        you "I'm sorry..."

        ignis "It won't change the fact they're dead."

        narrator1 "He turns away from you, wincing as his brow tightens over burnt skin."

        if happiness > 10:

            jump ask_on_date

        else:

            jump ask_about_redo

    elif citizens_first == False and said_you_saved_citizens == False:

        ignis "I heard from the Palace yesterday. A number of citizens in Padore district didn't make it to safety."

        you "They ... they didn't?"

        you "..."

        you "I'm sorry."

        you "It's my fault, I ..."



        if happiness > 10:

            ignis "I can't tell you it's all okay. "

            ignis "But at the same time, I can't pretend it wasn't a terrible decision to have to make. You were put on the spot, and faced with a choice."

            ignis "And the Astrals know we've all had enough of that recently."

            jump ask_on_date

        else:

            jump ask_about_redo


    else:

        ignis "I heard from the Palace yesterday. "

        if happiness > 10:

            jump ask_on_date

        else:

            jump ask_about_redo



label ask_on_date:

    # if you somehow manage to get to here without completing chapter three, reroute to bad end

    if reached_chapter_three == False:

        jump ask_about_redo

    ignis "I would like that very much."

    you "You would?"

    narrator1 ""



label ask_about_redo:

    ignis "Tell me, if you had the chance to do it all again..."

    ignis "Would you?"

    narrator1 "It's clear he's thinking about more than just your decisions."

    narrator1 "What the hell happened to him at the altar?"

    narrator1 "You want to ask him, but he deserves an answer first."

    menu:
        "Yes":
            you "Yes"
            $ want_to_reset = True
        "No":
            you "No"
            $ want_to_reset = False

    ignis "I'd like to be alone now."

    narrator1 "So, it seems you're not going to get the chance to ask him what happened anyway."

    scene black
    with Dissolve(0.5)

    pause 0.5

    jump time_for_a_redo



label time_for_a_redo:

    scene bg leville exterior
    with Dissolve(0.5)

    narrator1 "Outside, the world feels smaller, starker against the pale sky."

    narrator1 "People are still talking in cafés, acting like nothing has happened."

    narrator1 "Everything seems so dissonant, and inside, your heart feels about as broken as the city does."

    scene bg leville alleyway
    with Dissolve(0.5)

    narrator1 "You wind your way down alleyways somewhat carelessly, wondering if you could have made that go any better."

    narrator1 "A gust of wind picks up, rifling through your hair."

    narrator1 "It brings a chill to the street, and a familiar prickling sensation works its way down your neck."

    you "Huh?"

    narrator1 "A small shift, that's all it takes, then ..."

    scene bg leville alleyway whiteout
    with softflash

    narrator1 "Reality seems to bend in on itself. People walking at the other end of the street simply stop, as if held in time."

    narrator1 "You're still able to move, though, and you glance about, panicked, wondering what on earth is happening."

    show ardyn neon at left with softflash
    show ardyn trashbags at left with dissolve

    ardyn "Fancy meeting you here, little mouse."

    if reached_chapter_three == False:
        you "Who are you?"
    else:
        if ardyn_affiliation == "anger" or ardyn_affiliation == "play":
            you "{i}You{/i} again!"
        else:
            you "Ch - Chancellor..."

        ardyn "Ah, such a warm welcome!"

        if ardyn_affiliation == "anger" or ardyn_affiliation == "play":
            you "What the hell have you done?"
        else:
            you "What ... what is this?"

        narrator1 "You gesture at the inverted world around you."

        narrator1 "He merely laughs."

    ardyn "I'm sure Ignis would tell you. That is, if he ever opens up to you now."

    ardyn "I imagine you're {i}dying{/i} to know how he got his scars."

    ardyn "Aw. Missed your chance?"


    show ardyn trashbags at left with softflash

    narrator1 "Suddenly, he's far too close, and he whispers in your ear." with vpunch

    ardyn "How about I make it all right again?"

    you "Wait, what do you mean?"

    ardyn "I'm going to reset everything for you."

    if want_to_reset == False:

        you "Wait - but -"

        you "What's done is done - you shouldn't mess about with things this way!"

    else:

        ardyn "After all, everyone deserves a second chance."

        you "Really? What ... how?"

    narrator1 "He smirks, and casts one hand idly up into the air."

    show soot_particles behind ardyn
    show glow_particles behind ardyn

    narrator1 "Black miasma gathers around it, growing in strength, and you can feel the energy thrum in your veins."

    narrator1 "You want to run, but some otherworldly power freezes you to the spot."

    ardyn "Better luck next time round."

    narrator1 "Then a dark haze envelops you, drawing you into its comfortable depths."

    $ reset_game_once = True

    scene black
    with Dissolve(1.5)

    jump covenant_morning
