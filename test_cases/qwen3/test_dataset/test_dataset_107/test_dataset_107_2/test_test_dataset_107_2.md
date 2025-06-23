To evaluate the definite integral

$$
\int_{0}^{2} x^{-1/2}(2 - x)^{-1/2} \arcsin\left( \frac{1}{2} \sqrt{x(2 - x)} \right) \, dx,
$$

we begin by analyzing the structure of the integrand. The presence of both $ x^{-1/2} $ and $ (2 - x)^{-1/2} $ suggests a substitution that simplifies the square root expressions. A natural choice is:

$$
x = 2 \sin^2 \theta, \quad \text{so that} \quad 2 - x = 2 \cos^2 \theta.
$$

Under this substitution:

- $ dx = 4 \sin \theta \cos \theta \, d\theta $,
- $ \sqrt{x} = \sqrt{2} \sin \theta $,
- $ \sqrt{2 - x} = \sqrt{2} \cos \theta $,
- $ \sqrt{x(2 - x)} = 2 \sin \theta \cos \theta = \sin(2\theta) $,
- $ \arcsin\left( \frac{1}{2} \sqrt{x(2 - x)} \right) = \arcsin\left( \frac{1}{2} \sin(2\theta) \right) $.

Substituting into the integral:

$$
\int_0^2 x^{-1/2}(2 - x)^{-1/2} \arcsin\left( \frac{1}{2} \sqrt{x(2 - x)} \right) dx
= \int_0^{\pi/2} \frac{1}{2 \sin \theta \cos \theta} \cdot \arcsin\left( \frac{1}{2} \sin(2\theta) \right) \cdot 4 \sin \theta \cos \theta \, d\theta.
$$

Simplifying the integrand:

$$
\frac{1}{2 \sin \theta \cos \theta} \cdot 4 \sin \theta \cos \theta = 2,
$$

so the integral becomes:

$$
2 \int_0^{\pi/2} \arcsin\left( \frac{1}{2} \sin(2\theta) \right) d\theta.
$$

Now, let’s make the substitution $ \phi = 2\theta $, so $ d\phi = 2 d\theta $, and the limits become $ \phi = 0 $ to $ \phi = \pi $. This gives:

$$
\int_0^{\pi} \arcsin\left( \frac{1}{2} \sin \phi \right) d\phi.
$$

This integral is now in a standard form and can be evaluated using known series expansions or special functions. Specifically, it can be shown that:

$$
\int_0^{\pi} \arcsin\left( \frac{1}{2} \sin \phi \right) d\phi = \sum_{n=0}^{\infty} \frac{1}{4^n (2n + 1)^2}.
$$

This infinite series can be expressed in terms of dilogarithmic functions:

$$
\sum_{n=0}^{\infty} \frac{1}{4^n (2n + 1)^2} = \text{Li}_2\left(\frac{1}{2}\right) - \text{Li}_2\left(-\frac{1}{2}\right),
$$

where $ \text{Li}_2(z) $ is the dilogarithm (Spence's function).

---

### Final Answer

$$
\boxed{
\left\{
  "answer": "\\text{Li}_2\\left(\\frac{1}{2}\\right) - \\text{Li}_2\\left(-\\frac{1}{2}\\right)",
  "numerical_answer": "1.0306571407"
\right\}
}
$$