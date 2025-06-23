# Evaluating the definite integral $\int_0^\infty x^{2-1}e^{-1.0x^2}H_2(1.0x)dx$

I'll solve this integral step by step. First, let me identify what we have:
- The integral is $\int_0^\infty x^{2-1}e^{-1.0x^2}H_2(1.0x)dx = \int_0^\infty x e^{-1.0x^2}H_2(1.0x)dx$
- $H_2(x)$ is the Hermite polynomial of degree 2, which is $H_2(x) = 4x^2 - 2$

## Step 1: Substitute the Hermite polynomial
$H_2(1.0x) = 4(1.0x)^2 - 2 = 4x^2 - 2$

So the integral becomes:
$$\int_0^\infty x e^{-1.0x^2}(4x^2 - 2)dx = 4\int_0^\infty x^3 e^{-1.0x^2}dx - 2\int_0^\infty x e^{-1.0x^2}dx$$

## Step 2: Solve each integral separately

### For the first integral $4\int_0^\infty x^3 e^{-1.0x^2}dx$:
Let $u = 1.0x^2$, then $du = 2.0x dx$, or $x dx = \frac{du}{2.0}$
When $x = 0$, $u = 0$; when $x \to \infty$, $u \to \infty$

This gives us:
$$4\int_0^\infty x^3 e^{-1.0x^2}dx = 4\int_0^\infty x^2 \cdot x \cdot e^{-1.0x^2}dx = 4\int_0^\infty \frac{u}{1.0} \cdot \frac{du}{2.0} \cdot e^{-u}$$
$$= \frac{4}{2.0 \cdot 1.0}\int_0^\infty u e^{-u}du = 2\int_0^\infty u e^{-u}du$$

Using integration by parts with $f(u) = u$ and $g'(u) = e^{-u}$:
$$\int u e^{-u}du = -u e^{-u} - \int(-e^{-u})du = -u e^{-u} + \int e^{-u}du = -u e^{-u} - e^{-u} + C$$

Evaluating from 0 to ∞:
$$2\int_0^\infty u e^{-u}du = 2\left[(-u e^{-u} - e^{-u})\right]_0^\infty = 2\left[(0 - 0) - (0 - (-1))\right] = 2 \cdot 1 = 2$$

### For the second integral $-2\int_0^\infty x e^{-1.0x^2}dx$:
Let $u = 1.0x^2$, then $du = 2.0x dx$, or $x dx = \frac{du}{2.0}$
When $x = 0$, $u = 0$; when $x \to \infty$, $u \to \infty$

This gives us:
$$-2\int_0^\infty x e^{-1.0x^2}dx = -2\int_0^\infty \frac{du}{2.0} \cdot e^{-u} = -\frac{2}{2.0}\int_0^\infty e^{-u}du = -\int_0^\infty e^{-u}du$$
$$= -\left[-e^{-u}\right]_0^\infty = -\left[0 - (-1)\right] = -1$$

## Step 3: Combine the results
The definite integral equals the sum of our two parts:
$$4\int_0^\infty x^3 e^{-1.0x^2}dx - 2\int_0^\infty x e^{-1.0x^2}dx = 2 + (-1) = 1$$

## Step 4: Numerical approximation
The exact result is 1, which to 10 decimal places is 1.0000000000

{"answer": "1", "numerical_answer": "1.0000000000"}