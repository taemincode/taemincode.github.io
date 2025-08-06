from manim import *

class LearningRateComparison(Scene):
    def construct(self):
        # Titles
        small_title = Text("Small Learning Rate", font_size=28).to_edge(UP + LEFT).shift(RIGHT * 2)
        large_title = Text("Large Learning Rate", font_size=28).to_edge(UP + RIGHT).shift(LEFT * 2)

        # Axes
        small_axes = Axes(x_range=[-3, 3], y_range=[0, 10], x_length=5, y_length=4).shift(LEFT * 3)
        large_axes = Axes(x_range=[-3, 3], y_range=[0, 25], x_length=5, y_length=4).shift(RIGHT * 3)

        # Loss function
        loss_func = lambda x: x**2 + 1
        small_curve = small_axes.plot(loss_func, color=BLUE)
        large_curve = large_axes.plot(loss_func, color=BLUE)

        # Small learning rate path
        small_points = [1.8, 1.6, 1.4, 1.2, 1.0, 0.85, 0.7, 0.55, 0.4, 0.3, 0.2, 0.1, 0.05]
        small_dots = [Dot(small_axes.c2p(x, loss_func(x)), radius=0.05, color=WHITE) for x in small_points]
        small_arrows = [
            Arrow(
                small_axes.c2p(small_points[i], loss_func(small_points[i])),
                small_axes.c2p(small_points[i+1], loss_func(small_points[i+1])),
                buff=0.05, stroke_width=2, color=YELLOW
            ) for i in range(len(small_points)-1)
        ]

        # Large learning rate path
        large_points = [1.5, -2.0, 2.3, -2.5, 2.8]
        large_dots = [Dot(large_axes.c2p(x, loss_func(x)), radius=0.05, color=WHITE) for x in large_points]
        large_arrows = [
            Arrow(
                large_axes.c2p(large_points[i], loss_func(large_points[i])),
                large_axes.c2p(large_points[i+1], loss_func(large_points[i+1])),
                buff=0.05, stroke_width=2, color=RED
            ) for i in range(len(large_points)-1)
        ]

        # Axis labels
        loss_label_l = Text("loss", font_size=20).next_to(small_axes.y_axis.get_end(), LEFT)
        loss_label_r = Text("loss", font_size=20).next_to(large_axes.y_axis.get_end(), LEFT)
        weight_label_l = Text("value of\nweight", font_size=18).next_to(small_axes.x_axis.get_end(), DOWN)
        weight_label_r = Text("value of\nweight", font_size=18).next_to(large_axes.x_axis.get_end(), DOWN)

        # Add everything to the scene at once
        self.add(
            small_title, large_title,
            small_axes, large_axes,
            small_curve, large_curve,
            *small_dots, *small_arrows,
            *large_dots, *large_arrows,
            loss_label_l, loss_label_r,
            weight_label_l, weight_label_r,
        )

        # Required to render the final frame
        self.wait()