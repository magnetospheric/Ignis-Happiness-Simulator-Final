#Scene 03
#Ignis first convo

#contains labels:
    # first_conversation

# covers first coversation with ignis, and sets up start of evac process



label first_conversation:

    #scene bg yureilplazasteps

    "Up the pale marble steps to the plaza entrance now. Yureil Mansion is grand and decked with flags, red and gold fabric that's dampened in the gatheing rain."
    "Usually, you think it looks overbearing, but today, it seems solemn, more like a tomb. It's not an inviting omen."

    #show commander left in conversation
    scene bg yureilcorridor

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

    ignis "Tune in to frequency 4400 - "

    altissianguard "Sir, it's begun"

    scene bg yureilcorridordark

    ignis "All right. To your stations, everyone."

    captain "Good luck out there, [your_name]"

    return

# ignis shows you where to go on the map, then leaves after this

# if you go to help the citizens instead of rushing to his aid, he'll be happier with you
label en_route_to_altar:

    # captain gets you to search the room for the fuse switch before you head out.
    # this will teach you the 'flashlight' mechanic

    "The lights flicker off, casting the room into darkness."
    # have a sort of flash effect as the room goes dark, if possible.
    # Could be achieved by a sort of inverted colouring of the current room bg

    you "A power cut?"

    captain "There's a torch on the table next to you. See if you can't find the fuse switch."

    # info box: TORCH has been equipped

    # enter flashlight section

    captain "Take the torch with you, [your_name]. You might need it."


    "Ignis has forgotten to turn his mic off, and you can hear everything that's happening."

    "It's mostly muffled shouts and cries, accompanied by Ignis's breathing. He's clearly frantic, but doing an admirable job of stilling his own nerves."

    "Then, an angry voice."

    unidentified_voice "The King's lapdog, eh?"

    "And a sharp cry of pain. Ignis is hurt."

    "You check your map. You're only a street away from the citizens you've been tasked with helping."

    menu:
        "Continue onward to help the citizens":
            "You can't abandon your duty. You know this as clear as day."
            # highlight current route on map
            "The citizens aren't far away. You'll help them first, then come to Ignis's aid."
        "Divert your route to help Ignis":
            "You simply can't leave him in pain like that. What if the Niffs kill him, after all?"
            #highlight new route on the map
            "If you take this route, you can come to his aid and still be close enough to double back for the citizens afterward."

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
