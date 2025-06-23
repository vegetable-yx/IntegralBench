Given:  
\[
I = \int_0^\infty x^{2-1} e^{-1.0 x^2} H_2(1.0x) dx
\]
where \( H_2(x) \) is the Hermite polynomial of degree 2.

**Step 1: Expand the Hermite Polynomial**

Recall:
\[
H_2(x) = 4x^2 - 2
\]

So,
\[
H_2(1.0x) = 4(1.0x)^2 - 2 = 4x^2 - 2
\]

**Step 2: Write the Integral in Expanded Form**

\[
I = \int_0^\infty x e^{-x^2} (4x^2 - 2) dx
= 4 \int_0^\infty x^3 e^{-x^2} dx - 2 \int_0^\infty x e^{-x^2} dx
\]

Let us compute these two integrals separately.

---

**Step 3: Evaluate the Sub-Integrals**

Let:
\[
I_1 = \int_0^\infty x^3 e^{-x^2} dx
\]
\[
I_2 = \int_0^\infty x e^{-x^2} dx
\]

Recall:
\[
\int_0^\infty x^{n-1} e^{-a x^p} dx = \frac{1}{p} a^{-n/p} \Gamma\left( \frac{n}{p} \right)
\]

For \(I_1\):
- \(n=4\), \(a=1\), \(p=2\):

\[
I_1 = \frac{1}{2} \cdot 1^{-2} \Gamma\left(\frac{4}{2}\right) = \frac{1}{2} \Gamma(2)
\]
\[
\Gamma(2) = 1!
\]
So,
\[
I_1 = \frac{1}{2} \times 1 = \frac{1}{2}
\]

For \(I_2\):
- \(n=2\), \(a=1\), \(p=2\):

\[
I_2 = \frac{1}{2} \cdot 1^{-1} \Gamma\left(\frac{2}{2}\right) = \frac{1}{2} \Gamma(1)
\]
\[
\Gamma(1) = 1
\]
So,
\[
I_2 = \frac{1}{2}
\]

---

**Step 4: Plug Back Into the Expression**

\[
I = 4 \cdot I_1 - 2 \cdot I_2 = 4 \cdot \frac{1}{2} - 2 \cdot \frac{1}{2} = 2 - 1 = 1
\]

**Step 5: Numerical Approximation**

The result is exactly 1, so to 10 decimal places:
\[
1.0000000000
\]

---

```json
{"answer": "1", "numerical_answer": "1.0000000000"}
```