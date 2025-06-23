To solve the definite integral \(\int_0^8 \frac{\cos\sqrt{x}}{\sqrt{x}} \, dx\), we can proceed with the following steps:

### Step 1: Substitution
Let \( u = \sqrt{x} \). Then, \( x = u^2 \) and \( dx = 2u \, du \).

When \( x = 0 \), \( u = 0 \).  
When \( x = 8 \), \( u = \sqrt{8} = 2\sqrt{2} \).

The integral becomes:
\[
\int_0^8 \frac{\cos\sqrt{x}}{\sqrt{x}} \, dx = \int_0^{2\sqrt{2}} \frac{\cos u}{u} \cdot 2u \, du = 2 \int_0^{2\sqrt{2}} \cos u \, du.
\]

### Step 2: Integrate
The integral of \(\cos u\) is \(\sin u\):
\[
2 \int_0^{2\sqrt{2}} \cos u \, du = 2 \left[ \sin u \right]_0^{2\sqrt{2}} = 2 (\sin(2\sqrt{2}) - \sin(0)) = 2 \sin(2\sqrt{2}).
\]

### Step 3: Numerical Approximation
We compute \( 2 \sin(2\sqrt{2}) \) numerically. First, calculate \( 2\sqrt{2} \):
\[
2\sqrt{2} \approx 2.8284271247461903.
\]
Then, compute \(\sin(2.8284271247461903)\):
\[
\sin(2.8284271247461903) \approx 0.3107679047306654.
\]
Finally, multiply by 2:
\[
2 \sin(2\sqrt{2}) \approx 0.6215358094613308.
\]

### Final Answer
The exact answer is \( 2 \sin(2\sqrt{2}) \), and the numerical approximation is approximately \( 0.6215358095 \).

```json
{"answer": "2 \\sin(2\\sqrt{2})", "numerical_answer": "0.6215358095"}
```