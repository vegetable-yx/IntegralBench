Let's compute the integral:
\[
I = \int_0^{\frac{\pi}{2}}\frac{\ln(\sin x)}{\cos^2 x} \, dx
\]

## Step 1: Substitution

Let’s use the substitution \( u = \tan x \).

- When \( x = 0 \), \( u = 0 \)
- When \( x = \frac{\pi}{2} \), \( u \to +\infty \)
- \( dx = \frac{du}{1 + u^2} \)
- \( \sin x = \frac{u}{\sqrt{1+u^2}} \)
- \( \cos^2 x = \frac{1}{1 + u^2} \)

So,
\[
I = \int_{x=0}^{x=\frac{\pi}{2}} \frac{\ln \left( \sin x \right)}{\cos^2 x}\, dx
  = \int_{u=0}^{u=\infty} \ln \left( \frac{u}{\sqrt{1+u^2}} \right) \cdot (1+u^2) \cdot \frac{du}{1+u^2}
\]

So,
\[
I = \int_0^{\infty} \ln \left( \frac{u}{\sqrt{1+u^2}} \right) du
  = \int_0^{\infty} \left[ \ln u - \frac{1}{2}\ln(1+u^2) \right] du
\]

## Step 2: Split the integral

\[
I = \int_0^{\infty} \ln u \, du - \frac{1}{2}\int_0^{\infty} \ln(1 + u^2) du
\]

But these integrals, as written, diverge (the integral of \(\ln u\) over \(0\) to \(\infty\) doesn't converge). However, their combination is well-defined arising from the original definite integral.

Let's instead recall a powerful technique: use differentiation under the integral sign or known results for integrals involving \(\ln(\sin x)\).

## Step 3: Recognize a known result

There are classical definite integrals involving \(\ln(\sin x)\):

A well-known result is:
\[
\int_0^{\pi} \ln(\sin x) dx = -\pi \ln 2
\]

Let’s try integrating by parts.

Let:
- \( u = \ln(\sin x) \)
- \( dv = \sec^2 x dx \)

Then:
- \( du = \cot x dx \)
- \( v = \tan x \)

Integrating by parts:
\[
I = \left[ \ln(\sin x) \tan x \right]_0^{\frac{\pi}{2}} - \int_0^{\frac{\pi}{2}} \tan x \cdot \cot x\, dx
\]

But \(\tan x \cdot \cot x = 1\), so
\[
I = \left[ \ln(\sin x) \tan x \right]_0^{\frac{\pi}{2}} - \int_0^{\frac{\pi}{2}} dx
= \left[ \ln(\sin x) \tan x \right]_0^{\frac{\pi}{2}} - \frac{\pi}{2}
\]

Check the boundary terms:

- As \(x \to 0\): \(\ln(\sin x) \sim \ln x\), \(\tan x \sim x\) so their product is \(x \ln x \to 0\).

- As \(x \to \frac{\pi}{2}\):
  - \(\sin x \to 1\), \(\ln(\sin x) \to 0\)
  - \(\tan x \to +\infty\)
  - But in fact, near \(x = \frac{\pi}{2}\), \(\sin x \approx 1\), \(\tan x \sim \frac{1}{\frac{\pi}{2} - x}\)
  - \(\ln(\sin x) \sim -\frac{1}{2} (x - \frac{\pi}{2})^2\) (from Taylor expansions)
  - Product tends to zero as \(x \to \frac{\pi}{2}\), so the upper limit is zero.

Therefore,

\[
I = 0 - \frac{\pi}{2} = -\frac{\pi}{2}
\]

## Step 4: Numerical approximation

\[
-\frac{\pi}{2} \approx -1.5707963268
\]

## Step 5: Final result in JSON

```json
{"answer": "-\\frac{\\pi}{2}", "numerical_answer": "-1.5707963268"}
```