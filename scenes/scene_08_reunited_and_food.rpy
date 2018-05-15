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

    # finding harpoon bit should totally go here
    jump search_tigiano_rubble



label search_tigiano_rubble:

    call screen infobubble(title="Search the rubble", content="You never know what you might find.", confirmation="Let's go")

    hide screen infobubble
    #hide screen tigiano_inactive

    call screen tigiano_rubble



label harpoon:

    you "What is this? It looks different from the other mechs..."

    narrator1 "You prod the slab of metal and it clunks heavily to the side. Then you realise it's not a mech component at all, but rather a giant harpoon."


    menu:
        "Examine it some more?":

            $ examined_harpoon = True

            narrator1 "You peer closer."

            narrator1 "It doesn't seem to have any living or robotic components, and anyway, the circuits seem fried. You trace a finger along the chrome, marvelling at the intricacy."

            narrator1 "It looks almost like a hoverboard, and you're struck by the oddly hilarious mental image of someone trying to ride it."

            narrator1 "You file this away in your head. Never know when it might be useful."

        "Eh, it's probably dangerous":

            narrator1 "This is Imperial tech, and you really don't trust it. You step away before it does something weird."

    menu:
        "Keep looking through the rubble":
            call screen tigiano_rubble
        "Try something else":
            jump found_ignis



label painting:

    you "A picture? Wait..."

    narrator1 "You pull the framed canvas out from the rubble. It's a portrait of a man with a can of soup on his head."

    you "Whoa-oh."

    narrator1 "You replace the picture. It's not exactly useful."

    menu:
        "Keep looking through the rubble":
            call screen tigiano_rubble
        "Try something else":
            jump found_ignis



label found_ignis:

    narrator1 "You sigh and step back from the mess. Where to check now?"

    # sound effect: scrabbling and rocky noises

    narrator1 "A scrabbling amid the rubble to your right catches your attention."

    show ignis wet openmouth # should have wet ignis with eyesclosed and in pain
    with dissolve

    ignis "[your_name] ... Ah!"

    show ignis wet pained # should have wet ignis with eyesclosed and in pain
    with dissolve

    narrator1 "He stumbles, and you rush to support him."

    ignis "Th-thank you."

    show ignis wet openmouth # should have wet ignis with eyesclosed and in pain
    with dissolve

    narrator1 "It's a shock to see Ignis looking so dishevelled. You bite your lip as you steady him, thinking this is all your fault for being late."

    you "I — I heard over the radio. Who was that man? Are you okay?"

    ignis "Before I go into it, tell me — did you manage to save the citizens?"

    show ignis wet neutral # should have wet ignis with eyesclosed and in pain
    with dissolve

    if citizens_first == True:

        you "Yes."

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

                $ show_happiness = True

                pause 1.0

                $ happiness -= 1

                show screen happiness_text(title="Happiness decreased!")
                with dissolve
                pause 0.3
                hide screen happiness_text
                with dissolve

                ignis "I ... ah, I appreciate your concern for me, [your_name], but one cannot abandon one's duty."

                narrator1 "You pause. You hate to admit it, but he's right."

                jump chance_at_redemption

            "Tell him he was more important":

                you "I couldn't leave you!"

                $ show_happiness = True

                pause 1.0

                $ happiness -= 2

                show screen happiness_text(title="Happiness decreased a lot")
                with dissolve
                pause 0.3
                hide screen happiness_text
                with dissolve

                ignis "[your_name], it was your job to ensure the safety of those people."

                narrator1 "Okay, you really did not make a good impression here."

                narrator1 "You bite your lip — it doesn't feel great to be scolded on your job by a foreign diplomat, least of all someone as gracious as Ignis."

                jump chance_at_redemption



label saved_citizens:

    $ show_happiness = True

    pause 1.0

    $ happiness += 1

    show screen happiness_text(title="Happiness increased!")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    show ignis wet softsmile

    ignis "Ah, that's a relief. Good work."

    jump escape_tigiano



label chance_at_redemption:

    menu:
        "Apologise for your indiscretion":

            you "I reacted emotionally. I'm sorry."

            show ignis wet softsmile

            narrator1 "Ignis's expression softens slightly."

            jump escape_tigiano

        "Stand by your decision":

            you ""

            jump escape_tigiano



label escape_tigiano:

    you "So what did —"

    narrator1 "You're interrupted by the screeching sound of metal hitting concrete. Something has landed."


    narrator1 "But that's not all. The mech is joined by another, and another still. They're completely blocking off the way back to Padore."

    # show ignis wet stern
    ignis "Bloody hell ... is one not enough?"

    ignis "Don't let them see us!"

    if said_you_saved_citizens == False:

        ignis "There's no chance of getting back to save those people now."

    narrator1 "He grabs your hand and drags you behind a pile of rubble. There's a small passageway here that seems to lead to a lower level."

    ignis "There's nothing for it. We'll have to swim."

    menu:
        "Swim???":
            you "Swim???"

            ignis "Ah — are you able to swim?"

            you "Erm, I would prefer not to, but..."

            ignis "Right. In that case, I shall help you."

            jump other_side_of_canal

        "Let's do this!":

            you "All right, let's get to it then."

            narrator1 "You make sure your sword is tucked securely into your belt before you move to the water's edge, brushing the hair away from your face, readying yourself."

            narrator1 "Ignis seems impressed by your tenacity."

            jump other_side_of_canal
            


label other_side_of_canal:

    narrator1 "When you're over the other side, you spend a short while scouting for a route."

    narrator1 "The streets are decimated, the Empire's firepower completely disproportionate to its needs. This is no war zone, it's a slaughterhouse, and it's far beyond your wildest imaginings."

    narrator1 "At any rate, there doesn't seem to be a way back to the West Quarter. Not until those mechs move on."

    you "So, I wanted to say — who was that guy I heard on the radio? What did he do to you?"

    narrator1 "Ignis surveys the surroundings, a little too suspiciously for your liking. When he spots a stairwell leading down to a cellar, he motions toward it."

    ignis "Let's stop for a breather, shall we? It's not a good idea to talk too freely up here."

    narrator1 "You nod."

    you "You should get those wounds seen to, while we're at it."

    jump food_break

    return
