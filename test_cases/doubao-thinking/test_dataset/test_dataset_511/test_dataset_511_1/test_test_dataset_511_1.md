
To solve the definite integral \(\int_0^8 \frac{\cos\sqrt{x}}{\sqrt{x}} \, dx\), we use substitution:

### Step 1: Substitution
Let \( u = \sqrt{x} \). Then \( x = u^2 \), so \( dx = 2u \, du \). When \( x = 0 \), \( u = 0 \); when \( x = 8 \), \( u = \sqrt{8} = 2\sqrt{2} \).

### Step 2: Rewrite the Integral
Substituting \( u = \sqrt{x} \) and \( dx = 2u \, du \), the integral becomes:
\[
\int_0^8 \frac{\cos\sqrt{x}}{\sqrt{x}} \, dx = \int_0^{2\sqrt{2}} \frac{\cos u}{u} \cdot 2u \, du
\]
The \( u \) in the denominator cancels with the \( u \) from \( dx \), simplifying to:
\[
2 \int_0^{2\sqrt{2}} \cos u \, du
\]

### Step 3: Evaluate the Integral
The integral of \( \cos u \) is \( \sin u \). Evaluating from \( 0 \) to \( 2\sqrt{2} \):
\[
2 \left[ \sin u \right]_0^{2\sqrt{2}} = 2 \left( \sin(2\sqrt{2}) - \sin(0) \right) = 2 \sin(2\sqrt{2})
\]

### Step 4: Numerical Approximation
The exact value is \( 2 \sin(2\sqrt{2}) \). Numerically, \( 2\sqrt{2} \approx 2.8284271247 \), and \( \sin(2.8284271247) \approx 0.22252093396 \). Thus:
\[
2 \sin(2\sqrt{2}) \approx 2 \times 0.22252093396 \approx 0.4450418679
\]

### Final Answer
The exact answer is \( 2 \sin\left(2\sqrt{2}\right) \), and the numerical approximation is \( 0.4450418679 \).

{"answer": "2 \\sin\\left(2\\sqrt{2}\\right)", "numerical_answer": "0.4450418679"}