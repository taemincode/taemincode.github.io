from manim import *
import numpy as np

class LogisticVsOtherModels(Scene):
    def construct(self):
        # ---------- helpers ----------
        def sigmoid(z):
            z = np.clip(z, -35, 35)  # numeric stability
            return 1 / (1 + np.exp(-z))

        def logistic_boundary_w(X, y, lr=0.1, steps=4000):
            """
            Fit 2D logistic regression with bias using gradient descent.
            X: (n,2), y: (n,) in {0,1}
            Returns weights [w1, w2, b] for w1*x + w2*y + b = 0
            """
            Xb = np.hstack([X, np.ones((X.shape[0], 1))])
            w = np.zeros(3)
            for _ in range(steps):
                p = sigmoid(Xb @ w)
                grad = (Xb.T @ (p - y)) / y.size
                w -= lr * grad
            return w

        def line_segment_inside_axes(axes: Axes, w, color=YELLOW, stroke_width=4):
            """Clip the implicit line w1*x + w2*y + b = 0 to the axes rectangle."""
            w1, w2, b = w
            x_min, x_max = axes.x_range[0], axes.x_range[1]
            y_min, y_max = axes.y_range[0], axes.y_range[1]

            pts = []
            # left/right borders (x = const)
            if abs(w2) > 1e-12:
                y = -(w1 * x_min + b) / w2
                if y_min <= y <= y_max: pts.append(np.array([x_min, y]))
                y = -(w1 * x_max + b) / w2
                if y_min <= y <= y_max: pts.append(np.array([x_max, y]))
            # bottom/top borders (y = const)
            if abs(w1) > 1e-12:
                x = -(w2 * y_min + b) / w1
                if x_min <= x <= x_max: pts.append(np.array([x, y_min]))
                x = -(w2 * y_max + b) / w1
                if x_min <= x <= x_max: pts.append(np.array([x, y_max]))

            # dedupe and take two distinct points
            uniq = []
            for p in pts:
                if all(np.linalg.norm(p - q) > 1e-6 for q in uniq):
                    uniq.append(p)
            if len(uniq) < 2:
                return VGroup()  # nothing visible inside
            p1, p2 = uniq[0], uniq[1]
            return Line(axes.c2p(*p1), axes.c2p(*p2), color=color, stroke_width=stroke_width)

        # ---------- axes ----------
        axes_config = dict(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=5.5,
            y_length=5.5,
            axis_config={"include_numbers": True},
        )

        # ---------- LEFT: logistic does well (linearly separable) ----------
        axes1 = Axes(**axes_config).to_edge(LEFT, buff=0.8)
        title1 = Text("Logistic Regression", font_size=28).next_to(axes1, UP)

        np.random.seed(7)
        n1 = 60
        A = np.random.multivariate_normal(mean=[-1.5, -0.5],
                                          cov=[[0.6, 0.2], [0.2, 0.6]], size=n1)
        B = np.random.multivariate_normal(mean=[ 1.5,  0.5],
                                          cov=[[0.6,-0.1], [-0.1,0.6]], size=n1)
        dotsA_left = VGroup(*[Dot(axes1.c2p(x, y), radius=0.05, color=BLUE) for x, y in A])
        dotsB_left = VGroup(*[Dot(axes1.c2p(x, y), radius=0.05, color=RED)  for x, y in B])

        X_left = np.vstack([A, B])
        y_left = np.hstack([np.zeros(len(A)), np.ones(len(B))])
        w_left = logistic_boundary_w(X_left, y_left)
        line_left = line_segment_inside_axes(axes1, w_left)

        # ---------- RIGHT: logistic struggles; nonlinear model fits ----------
        axes2 = Axes(**axes_config).to_edge(RIGHT, buff=0.8)
        title2 = Text("Logistic Regression vs Other model", font_size=28).next_to(axes2, UP)

        n2 = 120
        r_inner = np.random.normal(loc=1.2, scale=0.25, size=n2 // 2)
        th_inner = np.random.uniform(0, 2*np.pi, size=n2 // 2)
        A2 = np.column_stack([r_inner * np.cos(th_inner), r_inner * np.sin(th_inner)])

        r_outer = np.random.normal(loc=2.6, scale=0.25, size=n2 // 2)
        th_outer = np.random.uniform(0, 2*np.pi, size=n2 // 2)
        B2 = np.column_stack([r_outer * np.cos(th_outer), r_outer * np.sin(th_outer)])

        dotsA_right = VGroup(*[Dot(axes2.c2p(x, y), radius=0.05, color=BLUE) for x, y in A2])
        dotsB_right = VGroup(*[Dot(axes2.c2p(x, y), radius=0.05, color=RED)  for x, y in B2])

        X_right = np.vstack([A2, B2])
        y_right = np.hstack([np.zeros(len(A2)), np.ones(len(B2))])
        w_right = logistic_boundary_w(X_right, y_right)
        line_right = line_segment_inside_axes(axes2, w_right)

        # Nonlinear boundary (visual guide)
        r_sep = 2.0
        circle_nonlinear = ParametricFunction(
            lambda t: axes2.c2p(r_sep*np.cos(t), r_sep*np.sin(t)),
            t_range=[0, 2*np.pi],
            color=GREEN,
            stroke_width=4,
        )

        # ---------- legend ----------
        legend_items = VGroup(
            Dot(color=BLUE), Text("Class A", font_size=24),
            Dot(color=RED), Text("Class B", font_size=24),
            Line(LEFT*0.3, RIGHT*0.3, color=YELLOW, stroke_width=6), Text("Logistic Boundary", font_size=24),
            Line(LEFT*0.3, RIGHT*0.3, color=GREEN, stroke_width=6), Text("Nonlinear Boundary", font_size=24),
        ).arrange(RIGHT, buff=0.35).to_edge(DOWN)

        # ---------- draw ----------
        self.add(
            # Left
            axes1, title1, dotsA_left, dotsB_left, line_left,
            # Right
            axes2, title2, dotsA_right, dotsB_right, line_right, circle_nonlinear,
            # Legend
            legend_items
        )
        self.wait()