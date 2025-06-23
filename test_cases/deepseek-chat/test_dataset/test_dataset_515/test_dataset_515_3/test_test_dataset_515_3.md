To compute the definite integral \(\int_1^\infty \frac{\log x}{x^2} \, dx\), we follow these steps:

### Step 1: Compute the integral analytically

We use integration by parts, where:
- \(u = \log x \Rightarrow du = \frac{1}{x} \, dx\)
- \(dv = \frac{1}{x^2} \, dx \Rightarrow v = -\frac{1}{x}\)

Applying integration by parts:
\[
\int \frac{\log x}{x^2} \, dx = -\frac{\log x}{x} + \int \frac{1}{x^2} \, dx = -\frac{\log x}{x} - \frac{1}{x} + C
\]

Now, evaluate the definite integral from 1 to \(\infty\):
\[
\int_1^\infty \frac{\log x}{x^2} \, dx = \left[ -\frac{\log x}{x} - \frac{1}{x} \right]_1^\infty
\]

Evaluate the limits:
- As \(x \to \infty\):
  \[
  \lim_{x \to \infty} \left( -\frac{\log x}{x} - \frac{1}{x} \right) = 0 - 0 = 0
  \]
- At \(x = 1\):
  \[
  -\frac{\log 1}{1} - \frac{1}{1} = -0 - 1 = -1
  \]

Thus:
\[
\int_1^\infty \frac{\log x}{x^2} \, dx = 0 - (-1) = 1
\]

### Step 2: Numerical approximation

The exact value is 1, so the numerical approximation is:
\[
1.0000000000
\]

### Final Answer

```json
{"answer": "1", "numerical_answer": "1.0000000000"}
```