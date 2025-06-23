To compute the definite integral \(\int_{-1}^1 \frac{1}{3^x + 1} \, \mathrm{d}x\), we can proceed with the following steps:

### Step 1: Simplify the Integral
Let \( I = \int_{-1}^1 \frac{1}{3^x + 1} \, \mathrm{d}x \).

We can use the substitution \( u = -x \), which implies \( \mathrm{d}u = -\mathrm{d}x \). When \( x = -1 \), \( u = 1 \), and when \( x = 1 \), \( u = -1 \). Thus, the integral becomes:
\[
I = \int_{1}^{-1} \frac{1}{3^{-u} + 1} (-\mathrm{d}u) = \int_{-1}^1 \frac{1}{3^{-u} + 1} \, \mathrm{d}u.
\]

Notice that \( \frac{1}{3^{-u} + 1} = \frac{3^u}{1 + 3^u} \). Therefore, we can write:
\[
I = \int_{-1}^1 \frac{3^u}{1 + 3^u} \, \mathrm{d}u.
\]

### Step 2: Add the Original and Transformed Integrals
Now, add the original integral \( I \) and the transformed integral:
\[
2I = \int_{-1}^1 \left( \frac{1}{3^x + 1} + \frac{3^x}{3^x + 1} \right) \, \mathrm{d}x = \int_{-1}^1 \frac{1 + 3^x}{3^x + 1} \, \mathrm{d}x = \int_{-1}^1 1 \, \mathrm{d}x.
\]

This simplifies to:
\[
2I = \int_{-1}^1 1 \, \mathrm{d}x = 2.
\]

### Step 3: Solve for \( I \)
Divide both sides by 2:
\[
I = 1.
\]

### Step 4: Numerical Approximation
The exact value of the integral is \( 1 \), so the numerical approximation is:
\[
1.0000000000
\]

### Final Answer
```json
{"answer": "1", "numerical_answer": "1.0000000000"}
```