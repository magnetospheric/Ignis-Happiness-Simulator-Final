# screen infobubble(who, what):
#     window id "window":
#         vbox:
#             spacing 10
#             xpos 150
#             ypos 200
#
#             text who id "who"
#             text what id "what"

style centered_button:
    xalign 0.5
    ypos 20

style info_bubble_text is text:
    hover_color "#e0cfa5"
    outlines [ (0, "#e0b753", 1, 1), (1, "#8f98a8", 0, 0) ]
    color "#e0b753"
    size 26

style info_bubble_title is text:
    outlines [ (0, "#fefefe", 1, 1), (1, "#8f98a8", 0, 0) ]
    color "#fefefe"
    size 28

screen infobubble(title, content):
    frame:
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.5
        xsize 600
        #background should be different
        background Image("ui/quit_box.png", xalign=0.5, yalign=0.5)

        vbox:
            text title id _("title"):
                style "info_bubble_title"
            null height 10
            text content id "content /n/n/n"
            textbutton _("Got it"):
                style "centered_button"
                text_style "info_bubble_text"
                action NullAction
