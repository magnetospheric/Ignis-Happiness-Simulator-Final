#Scene 15
#Recovery

#contains labels:
    # altar_aftermath

# covers the days following the ceremony,




label placeholder:

    scene black

    friend "..."

    friend "[your_name], are you even listening to me?"

    scene bg mc_room
    with dissolve

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

    scene bg leville ignis room
    with dissolve


    ignis "I would like that very much."

    you "You would?"

    narrator1 ""
