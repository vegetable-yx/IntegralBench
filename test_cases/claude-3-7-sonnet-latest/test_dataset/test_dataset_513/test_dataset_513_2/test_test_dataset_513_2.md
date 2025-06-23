# Evaluating $\int_{-4}^4|x^3-x|dx$

## Step 1: Find where $x^3-x = 0$
I need to determine where the expression inside the absolute value equals zero:
$x^3-x = x(x^2-1) = x(x-1)(x+1) = 0$

This gives us $x = 0$, $x = 1$, and $x = -1$

## Step 2: Determine the sign of $x^3-x$ in each interval
- When $x < -1$: $x^3-x < 0$ (so $|x^3-x| = -(x^3-x)$)
- When $-1 < x < 0$: $x^3-x > 0$ (so $|x^3-x| = x^3-x$)
- When $0 < x < 1$: $x^3-x < 0$ (so $|x^3-x| = -(x^3-x)$)
- When $x > 1$: $x^3-x > 0$ (so $|x^3-x| = x^3-x$)

## Step 3: Split the integral at these points
$\int_{-4}^4|x^3-x|dx = \int_{-4}^{-1}-(x^3-x)dx + \int_{-1}^{0}(x^3-x)dx + \int_{0}^{1}-(x^3-x)dx + \int_{1}^{4}(x^3-x)dx$

## Step 4: Evaluate each piece

For $\int_{-4}^{-1}-(x^3-x)dx = \int_{-4}^{-1}(-x^3+x)dx$:
$= \left[-\frac{x^4}{4}+\frac{x^2}{2}\right]_{-4}^{-1}$
$= \left[-\frac{(-1)^4}{4}+\frac{(-1)^2}{2}\right] - \left[-\frac{(-4)^4}{4}+\frac{(-4)^2}{2}\right]$
$= \left[-\frac{1}{4}+\frac{1}{2}\right] - \left[-\frac{256}{4}+\frac{16}{2}\right]$
$= \left[\frac{1}{4}\right] - \left[-64+8\right]$
$= \frac{1}{4} + 64 - 8 = \frac{1}{4} + 56 = \frac{225}{4}$

For $\int_{-1}^{0}(x^3-x)dx$:
$= \left[\frac{x^4}{4}-\frac{x^2}{2}\right]_{-1}^{0}$
$= \left[\frac{0^4}{4}-\frac{0^2}{2}\right] - \left[\frac{(-1)^4}{4}-\frac{(-1)^2}{2}\right]$
$= 0 - \left[\frac{1}{4}-\frac{1}{2}\right]$
$= 0 - \left[\frac{1}{4}-\frac{2}{4}\right]$
$= 0 - \left[-\frac{1}{4}\right] = \frac{1}{4}$

For $\int_{0}^{1}-(x^3-x)dx = \int_{0}^{1}(-x^3+x)dx$:
$= \left[-\frac{x^4}{4}+\frac{x^2}{2}\right]_{0}^{1}$
$= \left[-\frac{1^4}{4}+\frac{1^2}{2}\right] - \left[-\frac{0^4}{4}+\frac{0^2}{2}\right]$
$= \left[-\frac{1}{4}+\frac{1}{2}\right] - 0$
$= -\frac{1}{4}+\frac{1}{2} = \frac{1}{4}$

For $\int_{1}^{4}(x^3-x)dx$:
$= \left[\frac{x^4}{4}-\frac{x^2}{2}\right]_{1}^{4}$
$= \left[\frac{4^4}{4}-\frac{4^2}{2}\right] - \left[\frac{1^4}{4}-\frac{1^2}{2}\right]$
$= \left[\frac{256}{4}-\frac{16}{2}\right] - \left[\frac{1}{4}-\frac{1}{2}\right]$
$= \left[64-8\right] - \left[\frac{1}{4}-\frac{1}{2}\right]$
$= 56 - \left[\frac{1}{4}-\frac{2}{4}\right]$
$= 56 - \left[-\frac{1}{4}\right] = 56 + \frac{1}{4} = \frac{225}{4}$

## Step 5: Sum the parts
$\int_{-4}^4|x^3-x|dx = \frac{225}{4} + \frac{1}{4} + \frac{1}{4} + \frac{225}{4} = \frac{225 + 1 + 1 + 225}{4} = \frac{452}{4} = 113$

## Numerical approximation
The exact answer is 113, which as a decimal is 113.0000000000

{"answer": "113", "numerical_answer": "113.0000000000"}