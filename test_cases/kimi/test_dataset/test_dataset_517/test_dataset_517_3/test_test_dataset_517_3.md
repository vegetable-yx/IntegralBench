To solve the definite integral \(\int_{-\infty}^\infty e^{-2x^2-5x-3}dx\), we will follow these steps:

1. **Complete the square in the exponent**:
   The exponent \(-2x^2 - 5x - 3\) can be rewritten by completing the square.

   \[
   -2x^2 - 5x - 3 = -2\left(x^2 + \frac{5}{2}x\right) - 3
   \]

   To complete the square inside the parentheses:

   \[
   x^2 + \frac{5}{2}x = \left(x + \frac{5}{4}\right)^2 - \left(\frac{5}{4}\right)^2
   \]

   Therefore,

   \[
   -2\left(x^2 + \frac{5}{2}x\right) - 3 = -2\left(\left(x + \frac{5}{4}\right)^2 - \left(\frac{5}{4}\right)^2\right) - 3
   \]

   Simplifying further:

   \[
   -2\left(x + \frac{5}{4}\right)^2 + 2\left(\frac{5}{4}\right)^2 - 3 = -2\left(x + \frac{5}{4}\right)^2 + \frac{25}{8} - 3
   \]

   \[
   = -2\left(x + \frac{5}{4}\right)^2 + \frac{25}{8} - \frac{24}{8} = -2\left(x + \frac{5}{4}\right)^2 + \frac{1}{8}
   \]

   Thus, the integral becomes:

   \[
   \int_{-\infty}^\infty e^{-2\left(x + \frac{5}{4}\right)^2 + \frac{1}{8}} dx = e^{\frac{1}{8}} \int_{-\infty}^\infty e^{-2\left(x + \frac{5}{4}\right)^2} dx
   \]

2. **Evaluate the Gaussian integral**:
   The integral \(\int_{-\infty}^\infty e^{-2\left(x + \frac{5}{4}\right)^2} dx\) is a standard Gaussian integral of the form \(\int_{-\infty}^\infty e^{-ax^2} dx = \sqrt{\frac{\pi}{a}}\), where \(a = 2\).

   \[
   \int_{-\infty}^\infty e^{-2\left(x + \frac{5}{4}\right)^2} dx = \sqrt{\frac{\pi}{2}}
   \]

3. **Combine the results**:
   Therefore, the original integral is:

   \[
   e^{\frac{1}{8}} \sqrt{\frac{\pi}{2}}
   \]

4. **Numerical approximation**:
   To find the numerical approximation, we calculate:

   \[
   e^{\frac{1}{8}} \approx 1.1331484530668263
   \]

   \[
   \sqrt{\frac{\pi}{2}} \approx 1.2533141373155003
   \]

   Multiplying these values:

   \[
   1.1331484530668263 \times 1.2533141373155003 \approx 1.420985542436538
   \]

   Rounded to 10 decimal places, the numerical approximation is:

   \[
   1.4209855424
   \]

Finally, the answer in the requested JSON format is:

```json
{"answer": "e^{\\frac{1}{8}} \\sqrt{\\frac{\\pi}{2}}", "numerical_answer": "1.4209855424"}
```