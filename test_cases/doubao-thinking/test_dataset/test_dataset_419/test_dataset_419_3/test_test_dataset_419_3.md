

To calculate the definite integral \(\int_0^\infty \frac{x}{e^x - 1} \, dx\), we proceed as follows:

### Step 1: Express the integrand as a series
The term \(\frac{1}{e^x - 1}\) can be rewritten using a geometric series. For \(x > 0\), \(e^x > 1\), so \(e^{-x} < 1\). Thus:
\[
\frac{1}{e^x - 1} = \frac{e^{-x}}{1 - e^{-x}} = \sum_{n=1}^\infty e^{-nx}
\]
This is a convergent geometric series with common ratio \(e^{-x}\).

### Step 2: Interchange the sum and integral
Substituting this series into the integral, we get:
\[
\int_0^\infty \frac{x}{e^x - 1} \, dx = \int_0^\infty x \sum_{n=1}^\infty e^{-nx} \, dx
\]
By Tonelli's theorem (since the integrand is non-negative), we can interchange the sum and integral:
\[
\int_0^\infty x \sum_{n=1}^\infty e^{-nx} \, dx = \sum_{n=1}^\infty \int_0^\infty x e^{-nx} \, dx
\]

### Step 3: Evaluate the inner integral
The integral \(\int_0^\infty x e^{-nx} \, dx\) is a standard form. For \(a > 0\), \(\int_0^\infty x^k e^{-ax} \, dx = \frac{k!}{a^{k+1}}\). Here, \(k = 1\) and \(a = n\), so:
\[
\int_0^\infty x e^{-nx} \, dx = \frac{1!}{n^2} = \frac{1}{n^2}
\]

### Step 4: Recognize the resulting series
The integral now reduces to the sum of reciprocals of squares:
\[
\sum_{n=1}^\infty \frac{1}{n^2}
\]
This is the Riemann zeta function \(\zeta(2)\), which is known to equal \(\frac{\pi^2}{6}\).

### Numerical Approximation
The exact value is \(\frac{\pi^2}{6}\). Numerically, \(\pi \approx 3.141592653589793\), so \(\pi^2 \approx 9.869604401089358\). Dividing by 6 gives:
\[
\frac{\pi^2}{6} \approx 1.6449340668482264
\]
Rounded to 10 decimal places, this is \(1.6449340668\).

{"answer": "\(\frac{\pi^2}{6}\)", "numerical_answer": "1.6449340668"}