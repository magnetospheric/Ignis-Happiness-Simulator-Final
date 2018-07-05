
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       boom.rpy [When discovered by troopers]
#       screen which handles discovery conditions when stealth fails during
#       dropship mission
#
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


label boom:

    $ discovered = True
    # DISCOVERED val basically gives different flavour text during the traversal of the ship

    # IF lost_trooper_fight = TRUE at any point, option to sabotage ardyn's ship is lost
    # IF lost_trooper_fight = TRUE at any point, ability to get max happiness is lost
    # all NON-CRACK endings can still be obtained no matter the WINS and LOSSes


    # play screeching sound effect
    $ renpy.music.set_volume(0.3, delay=0, channel='foley')
    $ renpy.music.set_volume(0.3, delay=0, channel='foley2')
    play foley trooper_screech noloop
    show trooper dropship at center with fastesthardflash

    you "!!" with vpunch

    narrator1 "You've been discovered!"

    play foley2 trooper_screech2 noloop
    narrator1 "The trooper lunges toward you with a horrifying screech."

    narrator1 "You're terrified it will alert the others. So you..."

    # FIRST ENCOUNTER:
    #   shining torch in its eyes gets you a WIN
    #   using the sword gets you a LOSS

    if number_of_encounters == 0:
        $ number_of_encounters += 1
        menu:
            "Shine the torch in its eyes":
                $ shone_torch = True
                narrator1 "You react instantly, shining your torch into the thing's eyes." with fastsoftflash
                narrator1 "Amazingly, this works. The trooper stumbles backwards, temporarily blinded."
                narrator1 "In the inertia, you have enough time to overpower it with your sword, running through its red glowing core."
                $ renpy.jump(won_fight_label)
            "Strike it with your sword":
                $ used_sword = True
                narrator1 "A swing and a miss... Your sword clangs harshly against the trooper's armour."
                narrator1 "Before you know it, a metal fist collides against your skull and everything goes dark."
                $ lost_trooper_fight = True
                $ renpy.jump(lost_fight_label)

    # SECOND ENCOUNTER:
    #   if you shone the torch the first time,
    #       shining the torch gets you a LOSS
    #       and using the sword gets you a WIN
    #   if you used the sword the first time,
    #       shining the torch still gets you a LOSS
    #       and using the sword still gets you a WIN
    #       but the TEXT is different

    elif number_of_encounters == 1:
        if shone_torch == True:
            menu:
                "Try shining the torch in its eyes again":
                    $ shone_torch = True
                    narrator1 "You try the same move as before, shining the torch into the trooper's face." with fastsoftflash
                    narrator1 "But this one doesn't seem to react much to the light."
                    narrator1 "You gasp, and fumble for your sword, but..."
                    narrator1 "The trooper is faster. A metal fist collides against your skull and everything goes dark."
                    $ lost_trooper_fight = True
                    $ renpy.jump(lost_fight_label)
                "Use your sword instead":
                    $ used_sword = True
                    narrator1 "You don't want to rely on using the flashlight again - it seems like a fluke that it even worked."
                    narrator1 "So you drop the torch, and the noise distracts the trooper long enough for you to pull your sword from your belt, and drive the point through its exposed core."
                    $ renpy.jump(won_fight_label)
        else:
            menu:
                "Shine the torch in its eyes":
                    $ shone_torch = True
                    narrator1 "You react instantly, shining your torch into the thing's eyes." with fastsoftflash
                    narrator1 "Amazingly, this works. The trooper stumbles backwards, temporarily blinded."
                    narrator1 "In the inertia, you have enough time to overpower it with your sword, running through its red glowing core."
                    narrator1 "Before you know it, a metal fist collides against your skull and everything goes dark."
                    $ lost_trooper_fight = True
                    $ renpy.jump(lost_fight_label)
                "Use your sword again - faster this time!":
                    $ used_sword = True
                    narrator1 "You're not going to miss again. You move faster this time, parrying the trooper's blow with your sword."
                    narrator1 "Your next strike hits it right in the core, and the thing shrieks and collapses to dust."
                    narrator1 "You're left there, breathless, giddy that it worked this time."
                    $ renpy.jump(won_fight_label)

    # THIRD ENCOUNTER:
    #   if you shone the torch at all before,
    #       shining the torch gets you a LOSS
    #       and using the sword gets you a WIN
    #   if you used the sword at all before,
    #       shining the torch gets you a WIN
    #       and using the sword gets you a LOSS
    #   dodging always gets you a WIN

    else:
        $ number_of_encounters += 1
        narrator1 "You're getting real tired of this by now."

        if lost_trooper_fight == False:
            narrator1 "You haven't lost a fight yet, and you don't plan on doing so."
        else:
            narrator1 "You don't want to lose again. This might be your last chance."

            if shone_torch == True and used_sword == True:
                menu:
                    "Try shining the torch in its eyes ... again?":
                        narrator1 "You try the same move as before, shining the torch into the trooper's face." with fastsoftflash
                        narrator1 "But this one doesn't seem to react much."
                        narrator1 "You gasp, and fumble for your sword, but..."
                        narrator1 "The trooper is faster. A metal fist collides against your skull and everything goes dark."
                        $ lost_trooper_fight = True
                        $ renpy.jump(lost_fight_label)
                    "Reach for your sword ... again?":
                        $ used_sword = True
                        narrator1 "A swing and a miss... Your sword clangs harshly against the trooper's armour."
                        narrator1 "Before you know it, a metal fist collides against your skull and everything goes dark."
                        $ lost_trooper_fight = True
                        $ renpy.jump(lost_fight_label)
                    "Just dodge":
                        narrator1 "You don't spare any time for counterattacks. You dodge instead, slipping under the trooper's arm in mid-swing."
                        narrator1 "It stumbles forward and you run in the opposite direction, hiding beneath the first thing you find."
                        narrator1 "Whether it's a crate or a shelving unit, you can't really tell. You just lay low as the trooper searches the room."
                        narrator1 "It's confused. It can't figure out where you've gone."
                        narrator1 "You wait with bated breath until the trooper has left."
                        narrator1 "That was ... far too close for comfort."
                        narrator1 "But you made it."
                        $ renpy.jump(won_fight_label)
            elif shone_torch == True and used_sword == False:
                menu:
                    "Try shining the torch in its eyes ... again?":
                        narrator1 "You try the same move as before, shining the torch into the trooper's face." with fastsoftflash
                        narrator1 "But this one doesn't seem to react much."
                        narrator1 "You gasp, and fumble for your sword, but..."
                        narrator1 "The trooper is faster. A metal fist collides against your skull and everything goes dark."
                        $ lost_trooper_fight = True
                        $ renpy.jump(lost_fight_label)
                    "Reach for your sword":
                        $ used_sword = True
                        narrator1 "You drop the torch, and the noise distracts the trooper long enough for you to pull your sword from your belt, and drive the point through its exposed core."
                        $ renpy.jump(won_fight_label)
                    "Just dodge":
                        narrator1 "You don't spare any time for counterattacks. You dodge instead, slipping under the trooper's arm in mid-swing."
                        narrator1 "It stumbles forward and you run in the opposite direction, hiding beneath the first thing you find."
                        narrator1 "Whether it's a crate or a shelving unit, you can't really tell. You just lay low as the trooper searches the room."
                        narrator1 "It's confused. It can't figure out where you've gone."
                        narrator1 "You wait with bated breath until the trooper has left."
                        narrator1 "That was ... far too close for comfort."
                        narrator1 "But you made it."
                        $ renpy.jump(won_fight_label)
            else: # shone torch must be false and used sword must be true in this case
                menu:
                    "Shine the torch in its eyes":
                        $ shone_torch = True
                        narrator1 "You react instantly, shining your torch into the thing's eyes." with fastsoftflash
                        narrator1 "Amazingly, this works. The trooper stumbles backwards, temporarily blinded."
                        narrator1 "In the inertia, you have enough time to overpower it with your sword, running through its red glowing core."
                        $ renpy.jump(won_fight_label)
                    "Reach for your sword ... again?":
                        $ used_sword = True
                        narrator1 "A swing and a miss... Your sword clangs harshly against the trooper's armour."
                        narrator1 "Before you know it, a metal fist collides against your skull and everything goes dark."
                        $ lost_trooper_fight = True
                        $ renpy.jump(lost_fight_label)
                    "Just dodge":
                        narrator1 "You don't spare any time for counterattacks. You dodge instead, slipping under the trooper's arm in mid-swing."
                        narrator1 "It stumbles forward and you run in the opposite direction, hiding beneath the first thing you find."
                        narrator1 "Whether it's a crate or a shelving unit, you can't really tell. You just lay low as the trooper searches the room."
                        narrator1 "It's confused. It can't figure out where you've gone."
                        narrator1 "You wait with bated breath until the trooper has left."
                        narrator1 "That was ... far too close for comfort."
                        narrator1 "But you made it."
                        $ renpy.jump(won_fight_label)

    return
