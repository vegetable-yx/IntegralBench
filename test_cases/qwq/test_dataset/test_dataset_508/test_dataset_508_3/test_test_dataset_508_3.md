To compute the definite integral \(\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx\), we proceed as follows:

1. **Substitution**: Let \( t = \sqrt{x} \). Then, \( x = t^2 \) and \( dx = 2t \, dt \). The limits of integration change from \( x = 0 \) to \( t = 0 \) and from \( x = 441 \) to \( t = 21 \).

2. **Rewrite the Integral**: Substituting into the integral, we get:
   \[
   \int_0^{441} \frac{\pi \sin(\pi\sqrt{x})}{\sqrt{x}} \, dx = \int_0^{21} \frac{\pi \sin(\pi t)}{t} \cdot 2t \, dt = 2\pi \int_0^{21} \sin(\pi t) \, dt
   \]

3. **Integrate**: The integral of \(\sin(\pi t)\) is \(-\frac{1}{\pi} \cos(\pi t)\):
   \[
   2\pi \left[ -\frac{1}{\pi} \cos(\pi t) \right]_0^{21} = 2\pi \left( -\frac{1}{\pi} \left[ \cos(21\pi) - \cos(0) \right] \right)
   \]

4. **Simplify**: 
   - \(\cos(21\pi) = \cos(\pi \cdot 21) = \cos(\pi) = -1\) (since \(21\pi\) is an odd multiple of \(\pi\)),
   - \(\cos(0) = 1\).
   \[
   2\pi \left( -\frac{1}{\pi} \left[ -1 - 1 \right] \right) = 2\pi \left( -\frac{1}{\pi} (-2) \right) = 2\pi \cdot \frac{2}{\pi} = 4
   \]

5. **Numerical Approximation**: The exact value is 4, so the numerical approximation is 4.0000000000.

\[
\boxed{"answer": "4", "numerical_answer": "4.0000000000"}
\]