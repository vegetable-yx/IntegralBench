


To solve the definite integral \(\int_{\frac{1}{4}}^4 \frac{\tan^{-1}(x)}{x} \, dx\), we use the identity for the arctangent function and substitution.

### Step 1: Key Identity for Arctangent
For \(x > 0\), the arctangent function satisfies \(\tan^{-1}(x) + \tan^{-1}\left(\frac{1}{x}\right) = \frac{\pi}{2}\). This identity will simplify the integral.

### Step 2: Substitution
Let \(I = \int_{\frac{1}{4}}^4 \frac{\tan^{-1}(x)}{x} \, dx\). We substitute \(t = \frac{1}{x}\), so \(x = \frac{1}{t}\) and \(dx = -\frac{1}{t^2} dt\). When \(x = \frac{1}{4}\), \(t = 4\); when \(x = 4\), \(t = \frac{1}{4}\). The integral becomes:
\[
I = \int_{4}^{\frac{1}{4}} \frac{\tan^{-1}\left(\frac{1}{t}\right)}{\frac{1}{t}} \left(-\frac{1}{t^2}\right) dt = \int_{\frac{1}{4}}^4 \frac{\tan^{-1}\left(\frac{1}{t}\right)}{t} dt
\]
Renaming \(t\) back to \(x\), we have:
\[
I = \int_{\frac{1}{4}}^4 \frac{\tan^{-1}\left(\frac{1}{x}\right)}{x} dx
\]

### Step 3: Adding the Integrals
Adding the original integral \(I\) to this result:
\[
2I = \int_{\frac{1}{4}}^4 \left( \frac{\tan^{-1}(x)}{x} + \frac{\tan^{-1}\left(\frac{1}{x}\right)}{x} \right) dx
\]
Using the identity \(\tan^{-1}(x) + \tan^{-1}\left(\frac{1}{x}\right) = \frac{\pi}{2}\), the integrand simplifies to \(\frac{\pi}{2x}\):
\[
2I = \frac{\pi}{2} \int_{\frac{1}{4}}^4 \frac{1}{x} dx
\]

### Step 4: Evaluating the Integral
The integral of \(\frac{1}{x}\) is \(\ln|x|\). Evaluating from \(\frac{1}{4}\) to \(4\):
\[
\int_{\frac{1}{4}}^4 \frac{1}{x} dx = \ln(4) - \ln\left(\frac{1}{4}\right) = \ln(4) + \ln(4) = 2\ln(4)
\]
Thus:
\[
2I = \frac{\pi}{2} \cdot 2\ln(4) = \pi \ln(4)
\]
Since \(\ln(4) = 2\ln(2)\), we get \(I = \pi \ln(2)\).

### Numerical Approximation
The numerical value of \(\pi \ln(2)\) is approximately \(2.1775860903\) (rounded to 10 decimal places).

{"answer": "\(\pi \ln 2\)", "numerical_answer": "2.1775860903"}