from manim import *

class HousePriceRegression(Scene):
    def construct(self):
        # Title
        title = Text("Predicting House Prices with Linear Regression", font_size=36)
        title.to_edge(UP, buff=1)  # Move title slightly lower

        # Axes: area (x) vs price (y)
        axes = Axes(
            x_range=[0, 300, 50],
            y_range=[0, 800_000, 100_000],
            x_length=7,
            y_length=4,
            axis_config={"include_ticks": True, "include_numbers": True}
        ).to_edge(DOWN)

        # Axis labels
        x_label = axes.get_x_axis_label(Text("Area (㎡)", font_size=24))
        y_label = axes.get_y_axis_label(Text("Price ($)", font_size=24))

        # Sample data points
        house_data = [
            (50, 220_000),
            (80, 280_000),
            (100, 330_000),
            (150, 430_000),
            (180, 500_000),
            (220, 600_000),
            (250, 660_000)
        ]
        dots = [Dot(axes.c2p(x, y), color=WHITE) for x, y in house_data]

        # Regression line: y = 2300x + 100000
        regression_line = axes.plot(lambda x: 2300 * x + 100_000, color=BLUE)

        # Prediction at x = 200
        pred_x = 200
        pred_y = 2300 * pred_x + 100_000
        pred_dot = Dot(axes.c2p(pred_x, pred_y), color=RED)
        pred_label = MathTex(r"\hat{y} = 2300 \times 200 + 100{,}000 = 560{,}000", font_size=32)
        pred_label.next_to(pred_dot, UP + RIGHT)

        # Equation label, moved to top right corner with a bit more padding
        equation_label = MathTex(r"\hat{y} = 2300x + 100{,}000", font_size=32)
        equation_label.to_corner(UR, buff=0.6)

        # Add all elements
        self.add(title, axes, x_label, y_label, *dots, regression_line, pred_dot, pred_label, equation_label)