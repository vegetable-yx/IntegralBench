To compute the definite integral \(\int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx\), we can follow these steps:

### Step 1: Use Trigonometric Identities
First, we simplify the integrand \(\cos(x)\cos(3x)\cos(5x)\) using the product-to-sum identities. Recall that:
\[
\cos(A)\cos(B) = \frac{1}{2} [\cos(A+B) + \cos(A-B)]
\]
Applying this to \(\cos(x)\cos(3x)\):
\[
\cos(x)\cos(3x) = \frac{1}{2} [\cos(4x) + \cos(2x)]
\]
Now multiply by \(\cos(5x)\):
\[
\cos(x)\cos(3x)\cos(5x) = \frac{1}{2} [\cos(4x)\cos(5x) + \cos(2x)\cos(5x)]
\]
Apply the product-to-sum identity again to each term:
\[
\cos(4x)\cos(5x) = \frac{1}{2} [\cos(9x) + \cos(x)]
\]
\[
\cos(2x)\cos(5x) = \frac{1}{2} [\cos(7x) + \cos(3x)]
\]
Substituting back:
\[
\cos(x)\cos(3x)\cos(5x) = \frac{1}{4} [\cos(9x) + \cos(x) + \cos(7x) + \cos(3x)]
\]

### Step 2: Integrate Term by Term
Now, integrate each term from \(0\) to \(\pi\):
\[
\int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx = \frac{1}{4} \left[ \int_0^\pi \cos(9x) \, dx + \int_0^\pi \cos(x) \, dx + \int_0^\pi \cos(7x) \, dx + \int_0^\pi \cos(3x) \, dx \right]
\]
Each of these integrals is of the form \(\int_0^\pi \cos(kx) \, dx\), which evaluates to:
\[
\int_0^\pi \cos(kx) \, dx = \frac{\sin(k\pi)}{k} - \frac{\sin(0)}{k} = \frac{\sin(k\pi)}{k}
\]
Since \(\sin(k\pi) = 0\) for any integer \(k\), all these integrals evaluate to \(0\):
\[
\int_0^\pi \cos(9x) \, dx = 0, \quad \int_0^\pi \cos(x) \, dx = 0, \quad \int_0^\pi \cos(7x) \, dx = 0, \quad \int_0^\pi \cos(3x) \, dx = 0
\]
Thus:
\[
\int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx = \frac{1}{4} [0 + 0 + 0 + 0] = 0
\]

### Step 3: Numerical Approximation
The exact answer is \(0\), so the numerical approximation is also \(0\).

### Final Answer
```json
{"answer": "0", "numerical_answer": "0.0000000000"}
```