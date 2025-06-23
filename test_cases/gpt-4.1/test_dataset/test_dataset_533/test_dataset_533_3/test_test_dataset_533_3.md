Let's solve the integral step by step.

Given:
\[
\int_{-1}^1 (5x^3-3x)^2\,dx
\]

**Step 1: Expand the integrand**
\[
(5x^3 - 3x)^2 = (5x^3)^2 - 2(5x^3)(3x) + (3x)^2 = 25x^6 - 30x^4 + 9x^2
\]

So the integral becomes:
\[
\int_{-1}^1 (25x^6 - 30x^4 + 9x^2)\,dx = 25\int_{-1}^1 x^6\,dx - 30\int_{-1}^1 x^4\,dx + 9\int_{-1}^1 x^2\,dx
\]

**Step 2: Integrate each term**

Since the limits are symmetric and all terms are even powers of \(x\), integrate each:

\[
\int_{-1}^{1} x^n dx = 2\int_0^{1} x^n dx = 2\left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{2}{n+1}
\]

Compute for \(n = 6, 4, 2\):

- \(\int_{-1}^1 x^6 dx = \frac{2}{7}\)
- \(\int_{-1}^1 x^4 dx = \frac{2}{5}\)
- \(\int_{-1}^1 x^2 dx = \frac{2}{3}\)

**Step 3: Plug in the values**

\[
I = 25 \cdot \frac{2}{7} - 30 \cdot \frac{2}{5} + 9 \cdot \frac{2}{3}
\]

\[
I = \frac{50}{7} - \frac{60}{5} + \frac{18}{3}
\]

\[
I = \frac{50}{7} - 12 + 6
\]

\[
I = \frac{50}{7} - 6
\]

\[
I = \frac{50}{7} - \frac{42}{7} = \frac{8}{7}
\]

**Step 4: Numerical approximation**

\[
\frac{8}{7} \approx 1.1428571429
\]

**Final JSON output:**
```json
{"answer": "\\frac{8}{7}", "numerical_answer": "1.1428571429"}
```