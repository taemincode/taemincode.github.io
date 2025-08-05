from manim import *
import numpy as np

class GradientDescentSurface(ThreeDScene):
    def func(self, x, y):
        # Simulated cost function with multiple local minima
        return np.sin(3 * x) * np.cos(3 * y) + (x - 0.5)**2 + (y - 0.5)**2

    def construct(self):
        # Set up the 3D axes
        axes = ThreeDAxes(
            x_range=[0, 1, 0.2],
            y_range=[0, 1, 0.2],
            z_range=[-2, 3, 1],
            x_length=6,
            y_length=6,
            z_length=3,
        )

        labels = axes.get_axis_labels(
            Tex(r"$\theta_0$"), Tex(r"$\theta_1$"), Tex(r"$J(\theta_0, \theta_1)$")
        )

        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)

        surface = Surface(
            lambda u, v: axes.c2p(u, v, self.func(u, v)),
            u_range=[0, 1],
            v_range=[0, 1],
            resolution=(30, 30),
            fill_opacity=0.9,
            checkerboard_colors=[BLUE_C, TEAL_D],
            stroke_color=WHITE,
            stroke_opacity=0.1
        )

        # Gradient descent path
        path_points = [
            np.array([0.9, 0.9]),
            np.array([0.75, 0.75]),
            np.array([0.6, 0.6]),
            np.array([0.45, 0.5]),
            np.array([0.35, 0.4]),
            np.array([0.25, 0.35]),
            np.array([0.2, 0.3]),
        ]

        arrows = VGroup()
        for i in range(len(path_points) - 1):
            p1 = axes.c2p(*path_points[i], self.func(*path_points[i]))
            p2 = axes.c2p(*path_points[i+1], self.func(*path_points[i+1]))
            arrow = Arrow3D(p1, p2, color=RED, stroke_width=3)
            arrows.add(arrow)

        self.add(axes, labels, surface, arrows)