To evaluate the definite integral

$$
\int_0^2 x^{-3/4} (2 - x)^{-1/4} I_1\left(1.0 \cdot \sqrt[4]{x(2 - x)}\right) dx,
$$

we proceed through a series of analytical transformations and simplifications.

---

### **Step 1: Substitution to Normalize the Interval**

Let us perform the substitution $ x = 2y $, so that $ dx = 2dy $, and the limits $ x = 0 \to y = 0 $, $ x = 2 \to y = 1 $. The integrand becomes:

$$
\int_0^1 (2y)^{-3/4} (2 - 2y)^{-1/4} I_1\left(1.0 \cdot \sqrt[4]{2y(2 - 2y)}\right) \cdot 2 \, dy.
$$

Simplifying the powers:

$$
(2y)^{-3/4} (2(1 - y))^{-1/4} \cdot 2 = 2^{-3/4 - 1/4 + 1} y^{-3/4} (1 - y)^{-1/4} = y^{-3/4} (1 - y)^{-1/4}.
$$

The argument of the Bessel function becomes:

$$
\sqrt[4]{2y(2 - 2y)} = \sqrt[4]{4y(1 - y)} = \sqrt{2} \cdot \sqrt[4]{y(1 - y)}.
$$

So the integral simplifies to:

$$
\int_0^1 y^{-3/4} (1 - y)^{-1/4} I_1\left(\sqrt{2} \cdot \sqrt[4]{y(1 - y)}\right) dy.
$$

---

### **Step 2: Series Expansion of the Bessel Function**

We expand the modified Bessel function $ I_1(z) $ in its power series:

$$
I_1(z) = \sum_{k=0}^\infty \frac{(z/2)^{2k+1}}{k! (k+1)!}.
$$

Substitute $ z = \sqrt{2} \cdot \sqrt[4]{y(1 - y)} $, so $ z^2 = 2 \sqrt{y(1 - y)} $, and $ z^2/4 = \frac{\sqrt{y(1 - y)}}{2} $.

Thus:

$$
I_1\left(\sqrt{2} \cdot \sqrt[4]{y(1 - y)}\right) = \sum_{k=0}^\infty \frac{(z/2)^{2k+1}}{k! (k+1)!} = \sum_{k=0}^\infty \frac{2^{-(2k+1)} (\sqrt{2})^{2k+1} \cdot (y(1 - y))^{(2k+1)/4}}{k! (k+1)!}.
$$

Simplify the constants:

$$
2^{-(2k+1)} \cdot 2^{(2k+1)/2} = 2^{-(2k+1)/2}.
$$

So the series becomes:

$$
\sum_{k=0}^\infty \frac{2^{-(2k+1)/2} \cdot (y(1 - y))^{(2k+1)/4}}{k! (k+1)!}.
$$

Now, the integrand becomes:

$$
\int_0^1 y^{-3/4} (1 - y)^{-1/4} \sum_{k=0}^\infty \frac{2^{-(2k+1)/2} \cdot (y(1 - y))^{(2k+1)/4}}{k! (k+1)!} dy.
$$

Interchange the sum and integral (justified under uniform convergence):

$$
\sum_{k=0}^\infty \frac{2^{-(2k+1)/2}}{k! (k+1)!} \int_0^1 y^{-3/4 + (2k+1)/4} (1 - y)^{-1/4 + (2k+1)/4} dy.
$$

Simplify the exponents:

$$
\int_0^1 y^{(2k - 2)/4} (1 - y)^{(2k)/4} dy = \int_0