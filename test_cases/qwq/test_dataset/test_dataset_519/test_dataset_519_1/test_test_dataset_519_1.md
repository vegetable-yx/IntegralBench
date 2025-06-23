To compute the definite integral \(\int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx\), we proceed as follows:

1. **Simplify the integrand**:
   \[
   2 - \cos^2(x) = 1 + \sin^2(x)
   \]
   Thus, the integral becomes:
   \[
   \int_0^{\pi/2} \frac{\cos(x)}{1 + \sin^2(x)} \, dx
   \]

2. **Substitution**:
   Let \(u = \sin(x)\), hence \(du = \cos(x) \, dx\). The limits of integration change accordingly:
   - When \(x = 0\), \(u = 0\)
   - When \(x = \pi/2\), \(u = 1\)

   The integral transforms to:
   \[
   \int_0^1 \frac{1}{1 + u^2} \, du
   \]

3. **Evaluate the integral**:
   The integral of \(\frac{1}{1 + u^2}\) is \(\arctan(u)\). Evaluating from 0 to 1:
   \[
   \left[ \arctan(u) \right]_0^1 = \arctan(1) - \arctan(0) = \frac{\pi}{4} - 0 = \frac{\pi}{4}
   \]

4. **Numerical approximation**:
   The numerical value of \(\frac{\pi}{4}\) rounded to 10 decimal places is \(0.7853981634\).

### Final Answer
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}