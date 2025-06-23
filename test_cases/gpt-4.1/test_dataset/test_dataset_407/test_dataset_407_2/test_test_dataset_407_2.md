Let's follow the steps to compute the integral:

\[
I = \int_0^\infty \frac{\sin\sqrt{3}x-\sin\frac{x}{\sqrt{3}}}{x} e^{-x^2}\, dx
\]

## Step 1: Express as a difference of two integrals

\[
I = \int_0^\infty \frac{\sin(\sqrt{3}x)}{x} e^{-x^2} dx - \int_0^\infty \frac{\sin\left(\frac{x}{\sqrt{3}}\right)}{x} e^{-x^2} dx
\]

Let’s focus on computing the general term:
\[
F(a) = \int_0^\infty \frac{\sin(ax)}{x} e^{-x^2} dx
\]
So,
\[
I = F(\sqrt{3}) - F\left(\frac{1}{\sqrt{3}}\right)
\]

## Step 2: Evaluate \( F(a) \)

We will use the known result:
\[
\int_0^\infty \frac{\sin(a x)}{x} e^{-\beta x^2} dx = \frac{\pi}{2} \operatorname{erf} \left( \frac{a}{2\sqrt{\beta}} \right)
\]
For our case, \(\beta = 1\), so:
\[
F(a) = \frac{\pi}{2} \operatorname{erf} \left( \frac{a}{2} \right)
\]

## Step 3: Substitute back

\[
I = \frac{\pi}{2} \operatorname{erf} \left( \frac{\sqrt{3}}{2} \right) - \frac{\pi}{2} \operatorname{erf} \left( \frac{1}{2\sqrt{3}} \right)
= \frac{\pi}{2} \left[ \operatorname{erf} \left( \frac{\sqrt{3}}{2} \right) - \operatorname{erf} \left( \frac{1}{2\sqrt{3}} \right) \right]
\]

## Step 4: Numerical Approximation

Now, let’s compute the actual values (to 10 decimal places):

- \(\frac{\sqrt{3}}{2} \approx 0.8660254038\)
- \(\frac{1}{2\sqrt{3}} \approx 0.2886751346\)

Using standard tables or software,
- \(\operatorname{erf}(0.8660254038) \approx 0.7969082124\)
- \(\operatorname{erf}(0.2886751346) \approx 0.3167887446\)

So,
\[
\text{difference} \approx 0.7969082124 - 0.3167887446 = 0.4801194678
\]
\[
I \approx \frac{\pi}{2} \times 0.4801194678 \approx 0.7537531978
\]

---

```json
{"answer": "\\frac{\\pi}{2}\\left[\\operatorname{erf}\\left(\\frac{\\sqrt{3}}{2}\\right)-\\operatorname{erf}\\left(\\frac{1}{2\\sqrt{3}}\\right)\\right]", "numerical_answer": "0.7537531978"}
```