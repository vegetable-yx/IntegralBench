To compute the definite integral \(\int_{0}^{1} \left( \frac{1}{x} - \left\lfloor \frac{1}{x} \right\rfloor \right) \mathrm{d}x\), we proceed with the following steps:

### Step 1: Substitution
Let \( u = \frac{1}{x} \). Then, \( x = \frac{1}{u} \) and \( \mathrm{d}x = -\frac{1}{u^2} \mathrm{d}u \). The limits change as follows:
- When \( x = 0^+ \), \( u \to +\infty \).
- When \( x = 1 \), \( u = 1 \).

The integral becomes:
\[
\int_{+\infty}^{1} \left( u - \lfloor u \rfloor \right) \left( -\frac{1}{u^2} \right) \mathrm{d}u = \int_{1}^{+\infty} \frac{u - \lfloor u \rfloor}{u^2} \mathrm{d}u.
\]

### Step 2: Break into Intervals
The integrand \( \frac{u - \lfloor u \rfloor}{u^2} \) is periodic with period 1. We can break the integral into a sum over intervals \([n, n+1)\) for \( n \in \mathbb{N} \):
\[
\int_{1}^{+\infty} \frac{u - \lfloor u \rfloor}{u^2} \mathrm{d}u = \sum_{n=1}^{\infty} \int_{n}^{n+1} \frac{u - n}{u^2} \mathrm{d}u.
\]

### Step 3: Compute Each Interval Integral
For each \( n \), compute:
\[
\int_{n}^{n+1} \frac{u - n}{u^2} \mathrm{d}u = \int_{n}^{n+1} \left( \frac{1}{u} - \frac{n}{u^2} \right) \mathrm{d}u = \left[ \ln u + \frac{n}{u} \right]_{n}^{n+1}.
\]
Evaluating this:
\[
\left( \ln(n+1) + \frac{n}{n+1} \right) - \left( \ln n + 1 \right) = \ln\left(1 + \frac{1}{n}\right) + \frac{n}{n+1} - 1.
\]
Simplify:
\[
\ln\left(1 + \frac{1}{n}\right) - \frac{1}{n+1}.
\]

### Step 4: Sum the Series
The integral becomes:
\[
\sum_{n=1}^{\infty} \left( \ln\left(1 + \frac{1}{n}\right) - \frac{1}{n+1} \right).
\]
This is a telescoping series for the logarithmic terms:
\[
\sum_{n=1}^{\infty} \ln\left(1 + \frac{1}{n}\right) = \ln \left( \prod_{n=1}^{\infty} \left(1 + \frac{1}{n}\right) \right) = \ln \left( \lim_{N \to \infty} \frac{N+1}{1} \right) = \ln \left( +\infty \right) = +\infty.
\]
However, the combined series converges because the negative terms \( -\sum_{n=1}^{\infty} \frac{1}{n+1} \) offset the divergence. Instead, we recognize that:
\[
\sum_{n=1}^{\infty} \left( \ln\left(1 + \frac{1}{n}\right) - \frac{1}{n} \right) + \sum_{n=1}^{\infty} \left( \frac{1}{n} - \frac{1}{n+1} \right).
\]
The first sum converges to \( -\gamma \) (Euler's constant), and the second sum telescopes to 1. Thus:
\[
-\gamma + 1.
\]

### Step 5: Final Answer
The exact value of the integral is:
\[
1 - \gamma,
\]
where \( \gamma \) is the Euler-Mascheroni constant.

### Numerical Approximation
The numerical value of \( 1 - \gamma \) is approximately:
\[
1 - 0.5772156649 \approx 0.4227843351.
\]

### JSON Output
```json
{"answer": "1 - \\gamma", "numerical_answer": "0.4227843351"}
```