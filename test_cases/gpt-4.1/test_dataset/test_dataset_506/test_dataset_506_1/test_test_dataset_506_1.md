Let's calculate the given integral:

\[
I = \int_1^{2011} \frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}} \, dx
\]

**Step 1: Substitution**

Let’s use the substitution \( x \to 2012 - x \):
Let \( u = 2012 - x \), so \( dx = -du \).

When \( x = 1 \), \( u = 2011 \).

When \( x = 2011 \), \( u = 1 \).

So,
\[
I = \int_{x=1}^{x=2011} \frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}} dx = \int_{u=2011}^{u=1} \frac{\sqrt{2012-u}}{\sqrt{u}+\sqrt{2012-u}} (-du)
\]
\[
= \int_{u=1}^{u=2011} \frac{\sqrt{2012-u}}{\sqrt{u}+\sqrt{2012-u}} du
\]

**Step 2: Add original and substitution**

Let’s call the original \( I \):

\[
I = \int_1^{2011} \frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}} dx
\]
\[
J = \int_1^{2011} \frac{\sqrt{2012-x}}{\sqrt{x}+\sqrt{2012-x}} dx
\]

From the substitution, \( I = J \). (The variable is just a dummy variable.)

Now, sum \( I+J \):
\[
I+J = \int_1^{2011} \left(\frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}} + \frac{\sqrt{2012-x}}{\sqrt{x}+\sqrt{2012-x}}\right) dx
\]

Combine fractions:
\[
= \int_1^{2011} \frac{\sqrt{x}+\sqrt{2012-x}}{\sqrt{x}+\sqrt{2012-x}} dx = \int_1^{2011} 1 \, dx = 2011 - 1 = 2010
\]
Therefore,
\[
I + I = 2010 \implies 2I = 2010 \implies I = 1005
\]

**Step 3: Write exact and numerical answer**

The exact answer is 1005.

Numerical approximation to 10 decimal places: 1005.0000000000

---

Final answer (in JSON format):

```json
{"answer": "1005", "numerical_answer": "1005.0000000000"}
```