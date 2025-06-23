Let's compute the integral:
\[
I = \int_0^\infty e^{-x^2}\cos(2x)\ dx
\]

**Step 1. Express the cosine as the real part of a complex exponential:**

\[
I = \Re\left( \int_0^\infty e^{-x^2} e^{i2x} dx \right ) 
   = \Re\left( \int_0^\infty e^{-(x^2 - i2x)} dx \right )
\]

Rewrite:
\[
x^2 - i2x = (x - i)^2 - 1
\]
So:
\[
e^{-(x^2 - i2x)} = e^{-[(x - i)^2 - 1]} = e^{1} e^{-(x - i)^2}
\]

Therefore,
\[
I = \Re\left( e^1 \int_0^\infty e^{-(x - i)^2} dx \right )
\]

**Step 2. Express the Gaussian integral over a shifted contour:**

Make the substitution \(u = x - i\), \(x = u + i\), \(dx = du\):

- When \(x = 0\): \(u = -i\)
- When \(x = \infty\): \(u = \infty - i\), but since the function decays rapidly, we can integrate up to infinity for \(u\).

So,
\[
\int_0^\infty e^{-(x - i)^2} dx = \int_{-i}^{\infty - i} e^{-u^2} du
\]

But it's easier to relate this to the standard result:
\[
\int_0^\infty e^{-a x^2} \cos(b x)\ dx = \frac{1}{2}\sqrt{\frac{\pi}{a}}\, e^{-\frac{b^2}{4a}}, \qquad \Re(a) > 0
\]
Set \(a = 1\), \(b = 2\):
\[
I = \frac{1}{2}\sqrt{\pi} e^{-\frac{(2)^2}{4}} = \frac{1}{2}\sqrt{\pi} e^{-1}
\]

**Step 3. Numerical approximation:**

\[
I = \frac{1}{2}\sqrt{\pi} e^{-1}
\]

Compute:

- \(\sqrt{\pi} \approx 1.7724538509\)
- \(e^{-1} \approx 0.3678794412\)
- \(\frac{1}{2} \times 1.7724538509 \times 0.3678794412 \approx 0.3264827485\)

---

{"answer": "\\frac{1}{2}\\sqrt{\\pi}\\, e^{-1}", "numerical_answer": "0.3264827485"}