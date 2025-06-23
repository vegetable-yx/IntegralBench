Let's solve the integral:
\[
I = \int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx
\]

**Step 1: Substitution**

Let’s try the substitution \( u = \sin(x) \), so \( du = \cos(x)\,dx \). When \( x = 0 \), \( u = 0 \); when \( x = \frac{\pi}{2} \), \( u = 1 \).

\( \cos^2(x) = 1 - u^2 \), so \( 2 - \cos^2(x) = 2 - (1 - u^2) = 1 + u^2 \).

Thus,
\[
I = \int_{u=0}^{u=1} \frac{1}{1+u^2} du
\]

**Step 2: Antiderivative**

The antiderivative is:
\[
\int \frac{1}{1+u^2} du = \arctan(u)
\]

So,
\[
I = \arctan(u) \Big|_{0}^{1} = \arctan(1) - \arctan(0)
\]
We know \(\arctan(1) = \frac{\pi}{4}\), \(\arctan(0) = 0\).

Thus,
\[
I = \frac{\pi}{4}
\]

**Step 3: Numerical Evaluation**

\[
\frac{\pi}{4} \approx 0.7853981634
\]

**Step 4: JSON output**
```json
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}
```