
To solve the definite integral \(\int\limits_0^{2} x^{1/2}(2 - x)^{1/2} \cos\left(\sqrt{x(2 - x)}\right) dx\), we proceed as follows:

### Step 1: Simplify the Integrand and Substitute
First, note that \(x(2 - x) = 1 - (x - 1)^2\) by completing the square. Let \(u = x - 1\), so \(x = u + 1\) and \(dx = du\). The limits of integration change from \(x = 0\) to \(u = -1\) and \(x = 2\) to \(u = 1\). The integrand becomes:
\[
\sqrt{(u + 1)(1 - u)} \cos\left(\sqrt{(u + 1)(1 - u)}\right) = \sqrt{1 - u^2} \cos\left(\sqrt{1 - u^2}\right)
\]
Thus, the integral simplifies to:
\[
\int_{-1}^{1} \sqrt{1 - u^2} \cos\left(\sqrt{1 - u^2}\right) du
\]
By symmetry, this is \(2 \int_0^1 \sqrt{1 - u^2} \cos\left(\sqrt{1 - u^2}\right) du\).

### Step 2: Trigonometric Substitution
Let \(u = \sin\theta\), so \(du = \cos\theta d\theta\) and \(\sqrt{1 - u^2} = \cos\theta\). When \(u = 0\), \(\theta = 0\); when \(u = 1\), \(\theta = \pi/2\). The integral becomes:
\[
2 \int_0^{\pi/2} \cos\theta \cos(\cos\theta) \cdot \cos\theta d\theta = 2 \int_0^{\pi/2} \cos^2\theta \cos(\cos\theta) d\theta
\]

### Step 3: Use Bessel Function Identities
Using the identity \(\cos^2\theta = \frac{1 + \cos 2\theta}{2}\), we split the integral:
\[
\int_0^{\pi} \sin^2\theta \cos(\sin\theta) d\theta = \frac{1}{2} \int_0^{\pi} \cos(\sin\theta) d\theta - \frac{1}{2} \int_0^{\pi} \cos 2\theta \cos(\sin\theta) d\theta
\]
Using Bessel function integrals:
- \(\int_0^{\pi} \cos(\sin\theta) d\theta = \pi J_0(1)\) (where \(J_0\) is the Bessel function of the first kind of order 0)
- \(\int_0^{\pi} \cos 2\theta \cos(\sin\theta) d\theta = \pi J_2(1)\) (where \(J_2\) is the Bessel function of the first kind of order 2)

Thus, the integral simplifies to:
\[
\frac{\pi}{2} \left( J_0(1) - J_2(1) \right)
\]

### Step 4: Numerical Approximation
Using known values of Bessel functions:
- \(J_0(1) \approx 0.7651976865579666\)
- \(J_2(1) \approx 0.11490348493190048\)

The numerical value is:
\[
\frac{\pi}{2} \left( 0.7651976865579666 - 0.11490348493190048 \right) \approx 1.0217344380
\]

### Final Answer
The exact answer is \(\frac{\pi}{2} \left( J_0(1) - J_2(1) \right)\), and the numerical approximation is \(1.0217344380\).

{"answer": "\\frac{\\pi}{2} \\left( J_0(1) - J_2(1) \\right)", "numerical_answer": "1.0217344380"}