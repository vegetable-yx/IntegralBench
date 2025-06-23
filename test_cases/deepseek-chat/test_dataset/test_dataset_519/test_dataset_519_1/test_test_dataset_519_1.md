To compute the definite integral \(\int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx\), we follow these steps:

### Step 1: Simplify the Integrand
First, observe the denominator:
\[
2 - \cos^2(x) = 2 - (1 - \sin^2(x)) = 1 + \sin^2(x).
\]
So the integrand becomes:
\[
\frac{\cos(x)}{1 + \sin^2(x)}.
\]

### Step 2: Substitute to Simplify
Let \(u = \sin(x)\). Then \(du = \cos(x) dx\), and the integral transforms as follows:
\[
\int_0^{\pi/2} \frac{\cos(x)}{1 + \sin^2(x)} dx = \int_{0}^{1} \frac{du}{1 + u^2}.
\]

### Step 3: Evaluate the Simplified Integral
The integral \(\int \frac{du}{1 + u^2}\) is a standard form:
\[
\int \frac{du}{1 + u^2} = \arctan(u) + C.
\]
Evaluating from 0 to 1:
\[
\arctan(1) - \arctan(0) = \frac{\pi}{4} - 0 = \frac{\pi}{4}.
\]

### Step 4: Numerical Approximation
The exact answer is \(\frac{\pi}{4}\). Numerically, this is approximately:
\[
\frac{\pi}{4} \approx 0.7853981634.
\]

### Final Answer
```json
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}
```