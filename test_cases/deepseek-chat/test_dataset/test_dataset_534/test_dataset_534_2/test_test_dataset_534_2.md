To compute the definite integral \(\int_{-\infty}^\infty e^{-(x-2024)^2/4}\:dx\), we can follow these steps:

### Step 1: Substitution
Let \( u = \frac{x - 2024}{\sqrt{2}} \). Then, \( du = \frac{dx}{\sqrt{2}} \), and the integral becomes:
\[
\int_{-\infty}^\infty e^{-u^2} \cdot \sqrt{2} \: du = \sqrt{2} \int_{-\infty}^\infty e^{-u^2} \: du.
\]

### Step 2: Gaussian Integral
The integral \(\int_{-\infty}^\infty e^{-u^2} \: du\) is a well-known Gaussian integral, and its value is \(\sqrt{\pi}\). Therefore:
\[
\sqrt{2} \int_{-\infty}^\infty e^{-u^2} \: du = \sqrt{2} \cdot \sqrt{\pi} = \sqrt{2\pi}.
\]

### Step 3: Final Answer
The exact value of the integral is \(\sqrt{2\pi}\).

### Step 4: Numerical Approximation
The numerical value of \(\sqrt{2\pi}\) rounded to 10 decimal places is approximately 2.5066282746.

### JSON Output
```json
{"answer": "\\sqrt{2\\pi}", "numerical_answer": "2.5066282746"}
```