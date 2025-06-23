

To calculate the definite integral \(\int_{-4}^4 |x^3 - x| \, dx\), we follow these steps:

### Step 1: Identify where \(x^3 - x\) changes sign
The function \(f(x) = x^3 - x\) factors as \(x(x^2 - 1) = x(x - 1)(x + 1)\). Its roots are \(x = -1, 0, 1\). These roots divide the interval \([-4, 4]\) into subintervals where \(f(x)\) is either positive or negative. We determine the sign of \(f(x)\) in each subinterval:
- For \(x \in [-4, -1]\): \(f(x) < 0\), so \(|x^3 - x| = -x^3 + x\).
- For \(x \in [-1, 0]\): \(f(x) > 0\), so \(|x^3 - x| = x^3 - x\).
- For \(x \in [0, 1]\): \(f(x) < 0\), so \(|x^3 - x| = -x^3 + x\).
- For \(x \in [1, 4]\): \(f(x) > 0\), so \(|x^3 - x| = x^3 - x\).

### Step 2: Split the integral into subintervals
The integral becomes the sum of four integrals over these subintervals:
\[
\int_{-4}^4 |x^3 - x| \, dx = \int_{-4}^{-1} (-x^3 + x) \, dx + \int_{-1}^{0} (x^3 - x) \, dx + \int_{0}^{1} (-x^3 + x) \, dx + \int_{1}^{4} (x^3 - x) \, dx
\]

### Step 3: Evaluate each integral
We compute each integral using the antiderivatives of the polynomial expressions:

1. **First integral (\(\int_{-4}^{-1} (-x^3 + x) \, dx\))**:
   \[
   \text{Antiderivative: } -\frac{x^4}{4} + \frac{x^2}{2}
   \]
   Evaluating from \(-4\) to \(-1\):
   \[
   \left[ -\frac{(-1)^4}{4} + \frac{(-1)^2}{2} \right] - \left[ -\frac{(-4)^4}{4} + \frac{(-4)^2}{2} \right] = \left( -\frac{1}{4} + \frac{1}{2} \right) - \left( -64 + 8 \right) = \frac{1}{4} - (-56) = \frac{225}{4}
   \]

2. **Second integral (\(\int_{-1}^{0} (x^3 - x) \, dx\))**:
   \[
   \text{Antiderivative: } \frac{x^4}{4} - \frac{x^2}{2}
   \]
   Evaluating from \(-1\) to \(0\):
   \[
   \left[ \frac{0^4}{4} - \frac{0^2}{2} \right] - \left[ \frac{(-1)^4}{4} - \frac{(-1)^2}{2} \right] = 0 - \left( \frac{1}{4} - \frac{1}{2} \right) = 0 - \left( -\frac{1}{4} \right) = \frac{1}{4}
   \]

3. **Third integral (\(\int_{0}^{1} (-x^3 + x) \, dx\))**:
   \[
   \text{Antiderivative: } -\frac{x^4}{4} + \frac{x^2}{2}
   \]
   Evaluating from \(0\) to \(1\):
   \[
   \left[ -\frac{1^4}{4} + \frac{1^2}{2} \right] - \left[ -\frac{0^4}{4} + \frac{0^2}{2} \right] = \left( -\frac{1}{4} + \frac{1}{2} \right) - 0 = \frac{1}{4}
   \]

4. **Fourth integral (\(\int_{1}^{4} (x^3 - x) \, dx\))**:
   \[
   \text{Antiderivative: } \frac{x^4}{4} - \frac{x^2}{2}
   \]
   Evaluating from \(1\) to \(4\):
   \[
   \left[ \frac{4^4}{4} - \frac{4^2}{2} \right] - \left[ \frac{1^4}{4} - \frac{1^2}{2} \right] = \left( 64 - 8 \right) - \left( \frac{1}{4} - \frac{1}{2} \right) = 56 - \left( -\frac{1}{4} \right) = \frac{225}{4}
   \]

### Step 4: Sum the results
Adding the four integrals:
\[
\frac{225}{4} + \frac{1}{4} + \frac{1}{4} + \frac{225}{4} = \frac{452}{4} = 113
\]

### Numerical Approximation
The exact value is \(113\), so the numerical approximation (rounded to 10 decimal places) is \(113.0000000000\).

{"answer": "113", "numerical_answer": "113.0000000000"}