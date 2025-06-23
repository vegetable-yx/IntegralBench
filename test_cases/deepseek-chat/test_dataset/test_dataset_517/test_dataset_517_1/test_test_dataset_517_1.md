To compute the definite integral \(\int_{-\infty}^\infty e^{-2x^2-5x-3}dx\), we will follow these steps:

### Step 1: Complete the Square
First, we rewrite the exponent \(-2x^2 - 5x - 3\) in a form that allows us to use the Gaussian integral formula. We complete the square for the quadratic expression:

\[
-2x^2 - 5x - 3 = -2\left(x^2 + \frac{5}{2}x\right) - 3
\]

Now, complete the square inside the parentheses:

\[
x^2 + \frac{5}{2}x = \left(x + \frac{5}{4}\right)^2 - \left(\frac{5}{4}\right)^2 = \left(x + \frac{5}{4}\right)^2 - \frac{25}{16}
\]

Substitute this back into the expression:

\[
-2\left(\left(x + \frac{5}{4}\right)^2 - \frac{25}{16}\right) - 3 = -2\left(x + \frac{5}{4}\right)^2 + \frac{25}{8} - 3
\]

Simplify the constants:

\[
-2\left(x + \frac{5}{4}\right)^2 + \frac{25}{8} - \frac{24}{8} = -2\left(x + \frac{5}{4}\right)^2 + \frac{1}{8}
\]

Thus, the exponent becomes:

\[
-2x^2 - 5x - 3 = -2\left(x + \frac{5}{4}\right)^2 + \frac{1}{8}
\]

### Step 2: Rewrite the Integral
Substitute the completed square back into the integral:

\[
\int_{-\infty}^\infty e^{-2x^2-5x-3}dx = e^{\frac{1}{8}} \int_{-\infty}^\infty e^{-2\left(x + \frac{5}{4}\right)^2} dx
\]

Let \(u = x + \frac{5}{4}\), then \(du = dx\), and the integral becomes:

\[
e^{\frac{1}{8}} \int_{-\infty}^\infty e^{-2u^2} du
\]

### Step 3: Evaluate the Gaussian Integral
The integral \(\int_{-\infty}^\infty e^{-2u^2} du\) is a standard Gaussian integral. Recall that:

\[
\int_{-\infty}^\infty e^{-au^2} du = \sqrt{\frac{\pi}{a}}
\]

Here, \(a = 2\), so:

\[
\int_{-\infty}^\infty e^{-2u^2} du = \sqrt{\frac{\pi}{2}}
\]

### Step 4: Combine the Results
Multiply the results from Step 2 and Step 3:

\[
e^{\frac{1}{8}} \cdot \sqrt{\frac{\pi}{2}} = \sqrt{\frac{\pi}{2}} \cdot e^{\frac{1}{8}}
\]

### Step 5: Numerical Approximation
Compute the numerical value of the exact answer:

\[
\sqrt{\frac{\pi}{2}} \cdot e^{\frac{1}{8}} \approx 1.4614153930
\]

### Final Answer
The exact answer is \(\sqrt{\frac{\pi}{2}} e^{\frac{1}{8}}\), and the numerical approximation is \(1.4614153930\).

```json
{"answer": "\\sqrt{\\frac{\\pi}{2}} e^{\\frac{1}{8}}", "numerical_answer": "1.4614153930"}
```