To solve the definite integral 

\[
\int_1^{2011} \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}} \, dx,
\]

we can follow these steps:

### Step 1: Symmetry Substitution
Let’s consider the substitution \( x = 2012 - t \). Then \( dx = -dt \), and the limits change as follows:
- When \( x = 1 \), \( t = 2011 \).
- When \( x = 2011 \), \( t = 1 \).

The integral becomes:

\[
I = \int_{2011}^{1} \frac{\sqrt{2012 - t}}{\sqrt{t} + \sqrt{2012 - t}} (-dt) = \int_{1}^{2011} \frac{\sqrt{2012 - t}}{\sqrt{t} + \sqrt{2012 - t}} \, dt.
\]

### Step 2: Add the Original and Transformed Integrals
Now, let’s denote the original integral as \( I \):

\[
I = \int_{1}^{2011} \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}} \, dx.
\]

Adding \( I \) and its transformed version:

\[
2I = \int_{1}^{2011} \frac{\sqrt{x} + \sqrt{2012 - x}}{\sqrt{2012 - x} + \sqrt{x}} \, dx = \int_{1}^{2011} 1 \, dx = 2011 - 1 = 2010.
\]

Thus,

\[
I = \frac{2010}{2} = 1005.
\]

### Step 3: Numerical Verification
The exact value of the integral is \( 1005 \). The numerical approximation is simply:

\[
1005.0000000000.
\]

### Final Answer
```json
{"answer": "1005", "numerical_answer": "1005.0000000000"}
```