To compute the definite integral \(\int_0^\infty e^{-x^2}\cos(2x)\,dx\), we can follow these steps:

### Step 1: Use the known result for the Fourier transform of a Gaussian
The integral \(\int_{-\infty}^\infty e^{-x^2}e^{-i k x}\,dx\) is a well-known Fourier transform of the Gaussian function \(e^{-x^2}\). The result is:
\[
\int_{-\infty}^\infty e^{-x^2}e^{-i k x}\,dx = \sqrt{\pi} e^{-k^2/4}.
\]
Taking the real part of this (since \(\cos(2x)\) is the real part of \(e^{i 2x}\)), we get:
\[
\int_{-\infty}^\infty e^{-x^2}\cos(2x)\,dx = \sqrt{\pi} e^{-(2)^2/4} = \sqrt{\pi} e^{-1}.
\]
Since the integrand is even, we have:
\[
\int_0^\infty e^{-x^2}\cos(2x)\,dx = \frac{1}{2} \sqrt{\pi} e^{-1}.
\]

### Step 2: Verify the result
Alternatively, we can use differentiation under the integral sign. Consider the integral:
\[
I(a) = \int_0^\infty e^{-x^2} \cos(a x)\,dx.
\]
Differentiating \(I(a)\) with respect to \(a\):
\[
I'(a) = -\int_0^\infty x e^{-x^2} \sin(a x)\,dx.
\]
Using integration by parts with \(u = \sin(a x)\) and \(dv = -x e^{-x^2}\,dx\), we get:
\[
I'(a) = -\left[ \frac{1}{2} e^{-x^2} \sin(a x) \right]_0^\infty + \frac{a}{2} \int_0^\infty e^{-x^2} \cos(a x)\,dx = -\frac{a}{2} I(a).
\]
This gives the differential equation:
\[
I'(a) = -\frac{a}{2} I(a).
\]
Solving this:
\[
\frac{I'(a)}{I(a)} = -\frac{a}{2} \implies \ln I(a) = -\frac{a^2}{4} + C.
\]
At \(a = 0\), \(I(0) = \frac{\sqrt{\pi}}{2}\), so \(C = \ln \frac{\sqrt{\pi}}{2}\). Thus:
\[
I(a) = \frac{\sqrt{\pi}}{2} e^{-a^2/4}.
\]
For \(a = 2\):
\[
I(2) = \frac{\sqrt{\pi}}{2} e^{-1}.
\]

### Step 3: Numerical approximation
The exact value is \(\frac{\sqrt{\pi}}{2} e^{-1}\). Numerically:
\[
\sqrt{\pi} \approx 1.7724538509, \quad e^{-1} \approx 0.3678794412.
\]
Thus:
\[
\frac{\sqrt{\pi}}{2} e^{-1} \approx \frac{1.7724538509}{2} \times 0.3678794412 \approx 0.3257350079.
\]

### Final Answer
```json
{"answer": "\\frac{\\sqrt{\\pi}}{2} e^{-1}", "numerical_answer": "0.3257350079"}
```