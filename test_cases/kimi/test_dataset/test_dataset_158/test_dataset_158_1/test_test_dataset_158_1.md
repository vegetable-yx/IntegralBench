To solve the definite integral \(\int\limits_0^\infty x^{2-1}e^{-1.0x^2}H_2(1.0x)dx\), we need to understand the components involved. Here, \(H_2(x)\) is the Hermite polynomial of degree 2, which is given by:

\[ H_2(x) = 4x^2 - 2 \]

The integral can be rewritten as:

\[ \int\limits_0^\infty x e^{-x^2} (4x^2 - 2) \, dx \]

We can split this into two separate integrals:

\[ \int\limits_0^\infty x e^{-x^2} (4x^2 - 2) \, dx = 4 \int\limits_0^\infty x^3 e^{-x^2} \, dx - 2 \int\limits_0^\infty x e^{-x^2} \, dx \]

Let's evaluate each integral separately.

### First Integral: \(\int\limits_0^\infty x^3 e^{-x^2} \, dx\)

We use the substitution \(u = x^2\), hence \(du = 2x \, dx\). This transforms the integral as follows:

\[ \int\limits_0^\infty x^3 e^{-x^2} \, dx = \int\limits_0^\infty x^2 \cdot x e^{-x^2} \, dx = \int\limits_0^\infty \frac{u}{2} e^{-u} \, du \]

This simplifies to:

\[ \frac{1}{2} \int\limits_0^\infty u e^{-u} \, du \]

The integral \(\int\limits_0^\infty u e^{-u} \, du\) is a known Gamma function \(\Gamma(2)\):

\[ \Gamma(2) = 1! = 1 \]

Thus,

\[ \int\limits_0^\infty x^3 e^{-x^2} \, dx = \frac{1}{2} \cdot 1 = \frac{1}{2} \]

### Second Integral: \(\int\limits_0^\infty x e^{-x^2} \, dx\)

Using the same substitution \(u = x^2\), \(du = 2x \, dx\):

\[ \int\limits_0^\infty x e^{-x^2} \, dx = \int\limits_0^\infty \frac{1}{2} e^{-u} \, du \]

This simplifies to:

\[ \frac{1}{2} \int\limits_0^\infty e^{-u} \, du \]

The integral \(\int\limits_0^\infty e^{-u} \, du\) is a known Gamma function \(\Gamma(1)\):

\[ \Gamma(1) = 0! = 1 \]

Thus,

\[ \int\limits_0^\infty x e^{-x^2} \, dx = \frac{1}{2} \cdot 1 = \frac{1}{2} \]

### Combining the Results

Now we combine the results of the two integrals:

\[ 4 \int\limits_0^\infty x^3 e^{-x^2} \, dx - 2 \int\limits_0^\infty x e^{-x^2} \, dx = 4 \cdot \frac{1}{2} - 2 \cdot \frac{1}{2} = 2 - 1 = 1 \]

### Numerical Approximation

The numerical approximation of the result is:

\[ 1.0000000000 \]

### Final Answer in JSON Format

```json
{"answer": "1", "numerical_answer": "1.0000000000"}
```