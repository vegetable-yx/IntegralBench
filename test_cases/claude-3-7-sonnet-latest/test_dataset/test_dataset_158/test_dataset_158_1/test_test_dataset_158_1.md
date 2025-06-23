# Evaluating the definite integral $\int\limits_0^\infty x^{2-1}e^{-1.0x^2}H_2(1.0x)dx$

I'll evaluate $\int\limits_0^\infty x^{2-1}e^{-1.0x^2}H_2(1.0x)dx = \int\limits_0^\infty x e^{-x^2}H_2(x)dx$, where $H_2(x)$ is the Hermite polynomial of degree 2.

## Step 1: Identify the Hermite polynomial $H_2(x)$
The Hermite polynomial $H_2(x) = 4x^2-2$

## Step 2: Substitute the Hermite polynomial
$$\int\limits_0^\infty x e^{-x^2}H_2(x)dx = \int\limits_0^\infty x e^{-x^2}(4x^2-2)dx$$
$$= 4\int\limits_0^\infty x^3 e^{-x^2}dx - 2\int\limits_0^\infty x e^{-x^2}dx$$

## Step 3: Solve each integral separately

For the first integral $\int\limits_0^\infty x^3 e^{-x^2}dx$:
Let $u = x^2$, then $du = 2x\,dx$ and $x\,dx = \frac{du}{2}$
When $x = 0$, $u = 0$; when $x \to \infty$, $u \to \infty$

$$\int\limits_0^\infty x^3 e^{-x^2}dx = \int\limits_0^\infty x^2 \cdot x \cdot e^{-x^2}dx = \int\limits_0^\infty u \cdot e^{-u} \cdot \frac{du}{2} = \frac{1}{2}\int\limits_0^\infty u e^{-u}du$$

This is the gamma function $\Gamma(2) = 1$, so:
$$\frac{1}{2}\int\limits_0^\infty u e^{-u}du = \frac{1}{2} \cdot 1 = \frac{1}{2}$$

For the second integral $\int\limits_0^\infty x e^{-x^2}dx$:
Let $v = x^2$, then $dv = 2x\,dx$ and $x\,dx = \frac{dv}{2}$
When $x = 0$, $v = 0$; when $x \to \infty$, $v \to \infty$

$$\int\limits_0^\infty x e^{-x^2}dx = \int\limits_0^\infty e^{-v} \cdot \frac{dv}{2} = \frac{1}{2}\int\limits_0^\infty e^{-v}dv = \frac{1}{2}[{-e^{-v}}]_0^\infty = \frac{1}{2}(0-(-1)) = \frac{1}{2}$$

## Step 4: Combine the results

$$\int\limits_0^\infty x e^{-x^2}H_2(x)dx = 4 \cdot \frac{1}{2} - 2 \cdot \frac{1}{2} = 2 - 1 = 1$$

Therefore, the exact answer is 1.

## Step 5: Numerical approximation
The numerical approximation of the result, rounded to 10 decimal places, is 1.0000000000.

{"answer": "1", "numerical_answer": "1.0000000000"}