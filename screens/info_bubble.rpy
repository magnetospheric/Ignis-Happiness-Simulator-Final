#  INFO BUBBLE : Centre screen box that provides helpful info
#  CONTAINS:
#           info bubble styles
#           info bubble one (single button confirm)
#           info bubble two (confirm OR cancel)
#           input screen (uses infobubble styles)

# info bubble styles
style info_bubble_frame:
    xpadding 0
    top_padding 50
    xalign 0.5
    yalign 0.5
    xsize 666
    ysize 311

style centered_button:
    ypos 30

style centered_button_2column:
    ypos 40
    xsize 333

style info_bubble_button_text is text:
    hover_color "#eee1c1"
    outlines [ (0, "#e0b753", 1, 1), (1, "#8f98a8", 0, 0) ]
    color "#e0b753"
    size 26
    xalign 0.5
    text_align 0.5
    line_spacing 10

style info_bubble_button_text_2 is text:
    hover_color "#eee1c1"
    outlines [ (0, "#e0b753", 1, 1), (1, "#8f98a8", 0, 0) ]
    color "#e0b753"
    size 22
    xalign 0.5
    text_align 0.5
    line_spacing 10
    xpadding 20

style info_bubble_content is text:
    xalign 0.5
    text_align 0.5
    line_spacing 10
    background "#000000"

style info_bubble_title is text:
    outlines [ (0, "#fefefe", 1, 1), (1, "#8f98a8", 0, 0) ]
    color "#fefefe"
    size 28
    text_align 0.5
    xalign 0.5
    line_spacing 10


#  info bubble one
screen infobubble(title, content, confirmation):
    zorder 3
    frame:
        style "info_bubble_frame"
        background Image("ui/quit_box.png", xalign=0.5, yalign=0.5)

        vbox:
            yalign 0.0
            frame:
                xsize 666
                background None
                text title id _("title"):
                    style "info_bubble_title"
            null height 10
            frame:
                xsize 666
                background None
                text content id "content /n/n/n":
                    style "info_bubble_content"
                    ymaximum 50
        hbox:
            yalign 0.65
            xalign 0.5
            textbutton confirmation id _("confirmation"):
                style "centered_button"
                text_style "info_bubble_button_text"
                action NullAction


# info bubble two
screen infobubble_confirm_cancel(title, content, confirmation, cancel, cancel_destination):
    zorder 3
    frame:
        style "info_bubble_frame"
        background Image("ui/quit_box.png", xalign=0.5, yalign=0.5)
        vbox:
            yalign 0.0
            frame:
                xsize 680
                background None
                text title id _("title"):
                    style "info_bubble_title"
            null height 10
            frame:
                xsize 680
                background None
                text content id "content /n/n/n":
                    style "info_bubble_content"
                    ymaximum 50
        hbox:
            xsize 680
            yalign 0.65
            textbutton confirmation id _("confirmation"):
                style "centered_button_2column"
                text_style "info_bubble_button_text_2"
                action NullAction
            textbutton cancel id _("cancel"):
                style "centered_button_2column"
                text_style "info_bubble_button_text_2"
                action Jump(cancel_destination)


# input screen for text inputs, similar to infobubble
screen input_screen(title):
    frame:
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.5
        xsize 600
        background Image("ui/quit_box.png", xalign=0.5, yalign=0.5)

        vbox:

            text title id _("title"):
                style "info_bubble_title"
