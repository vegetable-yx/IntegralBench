To compute the definite integral \(\int_{-\infty}^\infty e^{-(x-2024)^2/4}\:dx\), we can follow these steps:

### Step 1: Substitution
Let \( u = \frac{x - 2024}{2} \). Then, \( du = \frac{dx}{2} \), so \( dx = 2 du \).

When \( x = -\infty \), \( u = -\infty \), and when \( x = \infty \), \( u = \infty \).

The integral becomes:
\[
\int_{-\infty}^\infty e^{-u^2} \cdot 2 \: du = 2 \int_{-\infty}^\infty e^{-u^2} \: du
\]

### Step 2: Gaussian Integral
The Gaussian integral is known:
\[
\int_{-\infty}^\infty e^{-u^2} \: du = \sqrt{\pi}
\]

Thus, the integral evaluates to:
\[
2 \sqrt{\pi}
\]

### Step 3: Numerical Approximation
The numerical value of \( 2 \sqrt{\pi} \) is approximately:
\[
2 \times 1.77245385091 \approx 3.54490770181
\]

### Final Answer
```json
{"answer": "2\\sqrt{\\pi}", "numerical_answer": "3.54490770181"}
```