#starting scene
#contains labels:
    # start
    # mc_room
    # to_work

# covers scene setup, location fn tutorial


# use this start label to test things
label start:

    #starting variables

    $ ignis_name = "Ignis"

    $ your_name = "Ilia"
    $ your_gender= "female"
    $ your_pronoun_subject= "she"
    $ your_pronoun_possessive = "hers"
    $ your_pronoun_object = "her"
    $ you_gender_nicename = "woman"
    $ you_gender_nickname = "lass"

    $ show_happiness = False

    $ happiness += 5

    $ citizens_first = False

    narrator1 "small test text before transition"

    jump citizens_test

    # #shows the first background
    # scene bg altissia_alleyway
    #
    # #shows the first character
    # show ignis neutral
    # with dissolve
    #
    # "Altissia, on the day of the Covenant. Everything is going to hell."
    #
    # ignis "I've run into a bit of trouble. Would you care to help me?"
    #
    # ignis "Look around this room and see if there's anything useful."
    #
    # call screen flashlight

# The game starts here.
label startn:

    # start scene needs to introduce the hunting-around mechanic for later
    # maybe protag is looking for their keys or something that'll be useful later

    #starting variables
    $ ignis_name = "Stranger"
    $ your_name = "You"
    $ ravus_name = "White-haired man"
    $ ardyn_name = "Sinister man"

    $ happiness = 1
    $ show_happiness = False

    #jump first_conversation

    #black background, maybe some wisping smoke
    scene black


    top_narrator "{size=20}{cps=15}{alpha=0.8}What does  {/alpha}{/cps}{/size}{alpha=1.0}{size=22}{cps=10}loyalty{/cps}{/size}{/alpha}{size=20}{cps=15}{alpha=0.8}  mean to you?{/alpha}{/cps}{/size}"

    topcentre_narrator "{size=20}{cps=15}{alpha=0.8}Who do you most want to protect?{/alpha}{/cps}{/size}"

    centre_narrator "{size=20}{cps=15}{alpha=0.8}It's not an easy question. The answer can  {/alpha}{/cps}{/size}{alpha=1.0}{size=22}{cps=10}change.{/alpha}  {size=20}{cps=15}{alpha=0.8}And you may surprise yourself.{/alpha}{/cps}{/size}"

    centrebottomright_narrator "{size=20}{cps=15}{alpha=0.8}Sometimes, {/alpha}{/cps}{/size}{size=22}{cps=10}{alpha=1.0}all it takes is one day.{/alpha}{/cps}{/size}"


    #scene dawns on an overview of altissia
    #slow fade in
    scene bg altissian_skyline
    with fastfade


    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}Altissia, on the day of the Covenant.{/outlinecolor}{/alpha}{nw}" with Dissolve(0.5)

    $ quick_menu = True

    narrator1 "Altissia, on the day of the Covenant."

    narrator1 "The sky is a pale pastel glow, but despite this, the atmosphere is tense. You can feel it around you, thick as syrup."

    narrator1 "Today is the day that the Oracle, Lady Lunafreya, summons a goddess."
    narrator1 "Leviathan. The stuff of legends."
    narrator1 "You remember the stories. The prayers. You never thought you would see this in the flesh."

    narrator1 "An important day, indeed."

    scene black

    centered "So it really doesn't help that today, of all days, you are late to work."

    jump mc_room



label mc_room:

    scene bg mc_room
    show screen keys_inactive
    #set up button here but don't make it clickable

    # show screen infobubble(title="Locate the keys")

    you "Ah, where did I put my keys?" with vpunch

    # main room view
    # would be cool to have a shaking effect here

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
