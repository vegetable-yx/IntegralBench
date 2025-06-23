Let's compute the integral:

\[
I = \int_{-1}^1 (5x^3 - 3x)^2 \, dx
\]

**Step 1: Expand the integrand**

\[
(5x^3 - 3x)^2 = (5x^3)^2 - 2 \times 5x^3 \times 3x + (3x)^2 = 25x^6 - 30x^4 + 9x^2
\]

So,
\[
I = \int_{-1}^1 \left(25x^6 - 30x^4 + 9x^2\right) dx = 25 \int_{-1}^1 x^6 dx - 30 \int_{-1}^1 x^4 dx + 9 \int_{-1}^1 x^2 dx
\]

**Step 2: Integrate each term**

Since all terms are even powers, the integrals over \([-1, 1]\) are twice their value from \(0\) to \(1\):

\[
\int_{-1}^1 x^n dx = 2\int_0^1 x^n dx = 2 \cdot \frac{1}{n+1}
\]

So:
- \(\int_{-1}^1 x^6 dx = 2 \cdot \frac{1}{7} = \frac{2}{7}\)
- \(\int_{-1}^1 x^4 dx = 2 \cdot \frac{1}{5} = \frac{2}{5}\)
- \(\int_{-1}^1 x^2 dx = 2 \cdot \frac{1}{3} = \frac{2}{3}\)

**Step 3: Combine**

\[
I = 25 \cdot \frac{2}{7} - 30 \cdot \frac{2}{5} + 9 \cdot \frac{2}{3}
\]
\[
= \frac{50}{7} - \frac{60}{5} + \frac{18}{3}
\]
\[
= \frac{50}{7} - 12 + 6
\]
\[
= \frac{50}{7} - 6
\]
\[
= \frac{50}{7} - \frac{42}{7} = \frac{8}{7}
\]

**Step 4: Numerical Approximation**

\[
\frac{8}{7} \approx 1.1428571429
\]

**Final answer:**

```json
{"answer": "\\frac{8}{7}", "numerical_answer": "1.1428571429"}
```