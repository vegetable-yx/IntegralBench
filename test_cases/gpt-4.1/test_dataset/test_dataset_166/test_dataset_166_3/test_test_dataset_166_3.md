Let
\[
I_n = \int_{0}^{\pi/2} \frac{\sin^{2n}x}{\sin^{2n}x + \cos^{2n}x} \, dx
\]

**Step 1: Symmetry Analysis**

Let’s consider the substitution \( x \mapsto \frac{\pi}{2} - x \):

- \(\sin x \mapsto \cos x\)
- \(\cos x \mapsto \sin x\)

Thus,
\[
I_n = \int_{0}^{\pi/2} \frac{\cos^{2n}x}{\cos^{2n}x + \sin^{2n}x} \, dx
\]

Therefore,
\[
I_n + I_n = \int_0^{\pi/2} \left( \frac{\sin^{2n}x}{\sin^{2n}x + \cos^{2n}x} + \frac{\cos^{2n}x}{\cos^{2n}x + \sin^{2n}x} \right) dx = \int_0^{\pi/2} 1 \, dx = \frac{\pi}{2}
\]
So,
\[
2I_n = \frac{\pi}{2} \implies I_n = \frac{\pi}{4}
\]

**Step 2: All necessary steps shown above.**

**Step 3: Numerical Approximation**

\[
\frac{\pi}{4} \approx 0.7853981634
\]

**Step 4: Final JSON output**

```json
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}
```