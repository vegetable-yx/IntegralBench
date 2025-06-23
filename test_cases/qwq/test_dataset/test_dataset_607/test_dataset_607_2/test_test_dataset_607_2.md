To solve the definite integral \(\int_0^{\frac{\pi}{2}} \cosh^{-1}(\sin(x) + \cos(x)) \, dx\), we start by analyzing the integrand and using trigonometric identities and substitutions to simplify the expression.

1. **Trigonometric Identity and Substitution**:
   - The integrand \(\sin(x) + \cos(x)\) can be rewritten using the identity \(\sin(x) + \cos(x) = \sqrt{2} \sin\left(x + \frac{\pi}{4}\right)\).
   - Substituting \(t = x + \frac{\pi}{4}\), the integral becomes \(\int_{\frac{\pi}{4}}^{\frac{3\pi}{4}} \cosh^{-1}\left(\sqrt{2} \sin(t)\right) \, dt\).

2. **Symmetry and Further Substitution**:
   - The integral is symmetric around \(\frac{\pi}{2}\). Using the substitution \(u = \frac{\pi}{2} - t\), the integral simplifies to \(2 \int_0^{\frac{\pi}{4}} \cosh^{-1}\left(\sqrt{2} \cos(t)\right) \, dt\).

3. **Integration by Parts and Simplification**:
   - Using integration by parts and further substitutions, we find that the integral can be transformed into a form that allows for analytical evaluation.
   - After several substitutions and simplifications, the integral is found to be related to logarithmic terms involving \(\sqrt{2}\).

4. **Final Result**:
   - The integral evaluates to \(\frac{\pi}{2} \ln(2)\) after considering the symmetry and properties of the hyperbolic functions involved.

### Final Answer
{"answer": "\\frac{\\pi}{2} \\ln 2", "numerical_answer": "1.088793043"}