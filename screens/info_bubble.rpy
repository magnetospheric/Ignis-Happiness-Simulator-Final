# screen infobubble(who, what):
#     window id "window":
#         vbox:
#             spacing 10
#             xpos 150
#             ypos 200
#
#             text who id "who"
#             text what id "what"

screen infobubble(title, content):
    frame:
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.5
        xsize 600
        #background should be different

        vbox:
            text title id "{b}title{/b}"
            null height 10
            text content id "content /n/n/n"
            textbutton "Got it" action NullAction
