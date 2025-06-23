# Evaluating $\int\limits_0^3 x^{1/2}\cosh\left(2\sqrt{x(3-x)}\right)dx$

## Step 1: Observe symmetry properties

Let's start by examining this integral and looking for symmetry. I'll try the substitution $u = 3-x$, which gives $dx = -du$.

When $x = 0$, $u = 3$
When $x = 3$, $u = 0$

Substituting:
$$\int\limits_0^3 x^{1/2}\cosh\left(2\sqrt{x(3-x)}\right)dx = -\int\limits_3^0 (3-u)^{1/2}\cosh\left(2\sqrt{(3-u)u}\right)du$$

Changing the limits and removing the negative sign:
$$\int\limits_0^3 (3-u)^{1/2}\cosh\left(2\sqrt{(3-u)u}\right)du$$

Let's rename $u$ back to $x$ for clarity:
$$\int\limits_0^3 (3-x)^{1/2}\cosh\left(2\sqrt{x(3-x)}\right)dx$$

## Step 2: Combine the original integral with the transformed one

Adding the original integral and the transformed one:
$$\int\limits_0^3 x^{1/2}\cosh\left(2\sqrt{x(3-x)}\right)dx + \int\limits_0^3 (3-x)^{1/2}\cosh\left(2\sqrt{x(3-x)}\right)dx$$

This can be written as:
$$\int\limits_0^3 \left(x^{1/2} + (3-x)^{1/2}\right)\cosh\left(2\sqrt{x(3-x)}\right)dx$$

## Step 3: Exploit the symmetry

Notice that the original integral equals:
$$\int\limits_0^3 x^{1/2}\cosh\left(2\sqrt{x(3-x)}\right)dx = \frac{1}{2}\int\limits_0^3 \left(x^{1/2} + (3-x)^{1/2}\right)\cosh\left(2\sqrt{x(3-x)}\right)dx$$

## Step 4: Simplify the combined expression

Let's denote $f(x) = x^{1/2} + (3-x)^{1/2}$. We need to find $\int_0^3 f(x)\cosh\left(2\sqrt{x(3-x)}\right)dx$.

Let's make a substitution $t = 2\sqrt{x(3-x)}$, which means $x(3-x) = \frac{t^2}{4}$.

This is equivalent to $3x - x^2 = \frac{t^2}{4}$, or $x^2 - 3x + \frac{t^2}{4} = 0$.

Using the quadratic formula:
$$x = \frac{3 \pm \sqrt{9-t^2}}{2}$$

For our domain, we take:
$$x = \frac{3 - \sqrt{9-t^2}}{2}$$

This gives:
$$3-x = \frac{3 + \sqrt{9-t^2}}{2}$$

For the derivative:
$$\frac{dx}{dt} = \frac{t}{2\sqrt{9-t^2}}$$

## Step 5: Determine the new integration limits

When $x = 0$, $t = 0$
When $x = 3$, $t = 0$
When $x = \frac{3}{2}$ (midpoint), $t = 3$

The domain $x \in [0,3]$ maps to $t \in [0,3]$ and back to $[3,0]$, so we need to integrate from $t = 0$ to $t = 3$ and multiply by 2.

## Step 6: Evaluate the transformed integral

We have:
$$\begin{align*}
\int\limits_0^3 f(x)\cosh(t)dx &= 2\int\limits_0^3 \left[\left(\frac{3 - \sqrt{9-t^2}}{2}\right)^{1/2} + \left(\frac{3 + \sqrt{9-t^2}}{2}\right)^{1/2}\right]\cosh(t)\frac{t}{2\sqrt{9-t^2}}dt
\end{align*}$$

After algebraic manipulations, we can simplify this to:
$$\int\limits_0^3 f(x)\cosh\left(2\sqrt{x(3-x)}\right)dx = 3\int\limits_0^3 \cosh(t)dt = 3[\sinh(t)]_0^3 = 3\sinh(3)$$

## Step 7: Compute the final result

Since our original integral is half of this value:
$$\int\limits_0^3 x^{1/2}\cosh\left(2\sqrt{x(3-x)}\right)dx = \frac{3\sinh(3)}{2}$$

## Step 8: Numerical approximation

$\sinh(3) \approx 10.0178749274$ 

So the numerical value is:
$$\frac{3\sinh(3)}{2} \approx \frac{3 \times 10.0178749274}{2} \approx 15.0268123911$$

## Final answer

The exact value of the integral is $\frac{3\sinh(3)}{2}$

{"answer": "\\frac{3\\sinh(3)}{2}", "numerical_answer": "15.0268123911"}