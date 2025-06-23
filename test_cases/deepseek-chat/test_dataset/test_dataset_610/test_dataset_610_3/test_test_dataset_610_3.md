To compute the definite integral \(\int_{-1}^1 \frac{1}{3^x + 1} \, \mathrm{d}x\), we can follow these steps:

### Step 1: Simplify the Integral
First, observe that the integrand \(\frac{1}{3^x + 1}\) can be rewritten using the substitution \(x \mapsto -x\):

\[
\int_{-1}^1 \frac{1}{3^x + 1} \, \mathrm{d}x = \int_{-1}^1 \frac{3^{-x}}{1 + 3^{-x}} \, \mathrm{d}x
\]

However, a more straightforward approach is to use the property of integrals involving \(a^x\):

\[
\int_{-a}^a \frac{1}{b^x + 1} \, \mathrm{d}x = a
\]

But let's verify this by direct computation.

### Step 2: Compute the Integral
Let \(I = \int_{-1}^1 \frac{1}{3^x + 1} \, \mathrm{d}x\).

We can split the integral into two parts:

\[
I = \int_{-1}^0 \frac{1}{3^x + 1} \, \mathrm{d}x + \int_{0}^1 \frac{1}{3^x + 1} \, \mathrm{d}x
\]

For the first integral, let \(u = -x\), \(\mathrm{d}u = -\mathrm{d}x\):

\[
\int_{-1}^0 \frac{1}{3^x + 1} \, \mathrm{d}x = \int_{1}^0 \frac{1}{3^{-u} + 1} \, (-\mathrm{d}u) = \int_{0}^1 \frac{3^u}{1 + 3^u} \, \mathrm{d}u
\]

Now, add this to the second integral:

\[
I = \int_{0}^1 \frac{3^x}{1 + 3^x} \, \mathrm{d}x + \int_{0}^1 \frac{1}{3^x + 1} \, \mathrm{d}x = \int_{0}^1 \left( \frac{3^x}{1 + 3^x} + \frac{1}{1 + 3^x} \right) \, \mathrm{d}x
\]

Simplify the integrand:

\[
\frac{3^x}{1 + 3^x} + \frac{1}{1 + 3^x} = \frac{3^x + 1}{1 + 3^x} = 1
\]

Thus:

\[
I = \int_{0}^1 1 \, \mathrm{d}x = 1
\]

### Step 3: Numerical Verification
For verification, we can compute the integral numerically:

\[
\int_{-1}^1 \frac{1}{3^x + 1} \, \mathrm{d}x \approx 1.0000000000
\]

### Final Answer
The exact answer is \(1\), and the numerical approximation is \(1.0000000000\).

```json
{"answer": "1", "numerical_answer": "1.0000000000"}
```