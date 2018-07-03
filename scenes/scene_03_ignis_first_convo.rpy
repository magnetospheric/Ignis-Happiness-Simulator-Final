#Scene 03
#Ignis first convo

#contains labels:
    # first_conversation

# covers first coversation with ignis, and sets up start of evac process



label first_conversation:

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}You race{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "Up the pale marble steps to the plaza entrance now. The Palace is grand and decked with flags, red and gold fabric that's dampened in the gathering rain."
    narrator1 "Usually, you think it looks overbearing, but today, it seems solemn, more like a tomb. It's not an inviting omen."

    stop foley fadeout 1.0
    scene bg yureilcorridor with Dissolve(1.0)

    $ renpy.music.set_volume(0.3, delay=1, channel='music')

    stop ambient fadeout 2.286
    play music morning_coffee2 fadein 2.286

    show captain neutral at left
    with dissolve

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}When you{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "When you report in, you notice the Captain of the Guard is accompanied by a stranger."

    #show ignis left looking to the side
    show ignis neutral at right with Dissolve(1.0)

    narrator1 "He's tall, slim, and all things considered, rather attractive indeed."
    narrator1 "You approach hesitantly, not wanting to interrupt them."

    you "Captain — ah, morning, Ma'am!"

    show captain neutral openmouth

    captain "Ah, [your_name]."

    you "Sorry I'm late, Ma'am."

    show captain smile

    narrator1 "The Captain waves your apology away."

    captain "Understandable. I hear the streets outside are swamped with people waiting to hear the Oracle's speech."

    you "Since I was called in to Yureil Plaza ... am I to be guarding her during her speech today?"

    captain "No — we need as many guards as possible on evac duty."

    you "Evac?"

    narrator1 "Here, the newcomer cuts in. His accent is sharp and learned, and you get the impression he's a foreign envoy of some sort."

    show ignis neutral openmouth

    ignis "Leviathan is a fickle goddess, powerful beyond measure. And with the Empire hanging by the sidelines, it is likely that we may see some destruction of the city."

    show ignis neutral

    narrator1 "You've heard of the floods of yore. You nod."

    show captain neutral openmouth

    captain "You will be stationed at the back of the plaza during her speech, but once the speech is over, we'll need you pointing the way to Finangia District."

    show captain neutral

    narrator1 "The furthest district from the Palace. It would be easy to get the citizens out of harm's way from there."

    narrator1 "Not that anything {i}that{/i} bad was going to happen, surely. You know you shouldn't read too much into this, but the mere presence of this foreign official has you curious."

    narrator1 "But you settle for your duty, and — is that an approving smile the handsome newcomer is shooting your way?"

    you "Understood, Captain."

    narrator1 "The Captain excuses herself then, making her way down the corridor to debrief the next cadre of guards."

    hide captain
    with dissolve

    show ignis neutral at center
    with move

    narrator1 "You're left with the stranger, who watches you with interest. No part of his gaze is uncalculated. You wonder if he's a diplomat, or perhaps a spy."
    narrator1 "It's hardly something you're going to say aloud to him, though. You settle for simple."

    you "Hi."

    show ignis neutral openmouth
    ignis "My apologies for not acknowledging you earlier. I did not wish to interrupt your superior."
    ignis "I'm Ignis, by the way. It's a pleasure to meet you."
    show ignis neutral

    $ ignis_name = "Ignis"

    narrator1 "Ignis. A name that means {i}of the fire{/i}. You think it sounds beautiful. You want to complement him somehow, but he interrupts your train of thought."

    show ignis neutral openmouth

    ignis "What was your name, again?"

    narrator1 "You introduce yourself, and Ignis nods as you speak your name."

    ignis "{color=#ffeff6}[your_name]{/color}? That's a lovely name."

    show ignis neutral

    narrator1 "You smile. You're not really sure it's appropriate to show too much emotion, especially not before such an important event as this, but you want to show your appreciation somehow."

    narrator1 "It gives you ... something of a thrill when Ignis smiles back."

    show ignis smile

    ignis "Well, it seems we shall both be on evacuation duty."

    you "Wait, you're on evacuation duty too?"

    narrator1 "You struggle to keep the incredulity out of your voice."

    ignis "Indeed."

    ignis "While I am a Lucian envoy, as my nation is responsible for invoking the Covenant, I must do all I can to aid Altissia for its efforts."

    ignis "You must be well aware of the danger this poses to your nation."

    show ignis neutral

    narrator1 "You feel like there's more to it than that, but you don't decide to bring it up at this point."

    show ignis neutral openmouth

    ignis "So, are you prepared, [your_name]?"

    show ignis neutral
    #here you should get the first choice to make to get his happiness up or down
    menu:
        "Express a desire to protect the Oracle":
            you "I shall do my best to protect the Oracle."
            show ignis smile
        "Tell him you'll protect the citizens as best you can":
            you "I shall do my best to ensure the citizens make it to safety."
            show ignis smile
        "Express doubt about your own capabilities":
            you "I'll see what I can do."

    $ show_happiness = True

    pause 1.0

    $ happiness += 2

    show screen happiness_text(title="Happiness increased!")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    ignis "Glad to hear it."

    show ignis neutral openmouth

    ignis "I'll be tuning in to the security frequency should we get separated."

    # the sound of crowds clapping outside draws your attention
    show ignis neutral

    $ renpy.music.set_volume(0.08, delay=0, channel='foley')
    $ renpy.music.set_volume(0.03, delay=0, channel='foley2')

    stop music fadeout 2.286
    play ambient undercurrent fadein 2.286

    play foley [ "<silence 2.286>", bells_chiming ] noloop
    play foley2 [ "<silence 2.286>", cheering1 ] noloop

    show ignis sidelong openmouth
    with dissolve

    narrator1 "Outside, the sound of the crowd is rising. You can hear clapping. And, from somewhere high up in the tower, the chime of a bell."

    ignis "Sounds like it's begun."

    narrator1 "Your transceiver crackles into life."

    show ignis sidelong

    captain "{i}All right. To your stations, everyone!{/i}" with hpunch

    captain "{i}You know the drill. Let's give this our all!{/i}"

    show ignis neutral openmouth
    with dissolve

    ignis "Come on, [your_name]. We best not disappoint."

    hide ignis
    with dissolve

    jump lunas_speech
