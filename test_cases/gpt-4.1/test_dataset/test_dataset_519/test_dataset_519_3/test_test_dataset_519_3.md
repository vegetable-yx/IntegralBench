Let's evaluate the given integral:
\[
I = \int_0^{\pi/2} \frac{\cos(x)}{2 - \cos^2(x)} \, dx
\]

### 1. Substitution

Let’s use the substitution:
\[
u = \sin(x), \quad du = \cos(x) dx
\]
When \(x = 0\), \(u = 0\). When \(x = \frac{\pi}{2}\), \(u = 1\).

The denominator:
\[
2 - \cos^2(x) = 2 - (1 - \sin^2(x)) = 2 - 1 + \sin^2(x) = 1 + \sin^2(x)
\]

Therefore, the integral becomes:
\[
I = \int_0^1 \frac{du}{1 + u^2}
\]

### 2. Integration

The integral of \(\frac{1}{1+u^2}\) is \(\arctan(u)\):

\[
I = \left. \arctan(u) \right|_0^1 = \arctan(1) - \arctan(0)
\]

\[
\arctan(1) = \frac{\pi}{4}, \quad \arctan(0) = 0
\]
So:
\[
I = \frac{\pi}{4}
\]

### 3. Numerical Approximation

\[
\frac{\pi}{4} \approx 0.7853981634
\]

### 4. JSON Output

```json
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}
```