To solve the definite integral \(\int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx\), we will follow the steps outlined:

### Step 1: Analytical Computation

Consider the integral:
\[ I = \int_{0}^{\pi/2} \frac{\sin^{2n}x}{\sin^{2n}x + \cos^{2n}x} \, dx. \]

We can use the symmetry of the integrand by making the substitution \( u = \frac{\pi}{2} - x \). This transforms the integral as follows:
\[ I = \int_{0}^{\pi/2} \frac{\sin^{2n}x}{\sin^{2n}x + \cos^{2n}x} \, dx = \int_{0}^{\pi/2} \frac{\cos^{2n}u}{\cos^{2n}u + \sin^{2n}u} \, du. \]

Notice that the integrand is symmetric in \(\sin^{2n}x\) and \(\cos^{2n}x\). Therefore, we can write:
\[ I = \int_{0}^{\pi/2} \frac{\cos^{2n}x}{\cos^{2n}x + \sin^{2n}x} \, dx. \]

Adding these two expressions for \(I\), we get:
\[ 2I = \int_{0}^{\pi/2} \left( \frac{\sin^{2n}x}{\sin^{2n}x + \cos^{2n}x} + \frac{\cos^{2n}x}{\cos^{2n}x + \sin^{2n}x} \right) \, dx. \]

Since the sum of the fractions is 1, we have:
\[ 2I = \int_{0}^{\pi/2} 1 \, dx = \frac{\pi}{2}. \]

Thus,
\[ I = \frac{\pi}{4}. \]

### Step 2: Numerical Approximation

To provide a numerical approximation of \(\frac{\pi}{4}\), we use the known value of \(\pi \approx 3.141592653589793\):
\[ \frac{\pi}{4} \approx \frac{3.141592653589793}{4} \approx 0.7853981633974483. \]

Rounded to 10 decimal places, this is:
\[ 0.7853981634. \]

### Step 3: JSON Output

The final answer in the required JSON format is:
```json
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}
```