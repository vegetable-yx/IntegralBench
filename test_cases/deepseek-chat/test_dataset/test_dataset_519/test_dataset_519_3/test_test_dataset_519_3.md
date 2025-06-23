To compute the definite integral \(\int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx\), follow these steps:

### Step 1: Simplify the Integrand
First, observe the denominator \(2 - \cos^2(x)\). Recall the Pythagorean identity \(\cos^2(x) = 1 - \sin^2(x)\). Substitute this into the denominator:
\[
2 - \cos^2(x) = 2 - (1 - \sin^2(x)) = 1 + \sin^2(x).
\]
Thus, the integrand becomes:
\[
\frac{\cos(x)}{1 + \sin^2(x)}.
\]

### Step 2: Perform a Substitution
Let \(u = \sin(x)\). Then, \(du = \cos(x) dx\). The integral transforms as follows:
- When \(x = 0\), \(u = 0\).
- When \(x = \pi/2\), \(u = 1\).
The integral becomes:
\[
\int_{0}^{1} \frac{du}{1 + u^2}.
\]

### Step 3: Evaluate the Simplified Integral
The integral \(\int \frac{du}{1 + u^2}\) is a standard form, and its antiderivative is \(\arctan(u)\). Thus:
\[
\int_{0}^{1} \frac{du}{1 + u^2} = \arctan(1) - \arctan(0) = \frac{\pi}{4} - 0 = \frac{\pi}{4}.
\]

### Step 4: Numerical Approximation
The exact value is \(\frac{\pi}{4}\). Numerically, this is approximately:
\[
\frac{\pi}{4} \approx 0.7853981634.
\]

### Final Answer
Here is the result in the requested JSON format:
```json
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}
```