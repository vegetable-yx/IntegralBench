

To calculate the definite integral \(\int_0^\infty \frac{x}{e^x - 1} \, dx\), we proceed as follows:

### Step 1: Series Expansion of the Integrand
The integrand \(\frac{1}{e^x - 1}\) can be expressed as a geometric series for \(x > 0\). Since \(e^x > 1\), we have:
\[
\frac{1}{e^x - 1} = \frac{e^{-x}}{1 - e^{-x}} = \sum_{n=1}^\infty e^{-nx}
\]
This is a convergent geometric series with common ratio \(e^{-x}\) (since \(|e^{-x}| < 1\) for \(x > 0\)).

### Step 2: Interchange Sum and Integral
Substituting the series into the integral, we get:
\[
\int_0^\infty \frac{x}{e^x - 1} \, dx = \int_0^\infty x \sum_{n=1}^\infty e^{-nx} \, dx
\]
By the Monotone Convergence Theorem (justified because the terms are non-negative), we interchange the sum and integral:
\[
\int_0^\infty x \sum_{n=1}^\infty e^{-nx} \, dx = \sum_{n=1}^\infty \int_0^\infty x e^{-nx} \, dx
\]

### Step 3: Evaluate the Inner Integral
The inner integral \(\int_0^\infty x e^{-nx} \, dx\) is a standard gamma function integral. Recall that \(\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt\). Let \(t = nx\), so \(x = \frac{t}{n}\) and \(dx = \frac{dt}{n}\). Substituting:
\[
\int_0^\infty x e^{-nx} \, dx = \int_0^\infty \frac{t}{n} e^{-t} \cdot \frac{dt}{n} = \frac{1}{n^2} \int_0^\infty t e^{-t} \, dt
\]
The integral \(\int_0^\infty t e^{-t} \, dt = \Gamma(2) = 1! = 1\). Thus:
\[
\int_0^\infty x e^{-nx} \, dx = \frac{1}{n^2}
\]

### Step 4: Sum the Series
The original integral reduces to the sum of \(\frac{1}{n^2}\) over \(n \geq 1\):
\[
\sum_{n=1}^\infty \frac{1}{n^2} = \zeta(2)
\]
where \(\zeta(s)\) is the Riemann zeta function. It is known that \(\zeta(2) = \frac{\pi^2}{6}\).

### Numerical Approximation
The exact value is \(\frac{\pi^2}{6}\). Numerically, \(\pi \approx 3.141592653589793\), so \(\pi^2 \approx 9.869604401089358\). Thus:
\[
\frac{\pi^2}{6} \approx \frac{9.869604401089358}{6} \approx 1.6449340668482264
\]
Rounded to 10 decimal places, this is \(1.6449340668\).

{"answer": "\\frac{\\pi^2}{6}", "numerical_answer": "1.6449340668"}