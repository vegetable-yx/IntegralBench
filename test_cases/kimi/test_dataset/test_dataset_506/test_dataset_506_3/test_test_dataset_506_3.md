To solve the definite integral \(\int_1^{2011} \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}} \, dx\), we will follow the steps outlined:

### Step 1: Analytical Computation

First, let's denote the integral as \(I\):
\[ I = \int_1^{2011} \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}} \, dx. \]

To simplify this integral, we can use a symmetry argument. Consider the substitution \(u = 2012 - x\). Then \(du = -dx\), and the limits of integration change as follows:
- When \(x = 1\), \(u = 2011\).
- When \(x = 2011\), \(u = 1\).

Thus, the integral becomes:
\[ I = \int_{2011}^{1} \frac{\sqrt{2012 - u}}{\sqrt{u} + \sqrt{2012 - u}} (-du) = \int_{1}^{2011} \frac{\sqrt{2012 - u}}{\sqrt{u} + \sqrt{2012 - u}} \, du. \]

Notice that this is the same integral as the original, but with \(x\) replaced by \(2012 - u\). Therefore, we can write:
\[ I = \int_{1}^{2011} \frac{\sqrt{2012 - x}}{\sqrt{x} + \sqrt{2012 - x}} \, dx. \]

Now, add the original integral and this new form:
\[ I + I = \int_{1}^{2011} \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}} \, dx + \int_{1}^{2011} \frac{\sqrt{2012 - x}}{\sqrt{x} + \sqrt{2012 - x}} \, dx. \]

This simplifies to:
\[ 2I = \int_{1}^{2011} \left( \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}} + \frac{\sqrt{2012 - x}}{\sqrt{x} + \sqrt{2012 - x}} \right) \, dx. \]

Since the sum of the fractions is 1:
\[ 2I = \int_{1}^{2011} 1 \, dx = 2011 - 1 = 2010. \]

Thus, we have:
\[ I = \frac{2010}{2} = 1005. \]

### Step 2: Numerical Approximation

The exact answer is \(1005\). To provide a numerical approximation rounded to 10 decimal places, we simply write:
\[ 1005.0000000000. \]

### Step 3: JSON Output

Finally, we output the answer in the specified JSON format:
```json
{"answer": "1005", "numerical_answer": "1005.0000000000"}
```