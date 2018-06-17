
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
    import time

    class DelayAction():
        wrapped = None
        start_time = 0

        def __init__(self, wrapped, delay):
            self.wrapped = wrapped
            self.start_time = time.time() + delay

        def __call__(self, *args, **kwargs):
            if time.time() > self.start_time:
                self.wrapped.__call__(*args, **kwargs)

    class Flashlight(renpy.Displayable):

        lightcount = 0
        lightcounttext = "0"
        timer = False
        buttonPosX = 0
        buttonPosY = 0
        button_idle_image = "images/items/fuse-box.png"
        button_hover_image = "images/items/fuse-box-hover.png"
        jump_destination = "images/items/fuse-box-hover.png"
        flashlight_size = "normal"

        def __init__(self, **kwargs):

            super(Flashlight, self).__init__(**kwargs)

            # set timer value for use in rest of class
            self.timer = kwargs["timer"]
            self.button_idle_image = kwargs["button_idle_image"]
            self.button_hover_image = kwargs["button_hover_image"]
            self.buttonPosX = kwargs["buttonPosX"]
            self.buttonPosY = kwargs["buttonPosY"]
            self.jump_destination = kwargs["jump_destination"]
            self.flashlight_size = kwargs["size"]

            # This image should be twice the width and twice the height
            # of the screen.
            self.child = Image("images/flashlight-off.png")
            self.button = None

            # (-1, -1) is the way the event system represents
            # "outside the game window".
            self.pos = (-1, -1)

            # Bar to show guards' awareness when flashlight is used
            # self.awareness = renpy.displayable(Solid("#F00"))
            # self.awareness = Image("images/ui/awarenessbar/awareness-bar0.png")
            # self.awareness = LiveComposite(
            #     (1280, 75),
            #     (0, 0), "awareness20",
            #     (0, 0), "awareness40",
            #     (0, 0), "awareness60",
            #     (0, 0), "awareness80",
            #     (0, 0), "awareness100"
            #     )
            self.awareness = Image("images/ui/awareness/awareness20.png")
            self.awareness2 = Image("images/ui/awareness/awareness40.png")

            self.awareness_size = (1280, 75)
            self.awareness_alpha = 0

            # Numerical value of times flashlight has been turned on
            # self.awareness_counter = renpy.displayable(Text(Flashlight.lightcounttext))
            # self.awareness_counter_size = (30,30)
            # self.awareness_counter_alpha = 0

            # Will also need variable to store seconds passed while flashlight on
            self.flashlight_start_time = 0
            self.some_time_val = 0;

        # method that gets called every x seconds
        def update(self, timeSelfShownFor):
            if self.flashlight_start_time > 0:
                self.some_time_val = timeSelfShownFor - self.flashlight_start_time
                if self.some_time_val > 0 and self.some_time_val <= 1 :
                    self.awareness = LiveComposite(
                        (1280, 75),
                        (0, 0), "awareness20"
                        )
                    self.awareness2 = Image("images/ui/awareness/awareness0.png")
                elif self.some_time_val > 1 and self.some_time_val <= 2:
                    self.awareness = Image("images/ui/awareness/awareness0.png")
                    self.awareness2 = LiveComposite(
                        (1280, 75),
                        (0, 0), "awareness40"
                        )
                elif self.some_time_val > 2 and self.some_time_val <= 3:
                    self.awareness = LiveComposite(
                        (1280, 75),
                        (0, 0), "awareness60"
                        )
                    self.awareness2 = Image("images/ui/awareness/awareness0.png")
                elif self.some_time_val > 3 and self.some_time_val <= 4:
                    self.awareness = Image("images/ui/awareness/awareness0.png")
                    self.awareness2 = LiveComposite(
                        (1280, 75),
                        (0, 0), "awareness80"
                        )
                elif self.some_time_val > 4 and self.some_time_val <= 5:
                    self.awareness = LiveComposite(
                        (1280, 75),
                        (0, 0), "awareness100"
                        )
                    self.awareness2 = Image("images/ui/awareness/awareness0.png")
                elif self.some_time_val > 5 and self.some_time_val <= 5.3:
                    self.awareness = Image("images/ui/awareness/awareness0.png")
                    self.awareness2 = LiveComposite(
                        (1280, 75),
                        (0, 0), "awarenesscrit"
                        )

                #reduce countdown by timeval

            # skip to timeout if time exceeds x seconds
            if self.timer == True:
                if self.some_time_val >= 5.3:
                    renpy.ui.jumps("boom")()

            # redraw after x seconds
            renpy.display.render.redraw(self, 0.3)

        def render(self, width, height, st, at):

            # run the update method
            self.update(st)

            render = renpy.Render(config.screen_width, config.screen_height)

            if self.pos == (-1, -1):
                # If we don't know where the cursor is, render pure black.
                render.canvas().rect("#000000f2", (0, 0, config.screen_width, config.screen_height))
                return render

            # Render the flashlight image.
            child_render = renpy.render(self.child, width, height, st, at)

            #
            if self.button != None:
                button_render = renpy.render(self.button, width, height, st, at)
                render.blit(button_render, (self.buttonPosX, self.buttonPosY))

            # Draw the image centered on the cursor.
            flashlight_width, flashlight_height = child_render.get_size()
            x, y = self.pos
            x -= flashlight_width / 2
            y -= flashlight_height / 2
            render.blit(child_render, (x, y))

            # Render Magitek Awareness (renders on top of flashlight)
            awareness = Transform(child=self.awareness, alpha=self.awareness_alpha)
            awareness2 = Transform(child=self.awareness2, alpha=self.awareness_alpha)
            awareness_render = renpy.render(awareness, 1280, 75, st, at)
            awareness2_render = renpy.render(awareness2, 1280, 75, st, at)
            if self.timer == True:
                render.blit(awareness_render, (0, 10))
                render.blit(awareness2_render, (0, 10))

            # Render Awareness counter (renders on top of flashlight)
            #^^THIS WILL CHANGE TO BATTERY LIFE (based on total time on?)
            # awarenesscount = Transform(child=self.awareness_counter, alpha=self.awareness_counter_alpha)
            # awareness_counter_render = renpy.render(awarenesscount, 30, 30, st, at)
            # if self.timer == True:
            #     render.blit(awareness_counter_render, ((flashlight_width / 4), 30))

            return render

        def event(self, ev, x, y, st):
            #redraw the instant event is triggered
            #this allows flashlight to appear without req. drag + pos change
            renpy.redraw(self, 0)

            # pass event to button
            if self.button!=None:
                self.button.event(ev, x, y, st)

            # has to be defined inside event
            def setlightcount(count):
                Flashlight.lightcount = count
                Flashlight.lightcounttext = "%d" % Flashlight.lightcount

            # would be real nice to have a small fade-in when torch turns on

            # if mouse clicked
            if renpy.map_event(ev,"mousedown_1"):

                if self.button!=None:

                    # swap out for flashlight OFF
                    self.child = Image("images/flashlight-off.png")
                    self.button = None

                    # turns off the countdown
                    self.flashlight_start_time = 0

                    # turn off awareness alphas to hide awareness bar
                    self.awareness_alpha = 0
                    # self.awareness_counter_alpha = 0

                else:

                    # need to somehow activate image buttons now
                    # self.button = renpy.displayable(ImageButton
                    # self.button = ui.imagebutton("images/items/fuse-box.png", hover = "images/items/fuse-box-hover.png", clicked = Return(), xpos=5, ypos= 0)

                    # swap out for flashlight ON (if countdown > 0)
                    if self.flashlight_size == "small":
                        self.child = Image("images/flashlight-small.png")
                    else:
                        self.child = Image("images/flashlight.png")
                    self.button = ui._imagebutton(idle_image = self.button_idle_image,
                                                  hover_image = self.button_hover_image,
                                                  clicked = DelayAction(Jump(self.jump_destination), 0.3))
                    #if countdown < 0,

                    #turns on countdown
                    self.flashlight_start_time = st

                    # increment counter for amount of times light turned on
                    setlightcount(Flashlight.lightcount + 1)

                    # turn on awareness alphas to show awareness bar
                    self.awareness_alpha = 1
                    # self.awareness_counter_alpha = 1

                    # update awareness counter's value
                    # self.awareness_counter = renpy.displayable(Text(Flashlight.lightcounttext))

                renpy.redraw(self,0)

            # Re-render if the position changed.
            #PROBABLY DONT NEED THIS IN FUTURE.
            #BUT GOOD TO KEEP IF I WANT TO GENERATE AN EVENT ON MOUSE MOVEMENT
            #LIKE IN UNTIL DAWN
            if self.pos != (x, y):
                renpy.redraw(self, 0)

            # Update stored position
            self.pos = (x, y)
            return None

        #return our objects
        def visit(self):
            return [ self.awareness, self.awareness2, self.child, self.button ]


screen flashlight:
    # everything happens in Flashlight class
    add Flashlight(timer=True)

screen flashlight_no_timer:
    # everything happens in Flashlight class
    add Flashlight(timer=False)

screen flashlight_palace_hallway:
    add Flashlight(
                    timer=False,
                    button_idle_image="images/items/yureil-hallway-door.png",
                    button_hover_image="images/items/yureil-hallway-door-hover.png",
                    buttonPosX=673,
                    buttonPosY=293,
                    jump_destination="find_fuse",
                    size="normal"
                )

screen door_idle:
    vbox:
        imagebutton:
            idle "images/items/yureil-hallway-door.png"
            hover "images/items/yureil-hallway-door.png"
            xpos 673 ypos 293
            action NullAction()

screen flashlight_fuse:
    add Flashlight(
                    timer=False,
                    button_idle_image="images/items/fuse-box.png",
                    button_hover_image="images/items/fuse-box-hover.png",
                    buttonPosX=96,
                    buttonPosY=181,
                    jump_destination="found_fuse",
                    size="normal"
                )
