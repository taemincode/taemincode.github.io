from manim import *
import numpy as np

class LinearVsPolynomial(Scene):
    def construct(self):
        # LEFT GRAPH: Linear Fit (Good)
        axes1 = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 20, 2],
            x_length=5.5,
            y_length=4,
            axis_config={"include_numbers": True},
        ).to_edge(LEFT, buff=1)

        np.random.seed(1)
        x1 = np.linspace(1, 9, 20)
        y1 = 2 * x1 + 1 + np.random.normal(0, 1.2, size=x1.shape)

        dots1 = VGroup(*[
            Dot(axes1.coords_to_point(x, y), radius=0.05, color=BLUE)
            for x, y in zip(x1, y1)
        ])

        coeffs1 = np.polyfit(x1, y1, 1)
        f1 = np.poly1d(coeffs1)
        line1 = axes1.plot(f1, x_range=[min(x1), max(x1)], color=YELLOW)

        title1 = Text("Linear Regression", font_size=28).next_to(axes1, UP)

        # RIGHT GRAPH: Linear vs Polynomial (Bad linear fit)
        axes2 = axes1.copy().to_edge(RIGHT, buff=1)

        x2 = np.linspace(1, 9, 30)
        y2 = 0.5 * (x2 - 5)**3 + 8 + np.random.normal(0, 2, size=x2.shape)

        dots2 = VGroup(*[
            Dot(axes2.coords_to_point(x, y), radius=0.05, color=BLUE)
            for x, y in zip(x2, y2)
        ])


        f2_linear = np.poly1d(np.polyfit(x2, y2, 1))
        f2_poly = np.poly1d(np.polyfit(x2, y2, 4))

        line2 = axes2.plot(f2_linear, x_range=[min(x2), max(x2)], color=YELLOW)
        curve2 = axes2.plot(f2_poly, x_range=[min(x2), max(x2)], color=GREEN)

        title2 = Text("Linear vs Polynomial", font_size=28).next_to(axes2, UP)

        # Legend (bottom center)
        legend_items = VGroup(
            Dot(color=YELLOW), Text("Linear Fit", font_size=24),
            Dot(color=GREEN), Text("Polynomial Fit", font_size=24)
        ).arrange(RIGHT, buff=0.3).to_edge(DOWN)

        # Main Title
        main_title = Text("\U0001F4DA Linear vs. Other Models", font_size=36).to_edge(UP)

        # Add everything at once (no animation)
        self.add(
            main_title,
            axes1, title1, dots1, line1,
            axes2, title2, dots2, line2, curve2,
            legend_items
        )

        self.wait()