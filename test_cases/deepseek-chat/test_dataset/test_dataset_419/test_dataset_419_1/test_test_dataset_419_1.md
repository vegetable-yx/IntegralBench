To compute the definite integral \(\int_0^\infty \frac{x}{e^x - 1} \, dx\), we can proceed with the following steps:

### Step 1: Express the integrand as a series
The integrand \(\frac{x}{e^x - 1}\) can be expressed using the geometric series expansion for \(\frac{1}{e^x - 1}\):
\[
\frac{1}{e^x - 1} = \sum_{n=1}^\infty e^{-nx} \quad \text{for} \quad x > 0.
\]
Thus, the integrand becomes:
\[
\frac{x}{e^x - 1} = x \sum_{n=1}^\infty e^{-nx} = \sum_{n=1}^\infty x e^{-nx}.
\]

### Step 2: Integrate term by term
Now, we can integrate term by term:
\[
\int_0^\infty \frac{x}{e^x - 1} \, dx = \sum_{n=1}^\infty \int_0^\infty x e^{-nx} \, dx.
\]
Each integral in the sum can be evaluated using integration by parts or by recognizing it as the integral defining the gamma function \(\Gamma(2)\):
\[
\int_0^\infty x e^{-nx} \, dx = \frac{1}{n^2} \int_0^\infty u e^{-u} \, du = \frac{1}{n^2} \Gamma(2) = \frac{1}{n^2},
\]
since \(\Gamma(2) = 1! = 1\).

### Step 3: Sum the series
The integral now becomes:
\[
\int_0^\infty \frac{x}{e^x - 1} \, dx = \sum_{n=1}^\infty \frac{1}{n^2} = \zeta(2),
\]
where \(\zeta(s)\) is the Riemann zeta function. The value of \(\zeta(2)\) is known to be:
\[
\zeta(2) = \frac{\pi^2}{6}.
\]

### Step 4: Numerical approximation
The numerical value of \(\frac{\pi^2}{6}\) is approximately:
\[
\frac{\pi^2}{6} \approx 1.6449340668.
\]

### Final Answer
The exact answer is \(\frac{\pi^2}{6}\), and the numerical approximation is \(1.6449340668\).

```json
{"answer": "\\frac{\\pi^2}{6}", "numerical_answer": "1.6449340668"}
```