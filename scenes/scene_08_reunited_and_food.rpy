#Scene 08
#Reuniting with Ignis and stopping for a food break

#contains labels:
    # meeting_ignis_again
    # food_break


# covers meeting back up with ignis again and stopping for food & supplies and restocking before he's dragged away again


label meeting_ignis_again:

    show bg mediumstreet with Dissolve(0.3)

    narrator1_nosound "{alpha=0.0}{outlinecolor=#ffffff00}..........{/outlinecolor}{/alpha}{nw}" with Dissolve(0.3)

    narrator1 "you find ignis...."

    jump food_break



label food_break:

    return



# conversation with ignis.... for later


# ignis "You wanted to save as many people as possible, right?"
#
# narrator1 "Is that why you became a guard?"
#
# narrator1 "You don't need to tell Ignis your reason why. But it's important to be honest with yourself."
#
# menu:
#     "I wanted to help people in times of need":
#         $ motivation = "help"
#     "I wanted to protect people from threats":
#         $ motivation = "protect"
#     "I just wanted to get paid regularly":
#         $ motivation = "survival"
#     "I wanted the prestige that comes with the position":
#         $ motivation = "prestige"
#     "I wanted to learn more about security":
#         $ motivation = "education"
