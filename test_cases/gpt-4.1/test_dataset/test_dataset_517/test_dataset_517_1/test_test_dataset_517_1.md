Let's solve the integral:
\[
I = \int_{-\infty}^{\infty} e^{-2x^2 - 5x - 3} \, dx
\]

**Step 1: Combine and Complete the Square**

Combine the quadratic and linear terms in the exponent:
\[
-2x^2 - 5x - 3 = -2 \left( x^2 + \frac{5}{2}x \right) - 3
\]

Complete the square for \( x^2 + \frac{5}{2}x \):

The coefficient of \( x \) is \( \frac{5}{2} \). Half that is \( \frac{5}{4} \), and the square is \( \frac{25}{16} \):

\[
x^2 + \frac{5}{2}x = \left( x + \frac{5}{4} \right)^2 - \frac{25}{16}
\]

Therefore,
\[
-2\left( x^2 + \frac{5}{2}x \right) = -2 \left[ \left( x + \frac{5}{4} \right)^2 - \frac{25}{16} \right] = -2 \left( x + \frac{5}{4} \right)^2 + \frac{25}{8}
\]

So, the exponent becomes:
\[
-2x^2 - 5x - 3 = -2 \left( x + \frac{5}{4} \right)^2 + \frac{25}{8} - 3 = -2 \left( x + \frac{5}{4} \right)^2 + \frac{25 - 24}{8} = -2 \left( x + \frac{5}{4} \right)^2 + \frac{1}{8}
\]

**Step 2: Rewrite the Integral**

\[
I = \int_{-\infty}^\infty \exp \left( -2 \left( x+\frac{5}{4} \right)^2 + \frac{1}{8} \right) dx
\]

The exponential factor \( e^{1/8} \) can be pulled out:
\[
I = e^{1/8} \int_{-\infty}^\infty e^{-2 ( x + \frac{5}{4} )^2 } dx
\]

Because the limits are \(-\infty\) to \(\infty\), and the quadratic term is centered at \(-5/4\), but integration is unchanged under a shift of variable.

Let \( y = x + \frac{5}{4} \Rightarrow dx = dy \), and as \( x \to \pm \infty \), \( y \to \pm \infty \):
\[
I = e^{1/8} \int_{-\infty}^{\infty} e^{-2 y^2} dy
\]

**Step 3: Evaluate the Gaussian Integral**

Recall:
\[
\int_{-\infty}^{\infty} e^{-a y^2} dy = \sqrt{\frac{\pi}{a}}
\]
Here, \( a = 2 \):

\[
\int_{-\infty}^{\infty} e^{-2 y^2} dy = \sqrt{ \frac{\pi}{2} }
\]

Therefore,
\[
I = e^{1/8} \sqrt{ \frac{\pi}{2} }
\]

**Step 4: Numerical Approximation**

First, calculate \( e^{1/8} \):

\[
e^{1/8} \approx e^{0.125} \approx 1.1331484531
\]

Now, compute \( \sqrt{ \frac{ \pi }{2 } } \):

\[
\pi \approx 3.141592653589793
\]
So
\[
\sqrt{ \frac{ 3.141592653589793 }{ 2 } } \approx \sqrt{ 1.5707963267948966 } \approx 1.2533141373
\]

Now, multiply:

\[
I \approx 1.1331484531 \times 1.2533141373 \approx 1.4214963041
\]

**Final Answer:**
```json
{"answer": "e^{1/8} \\sqrt{\\frac{\\pi}{2}}", "numerical_answer": "1.4214963041"}
```