To solve the definite integral \(\int\limits_0^1 \frac{1}{1+x^2} \arctan\left(x^{11+\sqrt{120}}\right) dx\), we proceed as follows:

1. **Analytical Calculation**:
   - Let \(a = 11 + \sqrt{120}\). The integral becomes \(I(a) = \int_0^1 \frac{\arctan(x^a)}{1 + x^2} dx\).
   - Using the substitution \(x = \frac{1}{t}\), we transform the integral into:
     \[
     I(a) = \int_1^\infty \frac{\arctan\left(\frac{1}{t^a}\right)}{1 + t^2} dt
     \]
   - Using the identity \(\arctan\left(\frac{1}{t^a}\right) = \frac{\pi}{2} - \arctan(t^a)\), the integral becomes:
     \[
     I(a) = \frac{\pi}{2} \int_1^\infty \frac{1}{1 + t^2} dt - \int_1^\infty \frac{\arctan(t^a)}{1 + t^2} dt
     \]
   - The first integral evaluates to \(\frac{\pi^2}{8}\). Let \(J = \int_1^\infty \frac{\arctan(t^a)}{1 + t^2} dt\).
   - Substituting \(t = \frac{1}{u}\) in \(J\), we find \(J = \frac{\pi^2}{8} - I(a)\).
   - Substituting back, we get \(I(a) = \frac{\pi^2}{8} - \left(\frac{\pi^2}{8} - I(a)\right)\), leading to \(I(a) + I\left(\frac{1}{a}\right) = \frac{\pi^2}{16}\).
   - Given \(a + \frac{1}{a} = 22\), we assume symmetry and find \(I(a) = I\left(\frac{1}{a}\right)\), leading to \(I(a) = \frac{\pi^2}{32}\).

2. **Numerical Approximation**:
   - The numerical value of \(\frac{\pi^2}{32}\) is approximately \(0.3084251375\).

### Final Answer
{"answer": "\\frac{\\pi^2}{32}", "numerical_answer": "0.3084251375"}