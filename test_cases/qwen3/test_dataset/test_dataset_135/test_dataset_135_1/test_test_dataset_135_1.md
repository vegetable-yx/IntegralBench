To evaluate the definite integral

$$
\int_{0}^{2} x^{-1/2} (2 - x)^{-1/2} \left[1 - \frac{1}{2}x(2 - x)\right] \, dx,
$$

we begin by simplifying the integrand. The term in the brackets simplifies as follows:

$$
1 - \frac{1}{2}x(2 - x) = 1 - x + \frac{1}{2}x^2.
$$

So the integral becomes:

$$
\int_{0}^{2} \frac{x^{-1/2} (2 - x)^{-1/2} (x^2 - 2x + 2)}{2} \, dx.
$$

This can be split into three separate integrals:

$$
\frac{1}{2} \int_0^2 x^{-1/2}(2 - x)^{-1/2} x^2 \, dx - \int_0^2 x^{-1/2}(2 - x)^{-1/2} x \, dx + \int_0^2 x^{-1/2}(2 - x)^{-1/2} \, dx.
$$

Each of these integrals is of the form:

$$
\int_0^2 x^{a}(2 - x)^{b} \, dx,
$$

which can be transformed into a Beta function using the substitution $ x = 2t $, $ dx = 2dt $, $ 2 - x = 2(1 - t) $. This leads to:

$$
\int_0^2 x^{a}(2 - x)^{b} \, dx = 2^{a + b + 1} \int_0^1 t^{a}(1 - t)^{b} \, dt = 2^{a + b + 1} B(a + 1, b + 1).
$$

Applying this transformation to each integral:

---

**First Integral:**

$$
\frac{1}{2} \int_0^2 x^{3/2}(2 - x)^{-1/2} \, dx = \frac{1}{2} \cdot 2^{3/2 - 1/2 + 1} B\left(\frac{5}{2}, \frac{1}{2}\right) = \frac{1}{2} \cdot 2^{2} B\left(\frac{5}{2}, \frac{1}{2}\right) = 2 B\left(\frac{5}{2}, \frac{1}{2}\right).
$$

Using the identity $ B(p, q) = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)} $, we compute:

$$
B\left(\frac{5}{2}, \frac{1}{2}\right) = \frac{\Gamma\left(\frac{5}{2}\right)\Gamma\left(\frac{1}{2}\right)}{\Gamma(3)} = \frac{\frac{3}{4} \sqrt{\pi} \cdot \sqrt{\pi}}{2} = \frac{3\pi}{8}.
$$

So the first integral evaluates to:

$$
2 \cdot \frac{3\pi}{8} = \frac{3\pi}{4}.
$$

---

**Second Integral:**

$$
\int_0^2 x^{1/2}(2 - x)^{-1/2} \, dx = 2^{1/2 - 1/2 + 1} B\left(\frac{3}{2}, \frac{1}{2}\right) = 2 B\left(\frac{3}{2}, \frac{1}{2}\right).
$$

$$
B\left(\frac{3}{2}, \frac{1}{2}\right) = \frac{\Gamma\left(\frac{3}{2}\right)\Gamma\left(\frac{1}{2}\right)}{\Gamma(2)} = \frac{\frac{1}{2} \sqrt{\pi} \cdot \sqrt{\pi}}{1} = \frac{\pi}{2}.
$$

So the second integral evaluates to:

$$
2 \cdot \frac{\pi}{2} = \pi.
$$

---

**Third Integral:**

$$
\int_0^2 x^{-1/2}(2 - x)^{-1/2} \, dx = 2^{-1/2 - 1/2 + 1} B\left(\frac{1}{2}, \frac{1}{2}\right)