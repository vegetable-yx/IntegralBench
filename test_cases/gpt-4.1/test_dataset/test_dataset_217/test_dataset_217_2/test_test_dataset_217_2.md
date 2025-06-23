Let's proceed step by step.

**Step 1. Analytic computation**

We are asked to compute:
\[
I = \int_0^1 x^{-3/4}(1-x)^{-3/4}\cos\left(2\sqrt{x(1-x)}\right)dx.
\]

Let us use the substitution \( x = \sin^2 \theta \), which implies \( 1-x = \cos^2\theta \), and \( dx = 2\sin\theta\cos\theta\,d\theta = \sin(2\theta)d\theta \). For \( x \) going from 0 to 1, \( \theta \) goes from 0 to \( \pi/2 \).

Now, compute the substituted terms:

- \( x^{-3/4} = (\sin^2\theta)^{-3/4} = (\sin\theta)^{-3/2} \)
- \( (1-x)^{-3/4} = (\cos^2\theta)^{-3/4} = (\cos\theta)^{-3/2} \)
- \( \sqrt{x(1-x)} = \sqrt{\sin^2\theta \cos^2\theta} = \sin\theta\cos\theta = \frac{1}{2}\sin(2\theta) \)
- \( dx = \sin(2\theta) d\theta \)

Substituting,
\[
I = \int_0^{\pi/2} (\sin\theta)^{-3/2} (\cos\theta)^{-3/2} \cos\left(2\cdot \frac{1}{2}\sin(2\theta)\right) \sin(2\theta)\,d\theta
\]
\[
= \int_0^{\pi/2} (\sin\theta)^{-3/2} (\cos\theta)^{-3/2} \cos(\sin(2\theta)) \sin(2\theta)\,d\theta
\]
But \( \sin(2\theta) = 2\sin\theta\cos\theta \), so:
\[
= \int_0^{\pi/2} (\sin\theta)^{-3/2} (\cos\theta)^{-3/2} \cos(\sin(2\theta)) \cdot 2\sin\theta\cos\theta\,d\theta
\]
\[
= 2 \int_0^{\pi/2} (\sin\theta)^{-1/2} (\cos\theta)^{-1/2} \cos(\sin(2\theta))\,d\theta
\]

So
\[
I = 2 \int_0^{\pi/2} \frac{\cos(\sin 2\theta)}{(\sin\theta)^{1/2} (\cos\theta)^{1/2}} d\theta
\]

Now, recall the following integral representation for the Bessel function:
\[
J_0(a) = \frac{1}{\pi} \int_0^{\pi} \cos(a \sin\theta) d\theta
\]
More generally, in Gradshteyn & Ryzhik 3.944.3,
\[
\int_0^{\pi/2} \sin^{\mu-1}\theta\,\cos^{\nu-1}\theta\,\cos\left(a\,\sin 2\theta\right) d\theta = \frac{1}{2} \Gamma\left(\frac{\mu}{2}\right)\Gamma\left(\frac{\nu}{2}\right) a^{1-\mu-\nu} J_{\mu+\nu-1}(a)\,/\,\Gamma\left(\frac{\mu+\nu}{2}\right)
\]
But our integral is:
\[
2 \int_0^{\pi/2} (\sin\theta)^{-1/2} (\cos\theta)^{-1/2} \cos(\sin 2\theta) d\theta
\]
This matches the above formula for \( a=1, \mu = \nu = 1/2 \):

So, set \( \mu = \nu = 1/2 \):

\[
I = 2 \int_0^{\pi/2} \sin^{-1/2}\theta\,\cos^{-1/2}\theta\,\cos(\sin 2\theta)\,d\theta
\]
Apply the formula:
\[
\int_0^{\pi/2} \sin^{\mu-1}\theta\,\cos^{\nu-1}\theta\,\cos(a\,\sin 2\theta)\,d\theta = \frac{1}{2}\Gamma\left(\frac{\mu}{2}\right)\Gamma\left(\frac{\nu}{2}\right)a^{1-\mu-\nu}J_{\mu+\nu-1}(a)/\Gamma\left(\frac{\mu+\nu}{2}\right)
\]
Plug in \( \mu = \nu = 1/2 \):
- \( \Gamma(1/4) \) appears
- \( a^{1-(1/2)-(1/2)} = a^{0} = 1 \)
- \( J_{(1/2)+(1/2)-1}(a) = J_{0}(a) \)
- \( (\mu+\nu)/2 = (1/2+1/2)/2 = 1/2 \), so \( \Gamma(1/2) \)

So:
\[
I = 2 \cdot \frac{1}{2}\Gamma\left(\frac{1}{4}\right)^2 \frac{J_0(1)}{\Gamma(1/2)}
= \Gamma\left(\frac{1}{4}\right)^2 \frac{J_0(1)}{\Gamma(1/2)}
\]

Recall that \( \Gamma(1/2) = \sqrt{\pi} \).

Therefore,
\[
I = \frac{\Gamma(1/4)^2}{\sqrt{\pi}}\,J_0(1)
\]

**Step 2. Final exact answer**

\[
\boxed{I = \frac{\Gamma\left(\frac{1}{4}\right)^2}{\sqrt{\pi}}\, J_0(1)}
\]

**Step 3. Numerical Value**

- \( \Gamma(1/4)\approx 3.6256099082 \)
- \( \sqrt{\pi} \approx 1.7724538509 \)
- \( J_0(1) \approx 0.7651976866 \)

So,
\[
I \approx \frac{(3.6256099082)^2}{1.7724538509}\cdot 0.7651976866
\]
\[
(3.6256099082)^2 = 13.1497178777
\]
\[
13.1497178777 / 1.7724538509 = 7.4246674476
\]
\[
7.4246674476 \times 0.7651976866 = 5.6833707432
\]

So, rounded to 10 decimal places:
\[
I \approx 5.6833707432
\]

**Step 4. JSON output**
```json
{"answer": "\\frac{\\Gamma\\left(\\frac{1}{4}\\right)^2}{\\sqrt{\\pi}}\\ J_0(1)", "numerical_answer": "5.6833707432"}
```