

To solve the definite integral \(\int_{0}^{1} x^{-1/2}(1-x)^{-1/2} T_{4}\left(\sqrt{x(1-x)}\right) dx\), we follow these steps:

### Step 1: Express \(T_4(z)\) explicitly
The Chebyshev polynomial of the first kind \(T_4(z)\) is given by \(T_4(z) = 8z^4 - 8z^2 + 1\). Here, \(z = \sqrt{x(1-x)}\), so \(z^2 = x(1-x)\) and \(z^4 = (x(1-x))^2 = x^2 - 2x^3 + x^4\). Substituting \(z = \sqrt{x(1-x)}\) into \(T_4(z)\), we get:
\[
T_4\left(\sqrt{x(1-x)}\right) = 8(x^2 - 2x^3 + x^4) - 8(x - x^2) + 1 = 8x^4 - 16x^3 + 16x^2 - 8x + 1.
\]

### Step 2: Rewrite the integrand
The integrand becomes:
\[
x^{-1/2}(1-x)^{-1/2} \cdot (8x^4 - 16x^3 + 16x^2 - 8x + 1).
\]
Simplifying the exponents, we split the integral into five terms:
\[
\int_{0}^{1} \left[ 8x^{7/2}(1-x)^{-1/2} - 16x^{5/2}(1-x)^{-1/2} + 16x^{3/2}(1-x)^{-1/2} - 8x^{1/2}(1-x)^{-1/2} + x^{-1/2}(1-x)^{-1/2} \right] dx.
\]

### Step 3: Evaluate each term using the Beta function
Each term is a Beta function \(B(p, q) = \int_{0}^{1} x^{p-1}(1-x)^{q-1} dx = \frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}\), where \(\Gamma\) is the Gamma function. We use properties of the Gamma function (\(\Gamma(n + 1/2) = \frac{(2n)!!}{4^n n!}\sqrt{\pi}\) and \(\Gamma(n) = (n-1)!\) for integers \(n\)):

1. \(8 \int_{0}^{1} x^{7/2}(1-x)^{-1/2} dx = 8 \cdot B\left(\frac{9}{2}, \frac{1}{2}\right) = 8 \cdot \frac{\Gamma(9/2)\Gamma(1/2)}{\Gamma(5)} = \frac{35\pi}{16}\).
2. \(-16 \int_{0}^{1} x^{5/2}(1-x)^{-1/2} dx = -16 \cdot B\left(\frac{7}{2}, \frac{1}{2}\right) = -16 \cdot \frac{\Gamma(7/2)\Gamma(1/2)}{\Gamma(4)} = -5\pi\).
3. \(16 \int_{0}^{1} x^{3/2}(1-x)^{-1/2} dx = 16 \cdot B\left(\frac{5}{2}, \frac{1}{2}\right) = 16 \cdot \frac{\Gamma(5/2)\Gamma(1/2)}{\Gamma(3)} = 6\pi\).
4. \(-8 \int_{0}^{1} x^{1/2}(1-x)^{-1/2} dx = -8 \cdot B\left(\frac{3}{2}, \frac{1}{2}\right) = -8 \cdot \frac{\Gamma(3/2)\Gamma(1/2)}{\Gamma(2)} = -4\pi\).
5. \(\int_{0}^{1} x^{-1/2}(1-x)^{-1/2} dx = B\left(\frac{1}{2}, \frac{1}{2}\right) = \frac{\Gamma(1/2)\Gamma(1/2)}{\Gamma(1)} = \pi\).

### Step 4: Sum the results
Adding these terms together:
\[
\frac{35\pi}{16} - 5\pi + 6\pi - 4\pi + \pi = \frac{3\pi}{16}.
\]

### Numerical Approximation
The numerical value of \(\frac{3\pi}{16}\) is approximately \(0.5890486225\) (rounded to 10 decimal places).

{"answer": "\\frac{3\\pi}{16}", "numerical_answer": "0.5890486225"}