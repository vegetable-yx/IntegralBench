Let's compute the definite integral:  
\[
I = \int_1^{2011} \frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}} \, dx
\]

### Step 1: Symmetry Transformation

Let’s consider the substitution \( x \to 2012 - x \).

Let \( u = 2012 - x \implies du = -dx \).

When \( x = 1 \), \( u = 2011 \),  
When \( x = 2011 \), \( u = 1 \).

Rewrite the integral:
\[
I = \int_{x=1}^{x=2011} \frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}} dx
\]
Change variables:
\[
= \int_{u=2011}^{u=1} \frac{\sqrt{2012-u}}{\sqrt{u}+\sqrt{2012-u}} (-du)
\]
Switching the limits, the negative sign disappears:
\[
= \int_{u=1}^{u=2011} \frac{\sqrt{2012-u}}{\sqrt{u}+\sqrt{2012-u}} du
\]

### Step 2: Adding the Integral to Itself

Let’s add the two forms:
\[
I = \int_1^{2011} \frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}} dx
\]
\[
I = \int_1^{2011} \frac{\sqrt{2012-x}}{\sqrt{x}+\sqrt{2012-x}} dx
\]

Add the two:
\[
2I = \int_1^{2011} \left( \frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}} + \frac{\sqrt{2012-x}}{\sqrt{x}+\sqrt{2012-x}} \right) dx
\]
\[
= \int_1^{2011} \left( \frac{\sqrt{x} + \sqrt{2012-x}}{\sqrt{x}+\sqrt{2012-x}} \right) dx
\]
\[
= \int_1^{2011} 1 \, dx = 2011 - 1 = 2010
\]

Therefore,
\[
2I = 2010 \implies I = \boxed{1005}
\]

---

### Step 3: Numerical Approximation

The integral is exactly 1005, to 10 decimal places:
\[
1005.0000000000
\]

---

### Step 4: JSON Output

```json
{"answer": "1005", "numerical_answer": "1005.0000000000"}
```