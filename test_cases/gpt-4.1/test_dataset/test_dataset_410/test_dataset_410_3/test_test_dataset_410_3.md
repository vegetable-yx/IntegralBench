Let's proceed step by step.

### 1. Compute the integral analytically

Consider the integral:
\[
I = \int_0^\infty e^{-x^2}\cos(2x) \, dx
\]

It is helpful to recall the following formula for \( a > 0 \), \( b \in \mathbb{R} \):
\[
\int_0^\infty e^{-a x^2} \cos(bx) dx = \frac{1}{2}\sqrt{\frac{\pi}{a}} \exp\left(-\frac{b^2}{4a}\right)
\]

Here \( a = 1 \), \( b = 2 \):
\[
I = \frac{1}{2} \sqrt{\pi} \exp\left(-\frac{(2)^2}{4}\right)
\]
\[
I = \frac{1}{2} \sqrt{\pi} \exp\left(-1\right)
\]

### 2. All necessary steps

- Recognize the standard form and substitute \( a = 1, b = 2 \).
- Plug into the formula:
  \[
  I = \frac{1}{2} \sqrt{\pi/a} \cdot e^{-b^2/(4a)}
  \]
- Simplify \( \sqrt{\pi/1} = \sqrt{\pi} \), \( b^2/(4a) = 4/4 = 1 \):
  \[
  I = \frac{1}{2} \sqrt{\pi} e^{-1}
  \]

### 3. Numerical approximation

Let’s compute \( \frac{1}{2}\sqrt{\pi}e^{-1} \):

- \( \sqrt{\pi} \approx 1.7724538509 \)
- \( e^{-1} \approx 0.3678794412 \)

So:
\[
I \approx \frac{1}{2} \times 1.7724538509 \times 0.3678794412 \approx 0.6503803654 \times 0.5 = 0.3251901827
\]

But let's verify:
\[
1.7724538509 \times 0.3678794412 = 0.6518986469
\]
\[
0.6518986469 \times \frac{1}{2} = 0.3259493235
\]

So the numerical value, rounded to 10 decimal places, is:

\[
0.3259493235
\]

### 4. JSON output

```json
{"answer": "\\frac{1}{2} \\sqrt{\\pi} e^{-1}", "numerical_answer": "0.3259493235"}
```