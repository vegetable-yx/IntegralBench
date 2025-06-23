# Evaluating $\int_{-1}^1(5x^3-3x)^2\:dx$

## Step 1: Expand the integrand
First, I'll expand $(5x^3-3x)^2$:
$(5x^3-3x)^2 = (5x^3)^2 - 2(5x^3)(3x) + (3x)^2$
$= 25x^6 - 30x^4 + 9x^2$

## Step 2: Integrate each term
Now I'll integrate each term and evaluate from $-1$ to $1$:

$\int_{-1}^1(5x^3-3x)^2\:dx = \int_{-1}^1(25x^6 - 30x^4 + 9x^2)\:dx$

For each term:
- $\int 25x^6\:dx = 25 \cdot \frac{x^7}{7} = \frac{25x^7}{7}$
- $\int -30x^4\:dx = -30 \cdot \frac{x^5}{5} = -\frac{30x^5}{5} = -6x^5$
- $\int 9x^2\:dx = 9 \cdot \frac{x^3}{3} = 3x^3$

Therefore:
$\int_{-1}^1(5x^3-3x)^2\:dx = \left[\frac{25x^7}{7} - 6x^5 + 3x^3\right]_{-1}^1$

## Step 3: Evaluate the antiderivative at the bounds
For $x = 1$:
$\frac{25(1)^7}{7} - 6(1)^5 + 3(1)^3 = \frac{25}{7} - 6 + 3 = \frac{25}{7} - 3 = \frac{25-21}{7} = \frac{4}{7}$

For $x = -1$:
$\frac{25(-1)^7}{7} - 6(-1)^5 + 3(-1)^3 = \frac{-25}{7} - (-6) + (-3) = \frac{-25}{7} + 6 - 3 = \frac{-25}{7} + 3 = \frac{-25+21}{7} = \frac{-4}{7}$

## Step 4: Calculate the final result
$\int_{-1}^1(5x^3-3x)^2\:dx = \frac{4}{7} - \left(\frac{-4}{7}\right) = \frac{4}{7} + \frac{4}{7} = \frac{8}{7}$

## Step 5: Numerical approximation
$\frac{8}{7} = 1.1428571429$ (rounded to 10 decimal places)

{"answer": "\\frac{8}{7}", "numerical_answer": "1.1428571429"}