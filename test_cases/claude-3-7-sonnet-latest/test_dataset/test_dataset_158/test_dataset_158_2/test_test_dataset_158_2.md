# Evaluating $\int_0^\infty x^{2-1}e^{-1.0x^2}H_2(1.0x)dx$

I'll compute the definite integral $\int_0^\infty x^{2-1}e^{-1.0x^2}H_2(1.0x)dx$. 

## Step 1: Simplify the integrand
First, I'll simplify the expression. We have $x^{2-1} = x^1 = x$.

Also, $H_2(1.0x)$ is the Hermite polynomial of degree 2 evaluated at $1.0x$.
The Hermite polynomial $H_2(y) = 4y^2-2$, so $H_2(1.0x) = 4(1.0x)^2-2 = 4x^2-2$.

So our integral becomes:
$$\int_0^\infty x \cdot e^{-1.0x^2} \cdot (4x^2-2)dx$$

Distributing:
$$\int_0^\infty (4x^3e^{-1.0x^2} - 2xe^{-1.0x^2})dx$$

## Step 2: Evaluate each part separately

### Part 1: $\int_0^\infty 4x^3e^{-1.0x^2}dx$

Let $u = 1.0x^2$, then $du = 2.0x\,dx$, or $x\,dx = \frac{du}{2.0}$
When $x = 0$, $u = 0$; when $x \to \infty$, $u \to \infty$

Substituting:
$$4\int_0^\infty x^2 \cdot x\,e^{-1.0x^2}dx = 4\int_0^\infty \frac{u}{1.0} \cdot \frac{du}{2.0} \cdot e^{-u} = \frac{4}{2.0 \cdot 1.0}\int_0^\infty u \cdot e^{-u}du$$

We know that $\int_0^\infty u \cdot e^{-u}du = 1$, so:
$$\frac{4}{2.0 \cdot 1.0} \cdot 1 = \frac{4}{2.0} = 2.0$$

### Part 2: $\int_0^\infty -2xe^{-1.0x^2}dx$

Using the substitution $u = 1.0x^2$, $du = 2.0x\,dx$, or $x\,dx = \frac{du}{2.0}$:
$$-2\int_0^\infty x\,e^{-1.0x^2}dx = -2\int_0^\infty \frac{du}{2.0} \cdot e^{-u} = -\frac{2}{2.0}\int_0^\infty e^{-u}du = -1.0 \cdot [-e^{-u}]_0^\infty = -1.0 \cdot (0-(-1)) = 1.0$$

## Step 3: Combine the results
Adding both parts:
$$2.0 + 1.0 = 3.0$$

## Step 4: Numerical approximation
The numerical value is exactly 3.0, which rounded to 10 decimal places is 3.0000000000.

{"answer": "3.0", "numerical_answer": "3.0000000000"}