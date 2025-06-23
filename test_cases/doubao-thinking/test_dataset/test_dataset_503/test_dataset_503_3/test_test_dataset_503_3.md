

To solve the definite integral \(\int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx\), we use trigonometric product-to-sum identities to simplify the integrand.

### Step 1: Simplify the product of cosines
First, use the identity \(\cos(A)\cos(B) = \frac{1}{2}[\cos(A+B) + \cos(A-B)]\) to expand \(\cos(x)\cos(3x)\):
\[
\cos(x)\cos(3x) = \frac{1}{2}[\cos(4x) + \cos(2x)]
\]
Next, multiply this result by \(\cos(5x)\):
\[
\cos(x)\cos(3x)\cos(5x) = \frac{1}{2}[\cos(4x) + \cos(2x)]\cos(5x)
\]
Apply the product-to-sum identity again to each term:
\[
\cos(4x)\cos(5x) = \frac{1}{2}[\cos(9x) + \cos(-x)] = \frac{1}{2}[\cos(9x) + \cos(x)]
\]
\[
\cos(2x)\cos(5x) = \frac{1}{2}[\cos(7x) + \cos(-3x)] = \frac{1}{2}[\cos(7x) + \cos(3x)]
\]
Combining these results, the integrand becomes:
\[
\cos(x)\cos(3x)\cos(5x) = \frac{1}{2} \left[ \frac{1}{2}[\cos(9x) + \cos(x)] + \frac{1}{2}[\cos(7x) + \cos(3x)] \right] = \frac{1}{4}[\cos(9x) + \cos(x) + \cos(7x) + \cos(3x)]
\]

### Step 2: Integrate term-by-term
The integral simplifies to:
\[
\int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx = \frac{1}{4} \int_0^\pi [\cos(9x) + \cos(x) + \cos(7x) + \cos(3x)] \, dx
\]
Integrate each cosine term separately. For any integer \(k\), \(\int \cos(kx) \, dx = \frac{1}{k}\sin(kx) + C\). Evaluating from \(0\) to \(\pi\):
\[
\int_0^\pi \cos(kx) \, dx = \left. \frac{1}{k}\sin(kx) \right|_0^\pi = \frac{1}{k}[\sin(k\pi) - \sin(0)] = 0
\]
since \(\sin(k\pi) = 0\) for all integers \(k\). Thus, each term in the integral evaluates to \(0\).

### Step 3: Final result
The entire integral is:
\[
\frac{1}{4}(0 + 0 + 0 + 0) = 0
\]

### Numerical Approximation
The exact result is \(0\), so the numerical approximation is \(0.0000000000\).

{"answer": "0", "numerical_answer": "0.0000000000"}