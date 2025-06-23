To compute the definite integral \(\int_0^{5\pi/2}\frac{dx}{2+\cos x}\), we follow these steps:

### Step 1: Use the Substitution \( t = \tan\left(\frac{x}{2}\right) \)
This substitution is standard for integrals involving \( \frac{1}{a + \cos x} \). Recall that:
\[
\cos x = \frac{1 - t^2}{1 + t^2}, \quad dx = \frac{2}{1 + t^2} dt
\]
Substituting these into the integral:
\[
\int \frac{dx}{2 + \cos x} = \int \frac{\frac{2}{1 + t^2}}{2 + \frac{1 - t^2}{1 + t^2}} dt = \int \frac{2}{(1 + t^2)\left(2 + \frac{1 - t^2}{1 + t^2}\right)} dt
\]
Simplify the denominator:
\[
2 + \frac{1 - t^2}{1 + t^2} = \frac{2(1 + t^2) + 1 - t^2}{1 + t^2} = \frac{3 + t^2}{1 + t^2}
\]
Thus, the integral becomes:
\[
\int \frac{2}{(1 + t^2)\left(\frac{3 + t^2}{1 + t^2}\right)} dt = \int \frac{2}{3 + t^2} dt
\]
This simplifies to:
\[
2 \int \frac{1}{3 + t^2} dt = \frac{2}{\sqrt{3}} \arctan\left(\frac{t}{\sqrt{3}}\right) + C
\]
Substituting back \( t = \tan\left(\frac{x}{2}\right) \):
\[
\frac{2}{\sqrt{3}} \arctan\left(\frac{\tan\left(\frac{x}{2}\right)}{\sqrt{3}}\right) + C
\]

### Step 2: Evaluate the Definite Integral from \( 0 \) to \( \frac{5\pi}{2} \)
The antiderivative is periodic with period \( 2\pi \), so we can evaluate it over the interval \( [0, 2\pi] \) and multiply by the number of full periods, plus the remaining part.

First, compute the integral over one full period \( [0, 2\pi] \):
\[
\int_0^{2\pi} \frac{dx}{2 + \cos x} = \left. \frac{2}{\sqrt{3}} \arctan\left(\frac{\tan\left(\frac{x}{2}\right)}{\sqrt{3}}\right) \right|_0^{2\pi}
\]
At \( x = 2\pi \), \( \tan\left(\frac{x}{2}\right) = \tan(\pi) = 0 \), and at \( x = 0 \), \( \tan(0) = 0 \). However, the antiderivative is discontinuous at \( x = \pi \), so we split the integral:
\[
\int_0^{2\pi} \frac{dx}{2 + \cos x} = \lim_{a \to \pi^-} \int_0^a \frac{dx}{2 + \cos x} + \lim_{b \to \pi^+} \int_b^{2\pi} \frac{dx}{2 + \cos x}
\]
Evaluating these:
\[
\lim_{a \to \pi^-} \left[ \frac{2}{\sqrt{3}} \arctan\left(\frac{\tan\left(\frac{a}{2}\right)}{\sqrt{3}}\right) - \frac{2}{\sqrt{3}} \arctan(0) \right] = \frac{2}{\sqrt{3}} \left( \frac{\pi}{2} - 0 \right) = \frac{\pi}{\sqrt{3}}
\]
\[
\lim_{b \to \pi^+} \left[ \frac{2}{\sqrt{3}} \arctan(0) - \frac{2}{\sqrt{3}} \arctan\left(\frac{\tan\left(\frac{b}{2}\right)}{\sqrt{3}}\right) \right] = \frac{2}{\sqrt{3}} \left( 0 - (-\frac{\pi}{2}) \right) = \frac{\pi}{\sqrt{3}}
\]
Adding these gives:
\[
\int_0^{2\pi} \frac{dx}{2 + \cos x} = \frac{2\pi}{\sqrt{3}}
\]

Now, for \( \int_0^{5\pi/2} \frac{dx}{2 + \cos x} \), note that \( \frac{5\pi}{2} = 2\pi + \frac{\pi}{2} \). Thus:
\[
\int_0^{5\pi/2} \frac{dx}{2 + \cos x} = \int_0^{2\pi} \frac{dx}{2 + \cos x} + \int_{2\pi}^{5\pi/2} \frac{dx}{2 + \cos x}
\]
The first term is \( \frac{2\pi}{\sqrt{3}} \). For the second term, let \( u = x - 2\pi \), so \( du = dx \), and the integral becomes:
\[
\int_{0}^{\pi/2} \frac{du}{2 + \cos u}
\]
Evaluating this:
\[
\left. \frac{2}{\sqrt{3}} \arctan\left(\frac{\tan\left(\frac{u}{2}\right)}{\sqrt{3}}\right) \right|_0^{\pi/2} = \frac{2}{\sqrt{3}} \left( \arctan\left(\frac{1}{\sqrt{3}}\right) - \arctan(0) \right) = \frac{2}{\sqrt{3}} \left( \frac{\pi}{6} - 0 \right) = \frac{\pi}{3\sqrt{3}}
\]
Adding the two parts:
\[
\int_0^{5\pi/2} \frac{dx}{2 + \cos x} = \frac{2\pi}{\sqrt{3}} + \frac{\pi}{3\sqrt{3}} = \frac{7\pi}{3\sqrt{3}}
\]
Rationalizing the denominator:
\[
\frac{7\pi}{3\sqrt{3}} = \frac{7\pi \sqrt{3}}{9}
\]

### Step 3: Numerical Approximation
The exact answer is \( \frac{7\pi \sqrt{3}}{9} \). Numerically:
\[
\frac{7\pi \sqrt{3}}{9} \approx 4.224504683
\]

### Final Answer
```json
{"answer": "\\frac{7\\pi \\sqrt{3}}{9}", "numerical_answer": "4.2245046830"}
```