#Scene 10
#Separation

#contains labels:
    # food_break
    # openup
    # ignis_opens_up
    # meet_prompto


# covers the explosion that separates you from Ignis


label separation:

    stop music fadeout 2.286
    $ renpy.music.set_volume(0.3, delay=0, channel='ambient')
    $ renpy.music.set_volume(0.3, delay=0, channel='ambient')
    play ambient undercurrent

    scene bg jettynearcellar with Dissolve(0.3)

    show ignis neutral wet at center with dissolve

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    ignis "Ah, there you are, [your_name]. Now, hurry, we have to..."

    $ renpy.music.set_volume(0.4, delay=0, channel='foley3')
    play foley2 airship_zoom noloop

    pause 0.5

    show ignis sidelong wet with vpunch

    ignis "What the devil—"

    stop ambient fadeout 2.286
    play music lights_out_1
    $ renpy.music.set_volume(0.3, delay=0, channel='foley3')
    play foley3 explosion03 noloop
    play foley mech_landing noloop
    play foley4 mech_bass noloop

    show ignis sidelong wet with hardflash
    show ignis sidelong wet with hardflash

    narrator1 "The flash of light is so intense you can see it even through your scrunched-up eyes."

    play foley2 engine_bassline loop fadein 2.286
    play foley3 explosion04 noloop
    narrator1 "Something roars in your ears, throwing you off-balance, and you have bare moments to try and reach for Ignis, but..."
    narrator1 "You're thrust backward."

    you "Aah!" with vpunch

    show ignis sidelong direct openmouth wet

    ignis "[your_name]!"

    jump awakening



label awakening:

    $ show_happiness = False
    scene black with Dissolve(1.5)
    stop music fadeout 2.286
    stop foley2 fadeout 4.286

    narrator1 "{cps=15}...{/cps}"

    narrator1 "{cps=15}......{/cps}"

    narrator1 "Silence."

    narrator1 "{cps=15}......{/cps}"

    narrator1 "What's going on?"

    you "{i}I need to ... I need to just move...{/i}"

    you "{i}Come on...{/i}"

    you "{i}Move!{/i}"

    show bg rubblestreet dark with Dissolve(1.5)
    play music bated_breath fadein 1.5

    narrator1 "When you come to, you're alone."

    narrator1 "The silence is replaced by a high-pitched tone, and then, at the edges, lower registers creep in."

    narrator1 "There's the sound of fire crackling, of water gently sloshing against you, and the distant hum of machines of war high above."

    you "What ... what happened?"

    you "I need to see..."

    show bg rubblestreet with Dissolve(1.0)

    narrator1 "You open your eyes, finally."

    you "Ignis?"

    you "..."

    you "Ignis, where are you?"

    narrator1 "Your voice is hoarse, and it hurts to yell."

    narrator1 "Not much more than a whisper comes out."

    narrator1 "Looking around, it seems the blast has knocked you back to the water's edge at Tigiano Square."

    narrator1 "You've landed beneath some debris, legs in the water, arms grasping at the shore."

    narrator1 "Everything hurts."

    narrator1 "You struggle to your feet, muscles threatening to cramp with each step."

    narrator1 "There's going to be some nasty bruises after this, but thankfully, you can still move."

    narrator1 "You groggily stumble around the square. The harpoon is gone."

    you "So Ignis and his friend must have been able to fix it..."

    narrator1 "A knot of worry settles into the pit of your stomach; the feeling of being forgotten."

    you "Ignis? Ignis!"

    narrator1 "Still no response. The square's as silent as a tomb."

    you "I was pretty hidden back there — maybe they just didn't see me..."

    narrator1 "You can only hope."

    narrator1 "What is there to do now?"

    narrator1 "You know Ignis is headed to the altar, but what more can you do to help right now?"

    narrator1 "it's possible you might just get in the way. And besides, doesn't he have his friend with him now?"

    menu:
        "Go after Ignis":

            narrator1 "You've managed to help so far. There may be more yet you can do."

            jump head_to_altar

        "Return to the evac point":

            narrator1 "It's probably better you return to the evac point. it's your job, after all."

            jump return_to_evac




label return_to_evac:

    $ reached_chapter_three = False

    show bg padore jetty with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    show altissianguard neutral at center
    with dissolve

    altissianguard "[your_name], are you okay? I was starting to really worry about you."

    you "Uh, yeah ... I'm sorry. I got caught up in something."

    altissianguard "By the Six, your bruises..."

    you "Oh, it'll be fine. I ... how are the people doing?"

    altissianguard "We evacuated the last of them, apart from the few you see dotted around ... they stayed on in case we needed more help."

    narrator1 "Okay, {i}that{/i} makes you feel a little guilty. This should have been your job, after all."

    you "Oh... I hope they're okay."

    altissianguard "We're hanging on, but — Leviathan's breath, [your_name], you look like you need to sit down."

    you "I'm fine. Just had a little run-in with the Empire, I suppose. Now, what needs doing?"

    narrator1 "Your colleague shakes his head."

    altissianguard "I think we're all sorted here. You can probably just go back now."

    narrator1 "Now that your duties are finished, what will you do?"

    narrator1 "The sounds of fighting still rage in the distance, and you're worried something has gone down at the altar."

    menu:
        "Return home":
            narrator1 "You've spent long enough playing the hero."
            narrator1 "It's time to head home."
            narrator1 "Ignis was a fascinating person to meet, but really..."
            narrator1 "What business have you interfering like this?"
            jump going_home
        "Go and check on Ignis":
            jump head_to_altar
