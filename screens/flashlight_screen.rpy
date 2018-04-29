
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       flashlight_screen.rpy [Flashlight]
#       screen which displays flashlight over current background and Character
#       calls a class named Flashlight, a custom renpy Displayable
#
#       Flashlight contains flashlight overlay,
#                           guard awareness counter and bar
#
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

init python:

    class Flashlight(renpy.Displayable):

        lightcount = 0
        lightcounttext = "0"
        timer = False

        def __init__(self, **kwargs):

            super(Flashlight, self).__init__(**kwargs)

            # set timer value for use in rest of class
            self.timer = kwargs["timer"]

            # This image should be twice the width and twice the height
            # of the screen.
            self.child = Image("images/flashlight-off.png")

            # (-1, -1) is the way the event system represents
            # "outside the game window".
            self.pos = (-1, -1)

            # Bar to show guards' awareness when flashlight is used
            self.awareness = renpy.displayable(Solid("#F00"))
            self.awareness_size = (1280,7)
            self.awareness_alpha = 0

            # Numerical value of times flashlight has been turned on
            self.awareness_counter = renpy.displayable(Text(Flashlight.lightcounttext))
            self.awareness_counter_size = (30,30)
            self.awareness_counter_alpha = 0

            # Will also need variable to store seconds passed while flashlight on
            self.flashlight_start_time = 0
            self.some_time_val = 0;

        # method that gets called every x seconds
        def update(self, timeSelfShownFor):
            if self.flashlight_start_time > 0:
                self.some_time_val = timeSelfShownFor - self.flashlight_start_time
                #reduce countdown by timeval

            # skip to timeout if time exceeds x seconds
            if self.timer == True:
                if self.some_time_val >= 5:
                    renpy.ui.jumps("boom")()

            # redraw after x seconds
            renpy.display.render.redraw(self, 0.3)

        def render(self, width, height, st, at):

            # run the update method
            self.update(st)

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

            # Render Guard Awareness (renders on top of flashlight)
            awareness = Transform(child=self.awareness, alpha=self.awareness_alpha)
            awareness_render = renpy.render(awareness, 1280, 7, st, at)
            if self.timer == True:
                render.blit(awareness_render, (0, 10))

            # Render Awareness counter (renders on top of flashlight)
            #^^THIS WILL CHANGE TO BATTERY LIFE (based on total time on?)
            awarenesscount = Transform(child=self.awareness_counter, alpha=self.awareness_counter_alpha)
            awareness_counter_render = renpy.render(awarenesscount, 30, 30, st, at)
            if self.timer == True:
                render.blit(awareness_counter_render, ((flashlight_width / 4), 30))

            return render


        def event(self, ev, x, y, st):
            #redraw the instant event is triggered
            #this allows flashlight to appear without req. drag + pos change
            renpy.redraw(self, 0)

            # has to be defined inside event
            def setlightcount(count):
                Flashlight.lightcount = count
                Flashlight.lightcounttext = "%d" % Flashlight.lightcount

            # would be real nice to have a small fade-in when torch turns on

            # if mouse clicked
            if renpy.map_event(ev,"mousedown_1"):

                if self.child == Image("images/flashlight.png"):

                    # swap out for flashlight OFF
                    self.child = Image("images/flashlight-off.png")

                    # turns off the countdown
                    self.flashlight_start_time = 0

                    # turn off awareness alphas to hide awareness bar
                    self.awareness_alpha = 0
                    self.awareness_counter_alpha = 0

                elif self.child == Image("images/flashlight-off.png"):

                    # swap out for flashlight ON (if countdown > 0)
                    self.child = Image("images/flashlight.png")
                    #if countdown < 0,

                    #turns on countdown
                    self.flashlight_start_time = st

                    # increment counter for amount of times light turned on
                    setlightcount(Flashlight.lightcount + 1)

                    # turn on awareness alphas to show awareness bar
                    self.awareness_alpha = 1
                    self.awareness_counter_alpha = 1

                    # update awareness counter's value
                    self.awareness_counter = renpy.displayable(Text(Flashlight.lightcounttext))

                renpy.redraw(self,0)

            # Re-render if the position changed.
            #PROBABLY DONT NEED THIS IN FUTURE.
            #BUT GOOD TO KEEP IF I WANT TO GENERATE AN EVENT ON MOUSE MOVEMENT
            #LIKE IN UNTIL DAWN
            if self.pos != (x, y):
                renpy.redraw(self, 0)

            # Update stored position
            self.pos = (x, y)

        #return our objects
        def visit(self):
            return [ self.awareness, self.awareness_counter, self.child ]


screen flashlight:
    # everything happens in Flashlight class
    add Flashlight(timer=True)

screen flashlight_no_timer:
    # everything happens in Flashlight class
    add Flashlight(timer=False)

# this will go in its own file eventually
label boom:
    # will have conditions here according to where in the game you are on discovery
    "Oh no..."

    "YOU'VE BEEN DISCOVERED!"

    return
