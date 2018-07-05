screen generator_button():
    vbox:
        imagebutton:
            idle "images/items/generator-button-idle.png"
            hover "images/items/generator-button-hover.png"
            xpos 267 ypos 303
            action Jump("room_02_post_generator")
