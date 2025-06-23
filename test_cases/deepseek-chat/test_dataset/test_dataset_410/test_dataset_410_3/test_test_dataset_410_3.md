To compute the definite integral \(\int_0^\infty e^{-x^2}\cos(2x)\,dx\), we will follow these steps:

### Step 1: Use the known result for the Fourier transform of a Gaussian
The integral \(\int_{-\infty}^\infty e^{-x^2}e^{-i k x}\,dx\) is the Fourier transform of the Gaussian function \(e^{-x^2}\). The result is:
\[
\int_{-\infty}^\infty e^{-x^2}e^{-i k x}\,dx = \sqrt{\pi} e^{-k^2/4}.
\]
Taking the real part (since \(\cos(2x)\) is the real part of \(e^{i 2x}\)), we have:
\[
\int_{-\infty}^\infty e^{-x^2}\cos(2x)\,dx = \sqrt{\pi} e^{-(2)^2/4} = \sqrt{\pi} e^{-1}.
\]
Since the integrand is even, we can write:
\[
\int_0^\infty e^{-x^2}\cos(2x)\,dx = \frac{1}{2} \sqrt{\pi} e^{-1}.
\]

### Step 2: Simplify the exact answer
The exact answer is:
\[
\int_0^\infty e^{-x^2}\cos(2x)\,dx = \frac{\sqrt{\pi}}{2 e}.
\]

### Step 3: Compute the numerical approximation
Using \(\sqrt{\pi} \approx 1.77245385091\) and \(e \approx 2.71828182846\), we get:
\[
\frac{\sqrt{\pi}}{2 e} \approx \frac{1.77245385091}{2 \times 2.71828182846} \approx 0.32573500794.
\]
Rounded to 10 decimal places, the numerical approximation is:
\[
0.3257350079.
\]

### Final Answer
```json
{"answer": "\\frac{\\sqrt{\\pi}}{2 e}", "numerical_answer": "0.3257350079"}
```