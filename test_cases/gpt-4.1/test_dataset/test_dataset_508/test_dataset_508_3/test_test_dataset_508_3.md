Let's proceed step by step.

**Step 1: Analytical computation**

Given:
\[
\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}\,dx
\]

Let’s use substitution.

Let \( u = \sqrt{x} \implies x = u^2, dx = 2u\, du \).
When \( x = 0 \Rightarrow u = 0 \)
When \( x = 441 \Rightarrow u = 21 \)

Substitute:
\[
\frac{\pi \sin(\pi \sqrt{x})}{\sqrt{x}} dx = \frac{\pi \sin(\pi u)}{u} \cdot 2u\, du = 2\pi \sin(\pi u)\, du
\]

So,
\[
\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx = \int_{u=0}^{u=21} 2\pi \sin(\pi u)\, du
\]

Now, integrate:
\[
2\pi \int_{0}^{21} \sin(\pi u)\, du
\]

Integral of \( \sin(\pi u) \) with respect to \( u \) is:
\[
\int \sin(\pi u)\, du = -\frac{1}{\pi}\cos(\pi u) + C
\]

Therefore,
\[
2\pi \int_{0}^{21} \sin(\pi u)\, du = 2\pi \left[-\frac{1}{\pi}\cos(\pi u)\right]_0^{21} = -2 [\cos(\pi u)]_0^{21}
\]
\[
= -2 (\cos(21\pi) - \cos(0))
\]

Recall that \( \cos(0) = 1 \) and \( \cos(21\pi) = \cos(\pi \cdot 21) \).
Since \( \cos(k\pi) = (-1)^k \) for integer \( k \), and 21 is odd:
\[
\cos(21\pi) = \cos(\pi) = -1
\]

So,
\[
-2 [\cos(21\pi) - 1] = -2 [-1 - 1] = -2[-2] = 4
\]

**Step 2: All steps are shown above. The answer is exactly 4.**

**Step 3: Numerical approximation**

The value is exactly \( 4 \), so numerically as well:
\[
4.0000000000
\]

**Step 4: Answer in JSON format**

```json
{"answer": "4", "numerical_answer": "4.0000000000"}
```