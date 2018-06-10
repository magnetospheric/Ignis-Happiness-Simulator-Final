#  BLANK OVERLAY : Box to smooth over transition to flashlight overlay when black overlay previously in use
#  Stops flicker between scenes
#
#  CONTAINS:
#           blank overlay


#  info bubble one
screen blank_overlay():
    timer 0.3 action [Hide("blank_overlay"), Return("value")]
    zorder 3
