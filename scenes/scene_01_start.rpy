# use this to test flashlight setup
label startn:

    #starting variables

    $ ignis_name = "Stranger"
    $ your_name = "You"

    #shows the first background
    scene bg altissia_alleyway

    #shows the first character
    show ignis neutral
    with dissolve

    "Altissia, on the day of the Covenant. Everything is going to hell."

    ignis "I've run into a bit of trouble. Would you care to help me?"

    ignis "Look around this room and see if there's anything useful."

    call screen flashlight

# The game starts here.
label start:

    #starting variables

    $ ignis_name = "Stranger"
    $ your_name = "You"

    #shows the first background
    scene bg altissia_alleyway

    #shows the first character
    show ignis neutral
    with dissolve

    # These display lines of dialogue.

    "Altissia, on the day of the Covenant. Everything is going to hell."

    "You've been stationed near Yureil Plaza."

    altissianguard "Morning. Please present your identification."

    "You show her your ID card."

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
        "Female":
            $ your_gender= "female"
            $ your_pronoun_subject= "she"
            $ your_pronoun_possessive = "hers"
            $ your_pronoun_object = "her"
        "Non-Binary":
            $ your_gender= "non-binary"
            $ your_pronoun_subject= "they"
            $ your_pronoun_possessive = "theirs"
            $ your_pronoun_object = "their"

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

    "When you report in, you notice your commander is accompanied by a stranger."

    "He's tall, slim, and all things considered, rather attractive indeed."

    you "Hi."

    ignis "I'm Ignis, by the way. Nice to meet you."

    $ ignis_name = "Ignis"

    "You introduce yourself."

    "He nods as you speak your name."

    ignis "[your_name]. That's a lovely name."

    ignis "I've run into a bit of trouble. Would you care to help me?"

    ignis "Look around this room and see if there's anything useful."

    # $ mouse_visible = False

    call screen flashlight

    # $ mouse_visible = True

    hide ignis neutral
    with dissolve

    #return to title screen
    return
