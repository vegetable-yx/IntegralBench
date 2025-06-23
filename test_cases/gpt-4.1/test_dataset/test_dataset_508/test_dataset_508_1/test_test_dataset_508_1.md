Let's compute the integral:
\[
I = \int_0^{441} \frac{\pi \sin(\pi \sqrt{x})}{\sqrt{x}} \, dx
\]

**Step 1: Substitution**

Let \( u = \sqrt{x} \Rightarrow x = u^2 \Rightarrow dx = 2u\, du \).

When \( x = 0 \), \( u = 0 \);  
When \( x = 441 \), \( u = 21 \).

Substitute into the integral:

\[
I = \int_{x=0}^{x=441} \frac{\pi \sin(\pi \sqrt{x})}{\sqrt{x}} \, dx
= \int_{u=0}^{u=21} \frac{\pi \sin(\pi u)}{u} \cdot 2u du
\]

The \( u \) in the numerator and denominator cancel:

\[
I = 2\pi \int_0^{21} \sin(\pi u) du
\]

**Step 2: Integrate**

The integral of \( \sin(\pi u) \) is:

\[
\int \sin(\pi u) du = -\frac{1}{\pi} \cos(\pi u)
\]

So,

\[
I = 2\pi \left[ -\frac{1}{\pi} \cos(\pi u) \right]_{u=0}^{u=21}
= -2 [\cos(\pi u)]_{u=0}^{u=21}
= -2 [\cos(21\pi) - \cos(0)]
\]

Recall that \(\cos(n\pi) = (-1)^n\), so:

\[
\cos(21\pi) = (-1)^{21} = -1 \\
\cos(0) = 1
\]

So,

\[
I = -2 [ -1 - 1 ]
= -2 [ -2 ]
= 4
\]

**Step 3: Numerical approximation**

The value is exactly 4.0.

**Step 4: Final JSON**

```json
{"answer": "4", "numerical_answer": "4.0000000000"}
```