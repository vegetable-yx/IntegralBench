


To solve the definite integral \(\int_{64}^{729}\frac{x^{1/2}}{x^{1/2}-x^{1/3}}dx\), we proceed with the following steps:

### Step 1: Substitution to Simplify the Integrand
The exponents \(1/2\) and \(1/3\) suggest using a substitution to eliminate the roots. Let \(t = x^{1/6}\), so \(x = t^6\) and \(dx = 6t^5 dt\). This transforms the limits of integration:
- When \(x = 64\), \(t = 64^{1/6} = 2\).
- When \(x = 729\), \(t = 729^{1/6} = 3\).

Rewriting the integrand in terms of \(t\):
- \(x^{1/2} = (t^6)^{1/2} = t^3\),
- \(x^{1/3} = (t^6)^{1/3} = t^2\),
- The denominator becomes \(t^3 - t^2 = t^2(t - 1)\),
- The integrand becomes \(\frac{t^3}{t^2(t - 1)} \cdot 6t^5 dt = \frac{6t^6}{t - 1} dt\).

### Step 2: Simplify the Rational Function
We simplify \(\frac{t^6}{t - 1}\) using polynomial long division. Since \(t^6 - 1 = (t - 1)(t^5 + t^4 + t^3 + t^2 + t + 1)\), we have:
\[
\frac{t^6}{t - 1} = t^5 + t^4 + t^3 + t^2 + t + 1 + \frac{1}{t - 1}.
\]

### Step 3: Integrate Term by Term
The integral becomes:
\[
6 \int_{2}^{3} \left( t^5 + t^4 + t^3 + t^2 + t + 1 + \frac{1}{t - 1} \right) dt.
\]

Integrating term by term:
\[
\int \left( t^5 + t^4 + t^3 + t^2 + t + 1 + \frac{1}{t - 1} \right) dt = \frac{t^6}{6} + \frac{t^5}{5} + \frac{t^4}{4} + \frac{t^3}{3} + \frac{t^2}{2} + t + \ln|t - 1| + C.
\]

### Step 4: Evaluate the Definite Integral
Evaluate the antiderivative from \(t = 2\) to \(t = 3\):
\[
\left[ \frac{t^6}{6} + \frac{t^5}{5} + \frac{t^4}{4} + \frac{t^3}{3} + \frac{t^2}{2} + t + \ln(t - 1) \right]_{2}^{3}.
\]

### Step 5: Compute the Exact Result
Substituting the limits and simplifying, the exact result is:
\[
6 \left( \frac{10747}{60} + \ln 2 \right) = \frac{10747}{10} + 6 \ln 2.
\]

### Step 6: Numerical Approximation
Using \(\ln 2 \approx 0.69314718056\), the numerical approximation is:
\[
\frac{10747}{10} + 6 \cdot 0.69314718056 \approx 1074.7 + 4.15888308336 = 1078.85888308336.
\]

Rounded to 10 decimal places, the result is \(1078.8588830834\).

{"answer": "\(\frac{10747}{10} + 6 \ln 2\)", "numerical_answer": "1078.8588830834"}