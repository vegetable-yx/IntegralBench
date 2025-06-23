Let's compute the integral:
\[
I = \int_0^\infty \frac{x}{e^x-1}\,dx
\]

**Step 1: Analytical Solution**

First, let's recall a standard result: 

\[
\int_0^\infty \frac{x^{k-1}}{e^x-1} dx = \Gamma(k)\zeta(k), \quad k > 1
\]

In our case, \( k = 2 \):

\[
I = \int_0^\infty \frac{x}{e^x-1}\,dx = \Gamma(2) \zeta(2)
\]

Now, \(\Gamma(2) = 1!\) so \(\Gamma(2) = 1\).

\(\zeta(2)\) is the Riemann zeta function at 2:
\[
\zeta(2) = \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}
\]

Therefore,

\[
I = \Gamma(2)\zeta(2) = 1 \times \frac{\pi^2}{6} = \frac{\pi^2}{6}
\]

**Step 2: Show all steps**

- Recognize representation as a special case of the more general integral involving Riemann zeta and Gamma functions.
- Use the values: \(\Gamma(2) = 1\), \(\zeta(2) = \frac{\pi^2}{6}\).
- Substitute these values into the formula.

**Step 3: Numerical Approximation**

Let’s calculate \(\frac{\pi^2}{6}\):

\[
\pi \approx 3.1415926536
\]
\[
\pi^2 \approx 9.8696044011
\]
\[
\frac{\pi^2}{6} \approx 1.6449340668
\]

**Step 4: Final JSON output**

```json
{"answer": "\\frac{\\pi^2}{6}", "numerical_answer": "1.6449340668"}
```