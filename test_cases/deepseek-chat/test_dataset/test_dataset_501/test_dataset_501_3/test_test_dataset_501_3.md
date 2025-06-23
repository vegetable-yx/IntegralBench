To compute the definite integral \(\int_0^1 \sin^2(\log x) \, dx\), we follow these steps:

### Step 1: Substitution
Let \( u = \log x \). Then, \( x = e^u \) and \( dx = e^u \, du \). When \( x = 0 \), \( u = -\infty \), and when \( x = 1 \), \( u = 0 \). The integral becomes:
\[
\int_{-\infty}^0 \sin^2(u) \cdot e^u \, du.
\]

### Step 2: Simplify the Integrand
Using the identity \(\sin^2(u) = \frac{1 - \cos(2u)}{2}\), the integral becomes:
\[
\frac{1}{2} \int_{-\infty}^0 (1 - \cos(2u)) e^u \, du = \frac{1}{2} \left( \int_{-\infty}^0 e^u \, du - \int_{-\infty}^0 \cos(2u) e^u \, du \right).
\]

### Step 3: Evaluate the First Integral
The first integral is straightforward:
\[
\int_{-\infty}^0 e^u \, du = \left. e^u \right|_{-\infty}^0 = 1 - 0 = 1.
\]

### Step 4: Evaluate the Second Integral
The second integral involves \(\cos(2u) e^u\). We use integration by parts twice or recognize it as a standard form. The antiderivative is:
\[
\int \cos(2u) e^u \, du = \frac{e^u (\sin(2u) + 2\cos(2u))}{5} + C.
\]
Evaluating from \(-\infty\) to \(0\):
\[
\left. \frac{e^u (\sin(2u) + 2\cos(2u))}{5} \right|_{-\infty}^0 = \frac{2}{5} - 0 = \frac{2}{5}.
\]

### Step 5: Combine Results
Substituting back:
\[
\frac{1}{2} \left( 1 - \frac{2}{5} \right) = \frac{1}{2} \cdot \frac{3}{5} = \frac{3}{10}.
\]

### Step 6: Numerical Approximation
The exact value is \(\frac{3}{10}\), which numerically is \(0.3\).

### Final Answer
```json
{"answer": "\\frac{3}{10}", "numerical_answer": "0.3000000000"}
```