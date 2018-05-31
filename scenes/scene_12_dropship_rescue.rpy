#Scene 12
#Dropship Rescue

#contains labels:
    # entering_dropship
    # finding_ignis_cell
    # finding_key
    # unlocking_cell
    # escaping_dropship

# covers heading to the altar, reaching it and seeing ardyn take ignis away, and talking to ravus for the first time

label entering_dropship:

    narrator1 "The dropship is not as heavily-guarded as you expect, with only two Magitek Troopers listlessly padding about the front."

    narrator1 "It's bigger than the other dropships you've seen around, but not quite as large as the Imperial Dreadnoughts that still hang in the sky."

    narrator1 "Perhaps this is Ardyn Izunia's personal ship?"

    narrator1 "Your heart's beating far too fast as you circle round the side of the thing first, looking for a way to enter that's not quite so out-in-the-open."

    narrator1 "There; a side door that's been left open, a box of discarded crates next to it. Whoever's been doing the unloading has obviously been sidetracked by more pressing matters."

    narrator1 "You take advantage of the opportunity, slipping inside before you can be noticed."

    show bg dropship loading bay
    show screen black_overlay
    with dissolve

    narrator1 "It's so dark in here. Your foot bumps into something hard. A crate, like the ones at the door."

    narrator1 "This must be the loading bay."

    narrator1 "You try to edge forward, and bump into another crate. Then you remember you still have the torch."

    narrator1 "You have no idea if anyone else is in this room or not. It doesn't sound like it, but then again, Magitek Troopers are hardly human, are they? They can be still as stone statues for all you know."

    narrator1 "Clutching the torch in hand, you let your thumb hover above the 'On' switch."

    narrator1 "It's time to make it through the loading bay."

    call screen infobubble(title="Get to Ignis", content="Use the torch to find a way forward. \nCareful though: keeping it on too long will alert the Magitek Troopers!", confirmation="Okay")

    hide screen infobubble
    hide screen black_overlay

    show bg dropship loading bay

    call screen flashlight_loading_bay

    show screen black_overlay
    show bg dropship loading bay

    jump finding_ignis_cell

label finding_ignis_cell:

    narrator1 "You shine your torch briefly across the room and catch sight of that distinctive purple patterned shirt."

    narrator1 "You rush to the door."

    you "Ignis!"

    narrator1 "The urge to shine the torch on him some more, to see him, is overwhelming, but you don't want to alert the soldiers to your presence."

    ignis "[your_name]? What ... what are you doing here?"





    ignis "[your_name]? Oh, thank the Six! I thought I'd lost you in the square!"

    you "No, no, I'm okay. Don't worry. But you... what about you?"

    ignis "I ... I've been better."

    narrator1 "You grip the bars, careful not to rattle them too hard in case the enemy hears. But even with a strong, firm push, the door won't give."

    you "Hold on. I'm gonna try and find the key."

    you "Is this connected to that blue light from before?"

    ignis "No, well, not entirely — ah!"

    narrator1 "He doubles over in pain."





    narrator1 "It's hard to keep your voice below a whisper, excited as you are to have found him."

    you "I came to rescue you!"

    narrator1 "There's a short silence while he processes your words."

    ignis "That ... was an incredibly risky thing to do, [your_name]. You could have been caught too."

    ignis "But I am grateful. Immensely so."

    narrator1 "He sounds so choked-up, so worn out. You steel yourself, and ask."

    you "Are you okay?"

    ignis "I..."

    ignis "No, I am very much not okay."

    you "Is there anything I can do? Well, uh, aside from getting you out of there."

    ignis "I... I could do with some water, actually. My head... my throat, it's all..."

    if extra_item == "water":

        you "Oh! I have some right here!"

        narrator1 "You've never been more glad that you stopped to pick up that bottle in the cellar."

        narrator1 "You pass the water through the bars and Ignis accepts it with oddly fumbling hands."

    else:

        you "I'll keep a lookout."

        you "But first, I gotta get you out of here."

    narrator1 "You run your hands over the door lock, feeling for a seam or something to exploit."

    narrator1 "There's nothing; only a gap for a key and not an inch of give between."

    ignis ""




label finding_key:

    # am thinking perhaps each room/corridor you need to get through will have a number to help you know where you are


    jump unlocking_cell

label unlocking_cell:

    you "Come on!"

    ignis "I... might need some help."

    narrator1 "He's stumbling about as he tries to get to his feet, and that's when you notice, shining the torchlight across his face."

    you "Oh gods..."

    you "Oh, no, no, no..."

    ignis "Ah - it's - it's only ... only a —"

    you "Don't you dare say 'flesh wound.'"

    narrator1 "He falls silent."

    you "Can you see at all?"

    ignis "..."

    ignis "No. Not yet, at any rate. Time will tell."

    you "What even ... what even happened back there? At the altar?"

    ignis "We should save the questions for outside. Focus on getting out first. We don't want this ship to take off with us still on it."

    you "Yeah, good point."


    jump escaping_dropship

label escaping_dropship:

    narrator1 "When you get to the loading bay, your heart falls as you find it filled with a small cadre of Magitek Troopers."

    narrator1 "The things are moving boxes about in their peculiar staccato fashion, seeming somewhat detached from their surroundings."

    narrator1 "They're far enough away that you can both whisper to each other, even move slightly without alerting their attention, but they also happen to be using the hatch, your only exit."

    ignis "What are they doing?"

    you "They're sorting boxes. We're in the loading bay."

    ignis "Ah. He must be planning to leave soon."

    narrator1 "Your heart thuds. You really, {i}really{/i} don't want to end up in Niflheim."

    you "There's a door to the right. We can't leave until they turn their backs."

    you "I think we'll get a clear shot once they're done loading up."

    ignis "It sounds like it shall be a small window of opportunity. Are you prepared?"

    narrator1 "You inhale deeply."

    you "Yes."

    ignis "Good. I'm grateful I can count on you, [your_name]."

    ignis "But for now, it seems we have to wait."

    you "Do you mind telling me what was going on at the altar? I only saw the end of it but I ... I'm a bit confused."

    you "I'm sorry if it's too much."

    ignis "No, not at all. The Chancellor is far more powerful than I realised."

    ignis "I had to tap into the power of the Lucian kings to even stand a chance against him."

    if ignis_revealed_suspicions == "True":
        you "That thing you said earlier, about something else being at play... Is this what you meant?"

        ignis "Indeed it is."
    else:
        ignis "I had been suspicious for a long time that someone had hidden motivations ... now I know who it is."

    ignis "I still don't know enough about {i}why{/i}, though. I still don't know his end game."

    you "Why did he not simply kill you?"



    you "I'll give him hell if I ever see him again!"

    narrator1 "You're aware you're clenching your fists, but you don't want to stop."

    you "How dare he... How dare he do {i}this{/i} to you!"

    ignis "About that..."

    ignis "My injuries were not caused by Ardyn."

    ignis "This was the ... price ... for tapping into the Power of Kings."

    narrator1 "He sounds so small, suddenly, and you want to hug him."

    menu:
        "Hug":
            narrator1 "You hug him"

        "Do not hug":
            narrator1 "He probably needs his space. You don't want to surprise him the wrong way, especially not if he's in pain."

    ignis "He — I had no choice — He was going to hurt Noct."

    ignis "I couldn't let that happen!"

    narrator1 "You can't bear hearing him so torn-up over this. There's such an ugly mix of emotions there; shame, weakness, failure, fear for his young charge."

    menu:
        "Reassure him that Noctis is safe for now":
            you ""
        "Tell him he did the right thing":
            you ""

        "Say nothing, but console him instead":
            you ""

    you "So that purple light was... Oh, gods..."

    narrator1 "You don't quite know what to say after this revelation, so you fall to deflection."

    you "I thought the Power of Kings was a myth."

    ignis "Once upon a time, I thought the same of Leviathan."

    you "Heh. You know, the older I get, the more the world seems a surprising place."

    ignis "More terrifying and more beautiful than I ever could have imagined."

    narrator1 "That phrase settles in your soul comfortably. He's right, absolutely right, and it seems such a bitterly hopeful thing to say in the circumstances."

    ignis "Are they leaving?"

    you "Mm."

    ignis "[your_name]..."

    narrator1 "There's a worried tinge to his voice, and seconds later it's accompanied by his fingers searching for yours. You bite back the raw feeling in your chest as you realise he's scared."

    narrator1 "It must be awful. For someone so capable to be suddenly cast out of power, helpless and in darkness."

    narrator1 "You can't imagine what it must feel like."

    narrator1 "But you don't need to waste precious seconds trying to put yourself in his shoes. The way lies open, and it's your responsibility to see him to safety now."

    you "Okay, hold on to my hand. Let's go."

    menu:
        "Make a dash for it":
            narrator1 "You make a mad dash for the door, pulling Ignis along behind you. He's not expecting the force of it, if his rushed intake of breath is anything to go by."
            narrator1 "On the way out, you both knock aside a few crates, which make a real din, but you pay it no mind, stumbling out on shaky, adrenaline-pumped legs."
        "Go a little slower but more safely":
            narrator1 "You don't dash for the door, but instead walk carefully, full of determination, round every obstacle. You figure, with Ignis in the state he's in, it's not going to be any faster to run wildly."

    narrator1 "The outdoors seems so achingly bright, despite the fact the clouds still hang dark and heavy over the besieged city."

    narrator1 "You don't stop here. You were far too loud back there; you've got to drag Ignis much more than a stone's throw away before you're comfortable letting either of you catch your breath."

    you "I can't believe we actually made it!"

    you "Whew! Oh man... Ohhhhh man."

    ignis ""

    ignis "Now, I must check on Noct."

    narrator1 "You help him back to the altar, where you hope Ravus still stands waiting."

    jump altar_aftermath
