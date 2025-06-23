To solve the definite integral \(\int_{-\infty}^\infty e^{-(x-2024)^2/4}\:dx\), we can use the properties of the Gaussian integral.

### Step 1: Recognize the Gaussian Integral Form

The given integral is in the form of a Gaussian integral:
\[ \int_{-\infty}^\infty e^{-a(x-b)^2}\:dx \]
where \(a = \frac{1}{4}\) and \(b = 2024\).

### Step 2: Use the Gaussian Integral Formula

The standard Gaussian integral formula is:
\[ \int_{-\infty}^\infty e^{-ax^2}\:dx = \sqrt{\frac{\pi}{a}} \]

For our integral, we can rewrite it as:
\[ \int_{-\infty}^\infty e^{-(x-2024)^2/4}\:dx \]

This is equivalent to:
\[ \int_{-\infty}^\infty e^{-\frac{1}{4}(x-2024)^2}\:dx \]

### Step 3: Apply the Gaussian Integral Formula

Using the Gaussian integral formula with \(a = \frac{1}{4}\):
\[ \int_{-\infty}^\infty e^{-\frac{1}{4}(x-2024)^2}\:dx = \sqrt{\frac{\pi}{\frac{1}{4}}} \]

Simplify the expression inside the square root:
\[ \sqrt{\frac{\pi}{\frac{1}{4}}} = \sqrt{4\pi} = 2\sqrt{\pi} \]

### Step 4: Numerical Approximation

To provide a numerical approximation, we use the value of \(\sqrt{\pi}\):
\[ \sqrt{\pi} \approx 1.772453850905516 \]

Thus:
\[ 2\sqrt{\pi} \approx 2 \times 1.772453850905516 = 3.544907701811032 \]

Rounded to 10 decimal places:
\[ 3.5449077018 \]

### Final Answer in JSON Format

```json
{"answer": "2\\sqrt{\\pi}", "numerical_answer": "3.5449077018"}
```