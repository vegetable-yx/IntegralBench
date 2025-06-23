Let's compute the integral
\[
I = \int_0^\infty \frac{\sin(\sqrt{3}x) - \sin\left(\frac{x}{\sqrt{3}}\right)}{x} e^{-x^2} \, dx.
\]

## Step 1: Separate the integral

\[
I = \int_0^\infty \frac{\sin(\sqrt{3}x)}{x} e^{-x^2} dx - \int_0^\infty \frac{\sin\left(\frac{x}{\sqrt{3}}\right)}{x} e^{-x^2} dx.
\]

Let us call:
\[
I(a) = \int_0^\infty \frac{\sin(a x)}{x} e^{-x^2} dx
\]

Then, 
\[
I = I(\sqrt{3}) - I\left(\frac{1}{\sqrt{3}}\right)
\]

## Step 2: Analytically compute \( I(a) \)

Recall a standard integral formula (see Gradshteyn & Ryzhik 3.944.2, also can be derived via Laplace transform techniques):

\[
\int_0^\infty \frac{\sin(a x)}{x} e^{-b x^2} dx = \frac{\pi}{2} \operatorname{erf}\left( \frac{a}{2\sqrt{b}} \right), \quad a,b > 0
\]

Here, \(b = 1\):
\[
I(a) = \frac{\pi}{2} \operatorname{erf}\left( \frac{a}{2} \right)
\]

So:
\[
I = \frac{\pi}{2} \left[ \operatorname{erf}\left(\frac{\sqrt{3}}{2}\right) - \operatorname{erf}\left( \frac{1}{2\sqrt{3}} \right) \right]
\]

## Step 3: Numerical evaluation

Compute
- \(\frac{\sqrt{3}}{2} \approx 0.8660254038\)
- \(\frac{1}{2\sqrt{3}} \approx 0.2886751346\)

Values of the error function (\(\operatorname{erf}\)):
- \(\operatorname{erf}(0.8660254038) \approx 0.7989854110\)
- \(\operatorname{erf}(0.2886751346) \approx 0.3161464880\)

So their difference:
\[
0.7989854110 - 0.3161464880 = 0.482838923
\]

Multiply by \(\frac{\pi}{2}\):
\[
I \approx \frac{\pi}{2} \times 0.482838923 \approx 1.570796327 \times 0.482838923 \approx 0.7588915778
\]

Rounded to 10 decimal places: \(0.7588915778\)

## Final Answer

```json
{"answer": "\\frac{\\pi}{2}\\left[\\operatorname{erf}\\left(\\frac{\\sqrt{3}}{2}\\right)-\\operatorname{erf}\\left(\\frac{1}{2\\sqrt{3}}\\right)\\right]", "numerical_answer": "0.7588915778"}
```