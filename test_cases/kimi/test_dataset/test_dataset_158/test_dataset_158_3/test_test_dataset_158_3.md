To solve the definite integral \(\int\limits_0^\infty x^{2-1}e^{-1.0x^2}H_2(1.0x)dx\), we need to understand the components involved. Here, \(H_2(x)\) is the Hermite polynomial of degree 2, which is given by:

\[ H_2(x) = 4x^2 - 2 \]

The integral can be rewritten as:

\[ \int\limits_0^\infty x e^{-x^2} (4x^2 - 2) \, dx \]

We can split this into two separate integrals:

\[ \int\limits_0^\infty x e^{-x^2} (4x^2 - 2) \, dx = 4 \int\limits_0^\infty x^3 e^{-x^2} \, dx - 2 \int\limits_0^\infty x e^{-x^2} \, dx \]

Let's evaluate each integral separately.

### First Integral: \(\int\limits_0^\infty x^3 e^{-x^2} \, dx\)

We use the substitution \(u = x^2\), hence \(du = 2x \, dx\) or \(dx = \frac{du}{2x}\). When \(x = 0\), \(u = 0\), and when \(x \to \infty\), \(u \to \infty\). The integral becomes:

\[ \int\limits_0^\infty x^3 e^{-x^2} \, dx = \int\limits_0^\infty x^2 \cdot x e^{-x^2} \, dx = \int\limits_0^\infty u \cdot \frac{e^{-u}}{2} \, du = \frac{1}{2} \int\limits_0^\infty u e^{-u} \, du \]

The integral \(\int\limits_0^\infty u e^{-u} \, du\) is a known result and equals \(\Gamma(2) = 1!\), where \(\Gamma\) is the Gamma function. Therefore:

\[ \int\limits_0^\infty u e^{-u} \, du = 1 \]

So,

\[ \int\limits_0^\infty x^3 e^{-x^2} \, dx = \frac{1}{2} \cdot 1 = \frac{1}{2} \]

### Second Integral: \(\int\limits_0^\infty x e^{-x^2} \, dx\)

Using the same substitution \(u = x^2\), \(du = 2x \, dx\), the integral becomes:

\[ \int\limits_0^\infty x e^{-x^2} \, dx = \int\limits_0^\infty \frac{e^{-u}}{2} \, du = \frac{1}{2} \int\limits_0^\infty e^{-u} \, du \]

The integral \(\int\limits_0^\infty e^{-u} \, du\) is a known result and equals \(\Gamma(1) = 0!\), which is 1. Therefore:

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