from manimlib import *
import numpy as np


def heart_point(theta):
    """
    Polar form of (x^2 + y^2 - 1)^3 = x^2 y^3.

    With x = r cos(theta), y = r sin(theta), solve the resulting
    scalar equation for its positive radial root using bisection.
    """
    c = np.cos(theta)
    s = np.sin(theta)
    angular_term = c * c * s * s * s

    lo, hi = 0.0, 3.0
    for _ in range(64):
        r = 0.5 * (lo + hi)
        value = (r * r - 1.0) ** 3 - (r ** 5) * angular_term
        if value > 0:
            hi = r
        else:
            lo = r

    r = 0.5 * (lo + hi)
    return np.array([r * c, r * s, 0.0])


class HeartEquation(Scene):
    def construct(self):
        self.camera.background_color = "#10131C"

        heading = Text(
            "A curve hidden in an equation",
            font_size=34,
            color=WHITE,
        ).to_edge(UP, buff=0.45)

        equation = Tex(
            R"(x^2+y^2-1)^3=x^2y^3",
            font_size=46,
            color="#F5F5F5",
        ).next_to(heading, DOWN, buff=0.28)

        # Build the exact implicit curve numerically in polar coordinates.
        thetas = np.linspace(0, TAU, 1601)
        points = [heart_point(theta) for theta in thetas]
        curve = VMobject()
        curve.set_points_smoothly(points)
        curve.set_stroke(color="#FF4F87", width=5)

        # A faint reference grid keeps the graph legible without competing
        # with the curve.
        grid = NumberPlane(
            (-1.8, 1.8, 0.5),
            (-1.6, 1.6, 0.5),
            background_line_style={
                "stroke_color": "#596273",
                "stroke_opacity": 0.22,
                "stroke_width": 1,
            },
            axis_config={
                "stroke_color": "#AAB2C0",
                "stroke_opacity": 0.55,
                "stroke_width": 1.5,
            },
        )
        grid.set_width(8.2)
        grid.move_to(DOWN * 0.55)

        curve.set_width(5.3)
        curve.move_to(grid.get_center() + DOWN * 0.02)

        caption = Text(
            "The heart curve",
            font_size=25,
            color="#FF9DBB",
        ).to_edge(DOWN, buff=0.42)

        self.play(FadeIn(heading, shift=DOWN * 0.15))
        self.play(Write(equation))
        self.play(ShowCreation(grid), run_time=1.5)
        self.wait(0.4)
        self.play(
            ShowCreation(curve, rate_func=linear),
            run_time=5,
        )
        self.play(FadeIn(caption, shift=UP * 0.12))
        self.wait(2)
