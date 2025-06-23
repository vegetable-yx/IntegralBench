To compute the definite integral \(\int_{-1}^1 \frac{1}{3^x + 1} \, \mathrm{d}x\), we can follow these steps:

### Step 1: Simplify the Integral
Let’s consider the integral:
\[
I = \int_{-1}^1 \frac{1}{3^x + 1} \, \mathrm{d}x
\]

We can use the substitution \( u = -x \), which implies \( \mathrm{d}u = -\mathrm{d}x \). When \( x = -1 \), \( u = 1 \), and when \( x = 1 \), \( u = -1 \). The integral becomes:
\[
I = \int_{1}^{-1} \frac{1}{3^{-u} + 1} \, (-\mathrm{d}u) = \int_{-1}^1 \frac{1}{3^{-u} + 1} \, \mathrm{d}u
\]

Notice that \( \frac{1}{3^{-u} + 1} = \frac{3^u}{1 + 3^u} \). Therefore:
\[
I = \int_{-1}^1 \frac{3^u}{1 + 3^u} \, \mathrm{d}u
\]

### Step 2: Add the Original and Transformed Integrals
Now, add the original integral \( I \) and the transformed integral \( I \):
\[
2I = \int_{-1}^1 \frac{1}{3^x + 1} \, \mathrm{d}x + \int_{-1}^1 \frac{3^x}{1 + 3^x} \, \mathrm{d}x = \int_{-1}^1 \left( \frac{1}{3^x + 1} + \frac{3^x}{1 + 3^x} \right) \, \mathrm{d}x
\]

Simplify the integrand:
\[
\frac{1}{3^x + 1} + \frac{3^x}{1 + 3^x} = \frac{1 + 3^x}{1 + 3^x} = 1
\]

Thus:
\[
2I = \int_{-1}^1 1 \, \mathrm{d}x = 2
\]

### Step 3: Solve for \( I \)
\[
2I = 2 \implies I = 1
\]

### Step 4: Numerical Approximation
The exact value of the integral is \( 1 \), so the numerical approximation is also:
\[
1.0000000000
\]

### Final Answer
```json
{"answer": "1", "numerical_answer": "1.0000000000"}
```