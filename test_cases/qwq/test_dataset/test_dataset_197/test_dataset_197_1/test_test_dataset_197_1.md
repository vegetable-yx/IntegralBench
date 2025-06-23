To compute the definite integral \(\int_0^1 x \arcsin x \arccos x \, dx\), we proceed as follows:

1. **Simplify the Integrand**:
   Using the identity \(\arccos x = \frac{\pi}{2} - \arcsin x\), the integral becomes:
   \[
   \int_0^1 x \arcsin x \left( \frac{\pi}{2} - \arcsin x \right) dx
   \]
   This splits into two integrals:
   \[
   \frac{\pi}{2} \int_0^1 x \arcsin x \, dx - \int_0^1 x (\arcsin x)^2 \, dx
   \]

2. **Compute the First Integral \(I_1 = \int_0^1 x \arcsin x \, dx\)**:
   - Use integration by parts with \(u = \arcsin x\) and \(dv = x \, dx\):
     \[
     du = \frac{1}{\sqrt{1 - x^2}} dx, \quad v = \frac{1}{2} x^2
     \]
     \[
     I_1 = \left[ \frac{1}{2} x^2 \arcsin x \right]_0^1 - \frac{1}{2} \int_0^1 \frac{x^2}{\sqrt{1 - x^2}} dx
     \]
   - Evaluate boundary term:
     \[
     \left[ \frac{1}{2} x^2 \arcsin x \right]_0^1 = \frac{\pi}{4}
     \]
   - Substitute \(x = \sin \theta\) for the remaining integral:
     \[
     \int_0^{\pi/2} \sin^2 \theta \, d\theta = \frac{\pi}{4}
     \]
     \[
     I_1 = \frac{\pi}{4} - \frac{\pi}{8} = \frac{\pi}{8}
     \]

3. **Compute the Second Integral \(I_2 = \int_0^1 x (\arcsin x)^2 \, dx\)**:
   - Use integration by parts with \(u = (\arcsin x)^2\) and \(dv = x \, dx\):
     \[
     du = \frac{2 \arcsin x}{\sqrt{1 - x^2}} dx, \quad v = \frac{1}{2} x^2
     \]
     \[
     I_2 = \left[ \frac{1}{2} x^2 (\arcsin x)^2 \right]_0^1 - \int_0^1 \frac{x^2 \arcsin x}{\sqrt{1 - x^2}} dx
     \]
   - Evaluate boundary term:
     \[
     \left[ \frac{1}{2} x^2 (\arcsin x)^2 \right]_0^1 = \frac{\pi^2}{8}
     \]
   - Substitute \(x = \sin \theta\) for the remaining integral:
     \[
     \int_0^{\pi/2} \theta \sin^2 \theta \, d\theta = \frac{\pi^2}{16} + \frac{1}{4}
     \]
     \[
     I_2 = \frac{\pi^2}{8} - \left( \frac{\pi^2}{16} + \frac{1}{4} \right) = \frac{\pi^2}{16} - \frac{1}{4}
     \]

4. **Combine Results**:
   \[
   \text{Original Integral} = \frac{\pi}{2} \cdot \frac{\pi}{8} - \left( \frac{\pi^2}{16} - \frac{1}{4} \right) = \frac{\pi^2}{16} - \frac{\pi^2}{16} + \frac{1}{4} = \frac{1}{4}
   \]

The numerical approximation of the result, rounded to 10 decimal places, is \(0.2500000000\).

### Final Answer
{"answer": "\\boxed{\\dfrac{1}{4}}", "numerical_answer": "0.2500000000"}