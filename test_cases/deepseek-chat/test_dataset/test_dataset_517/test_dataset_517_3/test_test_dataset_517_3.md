To compute the definite integral \(\int_{-\infty}^\infty e^{-2x^2-5x-3}dx\), we follow these steps:

### Step 1: Complete the Square
First, we rewrite the exponent \(-2x^2 - 5x - 3\) in a form that allows us to use the Gaussian integral formula. 

\[
-2x^2 - 5x - 3 = -2\left(x^2 + \frac{5}{2}x\right) - 3
\]

Now, complete the square for the quadratic expression inside the parentheses:

\[
x^2 + \frac{5}{2}x = \left(x + \frac{5}{4}\right)^2 - \left(\frac{5}{4}\right)^2 = \left(x + \frac{5}{4}\right)^2 - \frac{25}{16}
\]

Substitute this back into the exponent:

\[
-2\left(\left(x + \frac{5}{4}\right)^2 - \frac{25}{16}\right) - 3 = -2\left(x + \frac{5}{4}\right)^2 + \frac{25}{8} - 3 = -2\left(x + \frac{5}{4}\right)^2 + \frac{1}{8}
\]

Thus, the integral becomes:

\[
\int_{-\infty}^\infty e^{-2x^2-5x-3}dx = e^{\frac{1}{8}} \int_{-\infty}^\infty e^{-2\left(x + \frac{5}{4}\right)^2} dx
\]

### Step 2: Substitution
Let \( u = x + \frac{5}{4} \), then \( du = dx \), and the integral becomes:

\[
e^{\frac{1}{8}} \int_{-\infty}^\infty e^{-2u^2} du
\]

### Step 3: Gaussian Integral
The Gaussian integral \(\int_{-\infty}^\infty e^{-au^2} du\) is known to be \(\sqrt{\frac{\pi}{a}}\) for \(a > 0\). Here, \(a = 2\), so:

\[
\int_{-\infty}^\infty e^{-2u^2} du = \sqrt{\frac{\pi}{2}}
\]

### Step 4: Combine Results
Multiply the results from Step 1 and Step 3:

\[
e^{\frac{1}{8}} \cdot \sqrt{\frac{\pi}{2}} = \sqrt{\frac{\pi}{2}} \cdot e^{\frac{1}{8}}
\]

### Step 5: Numerical Approximation
Compute the numerical value:

\[
\sqrt{\frac{\pi}{2}} \approx 1.25331413732
\]
\[
e^{\frac{1}{8}} \approx 1.13314845307
\]
\[
\sqrt{\frac{\pi}{2}} \cdot e^{\frac{1}{8}} \approx 1.25331413732 \times 1.13314845307 \approx 1.42006289344
\]

Rounding to 10 decimal places:

\[
1.4200628934
\]

### Final Answer
```json
{"answer": "\\sqrt{\\frac{\\pi}{2}} e^{\\frac{1}{8}}", "numerical_answer": "1.4200628934"}
```