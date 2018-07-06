#starting scene
#contains labels:
    # start
    # mc_room
    # to_work

# covers scene setup, location fn tutorial


# use this start label to test things
label startn:

    #starting variables

    $ ignis_name = "Ignis"

    $ your_name = "Ilia"
    $ your_gender= "female"
    $ your_pronoun_subject= "She's"
    $ your_pronoun_possessive = "hers"
    $ your_pronoun_object = "her"
    $ you_gender_nicename = "woman"
    $ you_gender_nickname = "lass"

    $ ravus_name = "White-haired man"
    $ ardyn_name = "Sinister man"

    $ show_happiness = False

    $ happiness = 18
    $ ravus_happiness = 0
    $ ardyn_happiness = 0

    $ ignis_wants_to_sightsee = False

    $ citizens_first = False
    $ said_you_saved_citizens = False
    $ waited = False

    $ examined_harpoon = False

    $ ignis_favourite_food_known = False
    $ ignis_revealed_suspicions = False
    $ motivation = "help"
    $ ignis_opened_up = False
    $ extra_item = "water"

    $ ardyn_affiliation = "none"

    $ discovered = False
    $ number_of_encounters = 0
    $ shone_torch = False
    $ used_sword = False
    $ seen_ardyn_aboard_dropship_already = False
    $ deactivated_generator = False
    $ origin_label = "loading_bay"

    $ reached_chapter_three = True

    $ chose_tea = False
    $ chose_window = False
    $ chose_sleep = False

    $ noctis_friendly = False

    $ want_to_reset = False
    $ reset_game_once = None

    show screen gold_border

    $ show_happiness = True

    show bg restaurant

    show ignis smile at right

    ignis "Well now ... I wonder if they have seafood paella on the menu..."

    jump time_for_a_redo



# The game starts here.
label start:

    #starting variables
    $ ignis_name = "Stranger"
    $ your_name = "You"
    $ ravus_name = "White-haired man"
    $ ardyn_name = "Sinister man"

    $ happiness = 1
    $ show_happiness = False

    # set a default gender
    $ your_gender= "female"
    $ your_pronoun_subject= "She's"
    $ your_pronoun_possessive = "hers"
    $ your_pronoun_object = "her"
    $ you_gender_nicename = "woman"
    $ you_gender_nickname = "lass"
    $ you_gender_poshname = "the lady"

    $ show_happiness = False
    $ happiness = 1
    $ ravus_happiness = 0
    $ ardyn_happiness = 0

    $ ignis_wants_to_sightsee = False

    $ citizens_first = False
    $ said_you_saved_citizens = False
    $ waited = False

    $ examined_harpoon = False

    $ ignis_favourite_food_known = False
    $ ignis_revealed_suspicions = False
    $ motivation = "help"
    $ ignis_opened_up = False
    $ extra_item = "water"

    $ ardyn_affiliation = "none"

    $ discovered = False
    $ number_of_encounters = 0
    $ shone_torch = False
    $ used_sword = False
    $ seen_ardyn_aboard_dropship_already = False
    $ deactivated_generator = False
    $ origin_label = "loading_bay"

    $ reached_chapter_three = None

    $ chose_tea = False
    $ chose_window = False
    $ chose_sleep = False

    $ noctis_friendly = False

    $ want_to_reset = False
    $ reset_game_once = None

    $ ignis_buys_flower = False
    $ restaurant_choice = None

    # starts from here #

    scene black

    $ renpy.music.set_volume(0.4, delay=1, channel='music')

    pause 1.0
    play music bated_breath loop
    pause 1.0
    top_narrator "{size=20}{cps=15}{alpha=0.8}What does  {/alpha}{/cps}{/size}{alpha=1.0}{size=22}{cps=10}loyalty{/cps}{/size}{/alpha}{size=20}{cps=15}{alpha=0.8}  mean to you?{/alpha}{/cps}{/size}"

    topcentre_narrator "{size=20}{cps=15}{alpha=0.8}Who do you most want to protect?{/alpha}{/cps}{/size}"

    centre_narrator "{size=20}{cps=15}{alpha=0.8}It's not an easy question. The answer can  {/alpha}{/cps}{/size}{alpha=1.0}{size=22}{cps=10}change.{/alpha}  {size=20}{cps=15}{alpha=0.8}And you may surprise yourself.{/alpha}{/cps}{/size}"

    centrebottomright_narrator "{size=20}{cps=15}{alpha=0.8}Sometimes, {/alpha}{/cps}{/size}{size=22}{cps=10}{alpha=1.0}all it takes is one day.{/alpha}{/cps}{/size}"

    centered_titles "{cps=15}{size=26}Chapter One\n\n{/size}{p=0.5}{size=36}Awaken {/size}{/cps}"

    jump covenant_morning



label covenant_morning:

    $ renpy.music.set_volume(0.4, delay=1, channel='ambient')
    $ renpy.music.set_volume(1.0, delay=1, channel='foley')
    $ renpy.music.set_volume(1.0, delay=1, channel='foley2')

    stop music fadeout 2.286

    show screen gold_border
    scene bg altissian_skyline
    with Dissolve(1.5)

    play ambient morning_coffee1 fadein 2.286
    play foley birdsong1 fadein 4.0

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}Altissia, on the day of the Covenant.{/outlinecolor}{/alpha}{nw}" with Dissolve(0.5)

    $ quick_menu = True

    narrator1 "Altissia, on the day of the Covenant."

    narrator1 "The sky is a pale pastel glow, and birds call out from the terracotta rooftops, but despite this, the atmosphere is tense. You can feel it around you, thick as syrup."

    narrator1 "Today is the day that the Oracle, Lady Lunafreya, summons a goddess."
    narrator1 "Leviathan. The stuff of legends."
    narrator1 "You remember the stories. The prayers. You never thought you would see this in the flesh."

    narrator1 "An important day, indeed."

    scene black
    $ quick_menu = False

    stop foley fadeout 0.3

    centered "So it really doesn't help that today, of all days, you are late to work."

    jump mc_room



label mc_room:

    scene bg mc_room
    show screen keys_inactive

    play foley out_of_bed noloop
    $ quick_menu = True

    you "Ah, where did I put my keys?" with vpunch

    you "Y'know, it would be {i}really{/i} useful if I could just ... find them ..."

    jump find_keys



label find_keys:

    # this will teach you the 'find things' mechanic
    call screen infobubble(title="Locate the keys", content="Move your mouse around the room to find the keys, and click to pick them up.", confirmation="Got it")

    hide screen infobubble
    hide screen keys_inactive

    call screen keys




label citizens_test:

    show bg evacuee hideout dark with Dissolve(0.3)

    # rising sound of people chatting / murmuring

    show citizens dark
    with dissolve

    show citizens scared
    with dissolve

    citizen1 "So why isn't this damn game ready yet?"

    show citizens sceptical

    citizen3 "I know, right? I wanna hug Ignis!"

    show citizens reasonable

    citizen2 "Well, I hear there's a lot of artwork to create."

    show citizens sceptical

    citizen3 "Oh, like that street artist? I like her - "

    show citizens scared

    citizen1 "What, the one that drew the weirdass banana on that woman's face?"

    show citizens sceptical

    citizen3 "Yeah, her!"

    show citizens reasonable

    citizen2 "Yeah... uh... Not quite like that."

    show citizens sceptical

    citizen3 "Well, I guess we'll just wait another week then."

    show citizens scared

    citizen1 "UGGGHHHH"

    show citizens scared

    citizen1 "Fine!"

    hide citizens
    with dissolve

    call screen infobubble(title="THE GAME IS COMING SOON, FOLKS!", content="Life got in the way, but just a little longer and I'll make this thing the best I can!", confirmation="Got it")

    hide screen infobubble

    hide bg evacuee hideout dark
    with dissolve

    return

    jump escort_to_jetty


label ignis_animation_reel:

    show bg rubblestreet with Dissolve(0.3)

    show ignis neutral with dissolve

    pause 0.4

    show ignis neutral eyesclosed with dissolve

    pause 0.4

    show ignis neutral openmouth with dissolve

    pause 0.4

    show ignis neutral openmouth eyesclosed with dissolve

    pause 0.4

    show ignis smile with dissolve

    pause 0.4

    show ignis smile eyesclosed with dissolve

    pause 0.4

    show ignis touching glasses with dissolve

    pause 0.4

    show ignis touching glasses eyesclosed with dissolve

    pause 0.4

    show ignis unimpressed with dissolve

    pause 0.4

    show ignis unimpressed eyesclosed with dissolve

    pause 0.4

    show ignis unimpressed openmouth with dissolve

    pause 0.4

    show ignis unimpressed openmouth eyesclosed with dissolve

    pause 0.4

    show ignis sidelong with dissolve

    pause 0.4

    show ignis sidelong openmouth with dissolve

    pause 0.4

    show ignis sidelong direct with dissolve

    pause 0.4

    show ignis sidelong direct openmouth with dissolve

    pause 0.4

    #######

    show ignis neutral wet with dissolve

    pause 0.4

    show ignis neutral eyesclosed wet with dissolve

    pause 0.4

    show ignis neutral openmouth wet with dissolve

    pause 0.4

    show ignis neutral openmouth eyesclosed wet with dissolve

    pause 0.4

    show ignis smile wet with dissolve

    pause 0.4

    show ignis smile eyesclosed wet with dissolve

    pause 0.4

    show ignis touching glasses wet with dissolve

    pause 0.4

    show ignis touching glasses eyesclosed wet with dissolve

    pause 0.4

    show ignis unimpressed wet with dissolve

    pause 0.4

    show ignis unimpressed eyesclosed wet with dissolve

    pause 0.4

    show ignis unimpressed openmouth wet with dissolve

    pause 0.4

    show ignis unimpressed openmouth eyesclosed wet with dissolve

    pause 0.4

    show ignis sidelong wet with dissolve

    pause 0.4

    show ignis sidelong openmouth wet with dissolve

    pause 0.4

    show ignis sidelong direct wet with dissolve

    pause 0.4

    show ignis sidelong direct openmouth wet with dissolve

    pause 0.4

    show ignis neutral blind with dissolve

    pause 0.4

    show ignis neutral openmouth blind with dissolve

    pause 0.4

    show ignis smile blind with dissolve

    pause 0.4

    show ignis unimpressed blind with dissolve

    pause 0.4

    show ignis unimpressed openmouth blind with dissolve

    pause 0.4

    show ignis pain blind with dissolve

    pause 0.4

    show ignis pain openmouth blind with dissolve

    pause 0.4

    show ignis happy blind with dissolve

    pause 0.8

    hide ignis with dissolve

    hide bg with dissolve
