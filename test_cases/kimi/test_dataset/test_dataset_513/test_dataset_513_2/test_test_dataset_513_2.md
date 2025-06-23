To solve the definite integral \(\int_{-4}^4 |x^3 - x| \, dx\), we need to consider the behavior of the integrand \(|x^3 - x|\) over the interval \([-4, 4]\).

### Step 1: Analyze the integrand

The expression inside the absolute value is \(x^3 - x\). We need to determine where this expression changes sign within the interval \([-4, 4]\).

\[ x^3 - x = x(x^2 - 1) = x(x - 1)(x + 1) \]

The roots of \(x^3 - x\) are \(x = 0\), \(x = 1\), and \(x = -1\). These points divide the interval \([-4, 4]\) into four subintervals:
1. \([-4, -1]\)
2. \([-1, 0]\)
3. \([0, 1]\)
4. \([1, 4]\)

### Step 2: Determine the sign of \(x^3 - x\) in each subinterval

- For \(x \in [-4, -1]\), \(x^3 - x < 0\), so \(|x^3 - x| = -(x^3 - x) = -x^3 + x\).
- For \(x \in [-1, 0]\), \(x^3 - x > 0\), so \(|x^3 - x| = x^3 - x\).
- For \(x \in [0, 1]\), \(x^3 - x < 0\), so \(|x^3 - x| = -(x^3 - x) = -x^3 + x\).
- For \(x \in [1, 4]\), \(x^3 - x > 0\), so \(|x^3 - x| = x^3 - x\).

### Step 3: Split the integral into parts

We can now split the integral into four parts:

\[
\int_{-4}^4 |x^3 - x| \, dx = \int_{-4}^{-1} (-x^3 + x) \, dx + \int_{-1}^{0} (x^3 - x) \, dx + \int_{0}^{1} (-x^3 + x) \, dx + \int_{1}^{4} (x^3 - x) \, dx
\]

### Step 4: Compute each integral

1. \(\int_{-4}^{-1} (-x^3 + x) \, dx\):

\[
\int_{-4}^{-1} (-x^3 + x) \, dx = \left[ -\frac{x^4}{4} + \frac{x^2}{2} \right]_{-4}^{-1}
\]

Evaluating at the bounds:

\[
\left( -\frac{(-1)^4}{4} + \frac{(-1)^2}{2} \right) - \left( -\frac{(-4)^4}{4} + \frac{(-4)^2}{2} \right) = \left( -\frac{1}{4} + \frac{1}{2} \right) - \left( -\frac{256}{4} + \frac{16}{2} \right) = \left( \frac{1}{4} \right) - \left( -64 + 8 \right) = \frac{1}{4} + 56 = \frac{225}{4}
\]

2. \(\int_{-1}^{0} (x^3 - x) \, dx\):

\[
\int_{-1}^{0} (x^3 - x) \, dx = \left[ \frac{x^4}{4} - \frac{x^2}{2} \right]_{-1}^{0}
\]

Evaluating at the bounds:

\[
\left( \frac{0^4}{4} - \frac{0^2}{2} \right) - \left( \frac{(-1)^4}{4} - \frac{(-1)^2}{2} \right) = 0 - \left( \frac{1}{4} - \frac{1}{2} \right) = 0 - \left( -\frac{1}{4} \right) = \frac{1}{4}
\]

3. \(\int_{0}^{1} (-x^3 + x) \, dx\):

\[
\int_{0}^{1} (-x^3 + x) \, dx = \left[ -\frac{x^4}{4} + \frac{x^2}{2} \right]_{0}^{1}
\]

Evaluating at the bounds:

\[
\left( -\frac{1^4}{4} + \frac{1^2}{2} \right) - \left( -\frac{0^4}{4} + \frac{0^2}{2} \right) = \left( -\frac{1}{4} + \frac{1}{2} \right) - 0 = \frac{1}{4}
\]

4. \(\int_{1}^{4} (x^3 - x) \, dx\):

\[
\int_{1}^{4} (x^3 - x) \, dx = \left[ \frac{x^4}{4} - \frac{x^2}{2} \right]_{1}^{4}
\]

Evaluating at the bounds:

\[
\left( \frac{4^4}{4} - \frac{4^2}{2} \right) - \left( \frac{1^4}{4} - \frac{1^2}{2} \right) = \left( \frac{256}{4} - \frac{16}{2} \right) - \left( \frac{1}{4} - \frac{1}{2} \right) = \left( 64 - 8 \right) - \left( -\frac{1}{4} \right) = 56 + \frac{1}{4} = \frac{225}{4}
\]

### Step 5: Sum the results

\[
\int_{-4}^4 |x^3 - x| \, dx = \frac{225}{4} + \frac{1}{4} + \frac{1}{4} + \frac{225}{4} = \frac{452}{4} = 113
\]

### Step 6: Numerical approximation

The numerical approximation of 113 is 113.0000000000.

### Final Answer

\[
\boxed{
\begin{aligned}
\text{"answer": "113",} \\
\text{"numerical_answer": "113.0000000000"}
\end{aligned}
}
\]