

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
We integrate each term separately over \([-1, 1]\). Since \(x^6\), \(x^4\), and \(x^2\) are even functions (symmetric about the y-axis), we use the property \(\int_{-a}^a f(x) \, dx = 2\int_0^a f(x) \, dx\) for even \(f(x)\).

#### Integral of \(25x^6\):
\[
25 \int_{-1}^1 x^6 \, dx = 25 \cdot 2 \int_0^1 x^6 \, dx = 50 \left[ \frac{x^7}{7} \right]_0^1 = 50 \cdot \frac{1}{7} = \frac{50}{7}
\]

#### Integral of \(-30x^4\):
\[
-30 \int_{-1}^1 x^4 \, dx = -30 \cdot 2 \int_0^1 x^4 \, dx = -60 \left[ \frac{x^5}{5} \right]_0^1 = -60 \cdot \frac{1}{5} = -12
\]

#### Integral of \(9x^2\):
\[
9 \int_{-1}^1 x^2 \, dx = 9 \cdot 2 \int_0^1 x^2 \, dx = 18 \left[ \frac{x^3}{3} \right]_0^1 = 18 \cdot \frac{1}{3} = 6
\]

### Step 3: Combine the results
Adding the three integrals together:
\[
\frac{50}{7} - 12 + 6 = \frac{50}{7} - 6 = \frac{50 - 42}{7} = \frac{8}{7}
\]

### Step 4: Numerical approximation
The exact value is \(\frac{8}{7}\). Numerically, \(\frac{8}{7} \approx 1.1428571429\) (rounded to 10 decimal places).

{"answer": "\(\frac{8}{7}\)", "numerical_answer": "1.1428571429"}