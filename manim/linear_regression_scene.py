from manim import *

class LinearRegressionNoLaTeX(Scene):
    def construct(self):
        # Title using plain text
        title = Text("Linear Regression", font_size=36).to_edge(UP)

        # Plain coordinate grid using NumberPlane (no labels)
        grid = NumberPlane(
            x_range=[0, 7, 1],
            y_range=[0, 8, 1],
            x_length=7,
            y_length=4,
            background_line_style={"stroke_opacity": 0.4}
        ).to_edge(DOWN)

        # Manually add axis labels using Text (not MathTex)
        x_label = Text("x", font_size=24).next_to(grid.x_axis, RIGHT)
        y_label = Text("y", font_size=24).next_to(grid.y_axis, UP)

        # Data points
        points = [
            (1, 1.5),
            (2, 2),
            (3, 2.5),
            (4, 4),
            (5, 4.5),
            (6, 5.5)
        ]
        dots = [Dot(grid.c2p(x, y), color=YELLOW) for x, y in points]

        # Regression line: y = 0.8x + 0.5
        line = Line(
            start=grid.c2p(0, 0.5),
            end=grid.c2p(7, 6.1),
            color=BLUE
        )

        # Add all to scene
        self.add(title, grid, x_label, y_label, *dots, line)