To solve the definite integral \(\int_0^{\frac{\pi}{2}}\frac{\ln(\sin x)}{\cos^2x}\mathrm{d}x\), we will follow these steps:

### Step 1: Substitution
Let \( u = \tan x \). Then, \( \mathrm{d}u = \sec^2 x \, \mathrm{d}x \), and \( \cos^2 x = \frac{1}{1 + u^2} \). The limits change as follows:
- When \( x = 0 \), \( u = 0 \).
- When \( x = \frac{\pi}{2} \), \( u \to \infty \).

The integral becomes:
\[
\int_0^{\infty} \ln\left(\frac{u}{\sqrt{1 + u^2}}\right) \cdot (1 + u^2) \, \mathrm{d}u
\]
Simplify the integrand:
\[
\ln\left(\frac{u}{\sqrt{1 + u^2}}\right) = \ln u - \frac{1}{2} \ln(1 + u^2)
\]
Thus, the integral splits into two parts:
\[
\int_0^{\infty} \ln u \cdot (1 + u^2) \, \mathrm{d}u - \frac{1}{2} \int_0^{\infty} \ln(1 + u^2) \cdot (1 + u^2) \, \mathrm{d}u
\]

### Step 2: Evaluate the Integrals
The first integral is:
\[
\int_0^{\infty} \ln u \cdot (1 + u^2) \, \mathrm{d}u
\]
This integral diverges because \(\ln u\) grows without bound as \(u \to 0^+\) and \(u \to \infty\).

However, we can consider the original integral in terms of \(x\) and use integration by parts. Let:
\[
I = \int_0^{\frac{\pi}{2}} \frac{\ln(\sin x)}{\cos^2 x} \, \mathrm{d}x
\]
Let \( v = \tan x \), then \( \mathrm{d}v = \sec^2 x \, \mathrm{d}x \), and the integral becomes:
\[
I = \int_0^{\infty} \ln\left(\frac{v}{\sqrt{1 + v^2}}\right) \, \mathrm{d}v
\]
This simplifies to:
\[
I = \int_0^{\infty} \ln v \, \mathrm{d}v - \frac{1}{2} \int_0^{\infty} \ln(1 + v^2) \, \mathrm{d}v
\]
Both of these integrals diverge, which suggests that the original integral may not converge.

### Step 3: Re-evaluate the Approach
Let's reconsider the substitution. Let \( u = \sin x \), then \( \mathrm{d}u = \cos x \, \mathrm{d}x \), and \( \cos^2 x = 1 - u^2 \). The integral becomes:
\[
\int_0^{1} \frac{\ln u}{1 - u^2} \, \mathrm{d}u
\]
This integral is known and evaluates to:
\[
\int_0^{1} \frac{\ln u}{1 - u^2} \, \mathrm{d}u = -\frac{\pi^2}{8}
\]

### Step 4: Numerical Approximation
The numerical approximation of \(-\frac{\pi^2}{8}\) is approximately \(-1.23370055014\).

### Final Answer
```json
{"answer": "-\\frac{\\pi^2}{8}", "numerical_answer": "-1.2337005501"}
```