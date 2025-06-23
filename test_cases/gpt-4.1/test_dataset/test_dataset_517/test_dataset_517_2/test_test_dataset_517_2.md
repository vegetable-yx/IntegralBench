Let's solve the integral:
\[
I = \int_{-\infty}^{\infty} e^{-2x^2 - 5x - 3} \, dx
\]

**Step 1: Complete the square in the exponent.**

\[
-2x^2 - 5x - 3 = -2\left(x^2 + \frac{5}{2}x\right) - 3
\]

Complete the square for \(x^2 + \frac{5}{2}x\):

- Half of \(\frac{5}{2}\) is \(\frac{5}{4}\), square it: \(\left(\frac{5}{4}\right)^2 = \frac{25}{16}\).
- So,
  \[
  x^2 + \frac{5}{2}x = \left(x + \frac{5}{4}\right)^2 - \frac{25}{16}.
  \]
- Plug back:
  \[
  -2\left[ \left(x + \frac{5}{4}\right)^2 - \frac{25}{16} \right] - 3
  = -2\left(x + \frac{5}{4}\right)^2 + 2 \cdot \frac{25}{16} - 3
  = -2\left(x + \frac{5}{4}\right)^2 + \frac{25}{8} - 3
  = -2\left(x + \frac{5}{4}\right)^2 + \frac{25 - 24}{8}
  = -2\left(x + \frac{5}{4}\right)^2 + \frac{1}{8}
  \]

**Step 2: Rewrite the integral using the completed square.**

\[
I = \int_{-\infty}^{\infty} e^{-2x^2 - 5x - 3} dx = \int_{-\infty}^{\infty} e^{-2(x + \frac{5}{4})^2 + \frac{1}{8}} dx
= e^{1/8} \int_{-\infty}^{\infty} e^{-2(x + \frac{5}{4})^2} dx
\]

**Step 3: Make a substitution to reduce to a standard Gaussian.**

Let \(y = x + \frac{5}{4}\), so \(dy = dx\):
\[
I = e^{1/8} \int_{-\infty}^{\infty} e^{-2y^2} dy
\]

**Step 4: Evaluate the Gaussian integral.**

Recall:
\[
\int_{-\infty}^{\infty} e^{-a y^2} dy = \sqrt{\frac{\pi}{a}}
\]
Here, \(a = 2\), so:
\[
\int_{-\infty}^{\infty} e^{-2y^2} dy = \sqrt{\frac{\pi}{2}}
\]
Hence,
\[
I = e^{1/8} \cdot \sqrt{\frac{\pi}{2}}
\]

**Step 5: Substitute back and write the exact answer.**

\[
\boxed{I = e^{1/8} \sqrt{\frac{\pi}{2}}}
\]

**Step 6: Numerical approximation (rounded to 10 decimal places).**

Calculations:
- \(e^{1/8} \approx 1.1331484531\)
- \(\sqrt{\pi/2} \approx 1.2533141373\)
- Product: \(1.1331484531 \times 1.2533141373 \approx 1.4216166538\)

**Final answer:**  
```json
{"answer": "e^{1/8} \\sqrt{\\frac{\\pi}{2}}", "numerical_answer": "1.4216166538"}
```