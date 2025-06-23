


To calculate the definite integral \(\int_0^\infty e^{-x^2}\cos(2x)\, dx\), we proceed as follows:

### Step 1: Parameterize the Integral
Define \(I(a) = \int_0^\infty e^{-x^2}\cos(ax)\, dx\), where \(a\) is a parameter. Our target integral is \(I(2)\).

### Step 2: Differentiate \(I(a)\) with Respect to \(a\)
Using differentiation under the integral sign (Leibniz rule):
\[
I'(a) = \frac{d}{da} \int_0^\infty e^{-x^2}\cos(ax)\, dx = \int_0^\infty e^{-x^2} \cdot (-x\sin(ax))\, dx = -\int_0^\infty x e^{-x^2}\sin(ax)\, dx.
\]

### Step 3: Integrate by Parts
Let \(u = \sin(ax)\) and \(dv = x e^{-x^2}\, dx\). Then \(du = a\cos(ax)\, dx\) and \(v = -\frac{1}{2}e^{-x^2}\). Applying integration by parts:
\[
-\int_0^\infty x e^{-x^2}\sin(ax)\, dx = -\left[ \left. -\frac{1}{2}e^{-x^2}\sin(ax) \right|_0^\infty + \frac{a}{2}\int_0^\infty e^{-x^2}\cos(ax)\, dx \right].
\]
The boundary term vanishes (since \(e^{-x^2} \to 0\) as \(x \to \infty\) and \(\sin(0) = 0\)), leaving:
\[
I'(a) = -\frac{a}{2}I(a).
\]

### Step 4: Solve the Differential Equation
The equation \(I'(a) = -\frac{a}{2}I(a)\) is a first-order linear ODE. Separating variables and integrating:
\[
\int \frac{dI}{I} = -\frac{1}{2}\int a\, da \implies \ln|I| = -\frac{a^2}{4} + C \implies I(a) = K e^{-a^2/4},
\]
where \(K\) is a constant.

### Step 5: Determine \(K\) Using Initial Condition
When \(a = 0\), \(I(0) = \int_0^\infty e^{-x^2}\, dx = \frac{\sqrt{\pi}}{2}\). Substituting \(a = 0\) into \(I(a)\):
\[
\frac{\sqrt{\pi}}{2} = K e^0 \implies K = \frac{\sqrt{\pi}}{2}.
\]

### Step 6: Evaluate \(I(2)\)
Substituting \(a = 2\) into \(I(a)\):
\[
I(2) = \frac{\sqrt{\pi}}{2} e^{-2^2/4} = \frac{\sqrt{\pi}}{2} e^{-1} = \frac{\sqrt{\pi}}{2e}.
\]

### Numerical Approximation
The exact result is \(\frac{\sqrt{\pi}}{2e}\). Numerically:
\[
\sqrt{\pi} \approx 1.7724538509055159, \quad e \approx 2.718281828459045,
\]
so:
\[
\frac{\sqrt{\pi}}{2e} \approx \frac{1.7724538509055159}{2 \cdot 2.718281828459045} \approx 0.3260246660.
\]

{"answer": "\\frac{\\sqrt{\\pi}}{2e}", "numerical_answer": "0.3260246660"}