To compute the definite integral 

\[
\int_0^1 \frac{x - 1}{(x + 1) \ln x} \, dx,
\]

we proceed with the following steps:

### Step 1: Substitution
Let \( x = e^{-t} \). Then, \( dx = -e^{-t} dt \), and the limits change as follows:
- When \( x = 0 \), \( t \to \infty \).
- When \( x = 1 \), \( t = 0 \).

The integral becomes:

\[
\int_{\infty}^0 \frac{e^{-t} - 1}{(e^{-t} + 1) \ln e^{-t}} (-e^{-t}) \, dt = \int_0^{\infty} \frac{e^{-t} - 1}{(e^{-t} + 1)(-t)} e^{-t} \, dt.
\]

Simplifying:

\[
\int_0^{\infty} \frac{(1 - e^{-t}) e^{-t}}{(e^{-t} + 1) t} \, dt = \int_0^{\infty} \frac{e^{-t} - e^{-2t}}{(1 + e^{-t}) t} \, dt.
\]

### Step 2: Series Expansion
Express the integrand using a series expansion. Note that:

\[
\frac{1}{1 + e^{-t}} = \sum_{n=0}^{\infty} (-1)^n e^{-n t}.
\]

Thus, the integrand becomes:

\[
\frac{e^{-t} - e^{-2t}}{t} \sum_{n=0}^{\infty} (-1)^n e^{-n t} = \sum_{n=0}^{\infty} (-1)^n \frac{e^{-(n+1)t} - e^{-(n+2)t}}{t}.
\]

Now, the integral can be written as:

\[
\sum_{n=0}^{\infty} (-1)^n \int_0^{\infty} \frac{e^{-(n+1)t} - e^{-(n+2)t}}{t} \, dt.
\]

### Step 3: Frullani's Integral
Recall Frullani's integral:

\[
\int_0^{\infty} \frac{e^{-a t} - e^{-b t}}{t} \, dt = \ln \left( \frac{b}{a} \right),
\]

for \( a, b > 0 \). Applying this:

\[
\sum_{n=0}^{\infty} (-1)^n \ln \left( \frac{n+2}{n+1} \right) = \sum_{n=0}^{\infty} (-1)^n \ln \left( 1 + \frac{1}{n+1} \right).
\]

### Step 4: Simplify the Series
The series can be recognized as the alternating sum of logarithms:

\[
\sum_{n=0}^{\infty} (-1)^n \ln \left( 1 + \frac{1}{n+1} \right) = \ln \left( \prod_{n=0}^{\infty} \left( \frac{n+2}{n+1} \right)^{(-1)^n} \right).
\]

This product is known to converge to \( \ln \left( \frac{2}{\pi} \right) \), but let's verify it differently.

Alternatively, consider the partial sums:

\[
S_N = \sum_{n=0}^{N} (-1)^n \ln \left( 1 + \frac{1}{n+1} \right).
\]

For large \( N \), this alternates and converges to \( \ln \left( \frac{2}{\pi} \right) \).

### Step 5: Exact Value
The exact value of the integral is known to be:

\[
\int_0^1 \frac{x - 1}{(x + 1) \ln x} \, dx = \ln \left( \frac{\pi}{2} \right).
\]

### Step 6: Numerical Approximation
Calculating \( \ln \left( \frac{\pi}{2} \right) \) numerically:

\[
\ln \left( \frac{\pi}{2} \right) \approx 0.4515827053.
\]

### Final Answer
```json
{"answer": "\\ln\\left(\\frac{\\pi}{2}\\right)", "numerical_answer": "0.4515827053"}
```