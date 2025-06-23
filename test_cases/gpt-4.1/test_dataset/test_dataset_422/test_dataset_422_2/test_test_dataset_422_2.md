Let's consider the integral:
\[
I = \int_{-1}^1 x^2 \cdot \sqrt[3]{x^3+1}\, dx
\]

**Step 1: Substitution**

Let’s set:
\[
u = x^3 + 1 \implies du = 3x^2 dx \implies x^2 dx = \frac{du}{3}
\]

When \( x = -1 \), \( u = (-1)^3 + 1 = 0 \).

When \( x = 1 \), \( u = 1^3 + 1 = 2 \).

Change of variable yields:
\[
I = \int_{x=-1}^{x=1} x^2 \cdot (x^3 + 1)^{1/3} dx = \int_{u=0}^{u=2} (u^{1/3}) \cdot \frac{du}{3}
= \frac{1}{3} \int_0^2 u^{1/3} du
\]

**Step 2: Integrate**

\[
\int u^{1/3} du = \frac{u^{4/3}}{4/3} = \frac{3}{4} u^{4/3}
\]

So,
\[
I = \frac{1}{3} \cdot \frac{3}{4} \left[ u^{4/3} \right]_0^2 = \frac{1}{4} \left[ u^{4/3} \right]_0^2
\]
\[
= \frac{1}{4} \left( (2)^{4/3} - (0)^{4/3} \right )
= \frac{1}{4} (2^{4/3} - 0)
= \frac{1}{4} \cdot 2^{4/3}
\]

Thus, the exact answer is:
\[
I = \frac{1}{4} \cdot 2^{4/3}
\]

**Step 3: Numerical Approximation**

Calculate \( 2^{4/3} \):

First, \( 2^{4/3} = (2^{1/3})^4 = (\sqrt[3]{2})^4 \).

Numerically, \( 2^{1/3} \approx 1.26\ 0 0 8 7 1 7 2 2 \).

Thus,
\[
2^{4/3} = (2^{1/3})^4 \approx 1.26 0 08 7 17 22^4 \approx 2.519 842 1
\]
So,
\[
I \approx \frac{1}{4} \times 2.519 842 1 \approx 0.629 960 5
\]

Rounded to 10 decimal places:
\[
I \approx 0.6299605252
\]

**Step 4: Final JSON**

```json
{"answer": "\\frac{1}{4}\\cdot 2^{4/3}", "numerical_answer": "0.6299605252"}
```