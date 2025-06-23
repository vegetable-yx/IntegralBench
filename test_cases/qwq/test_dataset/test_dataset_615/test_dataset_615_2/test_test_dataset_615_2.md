To compute the definite integral \(\int_{0}^{7}\left(\sqrt[3]{\sqrt{x^{2}+1}+x}-\sqrt[3]{\sqrt{x^{2}+1}-x}\right)\:\mathrm{d}x\), we proceed as follows:

1. **Simplify the Integrand**:
   Let \(A = \sqrt[3]{\sqrt{x^2 + 1} + x}\) and \(B = \sqrt[3]{\sqrt{x^2 + 1} - x}\). The integrand is \(A - B\). Noting that \(A \cdot B = 1\), we have \(B = 1/A\). Thus, the integrand becomes \(A - 1/A\).

2. **Substitution**:
   Substitute \(x = \sinh\theta\), so \(\sqrt{x^2 + 1} = \cosh\theta\). Then, the terms inside the cube roots simplify to \(e^{\theta}\) and \(e^{-\theta}\), leading to:
   \[
   A = e^{\theta/3} \quad \text{and} \quad B = e^{-\theta/3}
   \]
   The integrand becomes \(2\sinh(\theta/3)\).

3. **Integral Transformation**:
   The integral transforms to:
   \[
   \int_{0}^{\sinh^{-1}(7)} 2\sinh\left(\frac{\theta}{3}\right) \cosh\theta \, d\theta
   \]
   Using hyperbolic identities, this simplifies to:
   \[
   \int_{0}^{\sinh^{-1}(7)} \left[\sinh\left(\frac{4\theta}{3}\right) - \sinh\left(\frac{2\theta}{3}\right)\right] d\theta
   \]

4. **Evaluate the Integral**:
   The antiderivative is:
   \[
   \left[\frac{3}{4}\cosh\left(\frac{4\theta}{3}\right) - \frac{3}{2}\cosh\left(\frac{2\theta}{3}\right)\right]
   \]
   Evaluating from \(0\) to \(\theta = 3\sinh^{-1}(1)\) (since \(\sinh^{-1}(7) = 3\sinh^{-1}(1)\)):
   \[
   \left[\frac{3}{4} \cdot 17 - \frac{3}{2} \cdot 3\right] - \left[\frac{3}{4} - \frac{3}{2}\right] = 9
   \]

5. **Verification**:
   By recognizing the differential equation \(y^3 + 3y = 2x\) and solving it, we confirm the integral evaluates to 9.

The exact answer is \(9\) and the numerical approximation is \(9.0000000000\).

\[
\boxed{"answer": "9", "numerical_answer": "9.0000000000"}
\]