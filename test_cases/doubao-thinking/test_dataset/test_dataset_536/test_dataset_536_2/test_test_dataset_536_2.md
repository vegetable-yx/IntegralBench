

To solve the definite integral \(\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\,dx\), we follow these steps:

### Step 1: Simplify the integrand using trigonometric identities
The product of cosine and sine can be simplified using the identity:
\[
\cos(A)\sin(B) = \frac{1}{2}\left[\sin(A+B) + \sin(B-A)\right]
\]
Here, \(A = 20x\) and \(B = 25x\). Substituting these values, we get:
\[
\cos(20x)\sin(25x) = \frac{1}{2}\left[\sin(45x) + \sin(5x)\right]
\]

### Step 2: Rewrite the integral
The original integral becomes:
\[
\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\,dx = \frac{1}{2}\int_{-\pi/2}^{\pi/2}\left[\sin(45x) + \sin(5x)\right]\,dx
\]

### Step 3: Evaluate the integral of each term
The integral of \(\sin(kx)\) is \(-\frac{1}{k}\cos(kx) + C\). We split the integral into two parts:
\[
\frac{1}{2}\left[\int_{-\pi/2}^{\pi/2}\sin(45x)\,dx + \int_{-\pi/2}^{\pi/2}\sin(5x)\,dx\right]
\]

#### First term: \(\int_{-\pi/2}^{\pi/2}\sin(45x)\,dx\)
\[
\int_{-\pi/2}^{\pi/2}\sin(45x)\,dx = \left[-\frac{1}{45}\cos(45x)\right]_{-\pi/2}^{\pi/2}
\]
Evaluating at the bounds:
\[
-\frac{1}{45}\left[\cos\left(45 \cdot \frac{\pi}{2}\right) - \cos\left(45 \cdot \left(-\frac{\pi}{2}\right)\right)\right]
\]
Since \(\cos\left(\frac{45\pi}{2}\right) = \cos\left(22\pi + \frac{\pi}{2}\right) = \cos\left(\frac{\pi}{2}\right) = 0\) and \(\cos\left(-\frac{45\pi}{2}\right) = \cos\left(\frac{45\pi}{2}\right) = 0\), the first term simplifies to \(0\).

#### Second term: \(\int_{-\pi/2}^{\pi/2}\sin(5x)\,dx\)
\[
\int_{-\pi/2}^{\pi/2}\sin(5x)\,dx = \left[-\frac{1}{5}\cos(5x)\right]_{-\pi/2}^{\pi/2}
\]
Evaluating at the bounds:
\[
-\frac{1}{5}\left[\cos\left(5 \cdot \frac{\pi}{2}\right) - \cos\left(5 \cdot \left(-\frac{\pi}{2}\right)\right)\right]
\]
Since \(\cos\left(\frac{5\pi}{2}\right) = \cos\left(2\pi + \frac{\pi}{2}\right) = \cos\left(\frac{\pi}{2}\right) = 0\) and \(\cos\left(-\frac{5\pi}{2}\right) = \cos\left(\frac{5\pi}{2}\right) = 0\), the second term also simplifies to \(0\).

### Step 4: Combine results
Both terms are \(0\), so the integral evaluates to \(0\).

### Step 5: Numerical approximation
The exact result is \(0\), so the numerical approximation (rounded to 10 decimal places) is \(0.0000000000\).

{"answer": "0", "numerical_answer": "0.0000000000"}