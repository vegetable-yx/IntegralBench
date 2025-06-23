To solve the definite integral 

\[
\int\limits_0^\infty x^{2-1}e^{-1.0x^2}H_2(1.0x)dx,
\]

we follow these steps:

### Step 1: Simplify the Integral
First, note that \( x^{2-1} = x \), and the Hermite polynomial \( H_2(y) \) is given by:

\[
H_2(y) = 4y^2 - 2.
\]

Substituting \( y = 1.0x \), we have:

\[
H_2(1.0x) = 4(1.0x)^2 - 2 = 4x^2 - 2.
\]

Thus, the integral becomes:

\[
\int\limits_0^\infty x e^{-x^2} (4x^2 - 2) dx.
\]

### Step 2: Expand the Integrand
Expand the integrand:

\[
x e^{-x^2} (4x^2 - 2) = 4x^3 e^{-x^2} - 2x e^{-x^2}.
\]

So, the integral splits into two parts:

\[
\int\limits_0^\infty 4x^3 e^{-x^2} dx - \int\limits_0^\infty 2x e^{-x^2} dx.
\]

### Step 3: Solve the Integrals
#### First Integral: \( \int\limits_0^\infty 4x^3 e^{-x^2} dx \)
Let \( u = x^2 \), then \( du = 2x dx \), and the integral becomes:

\[
\int\limits_0^\infty 4x^3 e^{-x^2} dx = 2 \int\limits_0^\infty u e^{-u} du.
\]

This is a gamma function integral:

\[
2 \int\limits_0^\infty u e^{-u} du = 2 \Gamma(2) = 2 \times 1! = 2.
\]

#### Second Integral: \( \int\limits_0^\infty 2x e^{-x^2} dx \)
Similarly, let \( u = x^2 \), then \( du = 2x dx \), and the integral becomes:

\[
\int\limits_0^\infty 2x e^{-x^2} dx = \int\limits_0^\infty e^{-u} du = 1.
\]

### Step 4: Combine the Results
Subtract the second integral from the first:

\[
2 - 1 = 1.
\]

### Step 5: Numerical Approximation
The exact value is \( 1 \), so the numerical approximation is:

\[
1.0000000000.
\]

### Final Answer
```json
{"answer": "1", "numerical_answer": "1.0000000000"}
```