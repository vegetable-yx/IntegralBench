Let's solve the definite integral:

\[
I = \int_1^\infty \frac{\log x}{x^2} \, dx
\]

**Step 1: Compute the indefinite integral**

Let \( u = \log x \). We'll use integration by parts:

Let
- \( u = \log x \implies du = \frac{1}{x} dx \)
- \( dv = x^{-2} dx \implies v = -x^{-1} \)

By integration by parts:

\[
\int \log x \cdot x^{-2} dx = -\log x \cdot x^{-1} - \int (-x^{-1}) \cdot \frac{1}{x} dx
\]
\[
= -\frac{\log x}{x} + \int \frac{1}{x^2} dx
\]
\[
= -\frac{\log x}{x} - \frac{1}{x} + C
\]

**Step 2: Evaluate the definite integral from \( x=1 \) to \( x=\infty \):**

\[
I = \left[ -\frac{\log x}{x} - \frac{1}{x} \right]_1^\infty
\]

Let's compute the limits separately.

First, as \( x \to \infty \):

- \( \log x / x \to 0 \), since logarithm grows much more slowly than \( x \).
- \( 1/x \to 0 \).

So,

\[
\lim_{x\to\infty} \left(-\frac{\log x}{x} - \frac{1}{x}\right) = 0
\]

Now, at \( x=1 \):

- \( \log 1 = 0 \)
- \( 1/1 = 1 \)

So,

\[
\left(-\frac{\log x}{x} - \frac{1}{x}\right)_{x=1} = -(0) - 1 = -1
\]

Altogether,

\[
I = 0 - (-1) = 1
\]

**Step 3: Numerical Approximation**

The result is exact: \( 1 \).

Rounded to 10 decimal places: \( 1.0000000000 \)

**Final Answer in JSON Format:**
```json
{"answer": "1", "numerical_answer": "1.0000000000"}
```