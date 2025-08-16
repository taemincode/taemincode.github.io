from manim import *
import numpy as np

class LogisticRegression(Scene):
    def construct(self):
        # Title
        title = Text("Logistic Regression", font_size=42).to_edge(UP)

        # Axes
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[0, 1, 0.1],
            x_length=7,
            y_length=5,
            tips=False,
            axis_config={
                "include_numbers": False,   # we'll add only 0, 0.5, 1
                "stroke_width": 2,
            },
        ).to_edge(DOWN)

        # Only show key y labels (0, 0.5, 1) to avoid clutter
        ylabels = VGroup(
            MathTex("0.0").scale(0.7).next_to(axes.c2p(0, 0.05), LEFT, buff=0.25),
            MathTex("0.5").scale(0.7).next_to(axes.c2p(0, 0.5), LEFT, buff=0.25),
            MathTex("1.0").scale(0.7).next_to(axes.c2p(0, 1.0), LEFT, buff=0.25),
        )
        # Light tick marks at these y values
        yticks = VGroup(*[
            Line(axes.c2p(-0.1, y), axes.c2p(0.1, y), stroke_width=2) for y in [0, 0.5, 1]
        ])

        # Minimal axis labels (same style as linear scene)
        x_label = axes.get_x_axis_label(MathTex("x"))
        y_label = axes.get_y_axis_label(MathTex("y"))

        # Logistic curve (blue)
        w, b = 1.6, 0.0
        sigmoid = lambda x: 1 / (1 + np.exp(-(w * x + b)))
        curve = axes.plot(sigmoid, x_range=[-6, 6], color=BLUE, stroke_width=6)

        # Compact equation, placed near the gentle part of curve (no overlap)
        eq = MathTex(r"p(y{=}1\mid x)=\frac{1}{1+e^{-(wx+b)}}", font_size=34)
        eq.next_to(axes.c2p(6, sigmoid(6)), UP, buff=0.25)

        # Threshold p = 0.5 (subtle grey, thin)
        thresh = DashedLine(
            axes.c2p(-6, 0.5), axes.c2p(6, 0.5),
            color=GREY, stroke_width=2, dash_length=0.15
        )
        t_label = MathTex("p=0.5", font_size=24, color=GREY)
        t_label.next_to(axes.c2p(6, 0.5), RIGHT, buff=0.15)

        # Data points (white dots, like your linear scene)
        # class 0 around y=0, class 1 around y=1; keep small jitter to avoid perfect line
        rng = np.random.default_rng(3)
        xs0 = rng.normal(loc=-3.2, scale=0.7, size=6)
        xs1 = rng.normal(loc= 3.0, scale=0.7, size=6)
        j0  = rng.uniform(-0.02, 0.02, size=len(xs0))
        j1  = rng.uniform(-0.02, 0.02, size=len(xs1))

        dots0 = VGroup(*[Dot(axes.c2p(float(x), float(0.04 + j0[i])), color=WHITE, radius=0.055)
                         for i, x in enumerate(xs0)])
        dots1 = VGroup(*[Dot(axes.c2p(float(x), float(0.96 + j1[i])), color=WHITE, radius=0.055)
                         for i, x in enumerate(xs1)])

        # Assemble (no animations; single clean frame)
        self.add(
            title, axes, x_label, y_label, yticks, ylabels,
            curve, eq, thresh, t_label, dots0, dots1
        )