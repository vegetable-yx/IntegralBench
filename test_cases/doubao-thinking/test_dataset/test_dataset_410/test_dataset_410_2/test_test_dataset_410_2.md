

To calculate the definite integral \(\int_0^\infty e^{-x^2}\cos(2x)\, dx\), we proceed as follows:

### Step 1: Define a parameterized integral
Consider the parameterized integral \(I(a) = \int_0^\infty e^{-x^2}\cos(ax)\, dx\), where \(a\) is a parameter. Our goal is to find \(I(2)\).

### Step 2: Differentiate \(I(a)\) with respect to \(a\)
Using Leibniz's rule for differentiation under the integral sign:
\[
\frac{dI}{da} = \int_0^\infty e^{-x^2} \cdot \frac{\partial}{\partial a} \cos(ax)\, dx = -\int_0^\infty x e^{-x^2} \sin(ax)\, dx.
\]

### Step 3: Integrate by parts
Let \(u = \sin(ax)\) and \(dv = x e^{-x^2}\, dx\). Then \(du = a \cos(ax)\, dx\) and \(v = -\frac{1}{2}e^{-x^2}\). Applying integration by parts:
\[
\int_0^\infty x e^{-x^2} \sin(ax)\, dx = \left[ -\frac{1}{2}e^{-x^2} \sin(ax) \right]_0^\infty + \frac{a}{2} \int_0^\infty e^{-x^2} \cos(ax)\, dx.
\]
The boundary term vanishes (since \(e^{-x^2} \to 0\) as \(x \to \infty\) and \(\sin(0) = 0\)), leaving:
\[
\int_0^\infty x e^{-x^2} \sin(ax)\, dx = \frac{a}{2} I(a).
\]
Thus, \(\frac{dI}{da} = -\frac{a}{2} I(a)\).

### Step 4: Solve the differential equation
The differential equation \(\frac{dI}{da} = -\frac{a}{2} I(a)\) is separable. Separating variables and integrating:
\[
\int \frac{dI}{I} = -\frac{1}{2} \int a\, da \implies \ln|I| = -\frac{a^2}{4} + C \implies I(a) = K e^{-a^2/4},
\]
where \(K\) is the constant of integration.

### Step 5: Determine \(K\) using the initial condition
When \(a = 0\), \(I(0) = \int_0^\infty e^{-x^2}\, dx = \frac{\sqrt{\pi}}{2}\). Substituting \(a = 0\) into \(I(a)\):
\[
I(0) = K e^0 = K \implies K = \frac{\sqrt{\pi}}{2}.
\]
Thus, \(I(a) = \frac{\sqrt{\pi}}{2} e^{-a^2/4}\).

### Step 6: Evaluate \(I(2)\)
For \(a = 2\):
\[
I(2) = \frac{\sqrt{\pi}}{2} e^{-2^2/4} = \frac{\sqrt{\pi}}{2} e^{-1} = \frac{\sqrt{\pi}}{2e}.
\]

### Numerical Approximation
The exact result is \(\frac{\sqrt{\pi}}{2e}\). Numerically, \(\sqrt{\pi} \approx 1.77245385091\) and \(e \approx 2.71828182846\), so:
\[
\frac{\sqrt{\pi}}{2e} \approx \frac{1.77245385091}{2 \cdot 2.71828182846} \approx 0.3256415285.
\]

{"answer": "\\frac{\\sqrt{\\pi}}{2e}", "numerical_answer": "0.3256415285"}