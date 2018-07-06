#Scene 16
#Date

#contains labels:
    # waitingforignis
    # street_musicians
    # eat_something_now
    # suggest_sightseeing
    # explore_the_park
    # totomostro


# this scene is triggered after the hotel conversation, if you have built up enough happiness points

label waitingforignis:

    # the music here should be like Peaceful Sleep in NieR

    stop ambient fadeout 2.286
    # play music andante fadein 2.286

    $ quick_menu = False

    scene black with Dissolve(1.5)

    centered "Eight o'clock swings round."

    centered "Are you ready?"

    pause 0.3

    scene bg listropark with Dissolve(2.0)

    $ quick_menu = True

    # faint rain sound effect

    narrator1 "Evening has fallen across Altissia. You're waiting by the sculpture at Listro Park, just as Ignis said."

    narrator1 "You still can't believe he wants to do this."

    show noctis silhouette at left
    show ignis silhouette blind at center
    with Dissolve(0.5)

    narrator1 "After a while, you spot him, that tall, svelte figure at the head of the stairs leading up to this place."

    narrator1 "He's accompanied by Prince Noctis."

    narrator1 "It's so odd, again, seeing the Prince out in the open like this, dressed down in ordinary clothing without any escort."

    narrator1 "At any rate, you're glad to see someone is helping him."

    narrator1 "The Prince pats his shoulder in solidarity, then vanishes back into the crowd."

    hide noctis with Dissolve(0.5)

    narrator1 "You take a deep breath, and walk over."

    pause 0.5

    show ignis neutral blind with Dissolve(0.5)

    pause 0.5

    you "Hi, Ignis."

    show ignis neutral openmouth blind
    ignis "A pleasure, [your_name]."
    show ignis neutral blind

    narrator1 "He's wearing the same shirt as ever, and its crisp, clean-pressed edges are turning slightly damp in the gentle rain."
    narrator1 "He doesn't look like he cares about that, though."

    you "How're you doing?"

    show ignis neutral openmouth blind
    ignis "Oh, I'm quite all right. Enjoying the fresh air. Feels good to feel the rain."
    show ignis neutral blind

    you "Same - it's really refreshing out here."

    show ignis neutral openmouth blind
    ignis "Well, then. Where shall we head first?"
    show ignis neutral blind

    narrator1 "You pause. You didn't exactly think this far."
    narrator1 "It's five in the evening. Maybe a little early for food? But you don't know when Ignis last ate."
    narrator1 "It feels like you should do some sightseeing together, but ... what to do without rubbing in the fact of his injury?"

    # format: buskers and hungry leads to eventually to explore, which leads on to restaurant if certain happiness achieved
    # see sights and totomostro lead to what?
    # I think they should also lead to restaurant and date IF certain happiness achieved...

    menu:
        "Suggest listening to the street musicians":

            jump street_musicians

        "Ask him if he's hungry":

            jump eat_something_now

        "See the sights":

            jump suggest_sightseeing

        "Explore Listro Park":

            you "How about we take a stroll around the Park?"

            show ignis smile blind with dissolve

            $ show_happiness = True

            pause 0.5

            $ happiness += 1

            show screen happiness_text(title="Happiness increased")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            ignis "That sounds lovely."

            narrator1 "You take his hand gently."

            jump explore_the_park

        "Mention the Totomostro games":

            jump totomostro



label street_musicians:

    you "What about those street musicians down there?"

    you "I heard them as I was coming up ..."

    you "I think they'd be quite nice to listen to."

    show ignis smile blind with dissolve
    ignis "Yes ... it really would."

    narrator1 "So you lead him down the steps, taking his hand gently."

    narrator1 "He clearly appreciates the help, because his hand grips yours warmly."

    you "Just a little farther..."

    show bg buskers with Dissolve(1.5)

    # stop music fadeout 2.286
    # play ambient listro_fandango fadein 2.286

    ignis "Is that a fandango rhythm I hear?"

    you "I ... I'm not really sure, to be honest."

    ignis "It's very nice."

    $ show_happiness = True

    pause 0.5

    $ happiness += 1

    show screen happiness_text(title="Happiness increased")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    ignis "Reminds me of something I heard in my youth."

    you "These guys are great - they're always playing round town. Really lifts the spirits."

    ignis "That it does."

    if ignis_wants_to_sightsee == True and happiness > 17:

        you "You mentioned you'd been to Altissia before, didn't you?"

        ignis "Yes, in my youth."

        narrator1 "He pauses."

        show ignis neutral openmouth blind
        ignis "Oh, I must have been, what - about ten years old?"
        ignis "I didn't get to explore that much."
        ignis "But I was a big fan of the classical guitar. I listened to all the Altissian forms - rondo, allegro, malagueña..."
        ignis "Always wanted to learn."
        show ignis neutral blind

        you "Did you ever get the chance?"

        show ignis neutral openmouth blind
        ignis "I {i}did{/i} ask my music tutors ..."
        show ignis neutral blind

        show ignis unimpressed openmouth blind
        ignis "They gave me a violin."
        show ignis unimpressed blind

        narrator1 "His pouting face seems so childish for someone so worldly, and it makes you laugh."

        show ignis neutral blind

        you "Sorry! Hehe... I'm just imagining little you being so miffed at your tutors."

        show ignis smile blind with dissolve
        pause 1.0
        show ignis neutral openmouth blind
        ignis "I was quite the little devil."
        show ignis neutral blind

        you "I think a lot of your violin skills would be easily transferable to guitar, you know."

        show ignis neutral openmouth blind
        ignis "Hmm ... maybe I should give it a go once I'm back in Lucis."
        show ignis neutral blind

        you "You really should!"

        show ignis smile blind with dissolve
        pause 1.0
        show ignis neutral openmouth blind
        ignis "I ... know I've said this before, [your_name], but you really are a very kind person, you know?"
        show ignis smile blind

        narrator1 "You can feel yourself blushing."

        narrator1 "The music continues, and you both fall back into contemplation."

    pause 0.5

    narrator1 "You spend a while together like this, not talking, merely listening."

    narrator1 "Ignis has his head tilted every so slightly; he's keenly attuned to every note."

    narrator1 "You're glad you brought him here."

    narrator1 "For these moments, you feel insulated against the world, but also, strangely, a part of it."

    narrator1 "It feels wonderful."

    narrator1 "Ignis grasps for your hand, and the guitar swells, and you somehow want to cry."

    narrator1 "There's a small part of your mind thinking {i}how ridiculous{/i}, and yeah, it is, kind of. But you wouldn't change it for the world."

    narrator1 "The music eventually dies down, and Ignis breaks his grip."

    # stop ambient fadeout 2.286

    show ignis neutral openmouth blind
    ignis "Thank you, [your_name]."
    show ignis neutral blind

    you "I'm glad you liked it."

    narrator1 "Ignis sighs contentedly, then sorts his collar and turns to face the park again."

    show ignis neutral openmouth blind
    ignis "Let's take a stroll."
    show ignis neutral blind

    you "Sure!"

    narrator1 "You take his hand once again, and lead him back to Listro Park."

    scene bg listropark
    show ignis smile blind at center
    with Dissolve(1.0)

    # play music andante fadein 2.286

    jump explore_the_park



label suggest_sightseeing:

    if ignis_wants_to_sightsee == True:
        you "Well ... you mentioned before that you wanted to go sightseeing?"
    else:
        you "Do you wanna do a bit of sightseeing?"

    show ignis unimpressed blind with dissolve

    $ show_happiness = True

    pause 0.5

    $ happiness -= 1

    show screen happiness_text(title="Happiness decreased")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    narrator1 "Ignis sighs."

    show ignis unimpressed openmouth blind
    ignis "I'm ... afraid I wouldn't get much out of that..."
    show ignis unimpressed blind

    narrator1 "You wince."
    narrator1 "A poor choice of words, on your part."

    you "Sorry."

    show ignis neutral openmouth blind
    ignis "Not to worry. Should we ... perhaps take a stroll around the park for a bit?"
    show ignis neutral blind

    narrator1 "You nod."

    narrator1 "He takes your hand, and you walk around the statue."

    jump explore_the_park



label eat_something_now:

    you "It's not too early for something to eat, is it?"

    show ignis neutral openmouth blind
    ignis "I suppose I could go for something small..."
    ignis "I'm not overly hungry yet, however."
    show ignis neutral blind

    you "Hmm, in that case..."
    you "What about ... gelato?"

    show ignis smile blind

    $ show_happiness = True

    pause 0.5

    $ happiness += 1

    show screen happiness_text(title="Happiness increased")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    ignis "That sounds lovely."

    show bg foodcart with Dissolve(1.5)

    narrator1 "You walk over to the gelato cart. The guy behind the counter smiles and asks you both what your favourite flavour is."

    show ignis neutral openmouth blind
    ignis "Oh, um ..."
    ignis "Do you have any orange flavour?"
    ignis "Mandarin? Or tangerine would do."
    show ignis neutral blind

    narrator1 "The vendor nods and checks his stock, before filling a cone with two generous scoops."

    narrator1 "What will you have?"

    menu:
        "Mint":
            you "Mint, please!"
            narrator1 "Nothing beats mint - so fresh, so springy, so relaxing."
            narrator1 "The green ice-cream is flecked with dark chocolate. Delicious."
        "Tangerine":
            you "Tangerine, please!"
            show ignis smile blind
            narrator1 "You join Ignis with the citrus-flavoured ice cream. It's tangy and summery and simply perfect for the evening at hand."
        "Vanilla":
            you "Vanilla, please!"
            narrator1 "You get a vanilla cone, with a few sprinkles on top. It's light and sweet and oh-so delicious."
        "Licorice":
            you "Licorice, please!"
            $ ardyn_happiness += 1
            narrator1 "The licorice ice cream is dark as galaxies, and salty-sweet."

    narrator1 "You and Ignis eat your ice cream while standing at the park balcony."

    narrator1 "It's a lookout point for the city, and while you enjoy the sight, Ignis enjoys the breeze."

    narrator1 "Eventually you're both finished with your ice cream, and while you lick your fingers, Ignis produces a handkerchief from his breast pocket and tidies off."

    show ignis neutral openmouth blind
    ignis "Well, that was delicious."

    if reached_chapter_three == True:
        ignis "As I said before, Altissia is famed for its cuisine, after all."

    ignis "Shall we take a stroll?"
    show ignis neutral blind

    narrator1 "You nod."

    you "Sure. Let's go!"

    narrator1 "You take his hand, and head back around the Park."

    scene bg listropark
    show ignis smile blind at center
    with Dissolve(1.0)

    jump explore_the_park



label totomostro:

    you "You know, the Totomostro games have started back up again."

    show ignis neutral openmouth blind
    ignis "They have? My, that's rather soon."
    ignis "I suppose the people need a distraction, though."
    show ignis neutral blind

    you "Do you want to go?"

    show ignis unimpressed blind with dissolve

    $ show_happiness = True

    pause 0.5

    $ happiness -= 1

    show screen happiness_text(title="Happiness decreased ever so slightly")
    with dissolve
    pause 0.3
    hide screen happiness_text
    with dissolve

    show ignis unimpressed openmouth blind with dissolve
    ignis "Ah ... I'm afraid it's not really my thing."
    ignis "I don't get a lot of enjoyment out of it."
    show ignis unimpressed blind with dissolve

    menu:
        "Apologise, and suggest something else":

            you "Oh ... sorry."

            show ignis neutral openmouth blind
            ignis "Not at all. I can see the attraction - Noct and Prompto had a whale of a time there, in the days before the ceremony."
            ignis "Prompto wouldn't stop playing that blasted horn, though."
            show ignis neutral blind

            narrator1 "He touches the side of his head at the memory."

            narrator1 "You laugh."

            you "Heh, it {i}does{/i} get quite loud!"

            you "So, how about something else, then?"

            show ignis smile blind with dissolve

            $ show_happiness = True

            pause 0.5

            $ happiness += 1

            show screen happiness_text(title="Happiness increased")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            show ignis neutral openmouth blind
            ignis "What have you in mind?"
            show ignis neutral blind

            you "I don't know ... hmm, let's take a stroll around the park."

            show ignis smile blind with dissolve

            narrator1 "You take his hand, and you walk around the statue."

        "Try and convince him":

            you "C'mon, it'll be fun!"

            show ignis unimpressed blind with dissolve

            $ show_happiness = True

            pause 0.5

            $ happiness -= 1

            show screen happiness_text(title="Happiness decreased ever so slightly")
            with dissolve
            pause 0.3
            hide screen happiness_text
            with dissolve

            narrator1 "Ignis doesn't look convinced."

            show ignis unimpressed openmouth blind
            ignis "I'd really rather not."
            ignis "It's rather too loud for me. Especially since ... well, I rely on my hearing a lot now. The arena's a little ... overwhelming."
            show ignis unimpressed blind

            narrator1 "Oh. You should have thought that through a bit better."

            ignis "..."

            show ignis neutral openmouth blind
            ignis "Perhaps we should take a stroll around the park for a bit?"
            show ignis neutral blind

            you "Okay, sounds good."

            narrator1 "He takes your hand, and you walk around the statue."

    jump explore_the_park



label explore_the_park:

    narrator1 "You {i}are{/i} assisting him, of course, but it feels less like guiding and more like walking together."

    narrator1 "The birds chitter as the light slowly dies away, and you stroll casually around Listro Park."

    narrator1 "To the left, the panorama of the city greets you. To the right, street sellers with their small wagons loaded with charms and bracelets."

    narrator1 "Behind you, children playing, getting soft reprimands for climbing on the statue."

    narrator1 "It's nice to imagine you don't have a care in the world."

    if happiness >= 19:

        $ ignis_buys_flower = True

        show bg flower_stall with Dissolve(1.0)

        show ignis neutral openmouth blind
        ignis "A moment, [your_name]..."
        show ignis neutral blind

        narrator1 "You stop, and look to your right."

        show ignis neutral openmouth blind
        ignis "That scent on the air ... are we next to a flower shop?"
        show ignis neutral blind

        you "Oh! Yes, well it's more of a street stall, but yeah. They're quite gorgeous."

        show ignis neutral openmouth blind
        ignis "They smell heavenly!"
        show ignis neutral blind

        you "Yeah, they really do."

        show ignis neutral openmouth blind
        ignis "Purple or white?"
        show ignis neutral blind

        you "Huh?"

        show ignis neutral openmouth blind
        ignis "Which do you like more?"
        show ignis neutral blind

        menu:
            "Purple":
                you "Um, purple!"
                narrator1 "Ignis breaks away from you, and talks to the flower seller."
                ignis "Can I take one of the cosmos, please."
                ignis "Yes - a purple one, if you have it."
                narrator1 "Your cheeks grow warm."
                narrator1 "Soon he turns back to you, and he hands you a purple flower."

                show ignis neutral openmouth blind
                ignis "For you."
                show ignis neutral blind

                you "Oh, Ignis, it's beautiful!"

                show ignis smile blind

                you "Thank you so much!"

                show ignis neutral openmouth blind
                ignis "Oh, think nothing of it, [your_name]."
                show ignis neutral blind

            "White":
                you "Um, white!"
                narrator1 "Ignis breaks away from you, and talks to the flower seller."
                ignis "Can I take one of the cosmos, please."
                ignis "Yes - a white one, if you have it."
                narrator1 "Soon he turns back to you, and he hands you a yellow flower."

                show ignis neutral openmouth blind
                ignis "She said it was the closest thing she had to white."
                show ignis neutral blind

                narrator1 "You stare at the brilliant yellow bloom."
                you "Ignis, this is really lovely!"

                show ignis neutral openmouth blind
                ignis "You are ... quite welcome, [your_name]."
                show ignis neutral blind

    else:
        narrator1 "You pass a flower stall, the scent of the blooms wafting past you."

        narrator1 "It's heavenly, and you slow your pace to enjoy it a little more."

    jump dinner_together



label dinner_together:

    narrator1 "The evening has drawn in so dark around you that the horizon is no longer tinged with that rosy blush."

    narrator1 "The air's gotten a few degrees cooler. It's not unpleasant at all, in fact, it's quite refreshing."

    narrator1 "The rain still patters down lightly."

    show ignis neutral openmouth blind
    ignis "I'm starting to feel rather peckish now, I must say."
    show ignis smile blind

    narrator1 "You pause. You're thinking about where you can go to eat."

    narrator1 "A few places come to mind."

    narrator1 "Maagho's, for one, but then, a man like Ignis has probably already been there."

    narrator1 "That old dog that runs the place, Weskham, he's so involved in the political scene - Ignis has probably met him already."

    narrator1 "No, you need to find somewhere else."

    if ignis_favourite_food_known == True:

        narrator1 "You remember that conversation, down in the basement of that grocery store. {i}Alas, this is no seafood paella,{/i} Ignis had said."

        narrator1 "And what was the other thing?"

        narrator1 "Orange cake. That was it!"

        narrator1 "A memory comes to the fore, and you realise you know exactly where to take him."

    else:

        narrator1 "You know there's a nice restaurant down by the Magisterial quarter."

    you "I can suggest somewhere you might not have tried yet..."

    ignis "Oh yes?"

    narrator1 "You take Ignis's hand, and walk him to the bridge."

    you "There's a place just round the corner that serves really good food! I thought you might like to try."

    ignis "That sounds magnificent!"

    ignis "I should like that very much."

    narrator1 "And so you lead him to the left of the plaza, and down a grand set of stairs to the Magisterial quarter."

    narrator1 "Not normally a place you'd bring tourists."

    narrator1 "You head under an archway and over another, smaller bridge, walking leisurely with Ignis alongside you."

    show bg magisterialsquare with Dissolve(1.0)

    ignis "Ah, isn't this near the First Lady's offices?"

    narrator1 "His internal map of the city is spot-on."

    you "Yeah - but it's not a place the political hobnobs frequent."

    you "It's really out-of-the-way, but the food quality is amazing."

    show ignis smile blind with dissolve

    show bg restaurant with Dissolve(1.0)

    narrator1 "You lead him across a stone slab walkway, and into a courtyard lit up bright with garden lights and street lamps."

    # you "You know, they do a mean seafood paella here."
    #
    # you "Tried and tested by yours truly."
    #
    # ignis "I should like to try."

    narrator1 "Right up to the booking table you walk, and luckily, there's not much of a queue."

    you "Table for two, please."

    waiter "Would you like to dine al fresco?"

    narrator1 "He motions at the tables outdoors, protected from the light rain by parasols. Under each parasol hangs a soft cluster of globe lights."

    narrator1 "It looks so romantic."

    ignis "I do enjoy dining al fresco, I must say."

    you "Al fresco, then!"

    waiter "Right this way."

    narrator1 "The waiter takes you to a secluded table off to the side. It still has a fantastic view of the Magisterial plaza, but it's out of the way enough to give you both some privacy."

    narrator1 "You sit down. The chair is comfortable, and you relax into it."

    if ignis_buys_flower == True:
        narrator1 "After a moment's thought, you place the flower Ignis got you in the vase at the centre of the table."

    if ignis_favourite_food_known == True:

        you "Hey, they have that dish you liked..."

        narrator1 "You tap the menu with the flat of your hand."

        you "Seafood paella. Wish a garnish of rosemary and basil, too."

        show ignis smile blind with dissolve

        pause 0.5

        show ignis neutral openmouth blind
        ignis "Honestly? [your_name], you never cease to amaze me."
        show ignis smile blind

    else:
        ignis "Would you mind, ah, reading me the menu?"

        you "Of course!"

        narrator1 "You go through the options available. Ignis's eyes light up at the mention of the mushroom risotto, then they grow ever wider when you reach the paella section."

        ignis "Is there a seafood option?"

        you "Yeah - this one's got crab, prawns and scallops."

        ignis "Oh, now I can't pass that up."

        ignis "My choice is made!"

    narrator1 "When the waiter comes round, Ignis orders a bottle of Altissian white wine, then points to you, indicating the waiter serve you first."

    $ you_gender_poshname = "the lady"

    waiter "Very well, Sir. What will [you_gender_poshname] have?"

    menu:
        "Pick the burger":
            $ restaurant_choice = "burger"
            you "Um, the burger sounds great. Extra bacon topping, please."
            show ignis smile blind with dissolve
            narrator1 "Ignis can't hide his wry smile."

        "Pick the mushroom risotto":
            $ restaurant_choice = "risotto"
            you "I'll take the mushroom risotto, please."
            ignis "A fine choice."
            waiter "It really is - our cream sauce is to die for!"
            waiter "So, Sir, what about you?"
        "Pick the same as Ignis":
            $ restaurant_choice = "paella"

    if restaurant_choice == "paella":
        ignis "I'll take the seafood paella too."
    else:
        ignis "I'll take the seafood paella - it sounds marvellous."
        waiter "We can add oysters on the side, too."
        ignis "Outstanding! Yes, please."

    if ignis_favourite_food_known == True:

        you "{i}There's orange chiffon cake on the dessert menu too, you know.{/i}"

        narrator1 "You don't think he could look any happier, at this point."

        ignis "[your_name], this is ridiculous!"

        narrator1 "Then, to the waiter,"

        show ignis neutral openmouth blind
        ignis "I'll take the orange cake for dessert, as well."
        show ignis smile blind

    narrator1 "The waiter nods, and clips his ordering pad back to his belt, dips his head ever so slightly before heading off to the kitchens."

    if restaurant_choice == "burger":
        you "What's so funny?"

        show ignis neutral openmouth blind
        ignis "That's also Noctis's favourite."
        show ignis smile blind

        you "Heh, no way!"
        narrator1 "You hadn't expected the Prince to enjoy something so ordinary."

        show ignis neutral openmouth blind
        ignis "Yes, although he prefers the Crow's Nest variety."
        ignis "I keep telling him to cut back on the junk food, but does he listen?"
        show ignis smile blind

        narrator1 "You grin."

        you "Well, at least mine comes with salad!"

        show ignis neutral openmouth blind
        ignis "True enough. But a burger every now and then is quite delicious, I must say."
        show ignis smile blind

    narrator1 "You sip at your wine while you wait for the food to arrive. You're feeling a little anxious, but far from as much as you had expected."

    narrator1 "{i}This really is a date,{/i} your mind is intent on reminding you."

    narrator1 "{i}Just don't mess it up.{/i}"

    narrator1 "You take a longer sip of your wine."



    ignis "I know they mean well, and I know they think they're doing what's best for me..."

    ignis ""

    ignis "I would never have expected a man like Ardyn to keep his word..."

    narrator1 "{i}Ardyn.{/i} Even being spoken so plainly, the name sends shivers down your spine."

    ignis "But still, it disturbs me. He offered me a {i}choice{/i}. I said no, and still, he..."

    you "A choice?"

    show ignis neutral openmouth blind
    ignis "Yes - he offered to take me to Niflheim."

    ignis "If it hadn't been for my ... for my eyes ... I wouldn't have to feel this same way every time people do something I don't ask them to."

    ignis "And again, I know they mean well."

    show ignis unimpressed openmouth blind
    ignis "But still, it's frustrating."
    show ignis unimpressed blind

    you "Well, right now, we're gonna change that."

    show ignis neutral blind with dissolve
    pause 1.5

    show ignis neutral openmouth blind
    ignis "How do you mean?"
    show ignis neutral blind

    you "I promise you'll love it."

    narrator1 "You take his hand, and rise from the table."

    narrator1 "A quick moment in which you sort the bill - yes, he's a diplomat but you're hardly going to let him pay - and you walk with him to the exit."

    jump gondola_ride



label gondola_ride:

    narrator1 "You pull Ignis down the streets - not too fast, but eagerly enough."

    ignis "I must admit, I'm intrigued about where you're taking me ..."

    narrator1 "You smile."

    you "Isn't the night air wonderful!"

    ignis "Quite invigorating!"

    show bg gondola with Dissolve(1.0)

    narrator1 "You take Ignis to the gondola stop. The water's lapping at the short wooden pier, and the boats creak softly."

    ignis "Is this a gondola station?"

    you "Yes."

    narrator1 "In tandem with your reply, the gondolier decides to sing \"Gooooondolaaaa! Care for a ride?\""

    narrator1 "It's so comically-timed that Ignis snorts."

    you "So, um, would you?"

    you "I thought we could take the full tour round the lagoon."

    show ignis neutral openmouth blind
    ignis "I would love to."
    show ignis neutral blind

    narrator1 "You tell the gondolier to take you both on the complete tour, and he nods, and ushers you both aboard."

    narrator1 "You have a mild panic over where to sit, but Ignis solves the issue by taking up one side of the couples' seat at the back of the gondola."

    show ignis smile blind at left with move

    narrator1 "Out on the far side of the lagoon, the gondolier slows the boat down."

    narrator1 "It's so muted out here, far from the noise of city activity, and a calmness falls over you."

    ignis ""



label ending:

    scene bg black

    if happiness == 20:
        centered "Congratulations! You reached maximum happiness! \n "
    if happiness >= 18:
        centered "Congratulations! "
    elif happiness >= 15:
        centered ""
    elif happiness >= 10:
        centered ""
    elif happiness >= 5:
        centered ""
    elif happiness < 5:
        centered ""
