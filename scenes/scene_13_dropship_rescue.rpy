#Scene 13
#Dropship Rescue

#contains labels:
    # returned_to_cell
    # dropship_corridor02
    # dropship_corridor03
    # ardyn_conversation
    # room01
    # room02

#contains screens:
    # flashlight_dropship_corridor02
    # flashlight_dropship_corridor03
    # flashlight_dropship_corridor02

# covers heading to the altar, reaching it and seeing ardyn take ignis away, and talking to ravus for the first time



label returned_to_cell:

    show bg dropship cell
    show screen black_overlay
    show cell bars
    with Dissolve(0.5)

    you "Owww, my head..."

    narrator1 "You're back in the prison."

    narrator1 "It seems the Magitek Trooper thought you were nothing more than an escaped prisoner."

    narrator1 "It isn't the sharpest tool in the box, because it seems to have left you in a cell with the door only loosely closed."

    you "Ignis?"

    ignis "[your_name], are you okay?"

    you "Yeah..."

    ignis "I heard the Magitek Trooper drag you into the cell adjacent to mine. Can you move?"

    you "It hit me on the head a little hard but... I'm okay."

    you "The door seems to be left open..."

    narrator1 "You struggle upright and push on the door. It gives with little problem."

    you "Okay. I'm gonna go searching again."

    ignis "Best of luck. And - do try to avoid their line of sight."

    you "Okay."

    jump dropship_corridor02



label dropship_corridor02:

    hide ignis
    hide cell bars
    show bg dropship corridor2
    show screen black_overlay
    with dissolve
    $ seen_ardyn_aboard_dropship_already = False

    narrator1 "You slip back out into the corridor, checking for signs of activity."

    narrator1 "So far so good."

    narrator1 "You turn left, heading further into the ship."

    call screen blank_overlay()

    hide screen blank_overlay
    hide screen black_overlay

    $ won_fight_label = "dropship_corridor02_success"
    $ lost_fight_label = "returned_to_cell"

    call screen flashlight_dropship_corridor02



screen flashlight_dropship_corridor02:
    add Flashlight(
                    timer=True,
                    button_idle_image="images/items/interior-corridor-2-door-idle.png",
                    button_hover_image="images/items/interior-corridor-2-door-hover.png",
                    buttonPosX=643,
                    buttonPosY=137,
                    jump_destination="dropship_corridor03",
                    size="small"
                )



label dropship_corridor03:

    show bg dropship corridor3
    show screen black_overlay
    with dissolve

    narrator1 "The next area is a sort of open room - your footsteps pan out into more of an echo when you enter."

    narrator1 "You can see faint lights in one corner. Time to get searching."

    call screen blank_overlay()

    hide screen blank_overlay
    hide screen black_overlay

    $ won_fight_label = "dropship_corridor03_success"
    $ lost_fight_label = "returned_to_cell"

    call screen flashlight_dropship_corridor03



screen flashlight_dropship_corridor03:
    add Flashlight(
                    timer=True,
                    button_idle_image="images/items/interior-corridor-3-door-idle.png",
                    button_hover_image="images/items/interior-corridor-3-door-hover.png",
                    buttonPosX=871,
                    buttonPosY=338,
                    jump_destination="ardyn_conversation",
                    size="small"
                )



label ardyn_conversation:

    show bg dropship corridor4
    show screen black_overlay_light
    with dissolve

    if seen_ardyn_aboard_dropship_already == True:

        narrator1 "Back into the room where you saw Ardyn talking to that trooper."

        narrator1 "Which direction will you go?"

        menu:
            "Go into the generator room":
                hide screen black_overlay_light
                jump room02
            "Trail Ardyn along the corridor":
                hide screen black_overlay_light
                jump room01

    else:
        stop music fadeout 2.286
        play ambient system_shocker

        show soot_particles

        narrator1 "Here you find stairs leading up to another level."

        narrator1 "The air's less humid up here, almost..."

        narrator1 "You try to avoid a cough. It's too dry, like there's little particles of sand in the air."

        narrator1 "A nauseous feeling overcomes you. You've felt this before, only recently, at the—"

        narrator1 "At the altar."

        narrator1 "Your stomach overturns."

        narrator1 "{i}The Chancellor is here.{/i}"

        show ardyn silhouette at SpriteLoc2(-0.08, 0.07) with moveinright

        show trooper dropship silhouette at SpriteLoc2(0.48, 0.0) with moveinleft

        show soot_particles_sparse

        you "Ah!"

        narrator1 "You hang back behind the railing."

        narrator1 "The Chancellor is fiddling with something in his pocket that makes a clinking sound. A key?"

        narrator1 "It must be."

        narrator1 "It's tantalising to have it so close within your grasp."

        ardyn "Well, I daresay we're just about ready to set off."

        ardyn "How's our dear friend doing down in the cargo bay, tell me - is he enjoying his station?"

        play foley trooper_screech noloop
        magitektrooper "{i}*screeches*{/i}" with hpunch

        ardyn "Ah, of course. You can't reply, can you?"

        narrator1 "You can't see the Chancellor too well, but you're pretty sure he's smirking."

        ardyn "No matter. Go see to the generators, now, run along."

        narrator1 "He pats the trooper comfortingly on the back - what an odd gesture to make - and stalks off down the corridor, coat swishing around his feet."

        show ardyn silhouette at SpriteLoc2(1.0, 0.07) with moveinleft

        $ seen_ardyn_aboard_dropship_already = True

        hide soot_particles

        narrator1 "The Magitek Trooper salutes his receding form, then walks off through the door on the left."

        show trooper dropship silhouette at SpriteLoc2(-1.08, 0.0) with moveinright

        narrator1 "Your eyes track Ardyn's silhouette. He's undoubtedly got the key, and you ought to be following him."

        narrator1 "But... it's tempting, to mess with the ship's operations."

        hide soot_particles_sparse

        narrator1 "It might buy you some more time to get Ignis to safety, but is it worth the time it will take?"

        narrator1 "What will you do?"

        menu:
            "Go into the generator room":
                hide screen black_overlay_light
                hide ardyn
                hide trooper
                stop ambient fadeout 2.286
                play music clone_resonance
                jump room02
            "Trail Ardyn along the corridor":
                hide screen black_overlay_light
                hide ardyn
                hide trooper
                stop ambient fadeout 2.286
                play music clone_resonance
                jump room01



label room01:

    if deactivated_generator == False:
        narrator1 "You pause outside the door to this room. You can hear movement inside."
        narrator1 "So you wait just a few moments, until the footsteps recede. It sounds like he's left the room through another exit. Should be safe."
    else:
        narrator1 "You can't hear any sound of movement within the room. It seems the Chancellor has moved on."

    show bg dropship room1
    show screen black_overlay
    with dissolve

    narrator1 "Hesitantly, slowly, you push open the door and slip inside."

    narrator1 "This room seems to be an office of some sort. At least, it looks like shelves line the wall."

    narrator1 "Time to search."

    call screen blank_overlay()

    hide screen blank_overlay
    hide screen black_overlay

    $ won_fight_label = "dropship_room01_success"
    $ lost_fight_label = "returned_to_cell"

    call screen flashlight_dropship_room01



screen flashlight_dropship_room01:
    add Flashlight(
                    timer=True,
                    button_idle_image="images/ui/transparent.png",
                    button_hover_image="images/items/cell-key-hover.png",
                    buttonPosX=770,
                    buttonPosY=405,
                    jump_destination="unlocking_cell",
                    size="small"
                )



label dropship_room01_success:

    show bg dropship room1
    show screen black_overlay
    with dissolve

    narrator1 "Well, that could have gone a little better..."

    narrator1 "You listen out for any other noise. It still feels like the Chancellor is too close. What if he heard your fight?"

    narrator1 "But nobody comes."

    narrator1 "It's safe to start searching again."

    call screen blank_overlay()

    hide screen blank_overlay
    hide screen black_overlay

    $ won_fight_label = "dropship_room01_success"
    $ lost_fight_label = "returned_to_cell"

    call screen flashlight_dropship_room01



label room02:

    show bg dropship room2
    show screen black_overlay_light
    with dissolve

    narrator1 "You enter the room quietly."

    show trooper dropship silhouette at center with dissolve

    narrator1 "The trooper has its back turned, and is busy fiddling with something at a terminal."

    narrator1 "It seems to be struggling with the buttons, and it is so utterly engrossed in its task that it fails to notice you enter."

    narrator1 "You have the element of surprise!"

    menu:
        "Attack with your sword":
            narrator1 "You creep towards the trooper and draw your sword."
            narrator1 "Raising it silently, you drive it forth and into the creature's neck."
            show trooper dropship at center with fastesthardflash
            narrator1 "By the time it's noticed you, it's too late."
            play foley trooper_screech noloop
            narrator1 "The trooper crumples to the floor with a ghastly shriek."
            hide trooper with dissolve
            jump room02_continue
        "Hit the trooper across the head":
            narrator1 "You creep up behind the trooper and hit it across the head with your fist."
            narrator1 "The blow throws it off balance, and it reels backward."
            narrator1 "It wasn't enough to knock it out, however..."
            menu:
                "Hit it again":
                    narrator1 "You strike again, but this time the trooper is prepared for it."
                    show trooper dropship at center with fastesthardflash
                    play foley trooper_screech noloop
                    narrator1 "It counters with a deafening shriek, and knocks you out cold."
                    scene black with Dissolve(0.5)
                    stop music fadeout 2.286
                    hide trooper
                    narrator1 "..."
                    narrator1 "......"
                    narrator1 "........."
                    play music clone_resonance fadein 6.286
                    jump returned_to_cell
                "Draw your sword":
                    narrator1 "You don't waste any more time, drawing your sword and striking swiftly."
                    show trooper dropship at center with fastesthardflash
                    play foley trooper_screech noloop
                    narrator1 "You aim for its core, and watch it dissolve into shadow with a shriek."
                    hide trooper with dissolve
                    jump room02_continue
        "Shine your flashlight at it":
            narrator1 "You shine your flashlight at the back of the trooper's head."
            narrator1 "It doesn't really have much effect."
            narrator1 "It does make the trooper notice you, though."
            show trooper dropship at center with fastesthardflash
            narrator1 "It wheels round and lunges for you immediately, more reflex than murderous intent."
            narrator1 "One strike, and you're knocked out cold."
            scene black with Dissolve(0.5)
            stop music fadeout 2.286
            hide trooper
            narrator1 "..."
            narrator1 "......"
            narrator1 "........."
            play music clone_resonance fadein 6.286
            jump returned_to_cell



label room02_continue:

    narrator1 "With the trooper dealt with, you turn your attention towards the terminal."

    narrator1 "There's a whirring sound coming from it."

    you "This must be the generator."

    narrator1 "It's probably not the only one a ship of this size has, but messing with it has got to be enough to make a serious dent in the ship's operations."

    narrator1 "It can't be that hard to put it out of commission, right?"

    call screen generator_button



label room_02_post_generator:

    $ deactivated_generator = True

    show bg dropship room2 active
    show screen black_overlay_light

    you "There! That went pretty well."

    narrator1 "Now that the generator is turned off, you turn your attentions to finding that key again."

    show bg dropship corridor4
    show screen black_overlay_light
    with dissolve

    narrator1 "You edge back out into the corridor, and creep slowly towards the door the Chancellor disappeared through."

    hide screen black_overlay_light

    jump room01



label unlocking_cell:

    you "Aha!"

    you "Found it!"

    show bg dropship corridor3
    show screen black_overlay
    with dissolve

    narrator1 "You backtrack to the cell once more, picking your way through the dark corridors."

    show bg dropship corridor2
    show screen black_overlay
    with dissolve

    narrator1 "Funny how it's always so much easier to retrace your steps. Seems shorter, somehow."

    narrator1 "You move swiftly, silently, and you reach the prison area in a matter of minutes."

    stop music fadeout 2.286
    play ambient footsteps_in_the_dark

    show bg dropship cell
    show screen black_overlay
    show ignis unimpressed injured at left
    show cell bars
    with dissolve

    you "Ignis! I found the key."

    ignis "Fantastic!"

    if discovered == False:

        you "Didn't get spotted once!"

        $ show_happiness = True

        pause 0.5

        $ happiness += 1

        show screen happiness_text(title="Happiness increased!")
        with dissolve
        pause 0.3
        hide screen happiness_text
        with dissolve

        ignis "I am rather impressed you retrieved the key without the guards noticing."

    narrator1 "You rush to the lock and get to it."

    you "Yes! It fits!"

    narrator1 "A creak, and then the cell door opens."

    you "You're free! Come on - let's get out of here."

    ignis "I... might need some help."

    narrator1 "He's stumbling as he tries to get to his feet, and that's when you notice, shining the torchlight across his face."

    show cell bars behind ignis
    hide screen black_overlay
    with dissolve

    you "Oh gods..."

    you "Oh, no, no, no..."

    narrator1 "The injury has split his skin red and raw, razed the flesh around his eyes. It looks so painful you want to turn away, but you hold fast your gaze."

    show ignis unimpressed openmouth injured with dissolve

    ignis "Ah - it's - it's only ... only a —"

    you "Don't you dare say 'flesh wound.'"

    show ignis unimpressed injured with dissolve

    narrator1 "He falls silent."

    you "Can you see at all?"

    ignis "..."

    show ignis unimpressed openmouth injured with dissolve

    ignis "No. Not yet, at any rate. Time will tell."

    show ignis unimpressed injured with dissolve

    you "What even ... what even happened back there? At the altar?"

    show ignis unimpressed openmouth injured with dissolve

    ignis "We should save the questions for outside. Focus on getting out first. We don't want this ship to take off with us still on it."

    show ignis unimpressed injured with dissolve

    you "Yeah, good point."

    narrator1 "You grasp his hand, gently but firmly, and lead him out of the prison."

    hide cell bars

    jump corridor_escaping_with_ignis



label corridor_escaping_with_ignis:

    show bg dropship corridor1
    show screen black_overlay_light
    with Dissolve(1.0)

    narrator1 "You backtrack through corridors already travelled. The interior of this ship is now so incredibly familiar to you that you barely need the flashlight."

    narrator1 "With Ignis's injury, and your haste, you're both a lot louder than you'd like, but by now the corridors are devoid of guards."

    narrator1 "Perhaps it's just luck."

    jump escaping_dropship



label escaping_dropship:

    show bg dropship loading bay exit
    with dissolve


    narrator1 "When you get to the loading bay, your heart falls as you find it filled with a small cadre of Magitek Troopers."

    narrator1 "They're moving boxes about in their peculiar staccato fashion, seeming somewhat detached from their surroundings."

    narrator1 "They're far enough away that you can both whisper without alerting their attention, but they also happen to be using the hatch, your only exit."

    show ignis neutral openmouth injured with dissolve

    ignis "I can hear soldiers. What are they doing?"

    show ignis neutral injured with dissolve

    you "They're sorting boxes. We're in the loading bay."

    show ignis neutral openmouth injured with dissolve

    ignis "Ah. He must be planning to leave soon."

    show ignis neutral injured with dissolve

    narrator1 "Your heart thuds. You really, {i}really{/i} don't want to end up in Niflheim."

    if deactivated_generator == True:

        you "Hey, while I was looking for the key, I managed to turn off a generator."

        show ignis smile injured with dissolve

        $ show_happiness = True

        pause 0.5

        $ happiness += 1

        show screen happiness_text(title="Happiness increased!")
        with dissolve
        pause 0.3
        hide screen happiness_text
        with dissolve

        ignis "You did?"

        ignis "Good job. That ought to buy us some time."

    you "There's a door to the right. We can't leave until they turn their backs."

    you "I think we'll get a clear shot once they're done loading up."

    show ignis neutral openmouth injured
    ignis "It sounds like it shall be a small window of opportunity. Are you prepared?"
    show ignis neutral injured

    narrator1 "You inhale deeply."

    you "Yes."

    show ignis neutral openmouth injured
    ignis "Good. I'm grateful I can count on you, [your_name]."
    ignis "But for now, it seems we have to wait."
    show ignis neutral injured

    narrator1 "You both settle back against the crates, relaxing as much as you're able to under the circumstances."

    narrator1 "The light showing from the open hatch is so close, so tantalising. But you can't make a move yet."

    narrator1 "Now's as good a time as any to ask about what happened."

    narrator1 "You keep one eye on the troopers while you talk."

    you "Do you mind telling me what was going on at the altar? I only saw the end of it but I ... I'm a bit confused."

    you "I'm sorry if it's too much to think about right now."

    show ignis neutral openmouth injured
    ignis "No, not at all."
    show ignis unimpressed openmouth injured
    ignis "The Chancellor is far more powerful than I realised."
    ignis "I had to tap into the power of the Lucian kings to even stand a chance against him."

    if ignis_revealed_suspicions == "True":

        show ignis unimpressed injured

        you "That thing you said earlier, about something else being at play... Is this what you meant?"

        show ignis unimpressed openmouth injured

        ignis "Indeed it is."
    else:
        ignis "I had been suspicious for a long time that {i}someone{/i} had hidden motivations ... now I know who it is."

    ignis "I still don't know enough about {i}why{/i}, though. I still don't know his end game."
    show ignis unimpressed injured

    you "He killed Luna..."

    show ignis unimpressed openmouth injured
    ignis "That, he regrettably did."
    show ignis unimpressed injured

    you "Why did he not simply kill you?"

    show ignis unimpressed openmouth injured
    ignis "He offered to let me join forces with him."
    ignis "I said no, but ... "
    narrator1 "He sighs, and indicates loosely at the ship walls."
    ignis "... it didn't seem to deter him."
    show ignis unimpressed injured

    you "I'll give him hell if I ever see him again!"

    narrator1 "You're aware you're clenching your fists, and it's on the point of hurting, but you don't want to relax."

    you "How dare he... How dare he do {i}this{/i} to you!"

    show ignis unimpressed openmouth injured
    ignis "About that..."
    ignis "My injuries were not caused by Ardyn."
    ignis "This was the ... price ... for tapping into the Power of Kings."
    show ignis unimpressed injured

    narrator1 "He sounds so small, suddenly, so {i}broken{/i}, and you want to hug him."

    menu:
        "Hug":
            narrator1 "You hug him."
            narrator1 "At first, his breath quickens."
            you "Sorry, I -"

            show ignis smile injured with dissolve

            $ show_happiness = True

            pause 0.5

            $ happiness += 1

            show screen happiness_text(title="Happiness increased!")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            ignis "No, I... I appreciate it."
            narrator1 "He doesn't seem used to the physical contact - there's something in the way he clings fervently on to you that shows this."
            narrator1 "When you eventually break from the hug, he sniffs, and leans back against the crate."

        "Do not hug":
            narrator1 "He probably needs his space. You don't want to surprise him the wrong way, especially not if he's in pain."

    show ignis unimpressed openmouth injured
    ignis "He — I had no choice — He was going to hurt Noct."
    ignis "I couldn't let that happen!"
    ignis "So I had to ... I had to use that power."
    show ignis unimpressed injured

    narrator1 "You can't bear hearing him so torn-up over this."

    narrator1 "There's such an ugly mix of emotions there; shame, weakness, failure, fear for his young charge."

    menu:
        "Reassure him that Noctis is safe for now":

            you "I understand. And, uh, Prince Noctis is safe for now."

            narrator1 "A shallow laugh from Ignis."

            show ignis smile injured

            ignis "{i}Ravus,{/i} hmm?"
            ignis "Well, the man came through after all."

            $ show_happiness = True

            pause 0.5

            $ happiness += 2

            show screen happiness_text(title="Happiness increased!")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            ignis "Thank you ... for letting me know Noct is okay."

        "Tell him he did the right thing":
            you "You did the right thing, you know."

            ignis "I did, I suppose..."

            narrator1 "He's still deep in thought. He's still blaming himself."

            you "Ignis, you tried. That's all anyone could ask for."

            $ show_happiness = True

            pause 0.5

            $ happiness += 2

            show screen happiness_text(title="Happiness increased!")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            show ignis neutral openmouth injured

            ignis "Perhaps."

            ignis "Thank you, [your_name]. I'm just ..."

            ignis "I think I might be in shock."

            you "Don't worry. I'm getting you out of here."

            narrator1 "After a while, Ignis's breathing grows steadier. The troopers still guard the entrance..."

        "Say nothing, but console him instead":
            narrator1 "You place a hand gently on his shoulder."
            narrator1 "You don't know what to say, and you worry the silence will be too awkward."
            narrator1 "But Ignis sighs, and his breathing grows steady after a while."

    you "So that purple light was... Oh, gods..."

    you "I thought the Power of Kings was a myth."

    show ignis neutral openmouth injured with dissolve
    ignis "Once upon a time, I thought the same of Leviathan."
    show ignis neutral injured

    you "Heh. You know, the older I get, the more the world seems a surprising place."

    show ignis neutral openmouth injured
    ignis "More terrifying and more beautiful than I ever could have imagined."
    show ignis neutral injured

    narrator1 "That phrase settles in your soul comfortably. He's right, absolutely right, and it seems such a bitterly hopeful thing to say in the circumstances."

    narrator1 "Then, movement, up ahead."

    show ignis neutral openmouth injured
    ignis "Are they leaving?"
    show ignis neutral injured

    you "Mm."

    show ignis neutral openmouth injured
    ignis "[your_name]..."
    show ignis neutral injured

    narrator1 "There's a worried tinge to his voice, and seconds later it's accompanied by his fingers searching for yours."

    narrator1 "You bite back the raw feeling in your chest as you realise he's scared."

    narrator1 "It must be awful. For someone so capable to be suddenly cast out of power, helpless and in darkness."

    narrator1 "You can't imagine what it must feel like."

    narrator1 "But you don't need to waste precious seconds trying to put yourself in his shoes."
    narrator1 "The way lies open, and it's your responsibility to see him to safety now."

    you "Okay, hold on to my hand. Let's go."

    menu:
        "Make a dash for it":
            narrator1 "You make a mad dash for the door, pulling Ignis along behind you. He's not expecting the force of it, if his rushed intake of breath is anything to go by."
            narrator1 "On the way out, you both knock aside a few crates, which make a real din, but you pay it no mind, stumbling out on shaky, adrenaline-pumped legs."
        "Go a little slower but more safely":
            narrator1 "You don't dash for the door, but instead walk carefully, full of determination, round every obstacle."
            narrator1 "You figure, with Ignis in the state he's in, it's not going to be any faster to run wildly."
            $ show_happiness = True

            pause 0.5

            $ happiness += 1

            show screen happiness_text(title="Happiness increased!")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            show ignis smile injured

    stop ambient fadeout 2.286
    play music undercurrent fadein 2.286

    show bg dropship exterior with Dissolve(1.5)

    narrator1 "The outdoors seems so achingly bright, despite the fact the clouds still hang dark and heavy over the besieged city."

    narrator1 "You don't stop here. You were far too loud back there; you've got to drag Ignis much more than a stone's throw away before you're comfortable letting either of you catch your breath."

    you "I can't believe we actually made it!"

    you "Whew! Oh man... Ohhhhh man."

    show ignis neutral openmouth injured
    ignis "That was quite the hair-raising adventure. Thank you."
    show ignis neutral injured

    you "Really not a problem. I ..."

    you "I couldn't leave you."

    show ignis smile injured with dissolve
    narrator1 "At this, Ignis smiles fondly."

    show ignis neutral openmouth injured
    ignis "Now, I must check on Noct."
    show ignis neutral injured

    narrator1 "You help him back to the altar, where you hope Ravus still stands waiting."

    jump altar_aftermath
