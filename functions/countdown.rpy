init:
    python:

        def countdown(start, end, length=0.0):

            remaining = length - start

            if remaining > 5.0:
                return Text("%.1f" % remaining, color="#fff", size=172), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=172), .1
            else:
                return anim.Blink(Text("0.0", color="#f00", size=172)), None
