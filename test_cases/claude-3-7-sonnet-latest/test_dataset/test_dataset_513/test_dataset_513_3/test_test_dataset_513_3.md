# Calculating $\int_{-4}^4|x^3-x|dx$

To evaluate this definite integral, I need to determine where $x^3-x$ changes sign, as this affects the absolute value.

## Step 1: Find where $x^3-x = 0$
$x^3-x = x(x^2-1) = x(x-1)(x+1) = 0$

This gives us $x = 0$, $x = 1$, and $x = -1$ as critical points.

## Step 2: Determine the sign of $x^3-x$ in each interval
- For $x < -1$: $x^3-x < 0$ (negative)
- For $-1 < x < 0$: $x^3-x > 0$ (positive)
- For $0 < x < 1$: $x^3-x < 0$ (negative)
- For $x > 1$: $x^3-x > 0$ (positive)

## Step 3: Split the integral according to these intervals
$\int_{-4}^4|x^3-x|dx = \int_{-4}^{-1}-(x^3-x)dx + \int_{-1}^{0}(x^3-x)dx + \int_{0}^{1}-(x^3-x)dx + \int_{1}^{4}(x^3-x)dx$

$= \int_{-4}^{-1}(-x^3+x)dx + \int_{-1}^{0}(x^3-x)dx + \int_{0}^{1}(-x^3+x)dx + \int_{1}^{4}(x^3-x)dx$

## Step 4: Evaluate each integral

For $\int_{-4}^{-1}(-x^3+x)dx$:
$\int(-x^3+x)dx = -\frac{x^4}{4}+\frac{x^2}{2}$
$\left[-\frac{x^4}{4}+\frac{x^2}{2}\right]_{-4}^{-1} = \left(-\frac{1}{4}+\frac{1}{2}\right) - \left(-\frac{256}{4}+\frac{16}{2}\right) = \frac{1}{4} - (-64+8) = \frac{1}{4} + 56 = \frac{225}{4}$

For $\int_{-1}^{0}(x^3-x)dx$:
$\int(x^3-x)dx = \frac{x^4}{4}-\frac{x^2}{2}$
$\left[\frac{x^4}{4}-\frac{x^2}{2}\right]_{-1}^{0} = (0-0) - \left(\frac{1}{4}-\frac{1}{2}\right) = 0 - (-\frac{1}{4}) = \frac{1}{4}$

For $\int_{0}^{1}(-x^3+x)dx$:
$\int(-x^3+x)dx = -\frac{x^4}{4}+\frac{x^2}{2}$
$\left[-\frac{x^4}{4}+\frac{x^2}{2}\right]_{0}^{1} = \left(-\frac{1}{4}+\frac{1}{2}\right) - (0-0) = \frac{1}{4}$

For $\int_{1}^{4}(x^3-x)dx$:
$\int(x^3-x)dx = \frac{x^4}{4}-\frac{x^2}{2}$
$\left[\frac{x^4}{4}-\frac{x^2}{2}\right]_{1}^{4} = \left(\frac{256}{4}-\frac{16}{2}\right) - \left(\frac{1}{4}-\frac{1}{2}\right) = (64-8) - (\frac{1}{4}-\frac{1}{2}) = 56 - (-\frac{1}{4}) = 56 + \frac{1}{4} = \frac{225}{4}$

## Step 5: Sum all parts
$\int_{-4}^4|x^3-x|dx = \frac{225}{4} + \frac{1}{4} + \frac{1}{4} + \frac{225}{4} = \frac{225}{4} + \frac{2}{4} + \frac{225}{4} = \frac{450}{4} + \frac{2}{4} = \frac{452}{4} = 113$

## Step 6: Numerical approximation
The numerical value is exactly 113, so rounded to 10 decimal places: 113.0000000000

{"answer": "113", "numerical_answer": "113.0000000000"}