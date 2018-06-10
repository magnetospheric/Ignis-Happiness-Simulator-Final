screen generator_button():
    vbox:
        imagebutton:
            idle "images/items/generator-button-idle.png"
            hover "images/items/generator-button-hover.png"
            xpos 60 ypos 510
            action Jump("room_02_post_generator")
