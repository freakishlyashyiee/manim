# Heart curve animation

This repository is a fork of the original 3Blue1Brown ManimGL project.
The animation is written for **ManimGL** (the `manimgl` package), not
Manim Community Edition.

## Equation

\[
(x^2+y^2-1)^3=x^2y^3
\]

## Run it

From the repository root, with ManimGL and its system dependencies installed:

```bash
manimgl heart_curve.py HeartEquation -w
```

The `-w` flag writes the rendered video. To preview interactively, omit `-w`.

The scene numerically solves the polar form of the implicit equation with
bisection, samples the resulting closed curve, and animates its outline.
