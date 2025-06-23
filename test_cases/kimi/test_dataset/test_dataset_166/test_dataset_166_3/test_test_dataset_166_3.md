To solve the definite integral \(\int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx\), we will follow the steps outlined:

### Step 1: Analytical Computation

Consider the integral:
\[ I = \int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx. \]

We can use the symmetry of the sine and cosine functions over the interval \([0, \pi/2]\). Notice that:
\[ \int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx = \int\limits_{0}^{\pi/2}\frac{\cos^{2n}x}{\cos^{2n}x+\sin^{2n}x}\:dx. \]

Let's denote the second integral as \( J \):
\[ J = \int\limits_{0}^{\pi/2}\frac{\cos^{2n}x}{\cos^{2n}x+\sin^{2n}x}\:dx. \]

Adding \( I \) and \( J \):
\[ I + J = \int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx + \int\limits_{0}^{\pi/2}\frac{\cos^{2n}x}{\cos^{2n}x+\sin^{2n}x}\:dx. \]

Since the integrands sum to 1:
\[ I + J = \int\limits_{0}^{\pi/2} 1 \:dx = \frac{\pi}{2}. \]

Given that \( I = J \), we have:
\[ 2I = \frac{\pi}{2} \implies I = \frac{\pi}{4}. \]

### Step 2: Numerical Approximation

To provide a numerical approximation, we can use the exact result:
\[ I = \frac{\pi}{4}. \]

Using the value of \(\pi \approx 3.141592653589793\):
\[ \frac{\pi}{4} \approx 0.7853981633974483. \]

### Step 3: JSON Output

The final answer in the required JSON format is:
```json
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}
```