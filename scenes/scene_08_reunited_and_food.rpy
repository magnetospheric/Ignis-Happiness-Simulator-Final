#Scene 08
#Reuniting with Ignis

#contains labels:
    # meeting_ignis_again
    # search_tigiano_rubble
    # harpoon
    # painting
    # found_ignis
    # saved_citizens
    # chance_at_redemption
    # escape_tigiano


# covers meeting back up with ignis again


label meeting_ignis_again:

    show bg mediumstreet with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "Retracing your steps once again, you head further in to the city."

    narrator1 "You don't turn your radio back on. Yes, it would let Ignis know you're coming to his aid, but there's no way of knowing if it will incite his assailant, make him hurt Ignis more."

    narrator1 "Better to surprise them all, anyway, if it comes to that."

    narrator1 "So there's nothing to do but keep going, and trust that he'll still be there, in Tigiano District."

    show bg rubblestreet with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "When you reach Tigiano, the square is empty. Nothing but mech debris and the smoking remnants of Magitek armour scattered about."

    narrator1 "There's certainly no sign of human life."

    you "Ignis?"

    narrator1 "No response."

    narrator1 "Were you too late?"

    narrator1 "You explore the square, shouting out at intervals. You don't even care if any Magitek Troopers hear you, you'll fight."

    narrator1 "Or so you tell yourself."

    you "Ignis? Ignis — come on, please be here!"

    jump search_tigiano_rubble



label search_tigiano_rubble:

    $ rubble_items_found = 0

    call screen infobubble_confirm_cancel(title="Search the rubble", content="You never know what you might find.", confirmation="Let's search!", cancel="I don't have time for this", cancel_destination="found_ignis")

    hide screen infobubble

    call screen tigiano_rubble



label harpoon:

    show screen harpoon_large
    with dissolve

    $ rubble_items_found += 1

    you "What is this? It looks different from the other mechs..."

    narrator1 "You prod the slab of metal and it clunks heavily to the side. Then you realise it's not a mech component at all, but rather a giant harpoon."

    hide screen harpoon_large
    with dissolve

    menu:
        "Examine it some more?":

            $ examined_harpoon = True

            show screen harpoon_large
            with dissolve

            narrator1 "You peer closer."

            narrator1 "It doesn't seem to have any living or robotic components, and anyway, the circuits seem fried. You trace a finger along the chrome, marvelling at the intricacy."

            narrator1 "There's this weird curved panel at the end, which seems like a good base to stand upon."

            narrator1 "It looks almost like a hoverboard, and you're struck by the hilarious mental image of someone trying to ride it."

            narrator1 "You file this away in your head. Never know when it might be useful."

        "Eh, it's probably dangerous":

            narrator1 "This is Imperial tech, and you really don't trust it. You step away before it does something weird."

    hide screen harpoon_large
    with dissolve

    if rubble_items_found < 2:
        menu:
            "Keep looking through the rubble":
                call screen tigiano_rubble
            "Try something else":
                jump found_ignis
    else:
        menu:
            "Try something else":
                jump found_ignis



label soupy:

    $ rubble_items_found += 1

    you "A picture? Wait..."

    show screen soupy_large
    with dissolve

    narrator1 "You pull the framed canvas out from the rubble. It's a portrait of a man with a can of soup on his head."

    narrator1 "Oh dear. It's probably the work of that street artist that hangs around Listro Park."

    narrator1 "What on earth could it mean?"

    you "Whoa-oh."

    narrator1 "You replace the picture. It's not exactly useful."

    hide screen soupy_large
    with dissolve

    if rubble_items_found < 2:
        menu:
            "Keep looking through the rubble":
                call screen tigiano_rubble
            "Try something else":
                jump found_ignis
    else:
        menu:
            "Try something else":
                jump found_ignis



label found_ignis:

    show bg rubblestreet

    narrator1 "You sigh and step back from the mess. Where to check now?"

    # sound effect: scrabbling and rocky noises

    narrator1 "A scrabbling amid the rubble to your right catches your attention."

    show ignis unimpressed openmouth wet noblink
    with dissolve

    ignis "[your_name] ... Ah!"

    show ignis unimpressed wet eyesclosed
    with vpunch

    narrator1 "He stumbles, and you rush to support him."

    show ignis neutral openmouth wet
    with dissolve

    ignis "Th-thank you."

    show ignis neutral wet

    # says s
    if citizens_first == True or waited == True:
        narrator1 "It's a shock to see Ignis looking so dishevelled. You bite your lip as you steady him, thinking this is all your fault for being late."
    else:
        narrator1 "It's a shock to see Ignis looking so dishevelled. You bite your lip as you steady him. Even though you came as fast as you could, it still wasn't enough."

    you "I — I heard over the radio. Who was that man? Are you okay?"

    show ignis neutral openmouth wet

    ignis "Before I go into it, tell me — did you manage to save the citizens?"

    if citizens_first == True:

        you "I did, yes."

        $ said_you_saved_citizens = True

        jump saved_citizens

    else:
        menu:
            "(Lie)":

                you "Yes."

                $ said_you_saved_citizens = True

                jump saved_citizens

            "Say you haven't yet but you will":

                you "Not yet, but I'm planning on going back as soon as I know you're okay."

                show ignis neutral wet

                $ show_happiness = True

                pause 0.5

                $ happiness -= 1

                show screen happiness_text(title="Happiness decreased!")
                with dissolve
                pause 0.3
                hide screen happiness_text
                with dissolve

                show ignis unimpressed openmouth wet with dissolve

                ignis "I ... ah, I appreciate your concern for me, [your_name], but one cannot abandon one's duty."

                show ignis unimpressed wet

                narrator1 "You pause. You hate to admit it, but he's right."

                jump chance_at_redemption

            "Tell him he was more important":

                you "I couldn't leave you!"

                show ignis unimpressed openmouth wet with dissolve

                $ show_happiness = True

                pause 0.5

                $ happiness -= 2

                show screen happiness_text(title="Happiness decreased a lot")
                with dissolve
                pause 0.3
                hide screen happiness_text
                with dissolve

                ignis "[your_name], it was your job to ensure the safety of those people."

                show ignis unimpressed wet

                narrator1 "Okay, you really did not make a good impression here."

                narrator1 "You bite your lip — it doesn't feel great to be scolded on your job by a foreign diplomat, least of all someone as gracious as Ignis."

                jump chance_at_redemption



label saved_citizens:

    show ignis smile wet

    $ show_happiness = True

    $ happiness += 1

    show screen happiness_text(title="Happiness increased!")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    ignis "Ah, that's a relief. Good work."

    you "Thanks. Um ..."

    you "It was — it was difficult hearing you in pain. I'm sorry I didn't come sooner."

    ignis "I'm ... quite flattered you care so much. You have a kind soul, [your_name]."

    narrator1 "You had not intended to fish for praise, but his words leave you glowing all the same. You offer a smile — not quite shy but not quite brazen either — and you bask in the feeling a few seconds longer before focussing on the next task."

    jump escape_tigiano



label chance_at_redemption:

    menu:
        "Apologise for your indiscretion":

            you "I ... maybe shouldn't have let my emotions get in the way of my duty. I know I can't change that now, but I'm sorry."

            show ignis neutral wet with dissolve

            narrator1 "Ignis's expression softens slightly."

            ignis "It's quite all right, [your_name]. Even for those of us trained for these eventualities, war makes hasty decision-makers of us all."

            ignis "And I'm still quite flattered, you ought to know."

            jump escape_tigiano

        "Stand by your decision":

            you "I couldn't leave you to be tortured by that man!"

            ignis ""

            show ignis unimpressed wet

            jump escape_tigiano



label escape_tigiano:

    $ show_happiness = False

    you "So what did —"

    show ignis sidelong wet with vpunch

    #sound effect - metal screeching and clanging and thudding (3 noises merged)

    narrator1 "You're interrupted by the screeching sound of metal hitting concrete. Something has landed nearby."

    # you soundeffect voice intake of breath (consider making diff intakes of breath for male and female and nb)
    you "A mech!"

    narrator1 "But that's not all. The mech is joined by another, and another still. They're as tall as buildings, and are completely blocking off the way back to Padore."

    show ignis sidelong openmouth wet

    ignis "Bloody hell ... is one not enough?"

    ignis "Don't let them see us!"

    if said_you_saved_citizens == False:

        show ignis sidelong direct openmouth wet

        ignis "There's no chance of getting back to save those people now."

    show ignis sidelong direct wet

    narrator1 "He grabs your hand and drags you behind a pile of rubble. There's a small passageway here that seems to lead to a lower level."

    ignis "There's nothing for it. We'll have to swim."

    menu:
        "Swim???":
            you "Swim???"

            show ignis sidelong direct openmouth wet

            ignis "Ah — are you able to swim?"

            you "Erm, I would prefer not to, but..."

            ignis "Right. In that case, I shall help you."

            narrator1 "Ignis allows you enough time to sort your weapon before he squats and sort of ... pats his own back. His meaning is clear, and you stifle a giggle as you hop on."

            narrator1 "He's actually giving you a {i}piggyback ride{/i} over the canal."

            narrator1 "Not that you're complaining, but it's definitely not how you saw this day panning out. You cling to his shoulders as he half-wades, half-swims to the opposite bank — even feeling his muscular back beneath you, you're still not keen on the whole water thing."

            hide ignis with dissolve

            jump other_side_of_canal

        "Let's do this!":

            you "All right, let's get to it then."

            narrator1 "You make sure your sword is tucked securely into your belt before you move to the water's edge, brushing the hair away from your face, readying yourself."

            show ignis smile wet
            with dissolve

            narrator1 "Ignis seems impressed by your tenacity."

            $ show_happiness = True

            pause 0.5

            $ happiness += 1

            show screen happiness_text(title="Happiness increased!")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            ignis "Fantastic — let's go."

            hide ignis
            with dissolve

            $ show_happiness = False

            jump other_side_of_canal



label other_side_of_canal:

    show bg jettynearcellar with Dissolve(0.3)

    show ignis neutral wet

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "When you're over the other side, you spend a short while scouting for a route."

    narrator1 "The streets are decimated, the Empire's firepower completely disproportionate to its needs. This is no war zone, it's a slaughterhouse, and it's far beyond your wildest imaginings."

    narrator1 "At any rate, there doesn't seem to be a way back to the West Quarter. Not until those mechs move on."

    you "That man I heard on the radio ... did he call those mechs?"

    show ignis touching glasses wet with dissolve

    narrator1 "Instead of replying immediately, Ignis surveys the surroundings, a little too suspiciously for your liking. When he spots a stairwell leading down to a cellar, he motions toward it."

    ignis "Let's stop for a breather, shall we? It's not a good idea to talk too freely up here."

    narrator1 "You nod."

    jump food_break

    return
