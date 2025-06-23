

To solve the definite integral \(\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\,dx\), we can use trigonometric identities and properties of odd functions.

### Step 1: Simplify the integrand using a product-to-sum identity
The product of cosine and sine can be simplified using the identity:
\[
\cos(A)\sin(B) = \frac{1}{2}\left[\sin(A+B) + \sin(B-A)\right]
\]
Here, \(A = 20x\) and \(B = 25x\). Substituting these values, we get:
\[
\cos(20x)\sin(25x) = \frac{1}{2}\left[\sin(45x) + \sin(5x)\right]
\]

### Step 2: Rewrite the integral
The integral becomes:
\[
\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\,dx = \frac{1}{2}\int_{-\pi/2}^{\pi/2}\left[\sin(45x) + \sin(5x)\right]\,dx
\]

### Step 3: Split the integral into two parts
\[
\frac{1}{2}\left[\int_{-\pi/2}^{\pi/2}\sin(45x)\,dx + \int_{-\pi/2}^{\pi/2}\sin(5x)\,dx\right]
\]

### Step 4: Evaluate each integral
The integral of \(\sin(kx)\) over \([-a, a]\) is:
\[
\int_{-a}^{a}\sin(kx)\,dx = \left[-\frac{\cos(kx)}{k}\right]_{-a}^{a} = -\frac{\cos(ka)}{k} + \frac{\cos(-ka)}{k}
\]
Since \(\cos(-ka) = \cos(ka)\), this simplifies to:
\[
-\frac{\cos(ka)}{k} + \frac{\cos(ka)}{k} = 0
\]
Thus, both \(\int_{-\pi/2}^{\pi/2}\sin(45x)\,dx\) and \(\int_{-\pi/2}^{\pi/2}\sin(5x)\,dx\) equal \(0\).

### Step 5: Conclusion
The original integral simplifies to:
\[
\frac{1}{2}(0 + 0) = 0
\]

### Numerical Approximation
The exact value is \(0\), so the numerical approximation to 10 decimal places is \(0.0000000000\).

{"answer": "0", "numerical_answer": "0.0000000000"}