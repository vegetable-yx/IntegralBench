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
Since the integrand is even, the integral from \(0\) to \(\infty\) is half of this:
\[
\int_0^\infty e^{-x^2}\cos(2x)\,dx = \frac{\sqrt{\pi} e^{-1}}{2}.
\]

### Step 2: Numerical approximation
The exact answer is \(\frac{\sqrt{\pi}}{2e}\). Numerically, this evaluates to:
\[
\frac{\sqrt{\pi}}{2e} \approx 0.4111122905.
\]

### Final Answer
```json
{"answer": "\\frac{\\sqrt{\\pi}}{2e}", "numerical_answer": "0.4111122905"}
```