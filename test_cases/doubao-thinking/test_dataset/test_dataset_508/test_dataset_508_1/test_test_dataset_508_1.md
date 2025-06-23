

To solve the definite integral \(\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx\), we proceed with the following steps:

### Step 1: Substitution
Let \( u = \sqrt{x} \). Then \( x = u^2 \), so \( dx = 2u \, du \). When \( x = 0 \), \( u = 0 \); when \( x = 441 \), \( u = \sqrt{441} = 21 \). Substituting these into the integral:

\[
\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx = \int_0^{21}\frac{\pi\sin(\pi u)}{u} \cdot 2u \, du
\]

The \( u \) in the numerator and denominator cancels, simplifying the integrand:

\[
\int_0^{21} 2\pi \sin(\pi u) \, du
\]

### Step 2: Evaluate the Integral
The antiderivative of \( \sin(\pi u) \) with respect to \( u \) is \( -\frac{1}{\pi}\cos(\pi u) \). Applying the Fundamental Theorem of Calculus:

\[
2\pi \int_0^{21} \sin(\pi u) \, du = 2\pi \left[ -\frac{1}{\pi}\cos(\pi u) \right]_0^{21}
\]

### Step 3: Simplify the Result
Evaluate the antiderivative at the bounds \( u = 21 \) and \( u = 0 \):

\[
2\pi \left( -\frac{1}{\pi}\cos(21\pi) + \frac{1}{\pi}\cos(0) \right)
\]

Since \( \cos(21\pi) = \cos(\pi) = -1 \) (because \( 21\pi = 10 \cdot 2\pi + \pi \)) and \( \cos(0) = 1 \):

\[
2\pi \left( -\frac{1}{\pi}(-1) + \frac{1}{\pi}(1) \right) = 2\pi \left( \frac{1}{\pi} + \frac{1}{\pi} \right) = 2\pi \cdot \frac{2}{\pi} = 4
\]

### Numerical Approximation
The exact value is \( 4 \), so the numerical approximation rounded to 10 decimal places is \( 4.0000000000 \).

{"answer": "4", "numerical_answer": "4.0000000000"}