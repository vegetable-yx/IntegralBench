

To solve the definite integral \(\int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx\), we use trigonometric identities to simplify the integrand.

### Step 1: Simplify the product of cosines
First, apply the product-to-sum identity to \(\cos(3x)\cos(5x)\):
\[
\cos(3x)\cos(5x) = \frac{1}{2}\left[\cos(3x+5x) + \cos(3x-5x)\right] = \frac{1}{2}\left[\cos(8x) + \cos(2x)\right]
\]
Next, multiply this result by \(\cos(x)\) and apply the product-to-sum identity again:
\[
\cos(x)\cos(3x)\cos(5x) = \cos(x) \cdot \frac{1}{2}\left[\cos(8x) + \cos(2x)\right] = \frac{1}{2}\left[\cos(x)\cos(8x) + \cos(x)\cos(2x)\right]
\]
For \(\cos(x)\cos(8x)\):
\[
\cos(x)\cos(8x) = \frac{1}{2}\left[\cos(9x) + \cos(7x)\right]
\]
For \(\cos(x)\cos(2x)\):
\[
\cos(x)\cos(2x) = \frac{1}{2}\left[\cos(3x) + \cos(x)\right]
\]
Combining these, the integrand becomes:
\[
\cos(x)\cos(3x)\cos(5x) = \frac{1}{2} \cdot \frac{1}{2}\left[\cos(9x) + \cos(7x) + \cos(3x) + \cos(x)\right] = \frac{1}{4}\left[\cos(9x) + \cos(7x) + \cos(3x) + \cos(x)\right]
\]

### Step 2: Integrate term-by-term
The integral simplifies to:
\[
\int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx = \frac{1}{4} \int_0^\pi \left[\cos(9x) + \cos(7x) + \cos(3x) + \cos(x)\right] dx
\]
Integrate each cosine term separately. For \(\int_0^\pi \cos(kx) \, dx\) (where \(k\) is an integer):
\[
\int_0^\pi \cos(kx) \, dx = \left.\frac{1}{k}\sin(kx)\right|_0^\pi = \frac{1}{k}\left[\sin(k\pi) - \sin(0)\right] = 0
\]
Since \(\sin(k\pi) = 0\) for all integers \(k\), each term in the integral evaluates to 0. Thus:
\[
\frac{1}{4} \left[0 + 0 + 0 + 0\right] = 0
\]

### Numerical Approximation
The exact result is \(0\), so the numerical approximation (rounded to 10 decimal places) is \(0.0000000000\).

{"answer": "0", "numerical_answer": "0.0000000000"}