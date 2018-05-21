screen tigiano_rubble():
    vbox:
        imagebutton:
            idle "images/items/harpoon-hidden.png"
            hover "images/items/harpoon-hover.png"
            xpos 60 ypos 510
            action Jump("harpoon")
        imagebutton:
            idle "images/items/soupy-hidden.png"
            hover "images/items/soupy-hover.png"
            xpos 831 ypos 232
            action Jump("soupy")

screen harpoon_large():
    vbox xalign 0.5 yalign 0.2:
        imagebutton:
            idle "images/items/harpoon-large.png"
            xalign 1.0

screen soupy_large():
    vbox xalign 0.5 yalign 0.2:
        imagebutton:
            idle "images/items/soupy-large.png"
            xalign 1.0
