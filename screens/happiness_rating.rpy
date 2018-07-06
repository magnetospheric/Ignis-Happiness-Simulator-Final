#define screen to notify whether happiness has increased or decreased
#this appears in the centre of the screen - show/hide must be controlled on scene side
screen happiness_text(title):
    frame:
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.5
        background None

        vbox:
            text title id _("title"):
                style "happiness_style"

style happiness_style is text:
    color "#fefefe"
    size 32
    yalign 0.5
    xalign 0.5
    drop_shadow (1, 1)
    outlines [ (2, "#040404", 0, 0), (1, "#444", 0, 0) ]


#set overlay in python

init python:

    #This controls when the floater appears.
    show_happiness=False

    ## ------------ Happiness Floater ----------------------

    def stats_overlay():

        # --- Happiness Bar -------
        if show_happiness:
            # set up a transparent frame to put things in
            ui.frame(
                xalign = 0.925,
                ypos = 0.04,
                style = "title_frame",
            )

            ui.vbox(xalign = 0)

            ui.bar(max_happiness, happiness,
                style="my_bar")

            ui.text ("HAPPINESS",
                font = "fonts/Birch.ttf",
                outlines = [ (2, "#ffffff26", 0, 0), (1, "#321226", 0, 0)  ],
                xalign = 1.0,
                ypos = 10,
                color = "#f7f3f1",
                size=26)

            ui.text ("[happiness]",
                font = "fonts/Birch.ttf",
                outlines = [ (2, "#ffffff26", 0, 0), (1, "#321226", 0, 0)  ],
                xalign = 1.0,
                ypos = 10,
                color = "#f7f3f1",
                size=26)

            ui.close() #closes vbox


    config.overlay_functions.append(stats_overlay)


    # def end_rating():
    #
    #     # --- Happiness Bar -------
    #     if show_rating:
    #
    #         # set up a transparent frame to put things in
    #         ui.frame(
    #         xalign = 0.96,
    #         ypos = 0.04,
    #         style = "title_frame",
    #         )
    #
    #         ui.vbox(xalign = 0)
    #
    #         if happiness == 20:
    #
    #
    #
    #         ui.close() #closes vbox
    #         # elif happiness >= 18:
    #         #
    #         # elif happiness >= 15:
    #         #
    #         # elif happiness >= 11:
    #         #
    #         # elif happiness >= 6:
    #         #
    #         # elif happiness >= 2:
    #
    #         ui.text ("HAPPINESS",
    #             xalign = 0.05,
    #             ypos = 2,
    #             color = "#ededda",
    #             size=20)
    #
    #         ui.bar(max_happiness, happiness,
    #             style="my_bar")
    #
    #
    #
    #
    # config.overlay_functions.append(stats_overlay)
    #

init -2 python:
    happiness = 2
    max_happiness = 18.6

init -5 python:
    #custom bar
    style.my_bar = Style(style.default)
    style.my_bar.xalign = 0.5
    style.my_bar.ypos = 0
    style.my_bar.xmaximum = 260 # bar width
    style.my_bar.ymaximum = 18 # bar height
    style.my_bar.left_gutter = 10
    style.my_bar.right_gutter = 0

    style.my_bar.left_bar = Frame("ui/bar_full.png", 0, 0)
    style.my_bar.right_bar = Frame("ui/bar_empty.png", 0, 0)

    # style.my_bar.thumb = "ui/thumb.png"
    # style.my_bar.thumb_shadow = None
    # style.my_bar.thumb_offset = 14

    style.my_bar.font = "fonts/AvantGarde-Book.ttf"

    style.title_frame = Style(style.default)
