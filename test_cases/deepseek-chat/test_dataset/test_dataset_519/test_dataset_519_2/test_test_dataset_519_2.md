To compute the definite integral \(\int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx\), follow these steps:

### Step 1: Simplify the Integrand
First, observe that the denominator can be rewritten using the Pythagorean identity:
\[
2 - \cos^2(x) = 2 - (1 - \sin^2(x)) = 1 + \sin^2(x)
\]
Thus, the integral becomes:
\[
\int_0^{\pi/2} \frac{\cos(x)}{1 + \sin^2(x)} dx
\]

### Step 2: Substitute to Simplify
Let \( u = \sin(x) \). Then, \( du = \cos(x) dx \). The limits of integration change as follows:
- When \( x = 0 \), \( u = 0 \).
- When \( x = \pi/2 \), \( u = 1 \).

The integral transforms to:
\[
\int_0^1 \frac{1}{1 + u^2} du
\]

### Step 3: Evaluate the Integral
The integral \(\int \frac{1}{1 + u^2} du\) is a standard form, and its antiderivative is \(\arctan(u)\). Thus:
\[
\int_0^1 \frac{1}{1 + u^2} du = \arctan(1) - \arctan(0) = \frac{\pi}{4} - 0 = \frac{\pi}{4}
\]

### Step 4: Numerical Approximation
The numerical value of \(\frac{\pi}{4}\) is approximately:
\[
0.7853981634
\]

### Final Answer
The exact answer is \(\frac{\pi}{4}\), and its numerical approximation is \(0.7853981634\). 

Here is the result in the requested JSON format:
```json
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}
```