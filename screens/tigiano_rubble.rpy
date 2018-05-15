screen tigiano_rubble():
    vbox:
        imagebutton:
            idle "images/items/keys-default.png"
            hover "images/items/keys-hover.png"
            xpos 92 ypos 327
            action Jump("harpoon")
        imagebutton:
            idle "images/items/keys-default.png"
            hover "images/items/keys-hover.png"
            xpos 92 ypos 327
            action Jump("found_ignis")

screen harpoon_inactive():
    vbox:
        imagebutton:
            idle "images/items/keys-default.png"
            xpos 92 ypos 327

screen harpoon_large():
    vbox xalign 0.5 yalign 0.2:
        imagebutton:
            idle "images/items/keys-large.png"
            xalign 1.0
