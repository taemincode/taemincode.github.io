from manim import *
import numpy as np

class CostLandscapes(Scene):
    def construct(self):
        # Title
        title = Text("MSE with linear vs logistic regression", font_size=42, color=WHITE).to_edge(UP)

        # Shared axis style
        def make_axes():
            ax = Axes(
                x_range=[-4, 4, 1],
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
            return ax

        # Two side-by-side panels (shifted lower)
        axes_L = make_axes().to_edge(LEFT).shift(DOWN*1)
        axes_R = make_axes().to_edge(RIGHT).shift(DOWN*1)

        # Left: Linear regression + convex
        lin_title = Text("linear regression", font_size=36, color=WHITE).next_to(axes_L, UP, buff=1)

        lin_eq = MathTex(r"f_{\vec{w},b}(\vec{x})=\vec{w}\cdot\vec{x}+b", font_size=34, color=WHITE)
        lin_eq.next_to(lin_title, DOWN, buff=0.25)

        def convex(x):
            return 0.35*(x-1.1)**2 + 0.6

        curve_L = axes_L.plot(convex, x_range=[-3.2, 3.2], color=BLUE, stroke_width=6)

        convex_lbl = Text("convex", font_size=30, color=WHITE).next_to(axes_L, DOWN, buff=0.2)

        left_group = VGroup(axes_L, curve_L, convex_lbl, lin_title, lin_eq)

        # Right: Logistic regression + non-convex
        logi_title = Text("logistic regression", font_size=36, color=WHITE).next_to(axes_R, UP, buff=1)

        logi_eq = MathTex(
            r"f_{\vec{w},b}(\vec{x})=\frac{1}{1+e^{-(\vec{w}\cdot\vec{x}+b)}}",
            font_size=34, color=WHITE
        ).next_to(logi_title, DOWN, buff=0.05)

        def nonconvex(x):
            return 0.7*np.sin(1.4*x) + 0.18*(x+1.2)**2 + 2.4

        curve_R = axes_R.plot(nonconvex, x_range=[-3.2, 3.2], color=BLUE, stroke_width=6)

        nonconvex_lbl = Text("non-convex", font_size=30, color=WHITE).next_to(axes_R, DOWN, buff=0.2)

        right_group = VGroup(axes_R, curve_R, nonconvex_lbl, logi_title, logi_eq)

        # Assemble
        self.add(title, left_group, right_group)