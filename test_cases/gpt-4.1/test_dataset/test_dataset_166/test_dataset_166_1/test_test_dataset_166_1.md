Let's denote the integral as \( I_n \):

\[
I_n = \int_{0}^{\pi/2} \frac{\sin^{2n} x}{\sin^{2n} x + \cos^{2n} x} \, dx
\]

### Step 1: Symmetry Trick

Let’s consider substituting \( x \to \frac{\pi}{2} - x \):

- \(\sin(\frac{\pi}{2} - x) = \cos x\)
- \(\cos(\frac{\pi}{2} - x) = \sin x\)

So,

\[
I_n = \int_{0}^{\pi/2} \frac{\sin^{2n} x}{\sin^{2n} x + \cos^{2n} x} \, dx
\]
\[
= \int_{0}^{\pi/2} \frac{\cos^{2n} x}{\cos^{2n} x + \sin^{2n} x} \, dx
\]

Let’s add the two expressions:

\[
I_n + I_n = \int_{0}^{\pi/2} \left[ \frac{\sin^{2n} x}{\sin^{2n} x + \cos^{2n} x} + \frac{\cos^{2n} x}{\sin^{2n} x + \cos^{2n} x} \right] dx
\]
\[
= \int_{0}^{\pi/2} 1 \, dx = \frac{\pi}{2}
\]

Therefore,

\[
2 I_n = \frac{\pi}{2}
\implies
I_n = \frac{\pi}{4}
\]

### Step 2: Boxed Answer

So, for all \( n \):

\[
I_n = \frac{\pi}{4}
\]

### Step 3: Numerical Approximation

Since \( \pi/4 = 0.7853981634 \) (rounded to 10 decimal places).

### Step 4: JSON Format

```json
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}
```