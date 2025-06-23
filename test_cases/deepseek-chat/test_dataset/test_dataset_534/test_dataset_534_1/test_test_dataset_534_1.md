To compute the definite integral \(\int_{-\infty}^\infty e^{-(x-2024)^2/4}\:dx\), we follow these steps:

### Step 1: Substitution
Let \( u = x - 2024 \). Then \( du = dx \), and the integral becomes:
\[
\int_{-\infty}^\infty e^{-u^2/4}\:du
\]

### Step 2: Recognize the Gaussian Integral
The integral \(\int_{-\infty}^\infty e^{-u^2/4}\:du\) is a standard Gaussian integral. The general form is:
\[
\int_{-\infty}^\infty e^{-au^2}\:du = \sqrt{\frac{\pi}{a}}
\]
In our case, \( a = \frac{1}{4} \), so:
\[
\int_{-\infty}^\infty e^{-u^2/4}\:du = \sqrt{\frac{\pi}{\frac{1}{4}}} = 2\sqrt{\pi}
\]

### Step 3: Numerical Approximation
The numerical value of \( 2\sqrt{\pi} \) is approximately:
\[
2\sqrt{\pi} \approx 3.5449077018
\]

### Final Answer
The exact answer is \( 2\sqrt{\pi} \), and the numerical approximation is \( 3.5449077018 \).

```json
{"answer": "2\\sqrt{\\pi}", "numerical_answer": "3.5449077018"}
```