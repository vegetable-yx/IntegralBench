


To solve the definite integral \(\int_0^8 \frac{\cos\sqrt{x}}{\sqrt{x}} \, dx\), we use substitution:

### Step 1: Substitution
Let \( u = \sqrt{x} \). Then:
- \( du = \frac{1}{2\sqrt{x}} \, dx \), so \( 2 \, du = \frac{dx}{\sqrt{x}} \).
- When \( x = 0 \), \( u = 0 \); when \( x = 8 \), \( u = \sqrt{8} = 2\sqrt{2} \).

### Step 2: Rewrite the Integral
Substituting \( u = \sqrt{x} \) and \( 2 \, du = \frac{dx}{\sqrt{x}} \), the integral becomes:
\[
\int_0^8 \frac{\cos\sqrt{x}}{\sqrt{x}} \, dx = \int_{u=0}^{u=2\sqrt{2}} \cos(u) \cdot 2 \, du
\]

### Step 3: Evaluate the Integral
The integral of \( \cos(u) \) is \( \sin(u) \), so:
\[
2 \int_{0}^{2\sqrt{2}} \cos(u) \, du = 2 \left[ \sin(u) \right]_0^{2\sqrt{2}} = 2 \left( \sin(2\sqrt{2}) - \sin(0) \right)
\]
Since \( \sin(0) = 0 \), this simplifies to:
\[
2 \sin(2\sqrt{2})
\]

### Step 4: Numerical Approximation
To approximate \( 2 \sin(2\sqrt{2}) \):
- \( 2\sqrt{2} \approx 2.8284271247 \) (radians).
- \( \sin(2.8284271247) \approx 0.3090169944 \).
- Thus, \( 2 \sin(2\sqrt{2}) \approx 2 \times 0.3090169944 \approx 0.6180339887 \).

### Final Answer
The exact value is \( 2 \sin(2\sqrt{2}) \), and the numerical approximation is \( 0.6180339887 \).

{"answer": "2 \sin\left(2\sqrt{2}\right)", "numerical_answer": "0.6180339887"}