Let's denote the integral as \( I \):

\[
I = \int_{-1}^{1} \frac{1}{3^x + 1} \; dx
\]

### Step 1: Analytically compute the integral

#### (a) Look for symmetry

Consider the substitution \( x \mapsto -x \):

\[
\int_{-1}^{1} f(x) \, dx = \int_{-1}^{1} f(-x) \, dx
\]

Compute \( f(-x) \):

\[
f(-x) = \frac{1}{3^{-x} + 1} = \frac{1}{\frac{1}{3^x} + 1} = \frac{1}{\frac{1 + 3^x}{3^x}} = \frac{3^x}{1 + 3^x}
\]

Therefore,

\[
f(x) + f(-x) = \frac{1}{3^x + 1} + \frac{3^x}{1 + 3^x} = \frac{1 + 3^x}{1 + 3^x} = 1
\]

So,

\[
I = \int_{-1}^1 \frac{1}{3^x + 1} dx = \int_{-1}^1 \frac{3^x}{3^x + 1} dx
\]

Therefore,

\[
2I = \int_{-1}^1 \left[ \frac{1}{3^x+1} + \frac{3^x}{3^x+1} \right] dx = \int_{-1}^1 1 \, dx = 2
\]

So,

\[
I = 1
\]

---

### Step 2: All necessary steps are shown above.

---

### Step 3: Numerical approximation

\( I = 1 \) exactly, so the numerical approximation to 10 decimal places is \( 1.0000000000 \).

---

### Step 4: Provide the answer in JSON format (exact and approximate):

```json
{"answer": "1", "numerical_answer": "1.0000000000"}
```