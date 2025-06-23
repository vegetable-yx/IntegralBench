To compute the definite integral \(\int_{0}^{1} \left( \frac{1}{x} - \left\lfloor \frac{1}{x} \right\rfloor \right) \mathrm{d}x\), we proceed with the following steps:

### Step 1: Change of Variables
Let \( u = \frac{1}{x} \). Then, \( x = \frac{1}{u} \) and \( \mathrm{d}x = -\frac{1}{u^2} \mathrm{d}u \). The limits change as follows:
- When \( x \to 0^+ \), \( u \to +\infty \).
- When \( x = 1 \), \( u = 1 \).

The integral becomes:
\[
\int_{+\infty}^{1} \left( u - \lfloor u \rfloor \right) \left( -\frac{1}{u^2} \right) \mathrm{d}u = \int_{1}^{+\infty} \frac{u - \lfloor u \rfloor}{u^2} \mathrm{d}u.
\]

### Step 2: Break the Integral into Intervals
The integrand \( \frac{u - \lfloor u \rfloor}{u^2} \) is periodic with period 1 on each interval \( [n, n+1) \), where \( n \) is a positive integer. Thus, we can write:
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
\ln(n+1) + \frac{n}{n+1} - \ln n - 1 = \ln\left(1 + \frac{1}{n}\right) + \frac{n}{n+1} - 1.
\]

### Step 4: Sum the Series
The integral becomes:
\[
\sum_{n=1}^{\infty} \left( \ln\left(1 + \frac{1}{n}\right) + \frac{n}{n+1} - 1 \right).
\]
Simplify each term:
\[
\ln\left(1 + \frac{1}{n}\right) = \ln(n+1) - \ln n,
\]
\[
\frac{n}{n+1} - 1 = -\frac{1}{n+1}.
\]
Thus, the sum telescopes:
\[
\sum_{n=1}^{\infty} \left( \ln(n+1) - \ln n - \frac{1}{n+1} \right) = \lim_{N \to \infty} \left( \ln(N+1) - \sum_{k=2}^{N+1} \frac{1}{k} \right).
\]
Using the asymptotic expansion of the harmonic series:
\[
\sum_{k=1}^{N} \frac{1}{k} = \ln N + \gamma + o(1),
\]
where \( \gamma \) is the Euler-Mascheroni constant, we find:
\[
\lim_{N \to \infty} \left( \ln(N+1) - (\ln(N+1) + \gamma - 1 + o(1)) \right) = 1 - \gamma.
\]

### Step 5: Numerical Approximation
The Euler-Mascheroni constant \( \gamma \approx 0.5772156649 \), so:
\[
1 - \gamma \approx 0.4227843351.
\]

### Final Answer
The exact answer is \( 1 - \gamma \), and the numerical approximation is \( 0.4227843351 \).

```json
{"answer": "1 - \\gamma", "numerical_answer": "0.4227843351"}
```