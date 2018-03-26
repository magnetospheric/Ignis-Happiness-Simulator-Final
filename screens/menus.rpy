################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.


screen navigation():

    if main_menu:

        vbox:
            style_prefix "navigation"

            xalign 0.77
            yalign 0.90

            spacing 0

            textbutton _("{k=-1.0}NEW GAME{/k}"):
                style "menu_item_1"
                text_style "menu_item_text"
                action Start()

            textbutton _("{k=-1.0}LOAD GAME{/k}"):
                style "menu_item_2"
                text_style "menu_item_text"
                action ShowMenu("load")

            textbutton _("{k=-1.0}OPTIONS{/k}"):
                style "menu_item_3"
                text_style "menu_item_text"
                action ShowMenu("preferences")

            textbutton _("{k=-1.0}ABOUT{/k}"):
                style "menu_item_4"
                text_style "menu_item_text"
                action ShowMenu("about")

            if renpy.variant("pc"):

                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("{k=-1.0}HELP{/k}"):
                    style "menu_item_5"
                    text_style "menu_item_text"
                    action ShowMenu("help")

                ## The quit button is banned on iOS and unnecessary on Android.
                textbutton _("{k=-1.0}QUIT{/k}"):
                    style "menu_item_6"
                    text_style "menu_item_text"
                    action Quit(confirm=not main_menu)

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)

    else:

        hbox:

            style_prefix "navigation_ingame"

            xalign 0.48
            yalign 0.84

            spacing 0

            textbutton _("{k=-0.4}SAVE{/k}"):
                style "menu_item_ingame"
                text_style "ingame_menu_item_text"
                action ShowMenu("save")

            textbutton _("{k=-0.4}LOAD{/k}"):
                style "menu_item_ingame"
                text_style "ingame_menu_item_text"
                action ShowMenu("load")

            textbutton _("{k=-0.4}OPTIONS{/k}"):
                style "menu_item_ingame"
                text_style "ingame_menu_item_text"
                action ShowMenu("preferences")

            textbutton _("{k=-0.4}ABOUT{/k}"):
                style "menu_item_ingame"
                text_style "ingame_menu_item_text"
                action ShowMenu("about")

            if _in_replay:

                textbutton _("End Replay") action EndReplay(confirm=True)


            textbutton _("{k=-0.4}MAIN MENU{/k}"):
                style "menu_item_ingame"
                text_style "ingame_menu_item_text"
                action MainMenu()

            if renpy.variant("pc"):

                    ## Help isn't necessary or relevant to mobile devices.
                    textbutton _("{k=-0.4}HELP{/k}"):
                        style "menu_item_ingame"
                        text_style "ingame_menu_item_text"
                        action ShowMenu("help")

                    ## The quit button is banned on iOS and unnecessary on Android.
                    textbutton _("{k=-0.4}QUIT{/k}"):
                        style "menu_item_ingame"
                        text_style "ingame_menu_item_text"
                        action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

## Styles for indented main menu items ##
style menu_item_text is text:
    # hover_color "#d1d7e3"
    hover_color "#cdb2cd"
    # outlines [ (0, "#fff", 1, 1), (2, "#8f98a8", 0, 0) ]
    outlines [ (0, "#fff", 1, 1), (2, "#481a36", 0, 0) ]
    color "#f5ddf5"
    size 18

style ingame_menu_item_text is text:
    hover_color "#cdb2cd"
    outlines [ (2, "#fff", 0, 0), (3, "#481a36", 1, 0) ]
    color "#f5ddf5"
    size 20

style menu_item_1:
    left_margin 0

style menu_item_2:
    left_margin 28

style menu_item_3:
    left_margin 56

style menu_item_4:
    left_margin 84

style menu_item_5:
    left_margin 112

style menu_item_6:
    left_margin 140

style menu_item_ingame:
    left_margin 20




## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        xalign -300
        ypos 526
        background "ui/main_menu_bg.png"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.

    if is_load_screen == False:
        use navigation

    if gui.show_name == False:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 1280

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
