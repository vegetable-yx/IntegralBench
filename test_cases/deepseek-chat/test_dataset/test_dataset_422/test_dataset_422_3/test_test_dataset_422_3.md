To solve the definite integral \(\int_{-1}^1 x^2 \cdot \sqrt[3]{x^3 + 1} \, dx\), we can proceed with the following steps:

### Step 1: Substitution
Let \( u = x^3 + 1 \). Then, the derivative of \( u \) with respect to \( x \) is:
\[
\frac{du}{dx} = 3x^2 \implies du = 3x^2 \, dx \implies x^2 \, dx = \frac{du}{3}.
\]
When \( x = -1 \), \( u = (-1)^3 + 1 = 0 \).  
When \( x = 1 \), \( u = (1)^3 + 1 = 2 \).

### Step 2: Rewrite the Integral
Substituting \( u \) and the limits into the integral:
\[
\int_{-1}^1 x^2 \cdot \sqrt[3]{x^3 + 1} \, dx = \int_{0}^{2} \sqrt[3]{u} \cdot \frac{du}{3} = \frac{1}{3} \int_{0}^{2} u^{1/3} \, du.
\]

### Step 3: Integrate
The integral of \( u^{1/3} \) is:
\[
\int u^{1/3} \, du = \frac{u^{4/3}}{4/3} = \frac{3}{4} u^{4/3}.
\]
Thus, evaluating from 0 to 2:
\[
\frac{1}{3} \left[ \frac{3}{4} u^{4/3} \right]_0^2 = \frac{1}{3} \cdot \frac{3}{4} \left( 2^{4/3} - 0 \right) = \frac{1}{4} \cdot 2^{4/3}.
\]

### Step 4: Simplify
We can express \( 2^{4/3} \) as \( (2^{1/3})^4 \), but it's more straightforward to leave it as \( 2^{4/3} \). Therefore, the exact answer is:
\[
\frac{2^{4/3}}{4}.
\]

### Step 5: Numerical Approximation
Calculating \( 2^{4/3} \):
\[
2^{4/3} \approx 2.51984209979.
\]
Dividing by 4:
\[
\frac{2.51984209979}{4} \approx 0.629960524947.
\]

### Final Answer
\[
\boxed{
{"answer": "\\frac{2^{4/3}}{4}", "numerical_answer": "0.6299605249"}
}
\]