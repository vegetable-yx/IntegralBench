To solve the definite integral \(\int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx\), we will follow the steps outlined:

### Step 1: Analytical Computation

Consider the integral:
\[ I = \int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx. \]

We can use the symmetry of the integrand by making the substitution \( u = \frac{\pi}{2} - x \). This transforms the integral as follows:
\[ I = \int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx = \int\limits_{0}^{\pi/2}\frac{\cos^{2n}u}{\cos^{2n}u+\sin^{2n}u}\:du. \]

Notice that the integrand is symmetric with respect to \( x \) and \( \frac{\pi}{2} - x \). Therefore, we can write:
\[ I = \int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx = \int\limits_{0}^{\pi/2}\frac{\cos^{2n}x}{\cos^{2n}x+\sin^{2n}x}\:dx. \]

Adding these two integrals, we get:
\[ 2I = \int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx + \int\limits_{0}^{\pi/2}\frac{\cos^{2n}x}{\cos^{2n}x+\sin^{2n}x}\:dx. \]

Since the sum of the integrands is 1, we have:
\[ 2I = \int\limits_{0}^{\pi/2} 1 \:dx = \frac{\pi}{2}. \]

Thus,
\[ I = \frac{\pi}{4}. \]

### Step 2: Numerical Approximation

To provide a numerical approximation, we can use the exact result:
\[ I = \frac{\pi}{4}. \]

Using a calculator or a numerical tool, we find:
\[ \frac{\pi}{4} \approx 0.7853981634. \]

### Step 3: JSON Output

The final answer in the required JSON format is:
```json
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}
```