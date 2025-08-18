from manim import *

class LinearRegression(Scene):
    def construct(self):
        # Title
        title = Text("Linear Regression", font_size=42)
        title.to_edge(UP)

        # Axes
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 8, 1],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": True},
        ).to_edge(DOWN)

        # Labels
        x_label = axes.get_x_axis_label(MathTex("x"), edge=RIGHT, direction=RIGHT)
        y_label = axes.get_y_axis_label(MathTex("y"), edge=UP, direction=UP)

        # Sample data points
        data = [(1, 1.5), (2, 2.1), (3, 2.8), (4, 4.2), (5, 4.9), (6, 5.7)]
        dots = [Dot(axes.c2p(x, y), color=WHITE) for x, y in data]

        # Regression line: y = 0.8x + 0.5
        regression_line = axes.plot(lambda x: 0.8 * x + 0.5, color=BLUE)

        # Equation label
        equation = MathTex("y = 0.8x + 0.5", font_size=36)
        equation.next_to(axes.c2p(4.5, 4.1), RIGHT)

        # Add to scene
        self.add(title, axes, x_label, y_label, regression_line, equation, *dots)

        # Hold on final frame
        self.wait()
