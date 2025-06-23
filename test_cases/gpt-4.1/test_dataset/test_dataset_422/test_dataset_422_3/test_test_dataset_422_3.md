Let's compute the definite integral:
\[
I = \int_{-1}^1 x^2 \cdot \sqrt[3]{x^3+1} \, dx
\]

### Step 1: Make a Substitution

Let \( u = x^3 + 1 \implies du = 3x^2 dx \implies x^2 dx = \frac{du}{3} \).

When \( x = -1 \), \( u = (-1)^3 + 1 = -1 + 1 = 0 \).

When \( x = 1 \), \( u = (1)^3 + 1 = 1 + 1 = 2 \).

Thus,
\[
I = \int_{x=-1}^{x=1} x^2 \cdot \sqrt[3]{x^3+1} \, dx = \int_{u=0}^{u=2} \sqrt[3]{u} \cdot \frac{du}{3}
= \frac{1}{3} \int_{u=0}^{u=2} u^{1/3} du
\]

### Step 2: Integrate

\[
\int u^{1/3} du = \frac{u^{4/3}}{4/3} = \frac{3}{4} u^{4/3}
\]
So,
\[
I = \frac{1}{3} \cdot \frac{3}{4} \left[ u^{4/3} \right]_{u=0}^{u=2} = \frac{1}{4} \left( (2)^{4/3} - (0)^{4/3} \right)
\]
\[
= \frac{1}{4} \cdot 2^{4/3}
\]

### Step 3: Analytical Answer

The exact answer is:
\[
\boxed{ \frac{1}{4} \cdot 2^{4/3} }
\]

### Step 4: Numerical Approximation

Calculate \( 2^{4/3} \):

\( 2^{4/3} = (2^{1/3})^4 = (\sqrt[3]{2})^4 \)

\( 2^{1/3} \approx 1.26\; 0 7 4 6 4 2 1 1 \)

\( (1.26 0 7 4 6 4 2 1)^4 \approx 2.5198 1 7 8 1 \)

Now:

\(
\frac{1}{4} \cdot 2.5198 1 7 8 1 \approx 0.6299 5 4 4 5
\)

So, to 10 decimal places:  
\( 0.6299604445 \)

### Final JSON Output

```json
{"answer": "\\frac{1}{4} 2^{4/3}", "numerical_answer": "0.6299604445"}
```