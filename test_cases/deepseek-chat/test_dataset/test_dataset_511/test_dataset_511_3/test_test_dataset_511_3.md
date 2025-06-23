To solve the definite integral \(\int_0^8 \frac{\cos\sqrt{x}}{\sqrt{x}} \, dx\), we can proceed with the following steps:

### Step 1: Substitution
Let \( u = \sqrt{x} \). Then, \( x = u^2 \) and \( dx = 2u \, du \).

When \( x = 0 \), \( u = 0 \).  
When \( x = 8 \), \( u = \sqrt{8} = 2\sqrt{2} \).

The integral becomes:
\[
\int_0^{2\sqrt{2}} \frac{\cos u}{u} \cdot 2u \, du = 2 \int_0^{2\sqrt{2}} \cos u \, du.
\]

### Step 2: Integrate
The integral of \(\cos u\) is \(\sin u\):
\[
2 \int \cos u \, du = 2 \sin u + C.
\]

### Step 3: Evaluate the Definite Integral
Evaluate from \( 0 \) to \( 2\sqrt{2} \):
\[
2 \left[ \sin(2\sqrt{2}) - \sin(0) \right] = 2 \sin(2\sqrt{2}).
\]

### Step 4: Numerical Approximation
Compute \( 2 \sin(2\sqrt{2}) \) numerically:
\[
2\sqrt{2} \approx 2.8284271247, \quad \sin(2.8284271247) \approx 0.3242402433.
\]
Thus:
\[
2 \sin(2\sqrt{2}) \approx 0.6484804866.
\]

### Final Answer
The exact answer is \( 2 \sin(2\sqrt{2}) \), and the numerical approximation is \( 0.6484804866 \).

```json
{"answer": "2 \\sin(2\\sqrt{2})", "numerical_answer": "0.6484804866"}
```