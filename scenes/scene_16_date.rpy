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

    $ renpy.music.set_volume(0.04, delay=1, channel='foley2')
    $ renpy.music.set_volume(0.09, delay=1, channel='foley3')

    play foley2 listro_crowd fadein 2.286
    play foley3 rain fadein 2.286

    $ renpy.music.set_volume(0.3, delay=1, channel='music')
    play music andante fadein 0.5 noloop
    queue music taberna_vieja noloop
    queue music andante noloop
    queue music taberna_vieja noloop
    queue music andante loop

    narrator1 "Evening has fallen across Altissia."

    narrator1 "You're waiting by the sculpture at Listro Park, just as Ignis said."

    narrator1 "You're out of uniform, but all the same you've opted for casual clothing that's still got some level of decorum."

    narrator1 "Your clothes feel suddenly stiff and scratchy, and you panic that you're too overdressed. Or underdressed?"

    narrator1 "Oh gosh."

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

    show ignis at right with move
    show bg buskers with Dissolve(1.5)

    stop music fadeout 2.286
    play music listro_fandanguillo fadein 2.286 noloop

    ignis "Is that a fandanguillo rhythm I hear?"

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

        ignis "Yes."

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

    stop music fadeout 4.286

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

    show ignis smile blind at center with move
    show bg listropark with Dissolve(1.0)

    play music andante fadein 0.5 noloop
    queue music taberna_vieja noloop
    queue music andante noloop
    queue music taberna_vieja noloop
    queue music andante loop

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

    show ignis smile blind at center with move
    show bg listropark with Dissolve(1.0)

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

        show ignis neutral openmouth blind at right with move
        show bg flowers with Dissolve(0.8)

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

    show ignis neutral blind at center with move

    show bg listroparkdark with Dissolve(1.0)

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

    narrator1 "Right up to the booking table you walk, and luckily, there's not much of a queue."

    you "Table for two, please."

    waiter "Would you like to dine al fresco?"

    narrator1 "He motions at the tables outdoors, protected from the light rain by parasols. Under each parasol hangs a soft cluster of globe lights."

    narrator1 "It looks so romantic."

    ignis "I do enjoy dining al fresco, I must say."

    you "Al fresco, then!"

    waiter "Right this way."

    $ renpy.music.set_volume(0.03, delay=1, channel='foley2')

    narrator1 "The waiter takes you to a secluded table off to the side. It still has a fantastic view of the Magisterial plaza, but it's out of the way enough to give you both some privacy."

    narrator1 "You sit down. The chair is comfortable, and you relax into it."

    narrator1 "Above you, the rain makes gentle pitter-patter sounds on the parasol canvas."

    if ignis_buys_flower == True:
        narrator1 "After a moment's thought, you place the flower Ignis got you in the vase at the centre of the table."
        narrator1 "It looks good. And Ignis obviously recognises what you've done, because the smell of the pollen reaches him and he smiles."

    narrator1 "You turn to the menu."

    if ignis_favourite_food_known == True:

        you "Hey, they have that dish you liked..."

        narrator1 "You tap the menu with the flat of your hand."

        you "Seafood paella. With a garnish of rosemary and basil, too."

        show ignis smile blind with dissolve

        pause 0.5

        show ignis neutral openmouth blind
        ignis "Why, that's my favourite!"
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
            narrator1 "Ignis can't hide his wry smile, and you make a note to ask him about it once the waiter's moved on."

        "Pick the mushroom risotto":
            $ restaurant_choice = "risotto"
            you "I'll take the mushroom risotto, please."
            ignis "A fine choice."
            waiter "It really is - our cream sauce is to die for!"

        "Pick the same as Ignis":
            $ restaurant_choice = "paella"
            you "I'll have the seafood paella!"
            waiter "A wonderful choice! Would you like oysters alongside?"
            you "Um ... yes, thanks."

    waiter "So, Sir, what about you?"

    if restaurant_choice == "paella":
        ignis "I'll take the seafood paella too. With all the trimmings."
    else:
        ignis "I'll take the seafood paella - it sounds marvellous."
        waiter "We can add oysters on the side, too."
        ignis "Oh, please, do so."

    if ignis_favourite_food_known == True:

        you "{i}There's orange chiffon cake on the dessert menu too, you know.{/i}"

        narrator1 "You don't think he could look any happier, at this point."

        ignis "[your_name], this is ridiculous!"

        narrator1 "Then, to the waiter,"

        show ignis neutral openmouth blind
        ignis "I'll take the orange cake for dessert, as well."
        show ignis smile blind

    narrator1 "The waiter nods, and clips his ordering pad back to his belt, dipping his head ever so slightly before heading off to the kitchens."

    if restaurant_choice == "burger":
        you "So. What's so funny?"

        show ignis neutral openmouth blind
        ignis "Burger with extra bacon? That's also Noctis's favourite."
        show ignis smile blind

        narrator1 "You hadn't expected the Prince to enjoy something so ordinary."
        you "Heh, no way!"

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

    show ignis neutral openmouth blind
    ignis "I ... realise I haven't thanked you for your efforts at the altar. Not properly, at least."
    show ignis smile blind

    you "Oh! Um, that's really okay -"

    show ignis neutral openmouth blind
    ignis "No, please, [your_name] - let me thank you."
    show ignis smile blind

    narrator1 "You fall silent as he takes your hand in both of his."

    show ignis neutral openmouth blind
    ignis "I deeply appreciate everything you did for me that day. You rescued me. You went above and beyond your call of duty. You {i}cared.{/i}"
    ignis "Thanks to you, I'm alive and very, very gratefully {i}not{/i} in Niflheim."
    show ignis smile blind

    narrator1 "He stops talking now, although it looks very much like he wants to say more."

    narrator1 "You struggle for words but come up empty, and resort merely to gripping his hands a little tighter."

    narrator1 "Then, he speaks."

    show ignis neutral openmouth blind
    ignis "Tell me, if you could change anything about what happened that day ... would you?"
    show ignis neutral blind

    narrator1 "There's this distant expression on his face, and it's clear he's thinking about more than just the obvious."

    you "..."

    you "Wow. Big question. Um..."

    menu:
        "Yes, I would change things":
            you "I think I would change things. It was ..."
            you "It was awful, what happened."
            you "The attack ... Luna ... {i}you ...{/i}"
            you "I'd want to make it better."
        "Maybe some things":
            you "If I had the choice, I think I'd find it hard not to change at least {i}some{/i} things..."
            you "I'd like to avoid people being in pain, if I could."
        "No, I wouldn't change anything":
            you "I wouldn't change anything."
            you "I don't think it's wise to alter the past."

    you "But ... why are you asking this?"

    you "This is about more than your injury, isn't it?"

    show ignis unimpressed openmouth blind
    if ignis_opened_up == True:
        ignis "It..."
        ignis "Ah, who am I fooling? You said it was good to open up, and so I should."
    else:
        ignis "I ... yes."
    show ignis neutral blind

    narrator1 "The food arrives, and you both fall silent as the waiter sorts everything out. Then, once he's gone, your conversation resumes."

    show ignis unimpressed openmouth blind
    ignis "I would never have expected a man like Ardyn to keep his word..."
    show ignis unimpressed blind

    narrator1 "{i}Ardyn.{/i} Even being spoken so plainly, the name sends shivers down your spine."

    show ignis unimpressed openmouth blind
    ignis "But still, it disturbs me. He offered me a {i}choice{/i}. I said no, and even so, he..."
    show ignis unimpressed blind

    you "A choice?"

    narrator1 "You remember the dropship conversation."

    you "You mean, to join forces with him?"

    show ignis unimpressed openmouth blind
    ignis "Well, not just that. To ... rewrite history."
    ignis "Gods have mercy, I wanted to..."
    show ignis unimpressed blind

    narrator1 "He looks like he's about to cry, and it's like a blade twisting at your heart."

    you "What are you not telling me, Ignis?"

    show ignis neutral openmouth blind
    if ignis_opened_up == True:
        ignis "I told you how I've been in the service of the Crown from my youth."
        show ignis neutral blind

        you "Yeah. Since you were six, right?"
        narrator1 "He nods."

        show ignis neutral openmouth blind
        ignis "And, also, on how protecting Prince Noctis is my top priority."
    else:
        ignis "My whole life has been in the service of the Crown. Protecting Prince Noctis has always been my top priority."

    show ignis unimpressed openmouth blind with dissolve
    ignis "Well, when I approached the altar..."
    ignis "I had a vision."
    ignis "I saw..."
    show ignis unimpressed blind

    narrator1 "His fingers grip the tablecloth."

    narrator1 "When he next speaks, his voice is barely above a whisper."

    show ignis unimpressed openmouth blind
    ignis "I saw Noctis die."
    show ignis unimpressed blind

    you "You ... oh my gosh."

    you "Was it a premonition?"

    show ignis neutral openmouth blind
    ignis "I believe so. One of the Oracle's Messengers showed it to me."
    show ignis neutral blind

    you "In the vision, how did he ... die?"

    show ignis neutral openmouth blind
    ignis "He used the full potential of the Power of Kings. And -"
    show ignis neutral blind

    narrator1 "He breaks off, his voice strained. Then, motioning at his own face, he says,"

    show ignis unimpressed openmouth blind
    ignis "And look what it did to me! I barely even did {i}anything{/i} useful with it, and now I - I may have lost my sight for good."
    ignis "So if he's going to fix this world, to end the Scourge, I fear, no, I {i}know{/i} it will cost him his life."
    show ignis unimpressed blind

    narrator1 "He thumps his hand down on the table."

    show ignis unimpressed openmouth blind
    ignis "Agh! I feel so helpless!"
    show ignis unimpressed blind

    narrator1 "Ignis is distraught. What will you say?"

    menu:
        "Give him hope":

            you "Ignis..."
            you "I believe the Oracle's Messenger showed you that vision to give you a choice."

            show ignis unimpressed openmouth blind
            ignis "But Ardyn! He gave me a choice - to come with him, to change fate - and I turned him down. I should have gone - I maybe could have found a way to stop the vision from coming to pass."
            show ignis unimpressed blind

            narrator1 "It pains you to hear him so ready to throw himself into the fire like this. You remember the words Ravus spoke at the altar, and you wince."
            you "No... he would only have used you."
            you "But hey - you can still find a way to stop it. I'm sure of it."
            you "Nobody cares for Noctis more than you, and with your dedication, with your skillset ... if anyone can do it, it's you."
            show ignis smile blind with dissolve
            ignis "Perhaps you are right."
            ignis "Thank you, [your_name]. That brings me some hope."

        "Commiserate":
            you "I'm sorry, Ignis. It must have been awful to witness."
            narrator1 "Ignis sniffs, then turns back to his food."

            show ignis neutral openmouth blind
            ignis "No - I'm sorry to bring such matters to the dinner table. We should be enjoying our food."
            show ignis neutral blind

            you "Please don't feel bad about it..."

            show ignis neutral openmouth blind
            ignis "I shall try."
            show ignis neutral blind

    narrator1 "You both turn back to your food. It feels trite to make small remarks on how good it tastes after the things Ignis has just talked about, and there's a near-on uncomfortable silence for a moment."

    narrator1 "Luckily, Ignis breaks it first."

    if restaurant_choice == "risotto":
        show ignis neutral openmouth blind
        ignis "How does the risotto taste?"
        show ignis neutral blind

        you "It's really good!"

        show ignis neutral openmouth blind
        ignis "Mind if I have a bite? I was quite keen to try it."
        show ignis neutral blind

        you "Go right ahead!"
        narrator1 "But then you realise he's going to have trouble doing that, knowing where to reach across the table and so on."
        you "Um, should I..."

        show ignis smile blind
        narrator1 "Ignis chuckles."

        show ignis neutral openmouth blind
        ignis "I suppose I don't consider it an indignity to be spoonfed by you."
        show ignis smile blind

        narrator1 "You laugh too. This situation is so intimately ridiculous."
        you "Heh, all right, well... Here goes."
        narrator1 "You pick a spoonful with a decent chunk of mushrooms and sauce, and somehow navigate the morsel to Ignis's mouth without messing up his shirt."
        narrator1 "Your hands only shake a little, thank goodness."

        show ignis neutral openmouth blind
        ignis "Oh, that's delicious!"
        show ignis neutral blind

        narrator1 "He wipes his lips with a napkin, and returns to his own dish."

        show ignis neutral openmouth blind
        ignis "I really am being spoiled rotten!"
        show ignis neutral blind

        you "Well, you totally deserve it!"

    else:
        show ignis neutral openmouth blind
        ignis "Well, I was sensible to order the paella, I don't regret a single morsel."
        show ignis neutral blind

        narrator1 "You smile."

        show ignis neutral openmouth blind
        ignis "How's yours?"
        show ignis neutral blind

        you "Heavenly."

        show ignis neutral openmouth blind
        ignis "I'm very glad you've afforded me this chance to get away from things. And to enjoy such fine cuisine!"
        show ignis neutral blind

        you "You deserve to tune off for a little."

    you "And I'm really glad you like the food! I don't get to bring many people here - my companions are either the fast food kind, or they've done it all before."

    show ignis neutral openmouth blind
    ignis "Well, I must say, that is a loss on their part. You are wonderful company."
    show ignis neutral blind

    narrator1 "You blush, and take another sip of your wine."

    narrator1 "At this stage, it's hard to tell if your cheeks are warm from the wine or the compliments."

    narrator1 "But you feel comfortable."

    narrator1 "Dessert soon comes around, and you stick to the sorbet while Ignis enjoys his cake."

    show ignis smile blind with dissolve

    narrator1 "It's so nice to see the smile back on his face."

    show ignis neutral openmouth blind
    ignis "I really ought to ask the chef what their egg white to cream of tartar ratio is..."
    show ignis neutral blind

    you "Is it quite a hard dish to make?"

    show ignis neutral openmouth blind
    ignis "It's difficult to get the right consistency. A common mistake is making the egg whites too stiff."
    ignis "This, however, is a fine cake. It's giving me ideas for a new recipe, I daresay!"
    show ignis smile blind

    narrator1 "When the food is gone and the wine bottle emptied, you both prepare to leave."

    narrator1 "You're just fishing our your wallet when the waiter turns up to clear the plates."

    waiter "I hope everything was to your liking?"

    narrator1 "You nod, and Ignis asks the waiter to pass on his compliments to the chef."

    narrator1 "Then the waiter notices Ignis is trying to get up. He's already seen the scars, the shaded glasses, and by the time either of you really clock what is happening, it's too late."

    show ignis neutral blind with dissolve

    narrator1 "He's grabbed Ignis and is helping him up from his chair without asking."

    show ignis unimpressed blind with dissolve

    narrator1 "Ignis doesn't outwardly make a fuss, but it's clear from his subtle huffs that he's uncomfortable with the exchange."

    waiter "There you go, Sir."

    narrator1 "You bristle."

    you "Um, can you not do that, please. He didn't ask for help."

    waiter "Oh, I... I do apologise..."

    narrator1 "The waiter looks at you both quite quizzically. It's clear he doesn't understand why it's a problem."

    narrator1 "You sigh."

    you "Can we have the bill, please."

    narrator1 "While the waiter hurries off, Ignis sinks back into the chair."

    show ignis unimpressed openmouth blind
    ignis "I know they mean well, and I know they think they're doing what's best for me..."
    ignis "But it's not the first time someone's tried something like that since the ceremony ended."
    show ignis unimpressed blind

    you "Ignis..."

    show ignis unimpressed openmouth blind
    ignis "If it hadn't been for my ... for my eyes ... I wouldn't have to feel this same way every time people do something I don't ask them to."
    ignis "And again, I know they mean well."
    ignis "But it's unbearable!"
    show ignis unimpressed blind

    narrator1 "You think about Ardyn, about how he was going to take Ignis to Niflheim regardless of his answer, and you realise that a lot's happened to shake Ignis's sense of personal autonomy."

    narrator1 "It's not fair; he's either stuck with people taking advantage of him, or babying him."

    narrator1 "And, with that thought, an idea sparks in your mind."

    you "Well, right now, we're gonna change that."

    show ignis neutral blind with dissolve
    pause 0.3

    show ignis neutral openmouth blind
    ignis "How do you mean?"
    show ignis neutral blind

    you "We're gonna do something cool! And kind of daring, if you like."

    show ignis smile blind with dissolve
    ignis "Daring, hmm?"
    ignis "Well, now, you have my interest."

    narrator1 "You reach for his hand, and he grips back. Then you finally rise from the table."

    narrator1 "A quick moment in which you sort the bill - yes, he's a diplomat but you're hardly going to let him pay - and you walk with him to the exit."

    $ renpy.music.set_volume(0.04, delay=1, channel='foley2')

    jump gondola_ride



label gondola_ride:

    show bg magisterialsquare with Dissolve(1.0)

    narrator1 "You escort Ignis eagerly down the streets."

    show ignis neutral openmouth blind
    ignis "I must admit, I'm intrigued about where you're taking me ..."
    show ignis neutral blind

    narrator1 "You smile."

    you "It's not too far now!"

    show bg listroparkdark with Dissolve(1.0)

    narrator1 "You all but dance your way back past the sculpture at Listro Park, taking care not to rush Ignis, and steering clear of any and all obstacles."

    narrator1 "Up above you, the moon is starting to show behind the clouds, and the air is cool on your skin."

    you "Isn't the night air wonderful!"

    show ignis neutral openmouth blind
    ignis "Quite invigorating!"
    show ignis smile blind

    show bg gondola with Dissolve(1.0)

    $ renpy.music.set_volume(0.03, delay=1, channel='foley2')

    narrator1 "You take Ignis to the gondola stop. The water's lapping at the short wooden pier, and the boats creak softly."

    narrator1 "Ignis perks up at the sounds."

    show ignis neutral openmouth blind
    ignis "Is this a gondola station?"
    show ignis neutral blind

    you "Yes."

    narrator1 "In tandem with your reply, the gondolier decides to sing \"Gooooondolaaaa! Care for a ride?\""

    narrator1 "It's so comically-timed that Ignis snorts."

    you "So, um, would you?"

    you "I was thinking we could take the full tour round the lagoon."

    you "We'd be pretty far from the land at that point, but it'd be really fun!"

    show ignis neutral openmouth blind
    ignis "I would love to."
    show ignis neutral blind

    narrator1 "You tell the gondolier to take you both on the complete tour, and he nods, and ushers you both aboard."

    narrator1 "Ignis's first step aboard the gondola is shaky, and he lilts ever so slightly, uncertain of his position."

    show ignis smile blind with dissolve
    narrator1 "But his balance kicks in and he rights himself in an instant, and his little self-triumphant smile doesn't go unnoticed by you."

    narrator1 "When it's your turn, you have a mild panic over where to sit, but Ignis solves the issue by taking up one side of the couples' seat at the back of the gondola, and motioning for you to join him there."

    show ignis smile blind at left with move

    narrator1 "You sit beside him on the couples' seat, rocking the boat a little with the inertia of your movements."

    narrator1 "Then it's a nod at the gondolier behind you, and with a soft, melodic whistle, the man pushes off from the pier."

    you "And we're off!"

    stop foley2 fadeout 2.286

    narrator1 "The water isn't choppy at all, even with the cloudy skies and the breeze they bring. There's just the gentle rocking as the gondola makes its way leisurely out into the open."

    show ignis neutral openmouth blind
    ignis "It feels good to be out on the water."
    show ignis neutral blind

    narrator1 "Out on the far side of the lagoon, the gondolier slows the boat down."

    narrator1 "It's so muted out here, far from the noise of city activity, and a calmness falls over you."

    you "This is so beautiful..."

    show ignis neutral openmouth blind
    ignis "It truly is."
    show ignis neutral blind

    narrator1 "Ignis's hands find yours again, and he strokes them gently. His expression is so sincere."

    show ignis neutral openmouth blind
    ignis "[your_name]..."
    show ignis neutral blind

    narrator1 "Your breath stills, even as your heart races."

    narrator1 "It's your move."

    if happiness >= 18:
        menu:
            "Kiss him":
                $ kissed_or_hugged_on_gondola = True
                $ kissed_on_gondola = True
                narrator1 "You lean in, spellbound, and a soft expression washes over Ignis's face as he feels your closeness."

                narrator1 "He tilts his head ever so slightly, and your lips meet his."

                narrator1 "You kiss him tenderly, and there's a surging moment as the tenderness gives way to passion. His lips are so pliant, he's so open to you right now."

                narrator1 "He kisses you back with an unexpected urgency, and you could simply {i}melt{/i} at this point."

                narrator1 "Then he pulls away, breathless."

                you "Ignis, I..."

                show ignis neutral openmouth blind
                ignis "No need to say anything."
                show ignis smile blind with dissolve

                narrator1 "His hand is on your shoulder now, and you feel a comfort you haven't felt since you were young."

                narrator1 "You lay your head on his shoulder and stay there a while, looking at the bright stars breaking through the clouds high above."

            "Hug him":
                $ kissed_or_hugged_on_gondola = True
                $ kissed_on_gondola = False
                narrator1 "Your hands shift upward, tracing along his arm so he's aware of every movement. Then, you thread your arms around him and pull him in to a hug."

                narrator1 "He responds immediately, drawing you closer so that your faces are buried in the crook of each other's collarbone, so that you can feel the rise and fall of your chests in unison."

                narrator1 "You hold him like you're scared of losing him again; you hold him like it might be your last chance."

                narrator1 "And Ignis does the same."

                narrator1 "Beneath the stars, surrounded by the water, you hold on together."

                narrator1 "Eventually, Ignis breaks off, and puts and arm comfortingly round your shoulder instead."

                narrator1 "You both relax back against the plush seat fabric, saying nothing, contented."

            "Do nothing":
                $ kissed_or_hugged_on_gondola = False
                $ kissed_on_gondola = False
                narrator1 "The moment passes."
    else:
        menu:
            "Hug him":
                $ kissed_or_hugged_on_gondola = True
                $ kissed_on_gondola = False
                narrator1 "Your hands shift upward, tracing along his arm so he's aware of every movement. Then, you thread your arms around him and pull him in to a hug."

                narrator1 "He responds immediately, drawing you closer so that your faces are buried in the crook of each other's collarbone, so that you can feel the rise and fall of your chests in unison."

                narrator1 "You hold him like you're scared of losing him again; you hold him like it might be your last chance."

                narrator1 "And Ignis does the same."

                narrator1 "Beneath the stars, surrounded by the water, you hold on together."

                narrator1 "Eventually, Ignis breaks off, and puts and arm comfortingly round your shoulder instead."

                narrator1 "You both relax back against the plush seat fabric, saying nothing, contented."

            "Do nothing":
                $ kissed_or_hugged_on_gondola = False
                $ kissed_on_gondola = False
                narrator1 "The moment passes."

    narrator1 "A while later, a splashing beside the boat interrupts you."

    show ignis neutral openmouth blind
    ignis "Is that a fish?"
    show ignis neutral blind

    narrator1 "You turn to the water. Close to the surface, a number of glowing shapes reveal themselves."

    you "No, they're ... jellyfish! Oh my gosh, they're glowing like crazy."

    show ignis neutral openmouth blind
    ignis "Bioluminescence?"
    show ignis neutral blind

    narrator1 "You remember that word dimly from your school days. A light-emitting quality possessed by certain ocean creatures."

    you "It seems like it. Hey, I think these are Altissian Aurelias!"

    narrator1 "You sometimes hear the fishermen talk about them. They're incredibly rare to see."

    show ignis neutral openmouth blind
    ignis "Now, that's really something special."
    ignis "Please ... describe them to me."
    show ignis smile blind with dissolve

    narrator1 "You watch them dance around the gondola, and tell Ignis everything."

    you "There's one slightly confused one that keeps bumping against the boat! Bless, I don't think it can make sense of us."

    you "The colour really is magnificent. They're mostly whitish blue, but there's some sea green and some soft yellows too. And - oh, one over there has a puple streak on the tendrils!"

    you "Wow ... I can see some larger ones even deeper in the water!"

    you "They're glowing a lot more slowly."

    you "Hah, and a tiny one over there thinks it's a strobe light at a party!"

    show ignis neutral openmouth blind
    ignis "Magnificent!"
    show ignis smile blind with dissolve

    narrator1 "Eventually the jellies disperse, and the gondolier asks if you would like to continue the tour."

    you "Ignis?"

    show ignis neutral openmouth blind
    ignis "That sounds lovely."
    show ignis smile blind with dissolve

    if kissed_or_hugged_on_gondola == True:
        narrator1 "The tour continues, and the two of you stay locked in each others arms as the gondola drifts forth across the water."
    else:
        narrator1 "The tour continues."

    narrator1 "You ask the gondolier to end the tour at the stop outside the Leville."

    show ignis at center with move
    show bg leville exterior dark with Dissolve(1.0)

    narrator1 "When you reach the pier, you tip the gondolier extra for his service, and offer a hand to help Ignis out of the boat."

    narrator1 "He takes it, and soon you're both back on solid ground, looking directly at each other in the moonlight."

    if kissed_on_gondola == True:
        narrator1 "Ignis leans forth to kiss you once more."
        narrator1 "Again, your heart surges, and you lean in to complete the kiss."

    elif kissed_or_hugged_on_gondola == True:
        narrator1 "Ignis embraces you one final time, and you cling to him, holding him close, scared for it to end."

    else:
        show ignis neutral openmouth blind
        ignis "Thank you, [your_name]. This meant a lot to me."
        show ignis neutral blind

        you "It did for me too."
        you "Ignis?"
        you "Thank you."

    if kissed_or_hugged_on_gondola == True:
        narrator1 "Precious few seconds pass, and it's not long enough."
        narrator1 "But it will have to do."
        narrator1 "You break away, smiling."

        show ignis neutral openmouth blind
        ignis "I never expected to meet someone like you, [your_name]."
        ignis "But in such a short space of time, you made things better for me."
        ignis "You {i}helped{/i}."
        ignis "And I really appreciate that."
        show ignis smile blind with dissolve

        narrator1 "Your chest is fit to burst just hearing this."
        you "I could say the same to all of that, you know."

        show ignis neutral openmouth blind
        ignis "I shall have to leave in due course, along with the Prince's entourage, but - "
        ignis "I suppose you were aware of that already?"
        show ignis smile blind with dissolve

        you "I was. I mean, I am. That fact alone was not worth passing up the chance with you."

        show ignis neutral openmouth blind
        ignis "I agree. We are both bound by our duties. And - "
        show ignis smile blind with dissolve

        narrator1 "Here, he pauses to stroke your shoulder tenderly."

    show ignis neutral openmouth blind
    ignis "We will make the world a better place."
    show ignis neutral blind with dissolve

    narrator1 "You're overcome with emotion, so you merely nod, fervently."

    show ignis neutral openmouth blind
    ignis "I hope we can meet again after this war is over."
    show ignis neutral blind

    you "I hope so, too."
    narrator1 "You step back. It's time to let Ignis get back to the others."
    you "You'll know where to find me."

    show ignis smile blind with dissolve

    narrator1 "Ignis smiles, and it's so heartfelt."

    show ignis neutral openmouth blind
    ignis "I wish you all the best."
    show ignis neutral blind with dissolve

    you "You too. Please sleep well."

    show ignis smile blind with dissolve
    narrator1 "He smiles, then he heads off into the hotel, where he's aided by the concierge."
    narrator1 "You watch until he's out of sight, making sure the concierge takes care of him."
    hide ignis with Dissolve(1.0)
    narrator1 "Then he is gone."
    narrator1 "You sigh deeply, then you make your way home."

    stop foley3 fadeout 2.286

    $ quick_menu = False
    $ show_happiness = False

    scene black with Dissolve(1.0)

    show bg mc_room
    show screen black_overlay
    with Dissolve(1.5)


    narrator1 "That evening, your room feels less lonely than it did before."

    narrator1 "You feel like you have a little more purpose."

    narrator1 "Ignis's words stay with you, and you get the feeling they will for some time."

    centered "{i}We will make the world a better place.{/i}"

    stop music fadeout 2.0

    pause 2.0

    jump ending



label ending:

    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music main_credit_music

    scene black
    hide screen black_overlay
    with Dissolve(2.5)

    pause 1.0

    if happiness == 21:
        centered "Congratulations! You reached maximum happiness!"
        centered "Ignis is very lucky to have met you."
    elif happiness >= 18:
        centered "Congratulations! You made Ignis incredibly happy!"
    elif happiness >= 15:
        centered "Well done! You made Ignis very happy!"
    elif happiness >= 10:
        centered "You made Ignis pretty happy!"
        centered "But you could probably do better."
    elif happiness >= 5:
        centered "You made Ignis a little bit happier, but you could definitely do better."
    elif happiness < 5:
        centered "Hmm, were you even trying? You didn't make Ignis that happy at all."
        centered "How did you even get to this scene?"

    pause 1.0

    # play composite animated image here
    show bg credit_backgrounds

    centered "{cps=15}Thanks for playing{/cps}" with dissolve

    pause 1.0

    centered "{cps=15}A MAD EGG Production{/cps}" with dissolve

    pause 1.0

    centered "{cps=15}Written, coded and composed by INVI{/cps}" with dissolve

    pause 1.0

    centered "{cps=15}With thanks to:{/cps}" with dissolve

    pause 1.0

    centered "{cps=15}{size=26}StylishChocobutt{/size} \n (for the gorgeous main menu art){/cps}" with dissolve

    pause 1.0

    centered "{cps=15}{size=26}PrettyPrompto{/size} \n(for sourcing Ignis reference images){/cps}" with dissolve

    pause 1.0

    centered "{cps=15}{size=26}Veronika Hørven Jensen{/size} \n(for the theme song vocals){/cps}" with dissolve


    pause 1.0

    centered "{cps=15}and of course \n {size=26}everyone who played the game{/size}{/cps}" with dissolve

    pause 1.0

    centered "{cps=15}Your support means a lot.{/cps}" with dissolve


    pause 1.0

    centered "{cps=15}This fan game would also not have been possible without:{/cps}" with dissolve

    pause 1.0

    centered "{cps=15}The immense efforts of the lovely folks at Square Enix,\n who keep our fantasies alive.{/cps}" with dissolve

    pause 1.0

    centered "{cps=15}soundtrack available on bandcamp{/cps}" with dissolve

    pause 1.0
    pause 1.0

    call screen infobubble_credits(title="Return to the title screen?", content="You don't need to go back just yet if you don't want to.", confirmation="Yes")

    return
