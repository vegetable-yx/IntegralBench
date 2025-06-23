To compute the definite integral \(\int_{-1}^1 (5x^3 - 3x)^2 \, dx\), we will follow these steps:

### Step 1: Expand the Integrand
First, expand \((5x^3 - 3x)^2\):
\[
(5x^3 - 3x)^2 = (5x^3)^2 - 2 \cdot 5x^3 \cdot 3x + (3x)^2 = 25x^6 - 30x^4 + 9x^2
\]

### Step 2: Integrate Term by Term
Now, integrate the expanded form term by term:
\[
\int_{-1}^1 (25x^6 - 30x^4 + 9x^2) \, dx = 25 \int_{-1}^1 x^6 \, dx - 30 \int_{-1}^1 x^4 \, dx + 9 \int_{-1}^1 x^2 \, dx
\]

Compute each integral separately:
\[
\int_{-1}^1 x^6 \, dx = \left[ \frac{x^7}{7} \right]_{-1}^1 = \frac{1^7}{7} - \frac{(-1)^7}{7} = \frac{1}{7} + \frac{1}{7} = \frac{2}{7}
\]
\[
\int_{-1}^1 x^4 \, dx = \left[ \frac{x^5}{5} \right]_{-1}^1 = \frac{1^5}{5} - \frac{(-1)^5}{5} = \frac{1}{5} + \frac{1}{5} = \frac{2}{5}
\]
\[
\int_{-1}^1 x^2 \, dx = \left[ \frac{x^3}{3} \right]_{-1}^1 = \frac{1^3}{3} - \frac{(-1)^3}{3} = \frac{1}{3} + \frac{1}{3} = \frac{2}{3}
\]

Substitute these results back into the expression:
\[
25 \cdot \frac{2}{7} - 30 \cdot \frac{2}{5} + 9 \cdot \frac{2}{3} = \frac{50}{7} - \frac{60}{5} + \frac{18}{3}
\]
Simplify each term:
\[
\frac{50}{7} - 12 + 6 = \frac{50}{7} - 6
\]
Convert \(-6\) to a fraction with denominator 7:
\[
\frac{50}{7} - \frac{42}{7} = \frac{8}{7}
\]

### Step 3: Numerical Approximation
The exact answer is \(\frac{8}{7}\). Numerically, this is approximately:
\[
\frac{8}{7} \approx 1.1428571429
\]

### Final Answer
```json
{"answer": "\\frac{8}{7}", "numerical_answer": "1.1428571429"}
```