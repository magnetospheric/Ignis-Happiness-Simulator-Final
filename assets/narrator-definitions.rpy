
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#
#       Assets: Narrator definitions
#
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


define centered = Character(
                            None,
                            what_size=20,
                            what_outlines=[(2, "#ffffff33", 0, 0)],
                            callback=clicky_typewriter_titles,
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.5,
                            window_yalign=0.32
                        )
define centered_titles = Character(
                            None,
                            what_size=20,
                            what_outlines=[(2, "#ffffff33", 0, 0)],
                            callback=clicky_typewriter_titles,
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.5,
                            window_yalign=0.32
                        )
define top_narrator = Character(
                            '',
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/transparent.png",
                            what_outlines=[(2, "#ffffff33", 0, 0)],
                            callback=clicky_typewriter,
                            window_yalign=0.1,
                            window_xalign=0,
                            window_xsize=800
                        )
define topcentre_narrator = Character(
                            '',
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/transparent.png",
                            what_outlines=[(2, "#ffffff33", 0, 0)],
                            callback=clicky_typewriter,
                            window_yalign=0.3,
                            window_xalign=0.2,
                            window_xsize=800
                        )
define centre_narrator = Character(
                            '',
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/transparent.png",
                            callback=clicky_typewriter,
                            window_yalign=0.5,
                            window_xalign=0.45,
                            window_xsize=900
                        )
define centrebottomright_narrator = Character('',
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/transparent.png",
                            callback=clicky_typewriter,
                            window_yalign=0.85,
                            window_xalign=0.7,
                            window_xsize=500
                        )
define narrator1 = Character(
                            '',
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            callback=clicky_typewriter,
                            window_background="images/ui/dialog_bg02.png",
                        )
define narrator1_nosound = Character(
                            '',
                            ctc="ctc_blink",
                            ctc_position="fixed",
                            window_background="images/ui/dialog_bg02.png"
                        )
