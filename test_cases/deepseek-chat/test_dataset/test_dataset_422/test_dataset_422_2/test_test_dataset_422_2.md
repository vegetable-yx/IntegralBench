To solve the definite integral \(\int_{-1}^1 x^2 \cdot \sqrt[3]{x^3 + 1} \, dx\), we will follow these steps:

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
\int_{-1}^1 x^2 \cdot \sqrt[3]{x^3 + 1} \, dx = \int_{0}^2 \sqrt[3]{u} \cdot \frac{du}{3} = \frac{1}{3} \int_{0}^2 u^{1/3} \, du.
\]

### Step 3: Integrate
Integrate \( u^{1/3} \):
\[
\frac{1}{3} \int_{0}^2 u^{1/3} \, du = \frac{1}{3} \left[ \frac{u^{4/3}}{4/3} \right]_0^2 = \frac{1}{3} \cdot \frac{3}{4} \left( 2^{4/3} - 0 \right) = \frac{1}{4} \cdot 2^{4/3}.
\]

### Step 4: Simplify
Simplify \( 2^{4/3} \):
\[
2^{4/3} = \left(2^{1/3}\right)^4 = \left(\sqrt[3]{2}\right)^4.
\]
So the exact answer is:
\[
\frac{1}{4} \cdot 2^{4/3}.
\]

### Step 5: Numerical Approximation
Compute the numerical value of \( \frac{1}{4} \cdot 2^{4/3} \):
\[
2^{4/3} \approx 2.51984209979, \quad \frac{1}{4} \cdot 2.51984209979 \approx 0.629960524947.
\]
Rounded to 10 decimal places:
\[
0.6299605250.
\]

### Final Answer
\[
\boxed{
{"answer": "\\frac{1}{4} \\cdot 2^{4/3}", "numerical_answer": "0.6299605250"}
}
\]