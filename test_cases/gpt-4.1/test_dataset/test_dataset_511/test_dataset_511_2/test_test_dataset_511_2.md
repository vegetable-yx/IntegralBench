Let's compute the given integral step-by-step:

\[
\int_0^8 \frac{\cos\sqrt{x}}{\sqrt{x}}\, dx
\]

**Step 1: Substitution**

Let \( u = \sqrt{x} \implies x = u^2, \, dx = 2u \, du \).

When \( x = 0 \), \( u = 0 \), and when \( x = 8 \), \( u = \sqrt{8} = 2\sqrt{2} \).

\[
\int_0^8 \frac{\cos\sqrt{x}}{\sqrt{x}}\, dx = \int_{u=0}^{u=2\sqrt{2}} \frac{\cos u}{u} \cdot 2u\, du = \int_0^{2\sqrt{2}} 2\cos u\, du
\]

**Step 2: Integrate**

\[
\int_0^{2\sqrt{2}} 2\cos u\, du = 2 \left[ \sin u \right]_0^{2\sqrt{2}} = 2\left(\sin(2\sqrt{2}) - \sin 0 \right)
\]

Since \(\sin 0 = 0\), the answer is:

\[
2\sin(2\sqrt{2})
\]

**Step 3: Numerical Approximation**

First, compute \( 2\sqrt{2} \):

\[
2\sqrt{2} \approx 2 \times 1.4142135624 = 2.8284271248
\]

Then, compute \( \sin(2.8284271248) \):

\[
\sin(2.8284271248) \approx 0.3095598757
\]

So,

\[
2 \times 0.3095598757 = 0.6191197514
\]

**Step 4: Format the Answer**

```json
{"answer": "2\\sin\\left(2\\sqrt{2}\\right)", "numerical_answer": "0.6191197514"}
```