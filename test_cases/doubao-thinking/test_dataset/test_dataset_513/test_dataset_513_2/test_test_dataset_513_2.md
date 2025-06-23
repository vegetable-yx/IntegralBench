

To calculate the definite integral \(\int_{-4}^4 |x^3 - x| \, dx\), we first determine where the expression inside the absolute value, \(x^3 - x\), changes sign. Factoring \(x^3 - x\) gives \(x(x-1)(x+1)\), so the roots are \(x = -1, 0, 1\). These roots divide the interval \([-4, 4]\) into subintervals where \(x^3 - x\) is either positive or negative. We analyze the sign of \(x^3 - x\) in each subinterval:

- For \(x \in [-4, -1]\): \(x^3 - x < 0\), so \(|x^3 - x| = -x^3 + x\).
- For \(x \in [-1, 0]\): \(x^3 - x > 0\), so \(|x^3 - x| = x^3 - x\).
- For \(x \in [0, 1]\): \(x^3 - x < 0\), so \(|x^3 - x| = -x^3 + x\).
- For \(x \in [1, 4]\): \(x^3 - x > 0\), so \(|x^3 - x| = x^3 - x\).

We split the integral into these subintervals and compute each part:

### 1. Integral over \([-4, -1]\):
\[
\int_{-4}^{-1} (-x^3 + x) \, dx
\]
The antiderivative of \(-x^3 + x\) is \(-\frac{x^4}{4} + \frac{x^2}{2}\). Evaluating at the bounds:
\[
\left[ -\frac{(-1)^4}{4} + \frac{(-1)^2}{2} \right] - \left[ -\frac{(-4)^4}{4} + \frac{(-4)^2}{2} \right] = \left( -\frac{1}{4} + \frac{1}{2} \right) - \left( -\frac{256}{4} + \frac{16}{2} \right) = \frac{1}{4} - (-56) = \frac{225}{4}
\]

### 2. Integral over \([-1, 0]\):
\[
\int_{-1}^{0} (x^3 - x) \, dx
\]
The antiderivative of \(x^3 - x\) is \(\frac{x^4}{4} - \frac{x^2}{2}\). Evaluating at the bounds:
\[
\left[ \frac{0^4}{4} - \frac{0^2}{2} \right] - \left[ \frac{(-1)^4}{4} - \frac{(-1)^2}{2} \right] = 0 - \left( \frac{1}{4} - \frac{1}{2} \right) = 0 - \left( -\frac{1}{4} \right) = \frac{1}{4}
\]

### 3. Integral over \([0, 1]\):
\[
\int_{0}^{1} (-x^3 + x) \, dx
\]
The antiderivative of \(-x^3 + x\) is \(-\frac{x^4}{4} + \frac{x^2}{2}\). Evaluating at the bounds:
\[
\left[ -\frac{1^4}{4} + \frac{1^2}{2} \right] - \left[ -\frac{0^4}{4} + \frac{0^2}{2} \right] = \left( -\frac{1}{4} + \frac{1}{2} \right) - 0 = \frac{1}{4}
\]

### 4. Integral over \([1, 4]\):
\[
\int_{1}^{4} (x^3 - x) \, dx
\]
The antiderivative of \(x^3 - x\) is \(\frac{x^4}{4} - \frac{x^2}{2}\). Evaluating at the bounds:
\[
\left[ \frac{4^4}{4} - \frac{4^2}{2} \right] - \left[ \frac{1^4}{4} - \frac{1^2}{2} \right] = \left( 64 - 8 \right) - \left( \frac{1}{4} - \frac{1}{2} \right) = 56 - \left( -\frac{1}{4} \right) = \frac{225}{4}
\]

### Total Integral:
Adding the results of the four subintervals:
\[
\frac{225}{4} + \frac{1}{4} + \frac{1}{4} + \frac{225}{4} = \frac{452}{4} = 113
\]

### Numerical Approximation:
The exact value is \(113\), so the numerical approximation rounded to 10 decimal places is \(113.0000000000\).

{"answer": "113", "numerical_answer": "113.0000000000"}