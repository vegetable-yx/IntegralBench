To compute the definite integral \(\int_{-1}^1 x^2 \cdot \sqrt[3]{x^3 + 1} \, dx\), we can proceed with the following steps:

### Step 1: Substitution
Let \( u = x^3 + 1 \). Then, the derivative of \( u \) with respect to \( x \) is:
\[
\frac{du}{dx} = 3x^2 \implies du = 3x^2 \, dx \implies x^2 \, dx = \frac{du}{3}.
\]
When \( x = -1 \), \( u = (-1)^3 + 1 = 0 \).
When \( x = 1 \), \( u = (1)^3 + 1 = 2 \).

### Step 2: Rewrite the Integral in Terms of \( u \)
Substituting into the integral:
\[
\int_{-1}^1 x^2 \cdot \sqrt[3]{x^3 + 1} \, dx = \int_{0}^2 \sqrt[3]{u} \cdot \frac{du}{3} = \frac{1}{3} \int_{0}^2 u^{1/3} \, du.
\]

### Step 3: Integrate with Respect to \( u \)
Compute the integral of \( u^{1/3} \):
\[
\int u^{1/3} \, du = \frac{u^{4/3}}{4/3} = \frac{3}{4} u^{4/3}.
\]
Now, evaluate from 0 to 2:
\[
\frac{1}{3} \left[ \frac{3}{4} u^{4/3} \right]_0^2 = \frac{1}{3} \cdot \frac{3}{4} \left( 2^{4/3} - 0 \right) = \frac{1}{4} \cdot 2^{4/3}.
\]

### Step 4: Simplify the Expression
Express \( 2^{4/3} \) as \( 2 \cdot 2^{1/3} \):
\[
2^{4/3} = 2^{1 + 1/3} = 2 \cdot 2^{1/3}.
\]
Thus, the exact answer is:
\[
\frac{1}{4} \cdot 2 \cdot 2^{1/3} = \frac{1}{2} \cdot 2^{1/3}.
\]
Alternatively, it can be written as:
\[
\frac{2^{1/3}}{2}.
\]

### Step 5: Numerical Approximation
Compute \( 2^{1/3} \) numerically:
\[
2^{1/3} \approx 1.25992104989.
\]
Multiply by \( \frac{1}{2} \):
\[
\frac{1.25992104989}{2} \approx 0.62996052494.
\]

### Final Answer
\[
\boxed{
{"answer": "\\frac{2^{1/3}}{2}", "numerical_answer": "0.6299605249"}
}
\]