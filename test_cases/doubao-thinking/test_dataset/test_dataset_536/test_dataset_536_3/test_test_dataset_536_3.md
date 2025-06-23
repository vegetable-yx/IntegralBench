

To solve the definite integral \(\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\,dx\), we follow these steps:

### Step 1: Simplify the integrand using trigonometric identities
We use the product-to-sum identity for \(\cos(A)\sin(B)\):
\[
\cos(A)\sin(B) = \frac{1}{2}\left[\sin(A+B) + \sin(B-A)\right]
\]
Here, \(A = 20x\) and \(B = 25x\), so:
\[
\cos(20x)\sin(25x) = \frac{1}{2}\left[\sin(45x) + \sin(5x)\right]
\]

### Step 2: Rewrite the integral
The integral becomes:
\[
\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\,dx = \frac{1}{2}\int_{-\pi/2}^{\pi/2}\left[\sin(45x) + \sin(5x)\right]\,dx
\]

### Step 3: Split the integral and integrate term-by-term
We split the integral into two parts:
\[
\frac{1}{2}\left[\int_{-\pi/2}^{\pi/2}\sin(45x)\,dx + \int_{-\pi/2}^{\pi/2}\sin(5x)\,dx\right]
\]

### Step 4: Evaluate each integral
The antiderivative of \(\sin(kx)\) is \(-\frac{1}{k}\cos(kx)\). For the first integral (\(k=45\)):
\[
\int_{-\pi/2}^{\pi/2}\sin(45x)\,dx = \left[-\frac{1}{45}\cos(45x)\right]_{-\pi/2}^{\pi/2}
\]
Evaluating at the bounds:
\[
-\frac{1}{45}\left[\cos\left(45 \cdot \frac{\pi}{2}\right) - \cos\left(45 \cdot \left(-\frac{\pi}{2}\right)\right)\right]
\]
Since \(\cos\left(\frac{45\pi}{2}\right) = \cos\left(22\pi + \frac{\pi}{2}\right) = \cos\left(\frac{\pi}{2}\right) = 0\) and \(\cos\left(-\frac{45\pi}{2}\right) = \cos\left(\frac{45\pi}{2}\right) = 0\), this term is \(0\).

For the second integral (\(k=5\)):
\[
\int_{-\pi/2}^{\pi/2}\sin(5x)\,dx = \left[-\frac{1}{5}\cos(5x)\right]_{-\pi/2}^{\pi/2}
\]
Evaluating at the bounds:
\[
-\frac{1}{5}\left[\cos\left(5 \cdot \frac{\pi}{2}\right) - \cos\left(5 \cdot \left(-\frac{\pi}{2}\right)\right)\right]
\]
Since \(\cos\left(\frac{5\pi}{2}\right) = \cos\left(2\pi + \frac{\pi}{2}\right) = \cos\left(\frac{\pi}{2}\right) = 0\) and \(\cos\left(-\frac{5\pi}{2}\right) = \cos\left(\frac{5\pi}{2}\right) = 0\), this term is also \(0\).

### Step 5: Combine results
Both integrals evaluate to \(0\), so:
\[
\frac{1}{2}\left[0 + 0\right] = 0
\]

### Step 6: Numerical approximation
The exact result is \(0\), so the numerical approximation is \(0.0000000000\) (rounded to 10 decimal places).

{"answer": "0", "numerical_answer": "0.0000000000"}