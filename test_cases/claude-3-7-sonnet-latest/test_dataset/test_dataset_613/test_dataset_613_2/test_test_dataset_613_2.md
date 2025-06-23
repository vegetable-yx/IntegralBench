# Evaluating $\int_{-1}^{0}5\left(x^{6}+x\right)^{4}\:\mathrm{d}x$

## Step 1: Substitution
Let's use the substitution method with $u = x^6 + x$

This gives us:
$\frac{du}{dx} = 6x^5 + 1$
$dx = \frac{du}{6x^5 + 1}$

## Step 2: Rewriting the integral
$\int_{-1}^{0}5\left(x^{6}+x\right)^{4}\:\mathrm{d}x = \int_{-1}^{0}5u^{4}\:\frac{du}{6x^5 + 1}$

This substitution is challenging because we can't easily express $x$ in terms of $u$. Let's try a different approach.

## Step 3: Using the Fundamental Theorem of Calculus
Let's find an antiderivative of $5(x^6+x)^4$ directly.

Let $F(x) = 5\int(x^6+x)^4\:dx$

We can use another substitution: $u = x^6+x$ and $du = (6x^5+1)dx$

This gives us:
$F(x) = 5\int u^4 \frac{du}{6x^5+1}$

Since $du = (6x^5+1)dx$, we have:
$F(x) = 5\int \frac{u^4}{6x^5+1} \cdot (6x^5+1)dx = 5\int u^4 du = 5 \cdot \frac{u^5}{5} + C = u^5 + C = (x^6+x)^5 + C$

## Step 4: Evaluating the definite integral
$\int_{-1}^{0}5\left(x^{6}+x\right)^{4}\:\mathrm{d}x = \left[(x^6+x)^5\right]_{-1}^{0}$

At $x = 0$: $(0^6+0)^5 = 0^5 = 0$

At $x = -1$: $((-1)^6+(-1))^5 = (1-1)^5 = 0^5 = 0$

Therefore:
$\int_{-1}^{0}5\left(x^{6}+x\right)^{4}\:\mathrm{d}x = 0 - 0 = 0$

## Step 5: Numerical approximation
The exact answer is 0, and the numerical approximation rounded to 10 decimal places is 0.0000000000.

{"answer": "0", "numerical_answer": "0.0000000000"}