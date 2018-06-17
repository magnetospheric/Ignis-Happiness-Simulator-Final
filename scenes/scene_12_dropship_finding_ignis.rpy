#Scene 12
#Dropship Rescue

#contains labels:
    # entering_dropship
    # loading_bay
    # loading_bay_success
    # loading_bay_discovered
    # dropship_corridor01
    # finding_ignis_cell

#contains screens:
    # flashlight_dropship_hangar
    # flashlight_dropship_corridor01

# covers heading to the altar, reaching it and seeing ardyn take ignis away, and talking to ravus for the first time



label entering_dropship:

    show bg dropship exterior with Dissolve(0.3)

    pause(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "The dropship is not as heavily-guarded as you expect, with only two Magitek Troopers listlessly padding about the front."

    you "The dropship is not as heavily-guarded as you expect, with only two Magitek Troopers listlessly padding about the front."

    narrator1 "It's bigger than the other dropships you've seen around, but not quite as large as the Imperial Dreadnoughts that still hang in the sky."

    narrator1 "Perhaps this is Ardyn Izunia's personal ship?"

    narrator1 "Your heart's beating far too fast as you circle round the side of the thing first, looking for a way to enter that's not quite so out-in-the-open."

    show bg dropship exterior door with dissolve

    narrator1 "There; a side door that's been left open, a box of discarded crates next to it."

    narrator1 "Whoever's been doing the unloading has obviously been sidetracked by more pressing matters."

    narrator1 "You take advantage of the opportunity, slipping inside before you can be noticed."

    jump loading_bay



label loading_bay:

    show bg dropship loading bay
    show screen black_overlay
    with dissolve

    #when inside the dropship, have atmospheric creaking and industrial sounds

    narrator1 "It's so dark in here. Your foot bumps into something hard. A crate, like the ones at the door."

    narrator1 "This must be the loading bay."

    narrator1 "You try to edge forward, and bump into another crate. Then you remember you still have the torch."

    narrator1 "Dare you turn it on? You have no idea if anyone else is in this room or not..."

    narrator1 "It doesn't sound like it, but then again, Magitek Troopers are hardly human, are they? They can be still as stone statues for all you know."

    narrator1 "Clutching the torch in hand, you let your thumb hover above the 'On' switch."

    narrator1 "It's time to make it through the loading bay."

    call screen infobubble(title="Get to Ignis", content="Use the torch to find a way forward. \nCareful though: keeping it on too long will alert the Magitek Troopers!", confirmation="Okay")

    hide screen infobubble
    hide screen black_overlay

    $ won_fight_label = "loading_bay_success"
    $ lost_fight_label = "loading_bay_discovered"

    show bg dropship loading bay
    call screen flashlight_dropship_hangar



screen flashlight_dropship_hangar:
    add Flashlight(
                    timer=True,
                    button_idle_image="images/items/loading-bay-door-idle.png",
                    button_hover_image="images/items/loading-bay-door.png",
                    buttonPosX=103,
                    buttonPosY=355,
                    jump_destination="dropship_corridor01",
                    size="small"
                )



label loading_bay_success:

    show trooper dropship shortcircuit at center with dissolve

    narrator1 "The trooper collapses to the ground, a dying gasp echoing in the tinny corridor."

    hide trooper with dissolve

    show screen black_overlay

    narrator1 "You freeze, flashlight off, tense and waiting for any further activity." with fastsoftflash

    narrator1 "But nobody comes running."

    narrator1 "Time to continue on."

    call screen infobubble(title="Try again", content="Remember to click the torch off if you sense a trooper coming! The red bar along the top shows how aware they are of your presence.", confirmation="Okay")

    hide screen infobubble
    hide screen black_overlay

    call screen flashlight_dropship_hangar



label loading_bay_discovered:

    narrator1 "You awaken amid a pile of rubble."

    narrator1 "The trooper that assaulted you is nowhere to be seen."

    you "Ow... my head..."

    narrator1 "It must have thought you were dead, perhaps?"

    narrator1 "Or part of the cargo?"

    narrator1 "Either way, it's time you continued on."

    call screen infobubble(title="Time to try again", content="Remember to click the torch off if you sense a trooper coming! The red bar along the top shows how aware they are of your presence.", confirmation="Okay")

    hide screen infobubble
    hide screen black_overlay

    call screen flashlight_dropship_hangar



label dropship_corridor01:

    narrator1 "In the corner of the room you find a door."

    narrator1 "You slip through."

    show bg dropship corridor1
    show screen black_overlay
    with dissolve

    if discovered == False:

        narrator1 "Nobody's seen you yet. So far so good."

    narrator1 "Your heart's thudding as you edge down the first corridor beyond the loading bay."

    narrator1 "Despite the low light, you can tell it's incredibly grimy in here."

    narrator1 "It feels... uncared for. And maybe that's because the Chancellor of Niflheim is more devoted to achieving his goals than in extraneous housekeeping?"

    narrator1 "That somehow seems a far scarier prospect than if he had kept the corridors squeaky clean."

    narrator1 "You grit your teeth, and continue."

    call screen blank_overlay()

    hide screen blank_overlay
    hide screen black_overlay

    $ won_fight_label = "loading_bay_success"
    $ lost_fight_label = "loading_bay_discovered"

    call screen flashlight_dropship_corridor01



screen flashlight_dropship_corridor01:
    add Flashlight(
                    timer=True,
                    button_idle_image="images/items/interior-corridor-1-door-idle.png",
                    button_hover_image="images/items/interior-corridor-1-door-hover.png",
                    buttonPosX=502,
                    buttonPosY=321,
                    jump_destination="finding_ignis_cell",
                    size="small"
                )



label finding_ignis_cell:

    show bg dropship cell
    show screen black_overlay
    show ignis unimpressed injured at left
    show cell bars
    with dissolve

    narrator1 "This next room you enter is even grimier than before. The humidity's clinging to the walls and you feel at once suffocated by it."

    narrator1 "There's something metal glinting in the low light. Bars?"

    narrator1 "Is this some kind of a cell?"

    narrator1 "In the shadows behind them, you think you can hear breathing."

    narrator1 "It doesn't sound like the troopers. It sounds more ... pained. More human."

    show ignis unimpressed injured at left
    show cell bars
    hide screen black_overlay
    with softflash

    narrator1 "You shine your torch briefly across the room and catch sight of that distinctive indigo patterned shirt."

    narrator1 "You rush to the door."

    you "Ignis!"

    narrator1 "The urge to shine the torch on him some more, to see him, is overwhelming, but you don't want to alert the soldiers to your presence."

    ignis "[your_name]? I thought I'd lost you in the square! What ... what are you doing here?"

    narrator1 "It's hard to keep your voice below a whisper, excited as you are to have found him."

    you "I came to rescue you!"

    narrator1 "There's a short silence while he processes your words."

    ignis "That ... was an incredibly risky thing to do, [your_name]. You could have been caught too."

    ignis "But I am grateful. Immensely so."

    narrator1 "He sounds so choked-up, so worn out. You steel yourself, and ask."

    you "Are you okay?"

    ignis "I..."

    ignis "I've been better."

    you "Is there anything I can do? Well, uh, aside from getting you out of there."

    ignis "I... I could do with some water, actually. My head... my throat, it's all..."

    if extra_item == "water":

        you "Oh! I have some right here!"

        narrator1 "You've never been more glad that you stopped to pick up that bottle in the cellar."

        narrator1 "You pass the water through the bars and Ignis accepts it with oddly fumbling hands."

        narrator1 "While he drinks, you run your hands over the door lock, feeling for a seam or something to exploit."

    else:

        you "I'll keep a lookout."

        you "But first, I gotta get you out of here."

        narrator1 "You run your hands over the door lock, feeling for a seam or something to exploit."

    narrator1 "There's nothing; only a gap for a key and not an inch of give between."

    ignis "It's rather surprising, really; I would have expected something a little more hi-tech."

    ignis "Perhaps our dear Chancellor simply has a penchant for the archaic."

    you "We need to find that key..."

    ignis "One moment - perhaps I can find something..."

    show bluelightning at SpriteLoc2(-0.11, -0.01) behind ignis with Dissolve(1.5)

    hide bluelightning with Dissolve(1.5)

    narrator1 "Again, that blue crackling and the faint smell of ozone filling the air."

    narrator1 "But no sooner does it spark than it sputters out. Ignis sighs."

    you "What was that light?"

    you "I saw it before when you killed that trooper."

    ignis "Ah, it's - royal magic. On loan, in effect, from the Line of Lucis."

    ignis "But ... I'm no longer strong enough to - agh!"

    narrator1 "He doubles over in pain."

    you "Hold on! Don't exert yourself any more, okay? I'm gonna try and find the key."

    narrator1 "You make for the door."

    ignis "All right. Take care, [your_name]. There's soldiers on rotation in the corridors beyond."

    if discovered == False:
        you "Some of them already got the jump on me on the way here."

        ignis "I see."

        you "I'll be more careful this time."

        ignis "Good to hear."

    you "Okay - I'll be careful."

    jump dropship_corridor02
