

To solve the definite integral \(\int_{0}^{1} \left( \frac{1}{x} - \left\lfloor \frac{1}{x} \right\rfloor \right) \, dx\), we proceed as follows:

### Step 1: Substitution
Let \( t = \frac{1}{x} \), so \( x = \frac{1}{t} \) and \( dx = -\frac{1}{t^2} dt \). When \( x = 0 \), \( t \to \infty \); when \( x = 1 \), \( t = 1 \). The integral transforms to:
\[
\int_{0}^{1} \left( \frac{1}{x} - \left\lfloor \frac{1}{x} \right\rfloor \right) dx = \int_{\infty}^{1} \left( t - \lfloor t \rfloor \right) \left( -\frac{1}{t^2} \right) dt = \int_{1}^{\infty} \frac{\{ t \}}{t^2} dt,
\]
where \( \{ t \} = t - \lfloor t \rfloor \) denotes the fractional part of \( t \).

### Step 2: Splitting the Integral
The fractional part \( \{ t \} \) satisfies \( \{ t \} = t - n \) for \( t \in [n, n+1) \) and \( n \in \mathbb{N} \). We split the integral over intervals \([n, n+1)\) for \( n \geq 1 \):
\[
\int_{1}^{\infty} \frac{\{ t \}}{t^2} dt = \sum_{n=1}^{\infty} \int_{n}^{n+1} \frac{t - n}{t^2} dt.
\]

### Step 3: Evaluating the Integral Over Each Interval
For each \( n \), compute the integral over \([n, n+1)\):
\[
\int_{n}^{n+1} \frac{t - n}{t^2} dt = \int_{n}^{n+1} \left( \frac{1}{t} - \frac{n}{t^2} \right) dt.
\]
Integrate term-by-term:
\[
\int_{n}^{n+1} \frac{1}{t} dt = \ln(t) \bigg|_{n}^{n+1} = \ln(n+1) - \ln(n),
\]
\[
\int_{n}^{n+1} \frac{n}{t^2} dt = -n \cdot \frac{1}{t} \bigg|_{n}^{n+1} = -n \left( \frac{1}{n+1} - \frac{1}{n} \right) = \frac{n}{n} - \frac{n}{n+1} = 1 - \frac{n}{n+1}.
\]
Thus, the integral over \([n, n+1)\) becomes:
\[
\left( \ln(n+1) - \ln(n) \right) - \left( 1 - \frac{n}{n+1} \right) = \ln\left( \frac{n+1}{n} \right) - \frac{1}{n+1}.
\]

### Step 4: Summing the Series
The original integral is the sum of these terms over \( n \geq 1 \):
\[
\sum_{n=1}^{\infty} \left( \ln\left( \frac{n+1}{n} \right) - \frac{1}{n+1} \right).
\]
The logarithmic terms form a telescoping series:
\[
\sum_{n=1}^{\infty} \ln\left( \frac{n+1}{n} \right) = \lim_{N \to \infty} \ln(N+1).
\]
The harmonic series terms sum to:
\[
\sum_{n=1}^{\infty} \frac{1}{n+1} = \sum_{k=2}^{\infty} \frac{1}{k} = \lim_{N \to \infty} \left( H_{N+1} - 1 \right),
\]
where \( H_{N} \) is the \( N \)-th harmonic number. Using the Euler-Mascheroni constant \( \gamma = \lim_{N \to \infty} (H_N - \ln N) \), we find:
\[
\lim_{N \to \infty} \left( \ln(N+1) - (H_{N+1} - 1) \right) = 1 - \gamma.
\]

### Exact and Numerical Results
The exact value of the integral is \( 1 - \gamma \), where \( \gamma \approx 0.5772156649 \). The numerical approximation is \( 1 - 0.5772156649 \approx 0.4227843351 \).

{"answer": "1 - \gamma", "numerical_answer": "0.4227843351"}