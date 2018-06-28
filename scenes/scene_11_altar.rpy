#Scene 11
#Altar

#contains labels:
    # head_to_altar
    # ardyn_appears
    # ravus_conversation

# covers heading to the altar, reaching it and seeing ardyn take ignis away, and talking to ravus for the first time

label head_to_altar:

    show bg jettynearcellar with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "It takes some effort to swim back over the canal, but you manage."

    narrator1 "This is the fastest way to the altar, now that the bridge is gone, after all."

    narrator1 "You race down the street, past the cellar, past the warehouse block, and on to new streets, new territories."

    show bg leviathan with Dissolve(0.3)

    narrator1 "The next street you turn down gives you quite the apocalyptic view."

    you "{i}Leviathan!{/i}"

    you "I can't belive I'm really seeing this!"

    narrator1 "A real Goddess, in the flesh. All those bedtime stories, all those songs of praise..."

    narrator1 "They're all true."

    narrator1 "It's a far cry from what you imagined, seeing her raging like this, surrounded by dropships and incoming fire."

    narrator1 "But then, if the older stories are to be believed, she always was a goddess of fury."

    narrator1 "It's strange how seeing the Empire attack her feels like a direct assault on you yourself. But Leviathan is perhaps the strongest symbol of Altissia there is."

    narrator1 "And, knowing the tales, you're not sure if you're more scared of them killing her, or of her bringing the fabled Floods as revenge."

    narrator1 "You realise you've stopped, and have been staring in awe for a while now."

    you "There's no time to waste — I have to keep going!"

    jump ardyn_appears



label ardyn_appears:

    scene black with dissolve
    centered "{size=26}Chapter Three\n\n{/size}{size=36}Machine Messiah{/size}"

    show bg altar whiteout with softflash

    show soot_particles behind ardyn
    show glow_particles behind ardyn
    show soot_particles_sparse

    narrator1 "The altar isn't far, but when you finally reach it, it's nothing like you expected."

    narrator1 "The whole place is rife with energy; the altar stands half-destroyed, and an unholy miasma fills the air."

    narrator1 "Leviathan has sunk below the waves now; whether dead or merely returned to her deep slumber, you do not know."

    narrator1 "But more stunning is the unearthly activity at the foot of the altar. It's like witnessing the centre of a storm."

    narrator1 "Through the flashes of chaotic purple lightning, you can just about make out two figures moving. Fighting."

    show ardyn silhouette at left with moveinright

    show ignis wet silhouette at right with moveinleft

    narrator1 "Is one of them... Ignis?"

    narrator1 "You're too far away to see properly."

    narrator1 "The fight rages on."

    narrator1 "Another crash, another lightning strike as their forces collide. Is Ignis really so powerful? And who the hell is this other guy?"

    # crash sf here
    show bg altar whiteout with hardflash
    show bg altar with Dissolve(1.0)

    narrator1 "The stranger lunges forth. After one final, terrifying strike, Ignis drops to the floor."

    hide ignis with fastdissolve

    narrator1 "The triumphant party laughs, and it's not a sound you're going to forget easily."

    narrator1 "It chills you to the bone."

    ardyn "Oh, poor, foolish boy — you really thought you could be a match for me?"

    ardyn "You didn't need to come here for the sake of your dear Prince, but..."

    ardyn "What can I say? Love is blind."

    narrator1 "He kicks the figure lying on the ground, and the resultant yell makes you flinch."

    you "{i}Ignis!{/i}"

    show ardyn silhouette with vpunch

    narrator1 "You've barely spoken above a whisper, and you're still a long way off, but all the same, the stranger turns your way, sense of hearing as acute as that of a predator."

    narrator1 "You duck behind a half-collapsed stone wall. Counting the seconds, urging your breaths into stillness, you wait."

    narrator1 "There's scraping; boots on concrete, and a jaunty melody being hummed."

    narrator1 "After what seems an age, he turns back to Ignis, and you exhale cautiously. That felt far too close."

    ardyn "You ought to have taken me up on —-------- such a pity ----- "

    narrator1 "Even with the stranger's voice, sonorous as it is, the rest of the sentence is muffled. You're too far away to hear."

    menu:
        "Get closer to catch his words":

            show bg altar whiteout static
            show ardyn trashbags with softflash
            show bg altar with fastdissolve

            ardyn "Ah, I thought I heard a little mouse creeping about."

            you "!!"

            narrator1 "You stare, wide-eyed. He's too close, all of a sudden, as though he has simply warped here from all those metres away."

            narrator1 "He's so close you can see the amber glint of his irises."

            narrator1 "There's nowhere you can run that he won't follow in the blink of an eye."

            narrator1 "You're practically vibrating with fear, but you have to try. So, you bring your arm up in an attempt to knock him out of the way, thinking maybe, just maybe, you can slip out to the side."

            #shit, gonna need an ardyn looking-to-the-side img here
            show ardyn trashbags with softflash

            narrator1 "He catches your throw languidly, as though he's doing little more than waving an irritating fly out of his face."

            narrator1 "Then his eyes turn on you again."

            $ reset_game_once = None

            if reset_game_once == True:
                ardyn "Did you not learn from last time? Can't have you spoiling the party."
            else:
                ardyn "I think not, little mouse. Can't have you spoiling the party."

            menu:
                "What the hell did you do to Ignis?":
                    ardyn "Oh, me? I did nothing; he did all that himself."
                    you "Seriously? I just saw you knock Ignis down... how on earth can you say that?"
                    ardyn "Believe me, I only speak the truth. But I can see you're not going to cooperate."
                    $ ardyn_affiliation = "anger";

                "C'mon, I {i}am{/i} the party!":
                    ardyn "Spirited, I'll grant you that. Perhaps you should come play sometime."
                    narrator1 "You don't know quite what to say to that."
                    narrator1 "But it turns out you don't have much time anyway."
                    $ ardyn_affiliation = "play";

                "\[run\]":
                    ardyn "Ah-ah, I think not."
                    narrator1 "You barely take a step before he blocks you."
                    $ ardyn_affiliation = "fear";

            narrator1 "A crooked smile, then —"

            hide ardyn
            show bg altar whiteout static
            show ardyn neon at center with MoveTransition(0.02)
            # show ardyn neon at right with MoveTransition(0.01)
            show ardyn neon at left with MoveTransition(0.02)
            # show bg altar whiteout static

            narrator1 "Something hits you at full force; a jolt of gravity to your solar plexus. The world seems to turn in on itself in shades of purple and red, then —"

            hide ardyn
            show black
            with fastdissolve
            # cut to black

            hide soot_particles
            hide glow_particles
            hide soot_particles_sparse

            narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

            narrator1 "..."

            narrator1 "......"

            narrator1 "You're getting really sick of this being-knocked-out business by now..."

            show bg altar
            hide black with dissolve

            narrator1 "When you wake this time, it feels like your head's been hit by a freight truck."

            narrator1 "Splotchy afterimages of that purple light invade you vision, while a poisonous feeling threads through your veins."

            narrator1 "It feels an order of magnitude worse than a night out on the town. In fact — you'd almost take being hit by another explosion over this feeling."

            narrator1 "You want to double over and puke."

            narrator1 "But you don't. Instead you struggle upward, and make your way to the head of the altar."

            narrator1 "There's no sign of the stranger, and no sign of Ignis. But instead —"

        "Stay where you are":

            narrator1 "You're not going to risk having this man hear you. You've seen him fight; it's clear he's infinitely dangerous."

            narrator1 "Not to mention the vibe you get off him is blood-curdling."

            narrator1 "So you resign yourself to watching as the stranger"

    jump ravus_conversation



label ravus_conversation:

    you "Oh no, what now..."

    show ravus neutral with dissolve

    narrator1 "There's a white-haired man standing at the altar. He cuts a solemn figure, head slightly bowed, arms loose at his sides."

    narrator1 "His pale clothes are sullied, and while their design screams {i}Empire{/i}, you're not reading any desire to fight off him."

    you "Where did that man take Ignis?"

    if ardyn_affiliation == 'anger':

        ravus "{i}That man...{/i} You really don't know what you were up against, do you?"

        you "Wh-what do you mean?"

        ravus "Really... Chancellor Ardyn Izunia corners you and you ... shout in his face!"

        narrator1 "The white-haired man spares a moment to laugh to himself. It's not unkind, more ... disbelieving."

        you "Oh gods... That was the Chancellor?"

        ravus "Yes, and while your actions were foolish, I'm ... actually quite impressed."

        narrator1 "You're unsure if he's trying to compliment you or not. Either way, it's a distraction from the main problem."

    if ardyn_affiliation == 'play':

        ravus "{i}That man{/i} was Chancellor Ardyn Izunia, and you would do well not to joke around with him."

        you "I know what I'm doing!"

        narrator1 "He eyes your dishevelled hair and snorts."

        ravus "Evidently."

        you "Enough."

    if ardyn_affiliation == 'run':

        ravus "For one who doesn't know who he is, you were wise to try to run."

        ravus "{i}That man{/i} was none other than Chancellor Ardyn Izunia."

        you "The Chancellor ... of Niflheim?"

        ravus "The very same."

        you "... Oh."

    if ardyn_affiliation == 'nothing':

        ravus "You were wise to keep your distance. That man was Chancellor Ardyn Izunia. Had he noticed you, you likely would not have survived long."

    you "Maybe you can tell me then. What did you do to Ignis?"

    you "Where is he!" with vpunch

    ravus "Calm down, brat. I didn't—"

    you "Look, I know you're with the Empire!"

    narrator1 "At this, the man laughs."

    ravus "Oh, I'm not just 'with' the Empire. Ravus Nox Fleuret — Commander of the Niflheim Military."

    $ ravus_name = "Ravus"

    narrator1 "So {i}this{/i} is Ravus. Brother of the Oracle. You've heard of him, for sure, but in person, you never expected him to look so ... young."

    narrator1 "You dimly wonder if the grey is natural."

    ravus "But I've absconded."

    ravus "I was only trying to protect my sister. And they... they..."

    $ quick_menu = True

    menu:
        "Show anger":
            you "I don't care!"
            ravus "I don't expect you to. But she's... "
            narrator1 "He cuts off. He's so close to crying, and that's when you spot her."
            narrator1 "She's lying a few metres off, next to another, darker shape."
            narrator1 "Prince Noctis."

        "Show empathy":
            you "Oh. I..."
            narrator1 "You cut yourself off, unsure how to finish."
            narrator1 "He's so close to crying, and that's when you spot her."
            narrator1 "Lady Lunafreya. She's lying a few metres off, next to another, darker shape."
            narrator1 "Prince Noctis."

    you "Oh my gosh, are they both —"
    ravus "No. Only Luna."
    narrator1 "The silence is awkward."
    you "I'm sorry."
    narrator1 "Ravus acts like he hasn't heard you. He's probably hurting too much to acknowledge it."
    ravus "I'm staying with them. If you want to rescue your friend, you'll need to head to the dropship over there."
    ravus "You'd best hurry. Our {i}esteemed{/i} Chancellor spoke of taking him to Niflheim."
    menu:
        "Thank him":
            you "Thank you, Ravus."
            narrator1 "Then you leave, heading for the dropship as fast as you can."
        "Don't waste any more time - Leave":
            narrator1 "You give only the briefest of nods before turning heel and racing toward the dropship he mentioned."

    narrator1 "There's no reason why he should lie. But all the same, your grip tightens on your sword."

    jump entering_dropship
