# Evaluating the Definite Integral $\int_{0}^{5}x^2\cosh\left(2\sqrt{x(5-x)}\right)dx$

I'll solve this definite integral step by step.

## Step 1: Observe the symmetry in the problem

Let's examine the integral $\int_{0}^{5}x^2\cosh\left(2\sqrt{x(5-x)}\right)dx$

First, I notice that the expression $\sqrt{x(5-x)}$ is symmetric around $x = 2.5$. Let's make a substitution $u = 5-x$ to explore this symmetry:

When $x = 0$, $u = 5$
When $x = 5$, $u = 0$

Under this substitution:
$dx = -du$
$\sqrt{x(5-x)} = \sqrt{(5-u)u} = \sqrt{u(5-u)}$

So the integral becomes:
$\int_{0}^{5}x^2\cosh\left(2\sqrt{x(5-x)}\right)dx = \int_{5}^{0}(5-u)^2\cosh\left(2\sqrt{u(5-u)}\right)(-du)$
$= \int_{0}^{5}(5-u)^2\cosh\left(2\sqrt{u(5-u)}\right)du$

## Step 2: Combine the original integral with the substituted form

Let's add the original integral and the substituted form:

$\int_{0}^{5}x^2\cosh\left(2\sqrt{x(5-x)}\right)dx + \int_{0}^{5}(5-x)^2\cosh\left(2\sqrt{x(5-x)}\right)dx$
$= \int_{0}^{5}[x^2+(5-x)^2]\cosh\left(2\sqrt{x(5-x)}\right)dx$
$= \int_{0}^{5}[x^2+25-10x+x^2]\cosh\left(2\sqrt{x(5-x)}\right)dx$
$= \int_{0}^{5}[2x^2-10x+25]\cosh\left(2\sqrt{x(5-x)}\right)dx$

Since we're adding two equal integrals (due to the symmetry), we get:

$2\int_{0}^{5}x^2\cosh\left(2\sqrt{x(5-x)}\right)dx = \int_{0}^{5}[2x^2-10x+25]\cosh\left(2\sqrt{x(5-x)}\right)dx$

## Step 3: Simplify further using the property of the problem

Note that:
$2x^2-10x+25 = 2(x^2-5x+\frac{25}{2})$
$= 2[(x-\frac{5}{2})^2+\frac{25}{4}]$
$= 2(x-\frac{5}{2})^2+\frac{50}{4} = 2(x-\frac{5}{2})^2+\frac{25}{2}$

So our combined integral becomes:
$2\int_{0}^{5}x^2\cosh\left(2\sqrt{x(5-x)}\right)dx = \int_{0}^{5}[2(x-\frac{5}{2})^2+\frac{25}{2}]\cosh\left(2\sqrt{x(5-x)}\right)dx$

Observe that $(x-\frac{5}{2})^2+\frac{25}{4}-x(5-x) = (x-\frac{5}{2})^2+\frac{25}{4}-(5x-x^2) = x^2-5x+\frac{25}{4}+\frac{25}{4}+5x-x^2 = \frac{25}{2}$

Therefore, $x(5-x) = \frac{25}{2}-(x-\frac{5}{2})^2$

## Step 4: Use the special property of the integral

The expression $\sqrt{x(5-x)}$ reaches its maximum value at $x = 2.5$, where it equals $\sqrt{6.25} = 2.5$

Due to the symmetry of $\cosh\left(2\sqrt{x(5-x)}\right)$ around $x = 2.5$, the integral of $(x-\frac{5}{2})^2\cosh\left(2\sqrt{x(5-x)}\right)$ over $[0,5]$ is zero.

This means:
$\int_{0}^{5}2(x-\frac{5}{2})^2\cosh\left(2\sqrt{x(5-x)}\right)dx = 0$

Therefore:
$2\int_{0}^{5}x^2\cosh\left(2\sqrt{x(5-x)}\right)dx = \int_{0}^{5}\frac{25}{2}\cosh\left(2\sqrt{x(5-x)}\right)dx$

## Step 5: Evaluate the remaining integral

Now we have:
$\int_{0}^{5}x^2\cosh\left(2\sqrt{x(5-x)}\right)dx = \frac{1}{4} \cdot \frac{25}{2}\int_{0}^{5}\cosh\left(2\sqrt{x(5-x)}\right)dx$

Let's use the substitution $u = 2\sqrt{x(5-x)}$. When $x$ goes from 0 to 5, $u$ goes from 0 to 0 (it increases to 5 at $x = 2.5$ and then decreases back to 0).

This gives us:
$\int_{0}^{5}\cosh\left(2\sqrt{x(5-x)}\right)dx = 2\int_{0}^{5}\cosh(u)du = 2\sinh(5)$

Therefore:
$\int_{0}^{5}x^2\cosh\left(2\sqrt{x(5-x)}\right)dx = \frac{25}{8} \cdot 2\sinh(5) = \frac{25\sinh(5)}{4}$

## Step 6: Calculate the numerical value

$\sinh(5) \approx 74.2032105777888$

Therefore:
$\frac{25\sinh(5)}{4} \approx \frac{25 \times 74.2032105777888}{4} \approx 463.7700661111800$

## Final Answer

The definite integral $\int_{0}^{5}x^2\cosh\left(2\sqrt{x(5-x)}\right)dx = \frac{25\sinh(5)}{4}$

Numerical approximation (to 10 decimal places): 463.7700661112

{"answer": "\\frac{25\\sinh(5)}{4}", "numerical_answer": "463.7700661112"}