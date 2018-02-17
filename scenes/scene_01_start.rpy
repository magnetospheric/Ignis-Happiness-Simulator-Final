#starting scene
#contains labels:
    # start
    # mc_room
    # to_work
    # setname
    # confirmname
    # setgender
    # confirmgender
    # after_user_name_set
    # first_conversation

# covers scene setup, point&click tutorial, mc options setup, and first coversation with ignis


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

    # start scene needs to introduce the hunting-around mechanic for later
    # maybe protag is looking for their keys or something that'll be useful later

    #starting variables
    $ ignis_name = "Stranger"
    $ your_name = "You"

    #scene dawns on an overview of altissia
    #scene bg altissia skyline

    "Altissia, on the day of the Covenant."

    "The atmosphere is tense. You can feel it around you, thick as syrup."

    "Today is the day that the Oracle, Lady Lunafreya, summons a goddess."
    "Leviathan. The stuff of legends."
    "You remember the stories. The prayers. You never thought you would see it in the flesh."

    "An important day, indeed."

    "So it really doesn't help that today, of all days, you are late to work."

    jump mc_room

label mc_room:

    # scene bg mc_room

    you "Ah, where did I put my keys?"

    # look up to left
    # look to right
    # main room view

    you "Y'know, it would be {i}really{/i} useful if I could just ... find them ..."

    # this will teach you the 'find things' mechanic
    show screen infobubble(who="meeee", what="yoouuuuu")

    # call screen focus
    # call screen flashlight
    # imagebutton "continue" xpos 300 ypos 300 action Return()

    you "Found 'em!"

    jump to_work

label to_work:
    #shows the first background
    scene bg altissia_alleyway

    "You race through the streets, shrugging on your jacket."
    "You've been working as a Municipal Guard for nigh on two months now. A good job with decent pay, and as far as jobs go, you enjoy it. So far."

    #scene bg yureilplazagates

    "Today, you've been stationed near Yureil Plaza. When you arrive at the gates, the guard on duty greets you with a salute."

    show altissianguard at left
    with dissolve

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

    altissianguard "All checks out fine, Guard [your_name]. Please proceed."

    you "Thank you."

    hide altissianguard
    with dissolve

    jump first_conversation

label first_conversation:

    #scene bg yureilplazasteps

    "Up the pale marble steps to the plaza entrance now. Yureil Mansion is grand and decked with flags, red and gold fabric that's dampened in the gatheing rain."
    "Usually, you think it looks overbearing, but today, it seems solemn, more like a tomb. It's not an inviting omen."

    #show commander left in conversation
    #scene yureilplazainteriorcorridor
    show captain neutral at left
    with dissolve

    "When you report in, you notice the Captain of the Guard is accompanied by a stranger."

    hide captain
    #show ignis left looking to the side
    show ignis neutral at right
    with dissolve

    "He's tall, slim, and all things considered, rather attractive indeed."
    "You approach hesitantly, not wanting to interrupt them."

    you "Captain."

    #show commander facing forward. neutral

    captain "Ah, [your_name]."

    you "Sorry I'm late, Ma'am."

    "The Captain waves your apology away."

    captain "Understandable. I hear the streets outside are swamped with people waiting to hear the Oracle's speech."

    you "Since I was called in to Yureil Plaza ... am I to be guarding her during her speech today?"

    captain "No - we need as many guards as possible on evac duty."

    you "Evac?"

    "Here, the newcomer cuts in. His accent is sharp and learned."

    #show ignis openmouth calm

    ignis "Leviathan is a fickle goddess, powerful beyond measure. And with the Empire hanging by the sidelines, it is likely that we may see some destruction of the city."

    #show ignis closedmouth neutral again

    "You've heard of the floods of yore. You nod."

    captain "You will be stationed at the back of the plaza during her speech, but once the speech is over, we'll need you pointing the way to Finangia District."

    "The furthest district from the Cathedral. It would be easy to get the citizens out of harm's way from there."

    you "Understood, Captain."

    "The Captain excuses herself then, making her way down the corridor to debrief the next guard outpost."

    "You're left with the stranger, who watches you with interest. No part of his gaze is uncalculated. You wonder if he's a diplomat, or perhaps a spy."
    "It's hardly something you're going to say aloud to him, though. You settle for simple."

    you "Hi."

    ignis "My apologies for not acknowledging you earlier. I did not wish to interrupt your superior."

    ignis "I'm Ignis, by the way. Nice to meet you."

    $ ignis_name = "Ignis"

    ignis "What was your name, again?"

    "You introduce yourself."
    "He nods as you speak your name."

    ignis "{color=#aa748d}[your_name]{/color}? That's a lovely name."

    "You smile."

    ignis "Well, it seems we shall both be on evacuation duty."

    you "Wait, you're on evacuation duty too?"

    "You struggle to keep the incredulity out of your voice."

    ignis "Indeed."

    ignis "While I am a Lucian envoy, as my nation is responsible for invoking the Covenant, I must do all I can to aid Altissia for its efforts."

    "You feel like there's more to it than that, but you don't decide to bring it up."

    #here you should get the first choice to make to get his happiness up or down
    menu:
        "Express a desire to protect the Oracle":
            you "I shall do my best to protect the Oracle."
        "Tell him you'll do your duty as best you can":
            you "I shall do my best to ensure the citizens make it to safety."
        "Express doubt about your own capabilities":
            you "I'll see what I can do."

    ignis "Glad to hear it."

    return

# captain gets you to search the room for an item of some kind before you head out.
# this will teach you the 'flashlight' mechanic

label searchtheroom:

    ignis "I've run into a bit of trouble. Would you care to help me?"

    ignis "Look around this room and see if there's anything useful."

    # $ mouse_visible = False

    call screen flashlight

    # $ mouse_visible = True

    hide ignis neutral
    with dissolve

    #return to title screen
    return
