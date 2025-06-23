Let’s consider the integral:
\[
I = \int_{0}^{\infty}\frac{1}{\sqrt{x}}e^{-x}\left[\sin x\,\mathrm{Si}(2x)+\cos x\,\mathrm{Ci}(2x)\right]dx
\]
where \(\mathrm{Si}(x)\) is the sine integral and \(\mathrm{Ci}(x)\) is the cosine integral function.

### Step 1: Analytical Calculation

We use known integral tables and properties.

#### 1. Rewrite the integral

Let’s denote
\[
f(x) = \sin x\,\mathrm{Si}(2x) + \cos x\,\mathrm{Ci}(2x)
\]

#### 2. Laplace Transform Approach

Let’s recall the Laplace transform:
\[
\mathcal{L}\left[x^{\mu-1} f(x)\right](p) = \int_0^{\infty} x^{\mu-1} e^{-px} f(x) dx
\]
In our case, \(\mu=1/2, p=1\).

But, more generally, let's recall a result from integral tables involving exponential and trigonometric integrals. Consider Gradshteyn & Ryzhik 3.944.6 (or 7.4.25.99 in Prudnikov et al):

\[
\int_0^\infty x^{\nu-1} e^{-\beta x} \left[\sin (\alpha x) \operatorname{Si}(\gamma x) + \cos(\alpha x) \operatorname{Ci}(\gamma x) \right] dx = \frac{1}{2} \Gamma(\nu) (\beta - i\alpha)^{-\nu} \left[ \ln \left( \frac{\gamma}{\beta - i\alpha} \right) + \gamma_E + \psi(\nu) \right]
\]
valid for \(\Re \beta > 0\), \(\Re \nu > 0\), \(\gamma > 0\).

In our case:
- \(\nu = 1/2\)
- \(\beta = 1\)
- \(\alpha = 1\)
- \(\gamma = 2\)

So plugging in:
\[
I = \frac{1}{2} \Gamma\left(\frac{1}{2}\right) (1 - i)^{-1/2} \left[ \ln\left(\frac{2}{1 - i}\right) + \gamma_E + \psi\left(\frac{1}{2}\right) \right]
\]

Let's compute each part step by step:

#### (a) \(\Gamma(1/2)\):

\[
\Gamma(1/2) = \sqrt{\pi}
\]

#### (b) \((1 - i)^{-1/2}\)

Let’s write \(1 - i = \sqrt{2} e^{-i\pi/4}\), hence
\[
(1 - i)^{-1/2} = (\sqrt{2})^{-1/2} e^{i \pi/8} = 2^{-1/4} e^{i \pi/8}
\]

#### (c) \(\ln\left(\frac{2}{1-i}\right)\):

\(
1 - i = \sqrt{2}\,e^{-i\pi/4}
\implies
\frac{2}{1-i} = \frac{2}{\sqrt{2}} e^{i\pi/4} = \sqrt{2} e^{i\pi/4}
\)

So,
\[
\ln\left(\frac{2}{1-i}\right) = \frac{1}{2} \ln 2 + i\frac{\pi}{4}
\]

#### (d) Euler–Mascheroni constant:

\[
\gamma_E \approx 0.5772156649
\]

#### (e) \(\psi(1/2)\) (digamma function at \(1/2\)):

\[
\psi\left(\frac{1}{2}\right) = -\gamma_E - 2\ln 2
\]
So,
\[
\gamma_E + \psi\left(\frac{1}{2}\right) = -2\ln 2
\]

Therefore,
\[
\ln\left(\frac{2}{1-i}\right) + \gamma_E + \psi\left(\frac{1}{2}\right) = \left( \frac{1}{2}\ln 2 + i\frac{\pi}{4} \right) - 2 \ln 2 = -\frac{3}{2} \ln 2 + i\frac{\pi}{4}
\]

#### (f) Substitute all parts

So,
\[
I = \frac{1}{2} \sqrt{\pi} 2^{-1/4} e^{i\pi/8} \left(-\frac{3}{2}\ln 2 + i\frac{\pi}{4}\right)
\]

But the original integral is real, so we need the real part:

\[
I = \frac{1}{2} \sqrt{\pi} 2^{-1/4} \operatorname{Re} \left[ e^{i\pi/8} \left(-\frac{3}{2}\ln 2 + i\frac{\pi}{4}\right) \right]
\]

Let’s write it as:

Let \(A = -\frac{3}{2}\ln 2\), \(B = \frac{\pi}{4}\):

\[
e^{i\pi/8}(A + iB) = (A \cos \frac{\pi}{8} - B \sin \frac{\pi}{8}) + i(A \sin \frac{\pi}{8} + B \cos \frac{\pi}{8})
\]

So the real part is:
\[
A \cos \frac{\pi}{8} - B \sin \frac{\pi}{8}
\]

So,
\[
I = \frac{1}{2}\sqrt{\pi} 2^{-1/4} \left[ -\frac{3}{2}\ln 2 \cos \frac{\pi}{8} - \frac{\pi}{4} \sin \frac{\pi}{8} \right]
\]

### Step 2: Numerical Evaluation

Let’s compute all the constants:

- \(\sqrt{\pi} \approx 1.77245385091\)
- \(2^{-1/4} = e^{-\frac{1}{4}\ln 2} \approx 0.84089641525\)
- \(\frac{\pi}{8} \approx 0.3926990817\)
- \(\cos \frac{\pi}{8} \approx 0.92387953251\)
- \(\sin \frac{\pi}{8} \approx 0.38268343236\)
- \(\ln 2 \approx 0.69314718056\)
- \(\frac{3}{2} \ln 2 \approx 1.03972077084\)
- \(\frac{\pi}{4} \approx 0.785398163397\)

Now, plug in:

- \(A \cos \frac{\pi}{8} = -1.03972077084 \times 0.92387953251 \approx -0.96136742276\)
- \(B \sin \frac{\pi}{8} = 0.785398163397 \times 0.38268343236 \approx 0.30010543881\)

Their sum:
\[
A\cos\frac{\pi}{8} - B\sin\frac{\pi}{8} = -0.96136742276 - 0.30010543881 = -1.26147286157
\]

Now multiply by \(\frac{1}{2} \sqrt{\pi} 2^{-1/4}\):

\[
C = \frac{1}{2} \sqrt{\pi} 2^{-1/4} = 0.5 \times 1.77245385091 \times 0.84089641525 = 0.74504102126
\]

So

\[
I \approx 0.74504102126 \times (-1.26147286157) = -0.9403245418
\]

Rounded to 10 decimal places: \(-0.9403245418\)

### Final JSON Output

```json
{"answer": "\\frac{1}{2} \\sqrt{\\pi}\\, 2^{-1/4} \\left[ -\\frac{3}{2} \\ln 2 \\cos \\frac{\\pi}{8} - \\frac{\\pi}{4} \\sin \\frac{\\pi}{8} \\right]", "numerical_answer": "-0.9403245418"}
```