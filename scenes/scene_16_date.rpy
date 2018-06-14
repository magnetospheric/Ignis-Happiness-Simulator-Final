#Scene 0X
#Date

#contains labels:
    # speech_and_evac
    # chaos_begins


# this scene is triggered after the hotel conversation, if you have built up enough happiness points

label waitingforignis:

    scene bg listropark
    # we start at listro park, then move to magisterial square for some dinner

    # gondola ride comes last, where kiss option happens

    # faint rain sound effect

    narrator1 "Night has fallen across Altissia. You're waiting by the sculpture at Listro Park, just as Ignis said."

    narrator1 "You still can't believe he wants to do this."

    narrator1 "After a while, you spot him, that tall, svelte figure at the head of the stairs leading up to this place."

    narrator1 "He's accompanied by the blond boy ... Prompto, was it?"

    narrator1 "At any rate, you're glad to see someone is helping him."

    narrator1 "His friend pats his shoulder in solidarity, then vanishes back into the crowd."

    narrator1 "You take a deep breath, and walk over."

    you "Hi, Ignis."

    ignis "A pleasure, [your_name]."

    narrator1 "He's wearing the same shirt as ever, and its crisp, clean-pressed edges are turning slightly damp in the gentle rain."

    narrator1 "He doesn't look like he cares."

    you "How're you doing?"

    ignis "Oh, I'm quite all right. Enjoying the fresh air. Feels good to feel the rain."


    menu:
        "Agree with him on the rain":
            you "Same - it's really refreshing out here."
        "Commiserate but say you prefer to stay dry":
            you ""

    you ""

    ignis "So how about you? Did your day go okay?"

    narrator1 "You feel a flush of warmth as he asks you this, such a little question about the most mundane of things."

    you "Yeah. I haven't really done much, to be honest. Still waiting to get back to work."

    ignis "Of course. Well, I'm glad the Captain's taking care of her staff."


    ignis "Well, then. Where shall we head first?"


    narrator1 "You pause for thought. You didn't exactly think this far."

    narrator1 "It's five in the evening. Maybe a little early for food? But you don't know when Ignis last ate."

    narrator1 "It feels like you should do some sightseeing together, but ... what to do without rubbing in the fact of his injury?"
    #suggest listening to the street musicians
    #ask him if he's hungry
    menu:
        "Suggest listening to the street musicians":

        "Ask him if he's hungry":

        "":


    jump dinner_together

label dinner_together:

    scene bg magisterialsquare



    jump gondola_ride



label gondola_ride:








ignis "I know they mean well, and I know they think they're doing what's best for me..."

ignis ""


ignis "I would never have expected a man like Ardyn to keep his word..."

narrator1 "{i}Ardyn.{/i} Even being spoken so plainly, the name sends shivers down your spine."

ignis "But still, it disturbs me. He offered me a {i}choice{/i}. I said no, and still, he..."

you "A choice?"

ignis "Yes - he offered to take me to Niflheim."

ignis "If it hadn't been for my ... for my eyes ... I wouldn't have to feel this same way every time people do something I don't ask them to."

ignis "And again, I know they mean well."


you "Well, right now, we're gonna change that "
