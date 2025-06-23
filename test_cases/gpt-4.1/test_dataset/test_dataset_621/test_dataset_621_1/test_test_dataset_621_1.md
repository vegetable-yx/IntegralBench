Let's denote the integral as \( I \):

\[
I = \int_0^{\frac{\pi}{2}} \frac{\ln(\sin x)}{\cos^2 x} \, dx
\]

**Step 1: Analytical Calculation**

Let us use substitution:

Let \( u = \tan x \). Then, \( x = \arctan u \) and when \( x = 0 \), \( u = 0 \); when \( x = \frac{\pi}{2} \), \( u \to +\infty \).

Note:
\[
\sin x = \frac{u}{\sqrt{1+u^2}},\qquad 
dx = \frac{du}{1+u^2},\qquad 
\cos^2 x = \frac{1}{1+u^2}
\]

So,
\[
\frac{dx}{\cos^2 x} = \frac{du}{1+u^2} \cdot (1+u^2) = du
\]

Thus:
\[
I = \int_{u=0}^{u=\infty} \ln\left(\frac{u}{\sqrt{1+u^2}}\right) du
  = \int_0^{\infty} [\ln u - \frac{1}{2} \ln(1+u^2)] du
\]

Next, split the integral:
\[
I = \int_0^{\infty} \ln u\, du - \frac{1}{2} \int_0^{\infty} \ln(1+u^2)\, du
\]

But both integrals diverge, so let's reconsider.

Let’s instead integrate by parts the original integral:

Let’s set:
\[
u = \ln(\sin x), \quad dv = \frac{dx}{\cos^2 x}
\]
Then \( du = \cot x\, dx \), and \( v = \tan x \).

So integration by parts gives:
\[
I = uv \Big|_0^{\frac{\pi}{2}} - \int_0^{\frac{\pi}{2}} v\, du
\]
\[
= \ln(\sin x) \tan x \Big|_0^{\frac{\pi}{2}} - \int_0^{\frac{\pi}{2}} \tan x \cot x\, dx
\]

Now, evaluate the boundary terms:
- As \( x \to 0 \): \(\ln(\sin x) \to -\infty \), \( \tan x \to 0 \), their product tends to 0.
- As \( x \to \frac{\pi}{2} \): \(\tan x \to +\infty \), \( \sin x \to 1 \), so \( \ln(\sin x) \to 0 \), total is 0.

So, the boundary terms vanish. Now,

\[
I = - \int_0^{\frac{\pi}{2}} \tan x \cot x\, dx
\]

Note that \(\tan x \cot x = 1\), since \(\tan x = \frac{\sin x}{\cos x}\), \(\cot x = \frac{\cos x}{\sin x}\).

Therefore:
\[
I = - \int_0^{\frac{\pi}{2}} 1\, dx = - \left[ x \right]_0^{\frac{\pi}{2}} = -\frac{\pi}{2}
\]

**Step 2: Numerical value rounded to 10 decimal places**

\[
-\frac{\pi}{2} \approx -1.5707963268
\]

**Step 3: JSON answer**

```json
{"answer": "-\\frac{\\pi}{2}", "numerical_answer": "-1.5707963268"}
```