# Evaluating $\int_{-4}^4|x^3-x|dx$

## Step 1: Find where $x^3-x = 0$
To handle the absolute value, I need to determine where $x^3-x$ changes sign.

$x^3-x = 0$
$x(x^2-1) = 0$
$x(x-1)(x+1) = 0$

So $x^3-x = 0$ when $x = 0$, $x = 1$, or $x = -1$.

## Step 2: Determine the sign of $x^3-x$ in different intervals
- When $x < -1$: $x^3-x < 0$ (negative)
- When $-1 < x < 0$: $x^3-x > 0$ (positive)
- When $0 < x < 1$: $x^3-x < 0$ (negative)
- When $x > 1$: $x^3-x > 0$ (positive)

## Step 3: Break the integral into parts
$$\int_{-4}^4|x^3-x|dx = \int_{-4}^{-1}-(x^3-x)dx + \int_{-1}^{0}(x^3-x)dx + \int_{0}^{1}-(x^3-x)dx + \int_{1}^{4}(x^3-x)dx$$

Simplifying the negatives:
$$\int_{-4}^4|x^3-x|dx = \int_{-4}^{-1}(x-x^3)dx + \int_{-1}^{0}(x^3-x)dx + \int_{0}^{1}(x-x^3)dx + \int_{1}^{4}(x^3-x)dx$$

## Step 4: Evaluate each integral

### First integral: $\int_{-4}^{-1}(x-x^3)dx$
$$\int(x-x^3)dx = \frac{x^2}{2} - \frac{x^4}{4} + C$$

Evaluating at the bounds:
$$\left[\frac{x^2}{2} - \frac{x^4}{4}\right]_{-4}^{-1} = \left(\frac{1}{2} - \frac{1}{4}\right) - \left(\frac{16}{2} - \frac{256}{4}\right) = \frac{1}{4} - (8 - 64) = \frac{1}{4} + 56 = \frac{225}{4}$$

### Second integral: $\int_{-1}^{0}(x^3-x)dx$
$$\int(x^3-x)dx = \frac{x^4}{4} - \frac{x^2}{2} + C$$

Evaluating at the bounds:
$$\left[\frac{x^4}{4} - \frac{x^2}{2}\right]_{-1}^{0} = (0 - 0) - \left(\frac{1}{4} - \frac{1}{2}\right) = 0 - \left(\frac{1}{4} - \frac{1}{2}\right) = \frac{1}{4}$$

### Third integral: $\int_{0}^{1}(x-x^3)dx$
$$\int(x-x^3)dx = \frac{x^2}{2} - \frac{x^4}{4} + C$$

Evaluating at the bounds:
$$\left[\frac{x^2}{2} - \frac{x^4}{4}\right]_{0}^{1} = \left(\frac{1}{2} - \frac{1}{4}\right) - (0 - 0) = \frac{1}{4}$$

### Fourth integral: $\int_{1}^{4}(x^3-x)dx$
$$\int(x^3-x)dx = \frac{x^4}{4} - \frac{x^2}{2} + C$$

Evaluating at the bounds:
$$\left[\frac{x^4}{4} - \frac{x^2}{2}\right]_{1}^{4} = \left(\frac{256}{4} - \frac{16}{2}\right) - \left(\frac{1}{4} - \frac{1}{2}\right) = (64 - 8) - \left(\frac{1}{4} - \frac{1}{2}\right) = 56 + \frac{1}{4} = \frac{225}{4}$$

## Step 5: Calculate the total integral
$$\int_{-4}^4|x^3-x|dx = \frac{225}{4} + \frac{1}{4} + \frac{1}{4} + \frac{225}{4} = \frac{225 + 1 + 1 + 225}{4} = \frac{452}{4} = 113$$

## Step 6: Numerical approximation
The exact value is 113, which is already an integer. In decimal form:
113.0000000000

{"answer": "113", "numerical_answer": "113.0000000000"}