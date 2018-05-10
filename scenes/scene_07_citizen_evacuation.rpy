#Scene 07
#Evacuating citizens and rescuing ignis

#contains labels:
    # reaching_citizens


# covers reaching the citizens, hearing Ignis on the intercom, and rescuing him

label reaching_citizens:

    show bg evacuee hideout dark with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "When you reach Padore District, it doesn't take you long to scout out the area. On the western edge you can see the port,"

    # rising sound of people chatting / murmuring

    narrator1 "The underpass of the aqueduct is where you find a group of citizens, huddled together in the awning and chittering away like frightened birds as the chaos rages around them."

    narrator1 "As soon as they see you, their faces light up ... only to fall once more when they realise you're the only guard having come to their aid."

    you "Everyone, please"

    return
