

To solve the definite integral \(\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx\), we proceed with the following steps:

### Step 1: Substitution
Let \( u = \sqrt{x} \). Then, \( du = \frac{1}{2\sqrt{x}}dx \), which implies \( 2du = \frac{dx}{\sqrt{x}} \). When \( x = 0 \), \( u = 0 \); when \( x = 441 \), \( u = \sqrt{441} = 21 \). Substituting these into the integral, we rewrite the integrand:

\[
\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx = \int_0^{21} \pi\sin(\pi u) \cdot 2du = 2\pi \int_0^{21} \sin(\pi u) du
\]

### Step 2: Evaluate the Integral
The antiderivative of \( \sin(\pi u) \) with respect to \( u \) is \( -\frac{1}{\pi}\cos(\pi u) \). Thus:

\[
2\pi \int_0^{21} \sin(\pi u) du = 2\pi \left[ -\frac{1}{\pi}\cos(\pi u) \right]_0^{21}
\]

### Step 3: Simplify and Evaluate Limits
Simplifying the expression:

\[
2\pi \cdot \left( -\frac{1}{\pi} \right) \left[ \cos(\pi \cdot 21) - \cos(\pi \cdot 0) \right] = -2 \left[ \cos(21\pi) - \cos(0) \right]
\]

Since \( \cos(21\pi) = \cos(\pi) = -1 \) (because \( 21\pi = 10 \cdot 2\pi + \pi \)) and \( \cos(0) = 1 \):

\[
-2 \left[ (-1) - 1 \right] = -2(-2) = 4
\]

### Numerical Approximation
The exact value is \( 4 \), so the numerical approximation to 10 decimal places is \( 4.0000000000 \).

{"answer": "4", "numerical_answer": "4.0000000000"}