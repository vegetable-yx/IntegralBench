

To calculate the definite integral \(\int_{-1}^1 (5x^3 - 3x)^2 \, dx\), follow these steps:

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
Integrate each term separately using the power rule \(\int x^n \, dx = \frac{x^{n+1}}{n+1}\):
- For \(25x^6\): \(\int 25x^6 \, dx = 25 \cdot \frac{x^7}{7} = \frac{25}{7}x^7\)
- For \(-30x^4\): \(\int -30x^4 \, dx = -30 \cdot \frac{x^5}{5} = -6x^5\)
- For \(9x^2\): \(\int 9x^2 \, dx = 9 \cdot \frac{x^3}{3} = 3x^3\)

Combining these, the antiderivative is:
\[
F(x) = \frac{25}{7}x^7 - 6x^5 + 3x^3
\]

### Step 3: Evaluate the definite integral
Evaluate \(F(x)\) at the bounds \(x = 1\) and \(x = -1\), then subtract:
- At \(x = 1\): \(F(1) = \frac{25}{7}(1)^7 - 6(1)^5 + 3(1)^3 = \frac{25}{7} - 6 + 3 = \frac{25}{7} - 3 = \frac{25 - 21}{7} = \frac{4}{7}\)
- At \(x = -1\): \(F(-1) = \frac{25}{7}(-1)^7 - 6(-1)^5 + 3(-1)^3 = -\frac{25}{7} + 6 - 3 = -\frac{25}{7} + 3 = -\frac{25 - 21}{7} = -\frac{4}{7}\)

Thus, the definite integral is:
\[
F(1) - F(-1) = \frac{4}{7} - \left(-\frac{4}{7}\right) = \frac{8}{7}
\]

### Step 4: Numerical approximation
The exact value is \(\frac{8}{7}\). Numerically, this is approximately \(1.1428571429\) (rounded to 10 decimal places).

{"answer": "\(\frac{8}{7}\)", "numerical_answer": "1.1428571429"}