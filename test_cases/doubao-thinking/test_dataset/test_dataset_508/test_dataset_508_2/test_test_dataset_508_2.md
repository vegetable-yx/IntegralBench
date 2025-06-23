

To solve the definite integral \(\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx\), we proceed with the following steps:

### Step 1: Substitution
Let \( u = \sqrt{x} \). Then, \( du = \frac{1}{2\sqrt{x}}dx \), which implies \( 2du = \frac{dx}{\sqrt{x}} \). This substitution simplifies the integral by eliminating the \( \frac{1}{\sqrt{x}} \) term.

### Step 2: Adjust Limits of Integration
When \( x = 0 \), \( u = \sqrt{0} = 0 \). When \( x = 441 \), \( u = \sqrt{441} = 21 \). Thus, the limits of integration change from \( x = 0 \) to \( x = 441 \) to \( u = 0 \) to \( u = 21 \).

### Step 3: Rewrite the Integral
Substituting \( u = \sqrt{x} \) and \( 2du = \frac{dx}{\sqrt{x}} \), the integral becomes:
\[
\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx = \int_0^{21} \pi \sin(\pi u) \cdot 2du = 2\pi \int_0^{21} \sin(\pi u) du
\]

### Step 4: Evaluate the Integral
The antiderivative of \( \sin(\pi u) \) with respect to \( u \) is \( -\frac{1}{\pi}\cos(\pi u) \). Thus:
\[
2\pi \int_0^{21} \sin(\pi u) du = 2\pi \left[ -\frac{1}{\pi}\cos(\pi u) \right]_0^{21}
\]

### Step 5: Simplify the Result
Simplifying the expression:
\[
2\pi \left( -\frac{1}{\pi}\cos(\pi \cdot 21) + \frac{1}{\pi}\cos(\pi \cdot 0) \right) = 2 \left( -\cos(21\pi) + \cos(0) \right)
\]

### Step 6: Evaluate Cosine Terms
Since \( \cos(21\pi) = \cos(\pi) = -1 \) (because \( 21\pi = 10 \cdot 2\pi + \pi \)) and \( \cos(0) = 1 \), we substitute these values:
\[
2 \left( -(-1) + 1 \right) = 2(1 + 1) = 4
\]

### Numerical Approximation
The exact result is \( 4 \), so the numerical approximation rounded to 10 decimal places is \( 4.0000000000 \).

{"answer": "4", "numerical_answer": "4.0000000000"}