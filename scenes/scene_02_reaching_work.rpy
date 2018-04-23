#Scene 02
#Reaching work

#contains labels:
    # to_work
    # setname
    # confirmname
    # setgender
    # confirmgender
    # after_user_name_set

# covers reaching work, and mc options setup


label found:

    hide screen keys

    you "Ah!"

    you "Found 'em!"

    jump to_work

label to_work:
    #shows the first background
    scene bg mc_home

    narrator1 "You race through the streets, shrugging on your coat."
    narrator1 "You've been working as a Municipal Guard for nigh on two months now. A good job with decent pay, and as far as jobs go, you enjoy it."

    scene bg altissian_skyline

    narrator1 "The air is colder than the soft skies would suggest. Although there's hardly a breeze to be felt, the cold cuts right through your coat."

    narrator1 "There's a low hum in the streets. People are up and about, but more hushed than normal. They're feeling the anticipation as keenly as you are."

    scene bg yureilplaza

    narrator1 "Today, you've been stationed near Yureil Plaza. When you arrive at the gates, the guard on duty greets you with a salute."

    show altissianguard neutral at left
    with dissolve

    altissianguard "Morning. Please present your identification."

    narrator1 "You show him your ID card."

    jump setname

label setname:

    python:
        your_name = renpy.input("Type in your name.")
        your_name = your_name.strip()
        if not your_name:
            your_name = "Ilia"
    "[your_name], is that right?"

    jump confirmname

label confirmname:

    menu:
        "Yes":
            jump setgender
        "No":
            $ your_name = ""
            jump setname

label setgender:

    "Select your gender:"
    menu:
        "Male":
            $ your_gender= "male"
            $ your_pronoun_subject= "he"
            $ your_pronoun_possessive = "his"
            $ your_pronoun_object = "him"
            $ you_gender_nicename = "man"
            $ you_gender_nickname = "lad"
        "Female":
            $ your_gender= "female"
            $ your_pronoun_subject= "she"
            $ your_pronoun_possessive = "hers"
            $ your_pronoun_object = "her"
            $ you_gender_nicename = "woman"
            $ you_gender_nickname = "lass"
        "Non-Binary":
            $ your_gender= "non-binary"
            $ your_pronoun_subject= "they"
            $ your_pronoun_possessive = "theirs"
            $ your_pronoun_object = "their"
            $ you_gender_nicename = "person"
            $ you_gender_nickname = "individual"

    "[your_gender], is that right?"

    jump confirmgender

label confirmgender:

    menu:
        "Yes":
            jump after_user_name_set
        "No":
            $ your_name = ""
            jump setgender

label after_user_name_set:

    narrator1 "The guard checks over your ID."

    show altissianguard smile

    altissianguard "All checks out fine, Guard [your_name]. Please proceed."

    you "Thank you."

    hide altissianguard
    with dissolve

    jump first_conversation
