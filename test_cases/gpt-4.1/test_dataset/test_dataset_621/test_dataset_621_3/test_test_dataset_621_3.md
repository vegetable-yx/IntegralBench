Let's compute the definite integral
\[
I = \int_0^{\frac{\pi}{2}} \frac{\ln(\sin x)}{\cos^2 x}\, dx.
\]

**Step 1: Substitution**

Let \( u = \tan x \), so
\[
x = \arctan u,\quad dx = \frac{du}{1 + u^2}.
\]
As \( x \) goes from \( 0 \) to \( \frac{\pi}{2} \), \( u \) goes from \( 0 \) to \( +\infty \).
Also,
\[
\sin x = \frac{u}{\sqrt{1 + u^2}}, \quad \cos x = \frac{1}{\sqrt{1 + u^2}},
\]
therefore,
\[
\cos^2 x = \frac{1}{1 + u^2},
\]
so
\[
\frac{1}{\cos^2 x} dx = (1 + u^2) dx = du.
\]

Now,
\[
\ln(\sin x) = \ln u - \frac{1}{2} \ln(1 + u^2).
\]

Thus,
\[
I = \int_0^{+\infty} \left[ \ln u - \frac{1}{2} \ln(1 + u^2) \right] du
\]

But, the integral of \(\ln u\) from 0 to infinity does not converge; however, consider the structure:
Since we have:
\[
I = \int_0^{+\infty} \ln u \, du - \frac{1}{2} \int_0^{+\infty} \ln(1 + u^2)\, du
\]

But both terms diverge; perhaps let's process the integral in another way.

---

Let's integrate by parts:

Let \( u = \ln(\sin x) \), \( dv = \sec^2 x dx \).

Then:
- \( du = \cot x dx \)
- \( v = \tan x \)

Thus,
\[
I = \left. \ln(\sin x) \tan x \right|_0^{\frac{\pi}{2}} - \int_0^{\frac{\pi}{2}} \tan x \cot x dx
\]

Compute boundary term:

As \( x \to 0 \):
- \( \ln(\sin x) \sim \ln x \to -\infty \)
- \( \tan x \sim x \to 0 \)
- So \( \ln x \cdot x \to 0 \) (since \( x \ln x \to 0 \) as \( x \to 0 \)).

As \( x \to \frac{\pi}{2} \):
- \( \ln(\sin x) \to \ln(1) = 0 \)
- \( \tan x \to +\infty \)
- But \( \ln(\sin x) \to -\infty \) very quickly as \( x \to \frac{\pi}{2}^- \).

But actually, \( \sin x \sim 1 - \frac{1}{2} (x - \frac{\pi}{2})^2 \) so \( \ln(\sin x) \sim -\frac{1}{2} (x-\frac{\pi}{2})^2 \).
\( \tan x \sim \frac{1}{\frac{\pi}{2} - x} \).
So the product tends to 0.

Therefore, the boundary term vanishes.

So
\[
I = - \int_0^{\frac{\pi}{2}} \tan x \cot x dx
\]
But
\[
\tan x \cot x = \frac{\sin x}{\cos x} \cdot \frac{\cos x}{\sin x} = 1
\]

So:
\[
I = - \int_0^{\frac{\pi}{2}} 1 dx = -\frac{\pi}{2}
\]

---

**Step 2: Check correctness of sign and steps:**

Yes, integrating by parts as above, we get the result:

\[
\boxed{I = -\frac{\pi}{2}}
\]

---

**Step 3: Numerical approximation**

\[
-\frac{\pi}{2} \approx -1.5707963268
\]

---

**Step 4: JSON Output**

```json
{"answer": "-\\frac{\\pi}{2}", "numerical_answer": "-1.5707963268"}
```