Let's denote the integral as \( I \):

\[
I = \int_1^{2011}\frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}}\ dx
\]

**Step 1: Simplify the integrand**

Let’s consider the substitution:

Let \( t = 2012 - x \). Then, as \( x \) goes from 1 to 2011, \( t \) goes from 2011 to 1.

- \( x = 2012 - t \)
- \( dx = -dt \)

Let’s compute the transformed integral:

\[
I = \int_{x=1}^{x=2011} \frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}}\,dx = \int_{t=2011}^{t=1} \frac{\sqrt{2012-t}}{\sqrt{t}+\sqrt{2012-t}} (-dt)
\]

Switch limits and remove the negative sign:

\[
I = \int_{t=1}^{t=2011} \frac{\sqrt{2012-t}}{\sqrt{t}+\sqrt{2012-t}}\,dt
\]

**Step 2: Add original and transformed integral**

We now have

\[
I = \int_{1}^{2011} \frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}}\ dx
\]
\[
I = \int_{1}^{2011} \frac{\sqrt{2012-x}}{\sqrt{x}+\sqrt{2012-x}}\ dx
\]

Add these two expressions:

\[
2I = \int_{1}^{2011} \left( \frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}} + \frac{\sqrt{2012-x}}{\sqrt{x}+\sqrt{2012-x}} \right) dx
\]

Notice both denominators are equal: \( \sqrt{x}+\sqrt{2012-x} \).

So:

\[
2I = \int_{1}^{2011} \frac{\sqrt{x} + \sqrt{2012-x}}{\sqrt{x}+\sqrt{2012-x}} dx = \int_{1}^{2011} dx = 2011 - 1 = 2010
\]

Therefore,

\[
I = \frac{2010}{2} = 1005
\]

**Step 3: Numerical approximation**

The answer is exactly 1005. Rounded to 10 decimal places: \( 1005.0000000000 \).

---

**Final answer in JSON:**
```json
{"answer": "1005", "numerical_answer": "1005.0000000000"}
```