To solve the definite integral \(\int_{-1}^1 x^2 \cdot \sqrt[3]{x^3 + 1} \, dx\), we will follow the steps outlined:

### Step 1: Compute the Integral Analytically

First, let's rewrite the integral for clarity:
\[
\int_{-1}^1 x^2 \cdot (x^3 + 1)^{1/3} \, dx
\]

We will use a substitution to simplify the integral. Let:
\[
u = x^3 + 1
\]
Then:
\[
du = 3x^2 \, dx \quad \Rightarrow \quad x^2 \, dx = \frac{1}{3} du
\]

Now, we need to adjust the limits of integration according to the substitution:
- When \(x = -1\), \(u = (-1)^3 + 1 = 0\)
- When \(x = 1\), \(u = 1^3 + 1 = 2\)

Substituting \(u\) and \(du\) into the integral, we get:
\[
\int_{-1}^1 x^2 \cdot (x^3 + 1)^{1/3} \, dx = \int_{0}^2 \left( \frac{1}{3} \right) u^{1/3} \, du
\]

Simplify the integral:
\[
\frac{1}{3} \int_{0}^2 u^{1/3} \, du
\]

Now, integrate \(u^{1/3}\):
\[
\int u^{1/3} \, du = \frac{u^{4/3}}{\frac{4}{3}} = \frac{3}{4} u^{4/3}
\]

So, the integral becomes:
\[
\frac{1}{3} \cdot \frac{3}{4} \left[ u^{4/3} \right]_0^2 = \frac{1}{4} \left[ u^{4/3} \right]_0^2
\]

Evaluate the definite integral:
\[
\frac{1}{4} \left( 2^{4/3} - 0^{4/3} \right) = \frac{1}{4} \cdot 2^{4/3}
\]

### Step 2: Numerical Approximation

To find the numerical approximation of \(2^{4/3}\):
\[
2^{4/3} \approx 2.5198421
\]

Thus:
\[
\frac{1}{4} \cdot 2.5198421 \approx 0.629960525
\]

### Step 3: Output the Final Answer in JSON Format

\[
\boxed{
\begin{aligned}
\text{"answer": "}\frac{1}{4} \cdot 2^{4/3}\text{"}, \\
\text{"numerical_answer": "0.629960525"}
\end{aligned}
}
\]