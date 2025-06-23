

To calculate the definite integral \(\int_{-4}^4 |x^3 - x| \, dx\), we follow these steps:

### Step 1: Identify where \(x^3 - x\) changes sign
The function \(f(x) = x^3 - x\) factors as \(x(x^2 - 1) = x(x - 1)(x + 1)\), so its roots are \(x = -1, 0, 1\). These roots divide the real line into intervals where \(f(x)\) is positive or negative:
- For \(x \in (-\infty, -1) \cup (0, 1)\), \(f(x) < 0\), so \(|x^3 - x| = -(x^3 - x)\).
- For \(x \in (-1, 0) \cup (1, \infty)\), \(f(x) > 0\), so \(|x^3 - x| = x^3 - x\).

### Step 2: Split the integral at the roots
The integral over \([-4, 4]\) splits into four intervals:
\[
\int_{-4}^4 |x^3 - x| \, dx = \int_{-4}^{-1} -(x^3 - x) \, dx + \int_{-1}^0 (x^3 - x) \, dx + \int_{0}^1 -(x^3 - x) \, dx + \int_{1}^4 (x^3 - x) \, dx
\]

### Step 3: Compute the antiderivative
The antiderivative of \(x^3 - x\) is \(F(x) = \frac{x^4}{4} - \frac{x^2}{2}\).

### Step 4: Evaluate each integral
1. **First integral (\(-4\) to \(-1\))**:
\[
\int_{-4}^{-1} -(x^3 - x) \, dx = -\left[ F(-1) - F(-4) \right] = -\left[ \left( \frac{(-1)^4}{4} - \frac{(-1)^2}{2} \right) - \left( \frac{(-4)^4}{4} - \frac{(-4)^2}{2} \right) \right]
\]
\[
= -\left[ \left( \frac{1}{4} - \frac{1}{2} \right) - \left( 64 - 8 \right) \right] = -\left[ -\frac{1}{4} - 56 \right] = \frac{1}{4} + 56 = 56.25
\]

2. **Second integral (\(-1\) to \(0\))**:
\[
\int_{-1}^0 (x^3 - x) \, dx = F(0) - F(-1) = \left( 0 - 0 \right) - \left( \frac{1}{4} - \frac{1}{2} \right) = 0 - \left( -\frac{1}{4} \right) = \frac{1}{4}
\]

3. **Third integral (\(0\) to \(1\))**:
\[
\int_{0}^1 -(x^3 - x) \, dx = -\left[ F(1) - F(0) \right] = -\left[ \left( \frac{1}{4} - \frac{1}{2} \right) - 0 \right] = -\left( -\frac{1}{4} \right) = \frac{1}{4}
\]

4. **Fourth integral (\(1\) to \(4\))**:
\[
\int_{1}^4 (x^3 - x) \, dx = F(4) - F(1) = \left( 64 - 8 \right) - \left( \frac{1}{4} - \frac{1}{2} \right) = 56 - \left( -\frac{1}{4} \right) = 56 + \frac{1}{4} = 56.25
\]

### Step 5: Sum the results
Adding the four integrals:
\[
56.25 + \frac{1}{4} + \frac{1}{4} + 56.25 = 56.25 + 0.25 + 0.25 + 56.25 = 113
\]

### Numerical Approximation
The exact value is \(113\), so the numerical approximation to 10 decimal places is \(113.0000000000\).

{"answer": "113", "numerical_answer": "113.0000000000"}