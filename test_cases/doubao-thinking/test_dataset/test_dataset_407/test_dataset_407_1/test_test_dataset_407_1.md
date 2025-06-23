
To solve the definite integral \(\int_0^\infty \frac{\sin\sqrt{3}\,x - \sin\frac{x}{\sqrt{3}}}{x} e^{-x^2}\, dx\), we proceed as follows:


### Step 1: Split the Integral
The integrand can be split into two separate integrals:
\[
\int_0^\infty \frac{\sin\sqrt{3}\,x - \sin\frac{x}{\sqrt{3}}}{x} e^{-x^2}\, dx = \int_0^\infty \frac{\sin\sqrt{3}\,x}{x} e^{-x^2}\, dx - \int_0^\infty \frac{\sin\frac{x}{\sqrt{3}}}{x} e^{-x^2}\, dx.
\]


### Step 2: Evaluate \(\int_0^\infty \frac{\sin(ax)}{x} e^{-x^2}\, dx\)
Let \(I(a) = \int_0^\infty \frac{\sin(ax)}{x} e^{-x^2}\, dx\). Differentiating \(I(a)\) with respect to \(a\) (justified by uniform convergence):
\[
\frac{dI}{da} = \int_0^\infty \cos(ax) e^{-x^2}\, dx.
\]
The integral \(\int_0^\infty \cos(ax) e^{-x^2}\, dx\) is a standard Gaussian integral, equal to \(\frac{\sqrt{\pi}}{2} e^{-a^2/4}\). Integrating back from \(0\) to \(a\) (with \(I(0) = 0\)):
\[
I(a) = \int_0^a \frac{\sqrt{\pi}}{2} e^{-t^2/4}\, dt.
\]
Substituting \(t = 2u\) (so \(dt = 2du\)):
\[
I(a) = \frac{\sqrt{\pi}}{2} \int_0^{a/2} e^{-u^2} \cdot 2\, du = \sqrt{\pi} \int_0^{a/2} e^{-u^2}\, du.
\]
Using the error function \(\text{erf}(z) = \frac{2}{\sqrt{\pi}} \int_0^z e^{-t^2}\, dt\), we rewrite:
\[
I(a) = \frac{\pi}{2} \text{erf}\left(\frac{a}{2}\right).
\]


### Step 3: Apply to the Original Integral
For \(a = \sqrt{3}\) and \(b = \frac{1}{\sqrt{3}}\), the original integral becomes:
\[
I(\sqrt{3}) - I\left(\frac{1}{\sqrt{3}}\right) = \frac{\pi}{2} \left[ \text{erf}\left(\frac{\sqrt{3}}{2}\right) - \text{erf}\left(\frac{1}{2\sqrt{3}}\right) \right].
\]


### Step 4: Numerical Approximation
Using precise values for the error function:
- \(\text{erf}\left(\frac{\sqrt{3}}{2}\right) \approx 0.781634060955\)
- \(\text{erf}\left(\frac{1}{2\sqrt{3}}\right) \approx 0.321350501263\)

Thus:
\[
\frac{\pi}{2} \left(0.781634060955 - 0.321350501263\right) \approx \frac{\pi}{2} \cdot 0.460283559692 \approx 0.7233035285.
\]


### Final Answer
The exact answer is \(\frac{\pi}{2} \left( \text{erf}\left(\frac{\sqrt{3}}{2}\right) - \text{erf}\left(\frac{1}{2\sqrt{3}}\right) \right)\), and the numerical approximation is \(0.7233035285\).

```json
{"answer": "\\frac{\\pi}{2} \\left( \\text{erf}\\left(\\frac{\\sqrt{3}}{2}\\right) - \\text{erf}\\left(\\frac{1}{2\\sqrt{3}}\\right) \\right)", "numerical_answer": "0.7233035285"}
```