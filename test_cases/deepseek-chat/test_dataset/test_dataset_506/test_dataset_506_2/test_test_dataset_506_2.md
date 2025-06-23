To compute the definite integral 

\[
I = \int_1^{2011} \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}} \, dx,
\]

we can use a clever substitution to simplify the integrand. Here's the step-by-step solution:

### Step 1: Symmetry Substitution
Let’s consider the substitution \( x = 2012 - t \). Then \( dx = -dt \), and the limits change as follows:
- When \( x = 1 \), \( t = 2011 \).
- When \( x = 2011 \), \( t = 1 \).

The integral becomes:

\[
I = \int_{2011}^{1} \frac{\sqrt{2012 - t}}{\sqrt{t} + \sqrt{2012 - t}} (-dt) = \int_{1}^{2011} \frac{\sqrt{2012 - t}}{\sqrt{t} + \sqrt{2012 - t}} \, dt.
\]

Now, observe that the integrand is symmetric in \( \sqrt{t} \) and \( \sqrt{2012 - t} \). Let’s denote the original integrand as:

\[
f(x) = \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}}.
\]

After the substitution, we have:

\[
f(2012 - t) = \frac{\sqrt{2012 - t}}{\sqrt{t} + \sqrt{2012 - t}}.
\]

Thus, the integral \( I \) can also be written as:

\[
I = \int_{1}^{2011} \frac{\sqrt{2012 - x}}{\sqrt{x} + \sqrt{2012 - x}} \, dx.
\]

### Step 2: Add the Two Expressions for \( I \)
Now, add the original expression for \( I \) and the one obtained after substitution:

\[
2I = \int_{1}^{2011} \left( \frac{\sqrt{x}}{\sqrt{2012 - x} + \sqrt{x}} + \frac{\sqrt{2012 - x}}{\sqrt{x} + \sqrt{2012 - x}} \right) dx.
\]

Simplify the integrand:

\[
\frac{\sqrt{x} + \sqrt{2012 - x}}{\sqrt{2012 - x} + \sqrt{x}} = 1.
\]

Thus,

\[
2I = \int_{1}^{2011} 1 \, dx = 2011 - 1 = 2010.
\]

### Step 3: Solve for \( I \)
Divide both sides by 2:

\[
I = \frac{2010}{2} = 1005.
\]

### Step 4: Numerical Approximation
The exact value is \( 1005 \), so the numerical approximation is:

\[
1005.0000000000.
\]

### Final Answer
```json
{"answer": "1005", "numerical_answer": "1005.0000000000"}
```