#Scene 15
#Recovery

#contains labels:
    # altar_aftermath

# covers the days following the ceremony,




label placeholder:

    scene black

    narrator1 "The Captain of the Guard sends you home after that."

    scene bg mc_room
    with dissolve
    show screen black_overlay

    narrator1 "Everything feels hollow once you get back to your lonely little room."

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



report_in_post_ceremony

    scene bg mc_room
    with dissolve

    show captain neutral at left with dissolve

    captain "[your_name]! I thought I told you to get some rest."

    captain "Look, I appreciate that you want to help, but you were right at the centre of the storm yesterday."

    captain "You've been through a lot. We can't have you burning out."

    you "But - there has to be something I can do!"

    captain ""

    narrator1 "It seems your help is not needed."

    narrator1 "Time to go home."



label cabin_fever

    friend "..."

    friend "[your_name], are you even listening to me?"

    you "Oh! Yeah ... sorry."

    narrator1 "You grip the phone more firmly against your ear"

    friend "You haven't said that much since the ceremony."

    menu:
        "I don't want to talk about it":
            you "Look, I really don't want to talk about it right now."
            friend "Okay. I'm just concerned, is all."
            you "Yeah, I get it."
            friend "I'm here if you need me."
        "Leave me alone!":
            you ""
            friend "Sheesh, I'm only trying to help..."
        "... It was awful":
            you ""


    narrator1 "You hang up."

    narrator1 "You're not sure how they could understand, to be honest."

    narrator1 "Maybe you just need more time."

    narrator1 "But it's already been three days."

    narrator1 "You spent the first two helping out with the relief effort, before they sent you home to recuperate."

    menu:
        "Make another cup of tea":
            $ chose_tea = true
        "Stare out the window":
            $ chose_window = true
        "Try to fall asleep":
            $ chose_sleep = true
            narrator1 "You lay back on the pillow"

            jump next_house_decision



label next_house_decision:

    if chose_tea = true:
        menu:
            "Stare out the window":
                $ chose_window = true
                jump second_house_decision
            "Try to fall asleep":
                $ chose_sleep = true
                narrator1 "You lay back on the pillow"
                jump second_house_decision
            "Give up":
                $ chose_tea = true
                jump give_up
    elif chose_window = true:
        menu:
            "Make another cup of tea":
                $ chose_tea = true
                jump second_house_decision
            "Try to fall asleep":
                $ chose_sleep = true
                narrator1 "You lay back on the pillow"
                jump second_house_decision
            "Give up":
                $ chose_tea = true
                jump give_up
    else:
        menu:
            "Make another cup of tea":
                $ chose_tea = true
                jump second_house_decision
            "Stare out the window":
                $ chose_window = true
                jump second_house_decision
            "Give up":
                $ chose_tea = true
                jump give_up



label second_house_decision:

    if chose_tea == True && chose_window == True:
        menu:
            "Try to fall asleep":
                $ chose_sleep = true
                narrator1 "You lay back on the pillow"
                jump final_house_decision
            "Give up":
                $ chose_tea = true
                jump give_up



label final_house_decision:

    narrator1 "Nothing's working"
    menu:
        "Give up":
            $ chose_tea = true
            jump give_up

label give_up:
    narrator1 "You give up with a sigh."

    you "What's the use? Nothing's helping."

    narrator1 "But more importantly, was Ignis okay?"

    narrator1 "You may have only met the diplomat for a brief day, but he left quite the impression."

    narrator1 "Was he happy? Was he doing okay?"

    you "I can't bear not knowing!"

    narrator1 "There seems little other choice. You need to see how he's doing."

    narrator1 "You jump up from the bed."

    you "Where did they say he was staying again?"

    you "Oh. The Leville."

    narrator1 "The hotel's a half hour away, in the tourist district."



label leville:

    scene bg leville exterior
    with dissolve

    scene bg leville hallway
    with dissolve

    show noctis at center
    with dissolve

    narrator1 "Outside the room, a black-haired youth stands waiting. He turns, and you recognise him as the Prince."

    you "Is, uh, is this where Ignis Scientia is staying?"

    narrator1 "You don't refer to the Prince by name."

    narrator1 "He must know that you know, because he smiles wryly."

    noctis "Yeah, it is."

    noctis "You must be the [you_gender_nicename] he told us about. You helped him, back there."

    you "Yeah, I... I tried, anyways."

    narrator1 "You stare at each other a little awkwardly, because even your best efforts hadn't stopped him from being injured."

    noctis "I'll let him know you've popped by."

    hide noctis with dissolve

    pause 0.5

    show noctis neutral at center with moveinright

    noctis "Go on ahead."

    you "Thanks."

    scene bg leville ignis room
    with dissolve

    show ignis silhouette blind at center with dissolve

    narrator1 "Ignis is sitting in one of the velvety chairs by the window."

    narrator1 "There's a cup of coffee on the table beside him, but it's long since cooled."

    narrator1 "You step forward, and he turns to meet you."

    show ignis neutral blind at center with dissolve

    narrator1 "Ignis is dressed much as you last saw him, only now he sports thick black glasses which barely cover the raw burn marks that still decorate his face."

    narrator1 "It still looks so painful, and it makes you wince."

    ignis "Is that ... "

    you "It's me, [your_name]."

    show ignis smile blind with dissolve

    ignis "You came to see me?"

    you "Of course I did!"

    ignis "Oh, where are my manners? Come and sit down - I'll get some biscuits."

    ignis "I'd offer tea, but I'm not entirely comfortable with hot water just yet."

    you "Oh - that's really okay, you don't need to worry about that."

    ignis "The biscuits are rather delicious, though."

    narrator1 "You take one out of politeness."

    you "Mm - you're right! Pretty good."

    ignis "I have yet to thank your First Secretary, she's been most accommodating of us since the ceremony ended."

    narrator1 "The mere mention of the ceremony brings a short stillness over you both."

    narrator1 "You finish eating the biscuit and force yourself out of the rut."

    you "You've ... got everything you need, right?"

    ignis "I believe so."

    you "Well, just let me know if not. I don't mind running errands."

    ignis "I wouldn't want you to worry - haven't you got a lot to do, with the recovery efforts?"

    you "Captain told me to stay at home until I get a medical assessment."

    you "I was going stir-crazy cooped up at home."

    ignis "Mm. I know the feeling."

    narrator1 "You smile, and he hears you, smiling too."

    if citizens_first == False && said_you_saved_citizens == True:

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

    else:

        ignis "I heard from the Palace yesterday. "

    ignis "I would like that very much."

    you "You would?"

    narrator1 ""
