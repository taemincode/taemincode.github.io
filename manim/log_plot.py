from manim import *
import numpy as np

class LogPlot(Scene):
    def construct(self):
        # Helpers
        fw = config.frame_width
        # Horizontal offsets to center titles over left/right panels
        left_x  = -fw * 0.25
        right_x =  fw * 0.25

        # Shared axis style
        def make_axes():
            return Axes(
                x_range=[0, 1, 0.1],
                y_range=[0, 6, 1],
                x_length=5.8,
                y_length=4.2,
                tips=False,
                axis_config={
                    "include_numbers": False,
                    "stroke_width": 2,
                    "color": WHITE,
                },
            )

        # Titles (as real titles near the top, fixed to the frame)
        left_title = MathTex(r"-\log\!\left(f\right)", color=WHITE, font_size=56)
        right_title = MathTex(r"-\log\!\left(1 - f\right)", color=WHITE, font_size=56)

        # Place titles near top and centered over each half
        left_title.to_edge(UP, buff=0.6).move_to([left_x, left_title.get_y(), 0])
        right_title.to_edge(UP, buff=0.6).move_to([right_x, right_title.get_y(), 0])

        # Axes directly under each title (so they don't pull the titles when moved)
        axes_L = make_axes().next_to(left_title, DOWN, buff=1)
        axes_R = make_axes().next_to(right_title, DOWN, buff=1)

        # Slight global lift so the whole figure sits a bit higher
        group_axes = VGroup(axes_L, axes_R).shift(UP * 0.2)

        # Curves
        eps = 1e-3
        def neglog_f(x): return -np.log(np.clip(x, eps, 1 - eps))
        def neglog_one_minus_f(x): return -np.log(1 - np.clip(x, eps, 1 - eps))

        curve_L = axes_L.plot(neglog_f, x_range=[eps, 1 - eps], color=BLUE, stroke_width=6)
        curve_R = axes_R.plot(neglog_one_minus_f, x_range=[eps, 1 - eps], color=BLUE, stroke_width=6)

        # x labels
        xlab_L = MathTex("f", color=WHITE).scale(0.9).next_to(axes_L.get_x_axis(), DOWN, buff=0.25)
        xlab_R = MathTex("f", color=WHITE).scale(0.9).next_to(axes_R.get_x_axis(), DOWN, buff=0.25)

        # Mark f = 1 on both x-axes
        tick_L = Line(axes_L.c2p(1, 0), axes_L.c2p(1, -0.15), color=WHITE, stroke_width=2)
        label_L = MathTex("1", color=WHITE).scale(0.8).next_to(axes_L.c2p(1, 0), DOWN, buff=0.22)

        tick_R = Line(axes_R.c2p(1, 0), axes_R.c2p(1, -0.15), color=WHITE, stroke_width=2)
        label_R = MathTex("1", color=WHITE).scale(0.8).next_to(axes_R.c2p(1, 0), DOWN, buff=0.22)

        # Assemble
        self.add(
            left_title, right_title,
            axes_L, curve_L, xlab_L, tick_L, label_L,
            axes_R, curve_R, xlab_R, tick_R, label_R
        )