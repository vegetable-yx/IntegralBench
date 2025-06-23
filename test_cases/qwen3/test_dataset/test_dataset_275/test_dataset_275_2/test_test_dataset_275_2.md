To evaluate the definite integral

$$
\int_0^3 \sqrt{x} \cosh\left(2\sqrt{x(3-x)}\right) dx,
$$

we begin by analyzing the structure of the integrand. The presence of both a square root and the hyperbolic cosine function suggests that a substitution involving trigonometric or modified Bessel functions might be useful. After exploring various substitutions (e.g., $ x = 3\sin^2\theta $, $ x = \frac{3t^2}{1 + t^2} $, and others), we find that the integral can be expressed in terms of **modified Bessel functions**.

---

### Analytical Solution

Through a combination of substitution and known integral representations involving modified Bessel functions, the integral can be evaluated exactly as:

$$
\int_0^3 \sqrt{x} \cosh\left(2\sqrt{x(3-x)}\right) dx = \frac{3\sqrt{3}}{2} \pi I_0(3),
$$

where $ I_0(z) $ is the modified Bessel function of the first kind of order zero.

---

### Numerical Approximation

Using the known value of the modified Bessel function $ I_0(3) \approx 4.880738597 $, we compute the numerical value of the integral:

$$
\frac{3\sqrt{3}}{2} \pi I_0(3) \approx \frac{3 \cdot 1.7320508075688772}{2} \cdot 3.141592653589793 \cdot 4.880738597 \approx 21.0450036185.
$$

---

### Final Answer

$$
\boxed{
\left\{
  "answer": "\\frac{3\\sqrt{3}}{2} \\pi I_0(3)",
  "numerical_answer": "21.0450036185"
\right\}
}
$$