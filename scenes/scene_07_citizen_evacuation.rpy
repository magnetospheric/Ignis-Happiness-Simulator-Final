#Scene 07
#Evacuating citizens and rescuing ignis

#contains labels:
    # reaching_padore_boats
    # radio_interruption
    # second_choice_who_to_rescue
    # reaching_citizens
    # escort_to_jetty
    # divert_to_ignis


# covers reaching the citizens, hearing Ignis on the intercom, and deciding whether to rescue citizens or ignis


label reaching_padore_boats:

    show bg padore jetty with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "When you reach Padore District, it doesn't take you long to scout out the area. On the western edge you can see the small jetty, and throngs of people, all busy boarding boats and sharing out bottled water."

    show altissianguard neutral at right
    with dissolve

    altissianguard "[your_name]! Gods, am I glad to see you!"

    you "Hi — I came as fast as I could. What's the situation here?"

    altissianguard "We have most residents out of the danger zone, but there's still a few clustered in the streets."

    altissianguard "Been seeing a lot of people run themselves dehydrated already with the panic."

    you "You got enough supplies?"

    altissianguard "I think so. But — can you round up the remaining people? I heard word they were waiting under the aqueduct."

    you "I'm on it."

    narrator1 "You turn on your heel and immediately set to the task at hand. There's no time to waste."

    hide altissianguard
    with dissolve

    jump radio_interruption



label radio_interruption:

    show bg mediumstreet with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "So it's back down the street you just came from, then."

    narrator1 "Being a guard during a time of crisis is more a logistical nightmare than expected — you're feeling a little bit like you're on an endless stream of fetch quests, but you suppose it can't be helped."

    narrator1 "You pass a few straggling Magitek units while slipping through the streets, but thankfully, you don't see more than two at a time, and they are too single-minded to notice you now you're keeping to the shadows."

    narrator1 "You're still a few blocks away from the aqueduct when your radio crackles. Immediately you duck behind a wall, and holding the receiver to your ear."

    narrator1 "You can't quite make it out at first, but it sounds like ... is that Ignis?"

    narrator1 "Why isn't he talking to you?"

    narrator1 "You pause, fingers running against the brick, other hand tightening round the receiver. You're expecting instructions, updates, something, anything, but it's just this strange mush of noise."

    narrator1 "Then you realise. Ignis has somehow hit the transmit button, and you can hear everything that's happening around him."

    narrator1 "It's mostly muffled shouts and cries, accompanied by Ignis's breathing. He's clearly frantic, but doing an admirable job of stilling his own nerves."

    narrator1 "Then, an angry voice cuts through. It's not one you recognise."

    unidentified_voice "{i}The Lucian King's lapdog, eh?{/i}"

    #sound effects here

    narrator1 "It's followed by a thud, and a sharp cry of pain. Ignis is hurt."

    narrator1 "The thudding comes again, followed by more yells. Whoever this stranger is — and he {i}must{/i} be from the Empire, he must — he's really got it in for Ignis."

    narrator1 "You're bristling. Your skin's flushing hot and you want nothing more than to race over there, to use all your force to put a stop to this."

    unidentified_voice "{i}We're going to blow this bridge. And then, you won't be able to reach your dearly beloved King!{/i}"

    ignis "{i}No! Don't —{/i}"

    # sound effect - hipass thud

    narrator1 "There's a noise so loud that it's capped by the tinny speaker, then the connection cuts out entirely."

    narrator1 "You thump the wall. You want to curse."

    narrator1 "One thing is certain: he's in Tigiano District. There's only one bridge on this side wide enough to warrant being blown up."

    narrator1 "You check your mental map of the city. You're far closer to the citizens you've been tasked with helping than you are to Ignis."

    narrator1 "An uncomfortable weight settles in your stomach. Both of the paths that diverge before you lead to protecting people, but it's a divergence of duty. And of numbers."

    narrator1 "There's far more people waiting under that aqueduct for you. They probably don't have combat experience like Ignis does — they're probably not going to last long if a squadron of Magitek Troopers find them. But at the same time, you don't want to leave Ignis alone at the mercy of the Empire."

    narrator1 "You try to imagine what Ignis would advise you to do."

    narrator1 "What will you do?"

    # would be good to have a ticking sound here - to highlight the 'i need more time' thing

    menu:
        "Continue onward to help the citizens first":

            $ citizens_first = True

            narrator1 "You can't abandon your duty. You know this as clear as day. More people are depending on you right now, and you can't let them down. You can't let Ignis down."

            narrator1 "You {i}promised{/i}."

            narrator1 "Besides, the citizens aren't far away. You'll help them first, then come to Ignis's aid."

            jump reaching_citizens

        "Divert your route to help Ignis first":

            $ citizens_first = False

            narrator1 "You simply can't leave Ignis in pain like that. What if the Niffs kill him, after all?"

            narrator1 "If you take a detour round the side of the aqueduct, you can come to his aid and still be close enough to double back for the citizens afterward."

            jump divert_to_ignis

        "Wait! I need more time!":

            $ waited = True

            narrator1 "You pace in agitation, trying to come to a decision. The pressure has your mind reeling."

            narrator1 "Ignis has that strange blue magic. It could be that he's just faking being hurt to get some information out of the enemy."

            narrator1 "It could have been a tactical move, getting the enemy to blow up that bridge..."

            narrator1 "You shake your head. Not likely."

            narrator1 "But you really can't delay any more."

            jump second_choice_who_to_rescue



label second_choice_who_to_rescue:

    menu:
        "Continue onward to help the citizens first":

            $ citizens_first = True

            narrator1 "You can't abandon your duty. You know this as clear as day. More people are depending on you right now, and you can't let them down. You can't let Ignis down."

            narrator1 "You {i}promised{/i}."

            narrator1 "Besides, the citizens aren't far away. You'll help them first, then come to Ignis's aid."

            jump reaching_citizens

        "Divert your route to help Ignis first":

            $ citizens_first = False

            narrator1 "You simply can't leave Ignis in pain like that. What if the Niffs kill him, after all?"

            narrator1 "If you take a detour round the side of the aqueduct, you can come to his aid and still be close enough to double back for the citizens afterward."

            jump divert_to_ignis



label reaching_citizens:

    show bg evacuee hideout dark with Dissolve(0.3)

    # rising sound of people chatting / murmuring

    show citizens dark
    with dissolve

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)


    narrator1 "The underpass of the aqueduct is where you find a group of citizens, huddled together in the awning and chittering away like frightened birds as the chaos rages around them."

    narrator1 "As soon as they see you, their faces light up ... only to fall once more when they realise you're the only guard to come to their aid."

    you "Everyone, please, calm down."

    show citizens scared
    with dissolve

    citizen1 "They can't have sent just you! We need more protection from those... those {i}things!{/i}"

    show citizens reasonable
    with dissolve

    citizen2 "They're not 'things', Marcus, they're Magitek Troopers. MTs."

    show citizens scared
    with dissolve

    citizen1 "Same difference — they aren't alive anyways. And do we really expect {i}[your_pronoun_object]{/i} to take care of them?"

    you "I assure you, I can handle them."

    show citizens sceptical
    with dissolve

    citizen3 "We saw whole squads of 'em walking around. One guard can't go up against all that. No matter how good you are. No offense."

    narrator1 "You stifle a sigh. The citizens have every right be worried, but this is taking too much time."

    show citizens dark
    with dissolve

    you "You're right, but we don't have much choice right now. Come on — it's not far to the jetty. If we don't move now, the MTs will find you for sure."

    narrator1 "You turn, facing the street, handling the grip of your weapon, and you move forth with determination."

    you "Follow me."

    narrator1 "The citizens anxiously wring their hands for precious seconds more, then they obey."

    jump escort_to_jetty



label escort_to_jetty:

    show bg mediumstreet with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "The whole way back to the evacuation zone, your panic climbs. Behind you, the citizens are scared and muttering away, and it reminds you that every second you spend saving them is another second you're not helping Ignis."

    narrator1 "You force the thoughts out of your mind."

    show bg padore jetty with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "It feels like an eternity passes before you reach the jetty, although you know it can't have been more than three or four minutes. Thankfully, no troopers surprise you along the way, and the citizens reach the water's edge unscathed."

    show citizens reasonable
    with dissolve

    citizen2 "Thanks for escorting us."

    show citizens sceptical
    with dissolve

    citizen3 "Yeah — we really appreciate it."

    show citizens scared
    with dissolve

    citizen1 "Wh-where do we go now?"

    narrator1 "You point at your fellow guard."

    you "Talk to him. He'll deal with the rest. Now — I have to go check on some others."

    narrator1 "About time. How many minutes did you waste? How many more bruises might Ignis have suffered? You grit your teeth and start to run."

    hide citizens
    with dissolve

    jump meeting_ignis_again



label divert_to_ignis:

    show bg mediumstreet with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "Back down the same streets, and it's starting to feel like deja-vu. You don't turn your radio back on for fear it might cause him to suffer more. You just trust that he'll still be there, in Tigiano District."

    jump meeting_ignis_again
