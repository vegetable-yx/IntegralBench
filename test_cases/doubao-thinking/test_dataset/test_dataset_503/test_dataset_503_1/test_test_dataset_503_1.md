

To calculate the definite integral \(\int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx\), we use trigonometric product-to-sum identities to simplify the integrand.

### Step 1: Simplify the product of cosines
First, apply the product-to-sum identity to \(\cos(3x)\cos(5x)\):
\[
\cos(3x)\cos(5x) = \frac{1}{2}\left[\cos(3x+5x) + \cos(3x-5x)\right] = \frac{1}{2}\left[\cos(8x) + \cos(2x)\right]
\]
(since \(\cos(-2x) = \cos(2x)\)).

Next, multiply by \(\cos(x)\) and apply the product-to-sum identity again to each term:
\[
\cos(x) \cdot \frac{1}{2}\left[\cos(8x) + \cos(2x)\right] = \frac{1}{2}\left[\cos(x)\cos(8x) + \cos(x)\cos(2x)\right]
\]

For \(\cos(x)\cos(8x)\):
\[
\cos(x)\cos(8x) = \frac{1}{2}\left[\cos(x+8x) + \cos(x-8x)\right] = \frac{1}{2}\left[\cos(9x) + \cos(7x)\right]
\]
(since \(\cos(-7x) = \cos(7x)\)).

For \(\cos(x)\cos(2x)\):
\[
\cos(x)\cos(2x) = \frac{1}{2}\left[\cos(x+2x) + \cos(x-2x)\right] = \frac{1}{2}\left[\cos(3x) + \cos(x)\right]
\]
(since \(\cos(-x) = \cos(x)\)).

### Step 2: Combine terms
Substituting these back, the integrand becomes:
\[
\frac{1}{2}\left[\frac{1}{2}\left(\cos(9x) + \cos(7x)\right) + \frac{1}{2}\left(\cos(3x) + \cos(x)\right)\right] = \frac{1}{4}\left[\cos(9x) + \cos(7x) + \cos(3x) + \cos(x)\right]
\]

### Step 3: Integrate term-by-term
The integral simplifies to:
\[
\int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx = \frac{1}{4} \int_0^\pi \left[\cos(9x) + \cos(7x) + \cos(3x) + \cos(x)\right] dx
\]

Integrate each cosine term separately. For any integer \(k\), \(\int \cos(kx) \, dx = \frac{1}{k}\sin(kx) + C\). Evaluating from \(0\) to \(\pi\):
\[
\int_0^\pi \cos(kx) \, dx = \left.\frac{1}{k}\sin(kx)\right|_0^\pi = \frac{1}{k}\left[\sin(k\pi) - \sin(0)\right] = 0
\]
since \(\sin(k\pi) = 0\) for all integers \(k\).

### Step 4: Final result
All terms in the integral vanish, so:
\[
\int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx = \frac{1}{4}(0 + 0 + 0 + 0) = 0
\]

### Numerical Approximation
The exact result is \(0\), so the numerical approximation is \(0.0000000000\).

{"answer": "0", "numerical_answer": "0.0000000000"}