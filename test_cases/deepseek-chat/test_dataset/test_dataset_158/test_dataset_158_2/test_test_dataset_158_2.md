To solve the definite integral \(\int\limits_0^\infty x^{2-1}e^{-1.0x^2}H_2(1.0x)dx\), we follow these steps:

### Step 1: Simplify the Integral
The integral is:
\[
\int_0^\infty x e^{-x^2} H_2(x) \, dx
\]
where \(H_2(x)\) is the Hermite polynomial of degree 2. The Hermite polynomial \(H_2(x)\) is given by:
\[
H_2(x) = 4x^2 - 2
\]
Thus, the integrand becomes:
\[
x e^{-x^2} (4x^2 - 2) = 4x^3 e^{-x^2} - 2x e^{-x^2}
\]

### Step 2: Split the Integral
The integral can be split into two parts:
\[
\int_0^\infty x e^{-x^2} H_2(x) \, dx = 4 \int_0^\infty x^3 e^{-x^2} \, dx - 2 \int_0^\infty x e^{-x^2} \, dx
\]

### Step 3: Solve the First Integral \(\int_0^\infty x^3 e^{-x^2} \, dx\)
Let \(u = x^2\), then \(du = 2x \, dx\), and the integral becomes:
\[
\int_0^\infty x^3 e^{-x^2} \, dx = \frac{1}{2} \int_0^\infty u e^{-u} \, du
\]
The integral \(\int_0^\infty u e^{-u} \, du\) is the Gamma function \(\Gamma(2) = 1! = 1\). Thus:
\[
\int_0^\infty x^3 e^{-x^2} \, dx = \frac{1}{2} \times 1 = \frac{1}{2}
\]

### Step 4: Solve the Second Integral \(\int_0^\infty x e^{-x^2} \, dx\)
Again, let \(u = x^2\), then \(du = 2x \, dx\), and the integral becomes:
\[
\int_0^\infty x e^{-x^2} \, dx = \frac{1}{2} \int_0^\infty e^{-u} \, du = \frac{1}{2} \times 1 = \frac{1}{2}
\]

### Step 5: Combine the Results
Substituting the results back:
\[
4 \times \frac{1}{2} - 2 \times \frac{1}{2} = 2 - 1 = 1
\]

### Step 6: Numerical Approximation
The exact value is \(1\), so the numerical approximation is:
\[
1.0000000000
\]

### Final Answer
```json
{"answer": "1", "numerical_answer": "1.0000000000"}
```