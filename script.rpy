# script for Prompto Happiness Simulator 2k17
# authored by Olly Ferrie
# created 07-05-2017
#last edited 08-05-2017

### Character definitions ###
define ignis = Character("Ignis")
#### Character Images ####
image ignis neutral  = "images/ignis-neutral.png"
#### Background Images ####
image bg altissia_alleyway = 'images/altissia-alleyway-night.jpg'

#plan - first we need a simple scene where your mouse cursor hovering creates a flashlight effect
#second, we need the same scene, but the flashlight effect is only triggered when you click


init python:

    class Flashlight(renpy.Displayable):
        def __init__(self):
            super(Flashlight, self).__init__()

            # This image should be twice the width and twice the height
            # of the screen.
            self.child = Image("images/flashlight-off.png")

            # (-1, -1) is the way the event system represents
            # "outside the game window".
            self.pos = (-1, -1)

        def render(self, width, height, st, at):
            render = renpy.Render(config.screen_width, config.screen_height)

            if self.pos == (-1, -1):
                # If we don't know where the cursor is, render pure black.
                render.canvas().rect("#000", (0, 0, config.screen_width, config.screen_height))
                return render

            # Render the flashlight image.
            child_render = renpy.render(self.child, width, height, st, at)

            # Draw the image centered on the cursor.
            flashlight_width, flashlight_height = child_render.get_size()
            x, y = self.pos
            x -= flashlight_width / 2
            y -= flashlight_height / 2
            render.blit(child_render, (x, y))
            return render

        def event(self, ev, x, y, st):

            #redraw the instant event is triggered
            #this allows flashlight to appear without req. drag + pos change
            renpy.redraw(self, 0)
            
            #if renpy.map_event(ev,"drag_activate"):
            if renpy.map_event(ev,"mousedown_1"):
                self.child = Image("images/flashlight.png")
            elif renpy.map_event(ev,"mouseup_1"):
                self.child = Image("images/flashlight-off.png")

            # Re-render if the position changed.
            if self.pos != (x, y):
                renpy.redraw(self, 0)

            # Update stored position
            self.pos = (x, y)

        def visit(self):
            return [ self.child ]


screen flashlight_demo:
    textbutton "continue" xpos 300 ypos 300 action Return()
    add Flashlight()


# The game starts here.

label start:

    #shows the first background
    scene bg altissia_alleyway

    #shows the first character
    show ignis neutral
    with dissolve

    # These display lines of dialogue.

    "Altissia, on the day of the Covenant. Everything is going to hell."

    ignis "I've run into a bit of trouble. Would you care to help me?"

    ignis "Look around this room and see if there's anything useful."

    $ mouse_visible = False
    call screen flashlight_demo

    hide ignis neutral
    with dissolve

    #return to title screen
    return
