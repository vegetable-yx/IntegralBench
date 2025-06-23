To solve the definite integral 

\[
\int_1^{2011} \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}} \, dx,
\]

we can use a clever substitution to simplify the integrand. Here's the step-by-step solution:

### Step 1: Symmetry Substitution
Let \( I \) be the integral:

\[
I = \int_1^{2011} \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}} \, dx.
\]

Consider the substitution \( x = 2012 - t \). Then \( dx = -dt \), and when \( x = 1 \), \( t = 2011 \), and when \( x = 2011 \), \( t = 1 \). The integral becomes:

\[
I = \int_{2011}^{1} \frac{\sqrt{2012 - t}}{\sqrt{t} + \sqrt{2012 - t}} (-dt) = \int_{1}^{2011} \frac{\sqrt{2012 - t}}{\sqrt{t} + \sqrt{2012 - t}} \, dt.
\]

Now, rename \( t \) back to \( x \) (since it's a dummy variable):

\[
I = \int_{1}^{2011} \frac{\sqrt{2012 - x}}{\sqrt{x} + \sqrt{2012 - x}} \, dx.
\]

### Step 2: Add the Two Expressions for \( I \)
Add the original expression for \( I \) and the one obtained after substitution:

\[
2I = \int_{1}^{2011} \frac{\sqrt{x} + \sqrt{2012 - x}}{\sqrt{2012 - x} + \sqrt{x}} \, dx = \int_{1}^{2011} 1 \, dx = 2011 - 1 = 2010.
\]

Thus,

\[
I = \frac{2010}{2} = 1005.
\]

### Step 3: Numerical Approximation
The exact value is \( 1005 \), so the numerical approximation is:

\[
1005.0000000000.
\]

### Final Answer
```json
{"answer": "1005", "numerical_answer": "1005.0000000000"}
```