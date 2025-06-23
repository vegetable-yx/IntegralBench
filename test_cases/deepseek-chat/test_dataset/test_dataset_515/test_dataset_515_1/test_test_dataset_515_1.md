To compute the definite integral \(\int_1^\infty \frac{\log x}{x^2} \, dx\), we follow these steps:

### Step 1: Integration by Parts
We use integration by parts, which is given by:
\[
\int u \, dv = uv - \int v \, du.
\]
Let:
\[
u = \log x \quad \Rightarrow \quad du = \frac{1}{x} \, dx,
\]
\[
dv = \frac{1}{x^2} \, dx \quad \Rightarrow \quad v = -\frac{1}{x}.
\]
Applying integration by parts:
\[
\int \frac{\log x}{x^2} \, dx = -\frac{\log x}{x} - \int \left(-\frac{1}{x}\right) \cdot \frac{1}{x} \, dx = -\frac{\log x}{x} + \int \frac{1}{x^2} \, dx.
\]
The remaining integral is straightforward:
\[
\int \frac{1}{x^2} \, dx = -\frac{1}{x}.
\]
Thus, the antiderivative is:
\[
\int \frac{\log x}{x^2} \, dx = -\frac{\log x}{x} - \frac{1}{x} + C = -\frac{\log x + 1}{x} + C.
\]

### Step 2: Evaluate the Definite Integral
Now, evaluate from 1 to \(\infty\):
\[
\int_1^\infty \frac{\log x}{x^2} \, dx = \left[ -\frac{\log x + 1}{x} \right]_1^\infty.
\]
First, as \(x \to \infty\):
\[
\lim_{x \to \infty} \frac{\log x + 1}{x} = 0 \quad \text{(since \(\log x\) grows slower than any positive power of \(x\))}.
\]
At \(x = 1\):
\[
-\frac{\log 1 + 1}{1} = -1.
\]
Therefore:
\[
\int_1^\infty \frac{\log x}{x^2} \, dx = 0 - (-1) = 1.
\]

### Step 3: Numerical Approximation
The exact value is 1, so the numerical approximation is:
\[
1.0000000000.
\]

### Final Answer
```json
{"answer": "1", "numerical_answer": "1.0000000000"}
```