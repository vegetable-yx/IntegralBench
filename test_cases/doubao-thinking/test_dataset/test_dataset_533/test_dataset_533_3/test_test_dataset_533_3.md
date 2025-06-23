

To calculate the definite integral \(\int_{-1}^1 (5x^3 - 3x)^2 \, dx\), we follow these steps:

### Step 1: Expand the integrand
First, expand \((5x^3 - 3x)^2\) using the formula \((a - b)^2 = a^2 - 2ab + b^2\):
\[
(5x^3 - 3x)^2 = (5x^3)^2 - 2(5x^3)(3x) + (3x)^2 = 25x^6 - 30x^4 + 9x^2
\]

### Step 2: Integrate term by term
The integral becomes:
\[
\int_{-1}^1 (25x^6 - 30x^4 + 9x^2) \, dx
\]
We integrate each term separately:
- For \(25x^6\): The antiderivative is \(\frac{25}{7}x^7\).
- For \(-30x^4\): The antiderivative is \(-6x^5\) (since \(\int x^4 \, dx = \frac{x^5}{5}\), so \(-30 \cdot \frac{x^5}{5} = -6x^5\)).
- For \(9x^2\): The antiderivative is \(3x^3\) (since \(\int x^2 \, dx = \frac{x^3}{3}\), so \(9 \cdot \frac{x^3}{3} = 3x^3\)).

### Step 3: Evaluate the antiderivatives over \([-1, 1]\)
Evaluate each term at the bounds \(x = 1\) and \(x = -1\):
1. For \(\frac{25}{7}x^7\):
\[
\left. \frac{25}{7}x^7 \right|_{-1}^1 = \frac{25}{7}(1^7 - (-1)^7) = \frac{25}{7}(1 - (-1)) = \frac{50}{7}
\]
2. For \(-6x^5\):
\[
\left. -6x^5 \right|_{-1}^1 = -6(1^5 - (-1)^5) = -6(1 - (-1)) = -12
\]
3. For \(3x^3\):
\[
\left. 3x^3 \right|_{-1}^1 = 3(1^3 - (-1)^3) = 3(1 - (-1)) = 6
\]

### Step 4: Combine the results
Add the evaluated terms:
\[
\frac{50}{7} - 12 + 6 = \frac{50}{7} - 6 = \frac{50}{7} - \frac{42}{7} = \frac{8}{7}
\]

### Numerical Approximation
The exact value is \(\frac{8}{7}\). Numerically, \(\frac{8}{7} \approx 1.142857142857\ldots\), which rounds to \(1.1428571429\) when rounded to 10 decimal places.

{"answer": "\(\frac{8}{7}\)", "numerical_answer": "1.1428571429"}