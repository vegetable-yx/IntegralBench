Let's solve the definite integral:
\[
I = \int_{-1}^{1} x^2 \cdot \sqrt[3]{x^3 + 1}\; dx
\]

**Step 1: Substitution**

Let’s use the substitution \( u = x^3 + 1 \).
- When \( x = -1 \), \( u = (-1)^3 + 1 = 0 \).
- When \( x = 1 \), \( u = 1^3 + 1 = 2 \).
- \( du = 3x^2 dx \implies x^2 dx = \frac{du}{3} \).

Thus:
\[
I = \int_{x=-1}^{x=1} x^2 (x^3 + 1)^{1/3} dx = \int_{u=0}^{u=2} u^{1/3} \cdot \frac{du}{3}
= \frac{1}{3} \int_{0}^{2} u^{1/3} du
\]

**Step 2: Integrate**

\[
\int u^{1/3} du = \frac{u^{4/3}}{4/3} = \frac{3}{4} u^{4/3}
\]

Thus:
\[
I = \frac{1}{3} \cdot \left. \frac{3}{4} u^{4/3} \right|_{0}^{2}
= \frac{1}{4} [u^{4/3}]_{0}^{2}
= \frac{1}{4} [2^{4/3} - 0^{4/3}]
= \frac{1}{4} \cdot 2^{4/3}
\]

**Step 3: Exact Answer**

\[
I = \frac{1}{4} \cdot 2^{4/3}
\]

Alternatively, since \( 2^{4/3} = (2^{1/3})^4 \), but the above is already simplest.

**Step 4: Numerical Approximation**

Calculate \( 2^{4/3} \):
- \( 2^{1/3} \approx 1.26\, \)
- \( 2^{4/3} \approx (2^{1/3})^4 \approx 1.26^4 \approx 2.5198 \)
But to be precise:
- \( 2^{4/3} = (2^{1.333333...}) \approx e^{(1.333333...) \cdot \ln 2} \approx e^{0.924} \approx 2.5198 \)
So,
\[
I \approx \frac{1}{4} \times 2.519815204435
= 0.6299538011
\]

**Step 5: Format**

```json
{"answer": "\\frac{1}{4} \\cdot 2^{4/3}", "numerical_answer": "0.6299538011"}
```