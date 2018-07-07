#Scene 15
#Recovery

#contains labels:
    # altar_aftermath

# covers the days following the ceremony, and asking ignis out




label going_home:


    hide screen black_overlay_light
    hide screen black_overlay

    $ quick_menu = False

    scene black with Dissolve(1.0)

    stop music fadeout 6.0
    centered "The cavalry arrives, and you get sent home."

    pause 0.3

    if reached_chapter_three == False:
        scene black with dissolve
        centered "{cps=15}{size=26}Chapter Three\n\n{/size}{p=0.5}{size=36}Your Move{/size}{/cps}"
    else:
        scene black with dissolve
        centered "{cps=15}{size=26}Chapter Four\n\n{/size}{p=0.5}{size=36}Your Move{/size}{/cps}"

    $ renpy.music.set_volume(0.1, delay=0, channel='ambient')
    play ambient undercurrent fadein 1.0

    scene bg mc_room with Dissolve(1.5)

    $ quick_menu = True

    narrator1 "Everything feels hollow back in your lonely little room."

    narrator1 "You did a good job, right? You {i}helped.{/i}"

    scene black
    centered "So why does everything feel so awful?"
    scene bg mc_room

    stop ambient fadeout 0.5
    play music home_blues fadein 0.5
    $ renpy.music.set_volume(0.4, delay=5, channel='ambient')

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

    scene black with Dissolve(1.5)

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

    you "I ... no, I know what I need to do."

    you "I need to know if Ignis is okay."

    narrator1 "You may have only met the diplomat for a brief time, but he left quite the impression."

    narrator1 "Was he doing okay?"

    you "I can't bear not knowing!"

    narrator1 "You jump up from the bed."

    narrator1 "There seems little other choice. You need to see how he's doing."

    you "Where did they say he was staying again?"

    you "Oh. The Leville." with vpunch

    narrator1 "The hotel's a half hour away, in the tourist district."

    you "Right, time to get going."

    stop music fadeout 2.286

    pause 0.2

    scene black
    with Dissolve(1.0)

    pause 0.2

    jump leville


label leville:

    play ambient morning_coffee1 fadein 2.286

    scene bg leville exterior
    with Dissolve(1.0)

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

        "Don't make a big deal about recognising him":
            $ noctis_friendly = True
            you "Hi."
            show noctis neutral openmouth with dissolve
            noctis "Heya."
            show noctis neutral
            you "Is, uh, is this where Ignis Scientia is staying?"
            narrator1 "It's clear that {i}he{/i} knows that {i}you{/i} know he's the Prince."
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

    pause 2.0

    show noctis neutral at center with moveinright
    show noctis neutral openmouth

    noctis "Go on ahead."

    show noctis neutral

    you "Thanks."


    scene black
    hide noctis
    with Dissolve(1.0)

    scene bg leville room
    with Dissolve(1.0)

    narrator1 "Inside, the room's colours are all muted, and a pale light shines in from the window."

    narrator1 "There's a scent like rosewater in the air. Fresh flowers on the bedside stand. A lot of them."

    show ignis silhouette blind at center with Dissolve(0.5)

    narrator1 "Ignis is sitting in one of the velvety chairs by the window."

    narrator1 "There's a cup of coffee on the table beside him, but it's long since cooled."

    narrator1 "You step forward, and he turns to meet you."

    show ignis neutral blind at center with dissolve

    narrator1 "Ignis is dressed much as you last saw him, only now he sports thick black glasses which barely cover the raw burn marks that still decorate his face."

    narrator1 "It looks so painful, and it makes you wince."

    show ignis neutral openmouth blind
    ignis "Is that ... "
    show ignis neutral blind

    pause 0.3

    you "It's me, [your_name]."

    show ignis smile blind with dissolve
    ignis "You came to see me?"

    you "Of course I did!"

    show ignis neutral openmouth blind
    ignis "Oh, where are my manners? Come and sit down - I'll get some biscuits."
    ignis "I'd offer tea, but I'm not entirely comfortable handling hot water just yet."
    show ignis smile blind

    you "Oh - that's really okay, you don't need to worry about that."

    show ignis neutral openmouth blind
    ignis "The biscuits are rather delicious, though."
    show ignis smile blind

    narrator1 "You take one out of politeness."

    you "Mm - you're right!"

    show ignis neutral openmouth blind
    ignis "I have yet to thank your First Secretary, she's been most accommodating of us since the ceremony ended."
    show ignis neutral blind

    narrator1 "The mere mention of the ceremony brings a brief stillness over you both."

    narrator1 "You finish eating the biscuit and force yourself out of the rut."

    you "You've ... got everything you need, right?"

    show ignis neutral openmouth blind
    ignis "I believe so."
    show ignis neutral blind

    you "Well, just let me know if not. I don't mind running errands. If I can get you anything - anything at all ..."

    show ignis neutral openmouth blind
    ignis "I wouldn't want you to worry. And besides, haven't you got a lot to do, what with the recovery effort?"
    show ignis neutral blind

    you "The Captain told me to stay at home until next week."

    you "I think right now I'd only get in their way. But I was going stir-crazy cooped up at home."

    show ignis neutral openmouth blind
    ignis "Mm. I know the feeling."
    show ignis smile blind

    narrator1 "You smile, and he hears the quickness of your breath, and smiles too."

    if citizens_first == False and said_you_saved_citizens == True:

        narrator1 "That smile changes, however, in a single second."

        show ignis neutral openmouth blind with dissolve
        ignis "I heard from the Palace yesterday. A number of citizens in Padore district didn't make it to safety."
        show ignis unimpressed openmouth blind with dissolve
        ignis "Apparently they were waiting for a guard escort who never came."
        show ignis unimpressed blind

        you "..."

        show ignis unimpressed openmouth blind
        ignis "You told me you had rescued them."
        show ignis unimpressed blind

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

        show ignis unimpressed openmouth blind
        ignis "So back then? You were just telling me what I wanted to hear?"
        show ignis unimpressed blind

        you "I'm sorry..."

        show ignis unimpressed openmouth blind
        ignis "It won't change the fact they're dead."
        show ignis unimpressed blind

        narrator1 "He turns away from you, wincing as his brow tightens over burnt skin."

        if happiness > 10:

            jump ask_on_date

        else:

            jump ask_about_redo

    elif citizens_first == False and said_you_saved_citizens == False:

        show ignis neutral openmouth blind
        ignis "I heard from the Palace yesterday. A number of citizens in Padore district didn't make it to safety."
        show ignis neutral blind

        $ show_happiness = True

        pause 0.5

        $ happiness -= 2

        show screen happiness_text(title="Happiness decreased a lot")
        with dissolve
        pause 0.3
        hide screen happiness_text
        with dissolve

        you "They ... they didn't?"

        you "..."

        you "I'm sorry."

        you "It's my fault, I ..."

        narrator1 "But you don't know what to say."

        if happiness > 10:

            show ignis neutral openmouth blind
            ignis "I can't tell you it's all okay."
            ignis "But at the same time, I can't pretend it wasn't a terrible decision to have to make. You were put on the spot, and faced with a choice."
            ignis "And the Astrals know we've all had enough of that recently."
            show ignis neutral blind

            jump ask_on_date

        else:

            jump ask_about_redo

    else:

        show ignis neutral openmouth blind
        ignis "I heard from the Palace yesterday. All citizens in Padore district made it to safety."
        show ignis smile blind

        ignis "..."

        $ show_happiness = True

        pause 0.5

        $ happiness += 1

        show screen happiness_text(title="Happiness increased")
        with dissolve
        pause 0.3
        hide screen happiness_text
        with dissolve

        show ignis neutral openmouth blind
        ignis "Thank you. Your efforts went well-rewarded."
        show ignis smile blind

        narrator1 "You bite back a retort, because how can he say such a thing when he's standing in front of you, injured like this?"

        you "But you..."

        show ignis neutral openmouth blind
        ignis "Those citizens will sleep well with their families tonight because of you."
        ignis "And that's no small thing."
        show ignis smile blind

        you "I, ah ..."

        you "Thanks."

        if happiness > 10:

            jump ask_on_date

        else:

            jump ask_about_redo



label ask_on_date:

    # if you somehow manage to get to here without completing chapter three, reroute to bad end

    if reached_chapter_three == False:

        jump ask_about_redo

    you "Hey, Ignis, I was wondering something."

    show ignis neutral openmouth blind
    ignis "Yes?"
    show ignis smile blind

    you "How would you like to get out of here for a bit?"

    show ignis neutral openmouth blind
    ignis "Are you offering to take me out?"
    show ignis smile blind

    you "I, uh ... yes. "

    show ignis neutral openmouth blind
    ignis "I would like that very much."
    show ignis smile blind with dissolve

    you "You would?"

    narrator1 "Ignis nods."

    show ignis neutral openmouth blind
    ignis "But I can't be seen outdoors like this! I must, ah ... sort my hair, for a start."
    show ignis smile blind with dissolve

    narrator1 "You smile. He's a little flustered, and it's really quite adorable."

    you "Well, shall we say ... meet at Listro Park, at eight?"

    show ignis neutral openmouth blind
    ignis "That sounds marvellous."
    show ignis smile blind with dissolve

    narrator1 "You make your farewells, and leave the hotel room."

    $ show_happiness = False

    hide ignis
    show bg leville exterior
    with Dissolve(1.0)

    narrator1 "You're giddy as you walk on through the streets. Mostly at the prospect of getting to spend more time with Ignis, but it's not just that."

    narrator1 "The way he smiled ... it's clear you mean a lot to him, too."

    narrator1 "You smile to yourself. You can't wait for the evening to fall."

    jump waitingforignis



label ask_about_redo:

    ignis "Tell me, if you had the chance to do it all again..."

    ignis "Would you?"

    narrator1 "It's clear he's thinking about more than just your decisions."

    narrator1 "What the hell happened to him at the altar?"

    narrator1 "You want to ask him, but he deserves an answer first."

    menu:
        "Yes":
            you "Yes."
            you "I ... I believe in second chances."
            you "I want to make things right."
            $ want_to_reset = True
        "No":
            you "No."
            you "We shouldn't change fate like that."
            you "I'd be a coward if I didn't now live with my decisions..."
            $ want_to_reset = False

    ignis "I see."

    pause 1.0

    ignis "I'd like to be alone now."

    narrator1 "So, it seems you're not going to get the chance to ask him what happened anyway."

    scene black
    with Dissolve(0.5)

    if examined_harpoon == True and noctis_friendly == True:

        scene bg leville corridor
        show noctis neutral at center
        with dissolve

        show noctis neutral openmouth with dissolve
        noctis "Everything okay?"
        show noctis neutral with dissolve

        you "Ah ..."

        you "Not really."

        show noctis neutral openmouth
        noctis "He's had a real rough time of it. He just needs a bit longer."
        show noctis neutral

        you "No, I think I messed up."

        show noctis neutral openmouth
        noctis "Look, we all kind of feel like that right now."
        noctis "Don't be too hard on yourself, okay?"
        show noctis neutral

        you "..."

        you "I'll try..."

        show noctis neutral openmouth
        noctis "Hey, wanna get some fresh air?"
        show noctis neutral

        you "Really?"

        show noctis neutral openmouth
        noctis "Yeah, why not?"
        show noctis smile with dissolve

        you "Okay!"

        scene bg leville exterior
        with Dissolve(0.5)

        narrator1 "When you're outside the Leville, Noctis strolls down the promenade with you."

        narrator1 "It seems only a few years separate Noctis and Ignis, but the young Prince's posture is so radically different."

        narrator1 "He still seems like a child; one who's been told to grow up too fast but can't quite seem to catch up."

        narrator1 "This makes you feel kind of melancholy, but hey, at least he's outdoors enjoying the sunshine for a bit."

        show noctis smile with dissolve

        if deactivated_generator == True:
            narrator1 "Seems you're walking too slow - Noctis turns and pulls you along, laughing."

            noctis "C'mon, I wanna show you something!"

            narrator1 "It's when you reach the pier that he stops, and points into the distance."

            noctis "Over there, across the lagoon..."

            narrator1 "You follow the direction he's pointing in, and see an open space decorated with flowers."

            noctis "They say the Empire's ships had difficulty retreating. So, that meadow didn't get bombed."

            noctis "It was where the wedding reception was going to take place."

            narrator1 "You don't ask him to elaborate. It's clear he means him and Lady Lunafreya."

            show noctis neutral openmouth
            noctis "I heard you were responsible for sabotaging the dropships."
            show noctis neutral

            you "I ... yeah."

            show noctis smile with dissolve

            noctis "Thanks."

            you "You can get a boat out to there, if you want."

            show noctis neutral openmouth
            noctis "I can?"
            show noctis neutral

            you "Sure! The gondoliers down by the port'd be happy to take you."

            show noctis smile with dissolve

            noctis "Cool. That'd mean a lot to me."

            show noctis neutral openmouth
            noctis "But, uh... that's not all."
            noctis "Iggy told me you did a lot more than just shutting down a generator."
            show noctis neutral

        else:
            show noctis neutral openmouth
            noctis "I wanna thank you, [your_name]."
            noctis "Ignis told us all what you did for us."
            show noctis neutral

        you "Oh, I..."

        show noctis neutral openmouth
        noctis "Wait, hear me out, 'kay?"
        noctis "I wouldn't have even reached the altar if it wasn't for your crazy idea with the harpoon."
        noctis "It gave me enough time to receive the blessing -"
        show noctis neutral

        narrator1 "He breaks off. It seems the memory that follows is too painful to think about."

        you "I'm ... glad I could help. I just wish I could have done more."

        show noctis neutral openmouth
        noctis "And you saved Ignis!"
        show noctis neutral

        narrator1 "Noctis's bottom lip quivers, then he all but throws himself on you, surrounding you in an intense hug."

        $ hugged_noctis = True

        narrator1 "He's almost shivering with emotion - gods, he must have been so scared Ignis would die - and it brings back once again how underprepared for this war the poor kid is."

        narrator1 "You hug him back tightly, patting his hair, soothing him."

        you "It's not a problem. I'd save him a thousand times if I could."

        narrator1 "Noctis eventually breaks from the hug."

        show noctis neutral openmouth
        noctis "Same."
        show noctis neutral

        you "Good luck on the road ahead."

        narrator1 "He nods."

        you "I'll hold down the fort here, fix things up a bit."

        you "So if you guys ever come back here, you can have a proper holiday."

        show noctis smile with dissolve

        noctis "I'll keep that in mind."

        narrator1 "He shrugs the stiffness out of his shoulders and looks around."

        noctis "I should get back to the others. Don't wanna leave Iggy alone too long."

        narrator1 "You smile."

        you "I'm glad he's got you."

        narrator1 "Noctis leaves you with a parting touch on your shoulder."

        hide noctis with dissolve

        narrator1 "You've earned the gratitude of a prince, which counts for something."

    pause 0.5

    jump time_for_a_redo



label time_for_a_redo:

    scene bg leville exterior
    with Dissolve(0.5)

    if hugged_noctis == True:
        narrator1 "But, now that you're on your own again, the world feels smaller, starker against the pale sky."
        narrator1 "People are still talking in cafés, acting like nothing has happened."
        narrator1 "Everything seems so dissonant, and you wonder how it can be made right again."
    else:
        narrator1 "Outside, the world feels smaller, starker against the pale sky."

        narrator1 "People are still talking in cafés, acting like nothing has happened."

        narrator1 "Everything seems so dissonant, and inside, your heart feels about as broken as the city does."

    # max ravus happiness is 7, if you get 6 or above you get this scene
    if ravus_happiness >= 6 and hugged_noctis == False:

        $ befriended_ravus = True

        show bg listropark with Dissolve(1.5)

        narrator1 "You don't know what to do with yourself after that, and so you walk around the city, listlessly checking the shops and attractions without much rhyme or reason."

        narrator1 "You're just musing on this when you see a familiar figure down a back-alley by Listro Park."

        show ravus neutral at right with Dissolve(0.5)

        you "{i}Ravus?{/i} What are you doing here?"
        narrator1 "Your voice is barely above a hiss, and your urgency cuts through to him, because he frowns."

        show ravus neutral openmouth
        ravus "Hush!"
        show ravus neutral

        narrator1 "He obviously doesn't want to attract attention, so you rush into the shadows and confront him quietly."

        you "{i}What are you doing here?{/i}"
        you "{i}What if th{/i}"

        narrator1 "You pout."

        you "I kind of feel like I should report you to the other guards, what with my job and all..."

        narrator1 "It shouldn't be possible for someone like Ravus to look any paler, but somehow he manages it."

        show ravus neutral openmouth
        ravus "I'm not here to cause any trouble."
        show ravus neutral

        you "Why {i}are{/i} you here, then?"

        you "I'm not trying to be rude, I really want to know."

        show ravus neutral openmouth
        ravus "Well, for you, I suppose my presence is a matter of national security, so I shall tell you."
        show ravus neutral

        narrator1 "You smile."
        narrator1 "You get the feeling he {i}let{/i} you see him."

        show ravus neutral openmouth
        ravus "I had to return to ... make sure they observed the proper burial rituals for Luna."
        ravus "We're Tenebraean. I have small confidence that Altissia will conduct things correctly."
        show ravus neutral

        narrator1 "You pause for thought. Ravus looks so sincere, as much as he did at the altar, and you don't doubt the validity of his reason."

        you "I see."

        narrator1 "You're busy studying him now, because you've realised he looks kind of ... tired."

        you "Hey, um ... You look a little parched. I could - I could bring you something to drink, if you like?"

        you "Since it's probably better you avoid being seen."

        show ravus smile with dissolve

        ravus "That is unneccesarily kind of you..."

        narrator1 "You're pretty sure he's trying to be grateful, so you smile, and dart off into the plaza."

        narrator1 "Moments later you return with a couple of iced drinks."

        show ravus neutral openmouth
        ravus "..."
        ravus "I can't believe you got me one with a little umbrella in it..."
        show ravus neutral

        you "It's a tourist zone, what do you expect?"

        narrator1 "You laugh as he picks at the straw. This is such an odd meeting. But then, the last few days have been so far out of the ordinary that you simply run with it."

        narrator1 "Ravus sits down to drink, his long, ornate coat scraping on dust and debris on a forgotten doorstep."

        narrator1 "You join him."

        you "So, did they get the rituals right?"

        narrator1 "Ravus sighs."

        show ravus neutral openmouth
        ravus "I never got that far."
        show ravus neutral

        you "You know, if you tell me what needs doing, I can try and make sure she's treated right."

        show ravus smile with dissolve

        ravus "I couldn't possibly expect you to -"

        you "Oh, come on. I'm not gonna break my word."

        narrator1 "He peers at you intently. After a moment he relaxes, and seems satisfied."

        show ravus neutral openmouth
        ravus "Very well."
        ravus "They should be using consecrated oil for the embalming, before the burial takes place. Piztalan oil, if you can obtain it. And - "
        ravus "The casket ought to be filled with sylleblossoms, although I expect they've doubtless done that already."
        ravus "Then there's the Oracle's Rites. I beg of you, don't let them forget those."
        ravus "Your city library probably has a copy of the Book of the Messengers ... you can find the petitions in there."
        show ravus neutral

        narrator1 "You nod."

        narrator1 "It's a lot to keep in mind, but you will do your best to get it right."

        you "Understood."

        narrator1 "Ravus takes a long swig of his soda - again, looking so dissonant in the act, dressed the way he is, crouched on a back-alley step like that."

        show ravus smile
        ravus "Good."

        narrator1 "Then he stands."

        narrator1 "You rise as well, and he places a hand on your shoulder, icy blue eyes staring deeply into yours."

        show ravus neutral openmouth
        ravus "I am grateful, loath as I am to admit I can't do this alone."
        show ravus neutral

        narrator1 "He pauses, and sighs."

        show ravus neutral openmouth
        ravus "I must return. I ..."
        show ravus neutral

        narrator1 "He seems scared. It's like an invisible guillotine is hanging over his head."

        you "You don't have to go back to Niflheim, you know."

        narrator1 "This makes him snort."

        show ravus neutral openmouth
        ravus "And what - confess to the Lucians? To your fellow countrymen in Altissia?"
        ravus "Even if I were not a military official - {i}ex-{/i}military offical - I would be tried as a war criminal nonetheless."
        show ravus neutral

        you "But maybe -"

        narrator1 "Ravus shakes his head."

        show ravus neutral openmouth
        ravus "It's where I belong. And besides ... everything is nearly come to an end."
        ravus "Treat this world well."
        show ravus smile with dissolve

        narrator1 "His grip on your shoulder tightens momentarily, then he smiles, and leaves you."

        hide ravus with Dissolve(1.0)
        narrator1 "You watch him head off into the shadows."

        narrator1 "There's been many people messed up from this war, and Ravus is no exception."

        narrator1 "You sigh. It's time to go home. You have some phone calls to make now."

    stop ambient fadeout 4.0

    jump ardyn_interrupts



label ardyn_interrupts:

    scene bg leville alleyway
    with Dissolve(0.5)

    if hugged_noctis == True:
        narrator1 "You wind your way down alleyways somewhat carelessly, wondering if you could have made things go any better between you and Ignis."
    elif befriended_ravus = =True:
        narrator1 "You wind your way down alleyways somewhat carelessly, wondering if you could have done anything differently."
    else:
        narrator1 "You wind your way down alleyways somewhat carelessly, wondering if you could have made that go any better."

    play music curious_encounter fadein 8.286
    narrator1 "A gust of wind picks up, rifling through your hair."

    narrator1 "It brings a chill to the street, and a familiar prickling sensation works its way down your neck."

    you "Huh?"

    narrator1 "Something is wrong."

    narrator1 "A small shift, that's all it takes, then ..."

    scene bg leville alleyway whiteout
    with softflash

    narrator1 "Reality seems to bend in on itself. People walking at the other end of the street simply stop, as if held in time."

    narrator1 "You're still able to move, though, and you glance about, panicked, wondering what on earth is happening."

    show ardyn neon at left with softflash
    show ardyn trashbags at left with dissolve

    ardyn "Fancy meeting you here, little mouse."

    if reset_game_once == True:
        you "No... No, come on! Don't do this!"
    elif reached_chapter_three == False:
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

    if reset_game_once == True:
        ardyn "Don't do what now? There's no reason to fear."
        ardyn "That is, unless you failed somewhere along the way..."
    else:
        ardyn "I'm sure Ignis would tell you. That is, if he ever opens up to you now."

        ardyn "I imagine you're {i}dying{/i} to know how he really got his scars."

    ardyn "Aw. Missed your chance?"

    if hugged_noctis == True:
        ardyn "You certainly didn't waste any time with the Prince, hmm?"
    elif befriended_ravus == True:
        ardyn "You certainly didn't waste any time with that traitorous son of Tenebrae, hmm?"

    show ardyn trashbags at left with softflash

    narrator1 "Suddenly, he's far too close, and he whispers in your ear." with vpunch

    ardyn "How about I make it all right again?"

    if reset_game_once == True:
        you "Come on, don't do this!"
    else:
        you "Wait, what do you mean?"

    ardyn "I'm going to reset everything for you."

    if reset_game_once == True:
        you "No!"

        ardyn "Come now, everyone deserves a second chance. Or, in your case, a third. Or a fourth."
        
        ardyn "My, how long will you keep doing this for?"

    elif want_to_reset == False:

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
