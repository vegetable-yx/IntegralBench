# Evaluating $\int\limits_0^{2.0}x^{1/2}(2.0-x)^{-1/2}\cos\left(1.0\sqrt{x(2.0-x)}\right)dx$

## Step 1: Analyze the integral and make a substitution

Let's examine the structure of this integral. We have:
$$\int\limits_0^{2.0}x^{1/2}(2.0-x)^{-1/2}\cos\left(1.0\sqrt{x(2.0-x)}\right)dx$$

I notice that $\sqrt{x(2.0-x)}$ appears in the cosine function, so it might be helpful to make a substitution involving this expression.

Let's try the substitution $u = \sqrt{x(2.0-x)}$. This means:
$$u^2 = x(2.0-x) = 2.0x - x^2$$

Differentiating both sides with respect to $x$:
$$2u\frac{du}{dx} = 2.0 - 2x$$
$$\frac{du}{dx} = \frac{2.0 - 2x}{2u} = \frac{1.0 - x}{u}$$

So we have:
$$dx = \frac{u}{1.0 - x}du$$

## Step 2: Express $x$ and $(2.0-x)$ in terms of $u$

From $u^2 = 2.0x - x^2$, we can solve for $x$ in terms of $u$:

$x^2 - 2.0x + u^2 = 0$

Using the quadratic formula:
$$x = \frac{2.0 \pm \sqrt{4.0 - 4u^2}}{2} = 1.0 \pm \sqrt{1.0 - u^2}$$

Since $x$ ranges from 0 to 2.0, and we need $x$ to be continuous, we must have:
$$x = 1.0 - \sqrt{1.0 - u^2}$$

Then:
$$2.0 - x = 2.0 - (1.0 - \sqrt{1.0 - u^2}) = 1.0 + \sqrt{1.0 - u^2}$$

## Step 3: Determine the new limits of integration

When $x = 0$, $u^2 = 0 \cdot (2.0 - 0) = 0$, so $u = 0$.
When $x = 2.0$, $u^2 = 2.0 \cdot (2.0 - 2.0) = 0$, so $u = 0$.

However, as $x$ increases from 0 to 1.0, $u$ increases from 0 to 1.0, and as $x$ increases from 1.0 to 2.0, $u$ decreases from 1.0 back to 0. So our integration limits for $u$ will be from $u = 0$ to $u = 1.0$ and then back to $u = 0$.

## Step 4: Rewrite the integral in terms of $u$

First, let's calculate $x^{1/2}$:
$$x^{1/2} = (1.0 - \sqrt{1.0 - u^2})^{1/2}$$

And $(2.0-x)^{-1/2}$:
$$(2.0-x)^{-1/2} = (1.0 + \sqrt{1.0 - u^2})^{-1/2}$$

Also, $\cos(1.0\sqrt{x(2.0-x)}) = \cos(1.0u)$

Now, we need to be careful with the substitution because the path from $x = 0$ to $x = 2.0$ corresponds to a path from $u = 0$ to $u = 1.0$ and then back to $u = 0$.

## Step 5: Observe symmetry in the integrand

Let's take a different approach. Notice that the integral has a symmetry about the point $x = 1.0$. 

If we substitute $y = 2.0 - x$, then when $x = 0$, $y = 2.0$, and when $x = 2.0$, $y = 0$. Under this substitution:
$$dx = -dy$$
$$x^{1/2} = (2.0 - y)^{1/2}$$
$$(2.0 - x)^{-1/2} = y^{-1/2}$$
$$\sqrt{x(2.0-x)} = \sqrt{(2.0-y)y} = \sqrt{y(2.0-y)}$$

So our integral becomes:
$$\int\limits_{2.0}^{0}(2.0-y)^{1/2}y^{-1/2}\cos\left(1.0\sqrt{y(2.0-y)}\right)(-dy)$$

Which is:
$$\int\limits_{0}^{2.0}(2.0-y)^{1/2}y^{-1/2}\cos\left(1.0\sqrt{y(2.0-y)}\right)dy$$

Comparing this with our original integral, we notice they're identical except for the variables. This means the integral must equal itself.

Let's denote our integral as $I$:
$$I = \int\limits_0^{2.0}x^{1/2}(2.0-x)^{-1/2}\cos\left(1.0\sqrt{x(2.0-x)}\right)dx$$

Let's also define:
$$J = \int\limits_0^{2.0}x^{-1/2}(2.0-x)^{1/2}\cos\left(1.0\sqrt{x(2.0-x)}\right)dx$$

From our substitution, we know $I = J$. 

Now, let's add these two integrals:
$$I + J = \int\limits_0^{2.0}\left[x^{1/2}(2.0-x)^{-1/2} + x^{-1/2}(2.0-x)^{1/2}\right]\cos\left(1.0\sqrt{x(2.0-x)}\right)dx$$

## Step 6: Simplify the combined integrand

The term in brackets can be simplified:
$$x^{1/2}(2.0-x)^{-1/2} + x^{-1/2}(2.0-x)^{1/2} = \frac{x^{1/2}(2.0-x)^{1/2} + x^{1/2}(2.0-x)^{1/2}}{x^{1/2}(2.0-x)^{1/2}} = \frac{2\sqrt{x(2.0-x)}}{\sqrt{x(2.0-x)}} = 2$$

So:
$$I + J = \int\limits_0^{2.0}2\cos\left(1.0\sqrt{x(2.0-x)}\right)dx = 2\int\limits_0^{2.0}\cos\left(1.0\sqrt{x(2.0-x)}\right)dx$$

## Step 7: Use the substitution $u = \sqrt{x(2.0-x)}$

Now, let's use the substitution $u = \sqrt{x(2.0-x)}$, which gives us:
$$x = 1.0 - \sqrt{1.0 - u^2}$$

With differential:
$$dx = \frac{u}{\sqrt{1.0 - u^2}}du$$

When $x$ ranges from 0 to 2.0, $u$ goes from 0 to 1.0 and then back to 0. So we'll split the integral into two parts:

$$2\int\limits_0^{2.0}\cos\left(1.0\sqrt{x(2.0-x)}\right)dx = 2\int\limits_0^{1.0}\cos(1.0u) \cdot 2 \cdot \frac{u}{\sqrt{1.0 - u^2}}du = 4\int\limits_0^{1.0}\frac{u\cos(1.0u)}{\sqrt{1.0 - u^2}}du$$

## Step 8: Integrate using integration by parts

Let's use integration by parts with:
$$\begin{align*}
v &= \frac{u}{\sqrt{1.0 - u^2}} \\
dw &= \cos(1.0u)du
\end{align*}$$

This gives us:
$$\begin{align*}
dv &= \frac{1.0}{\sqrt{1.0 - u^2}} + \frac{u^2}{(1.0 - u^2)^{3/2}}du = \frac{1.0}{(1.0 - u^2)^{3/2}}du \\
w &= \sin(1.0u)
\end{align*}$$

So by integration by parts:
$$\int v \, dw = vw - \int w \, dv$$

$$\int\frac{u\cos(1.0u)}{\sqrt{1.0 - u^2}}du = \frac{u\sin(1.0u)}{\sqrt{1.0 - u^2}} - \int\frac{\sin(1.0u)}{(1.0 - u^2)^{3/2}}du$$

The second integral is complicated, so let's try a different approach.

## Step 9: Use a new substitution

Let's try the substitution $u = \sin(t)$ for $t \in [0, \frac{\pi}{2}]$. Then:
$$du = \cos(t)dt$$
$$\sqrt{1.0 - u^2} = \sqrt{1.0 - \sin^2(t)} = \cos(t)$$

When $u = 0$, $t = 0$, and when $u = 1.0$, $t = \frac{\pi}{2}$.

Our integral becomes:
$$4\int\limits_0^{1.0}\frac{u\cos(1.0u)}{\sqrt{1.0 - u^2}}du = 4\int\limits_0^{\pi/2}\frac{\sin(t)\cos(1.0\sin(t))}{\cos(t)}\cos(t)dt = 4\int\limits_0^{\pi/2}\sin(t)\cos(1.0\sin(t))dt$$

## Step 10: Recognize the final form

This is a standard integral that evaluates to:
$$4\int\limits_0^{\pi/2}\sin(t)\cos(1.0\sin(t))dt = 4 \cdot \sin(1.0)$$

So:
$$I + J = 4\sin(1.0)$$

Since $I = J$, we have:
$$2I = 4\sin(1.0)$$
$$I = 2\sin(1.0)$$

Therefore:
$$\int\limits_0^{2.0}x^{1/2}(2.0-x)^{-1/2}\cos\left(1.0\sqrt{x(2.0-x)}\right)dx = 2\sin(1.0)$$

## Step 11: Calculate the numerical value

$\sin(1.0) \approx 0.8414709848$ (in radians)

So $2\sin(1.0) \approx 2 \times 0.8414709848 = 1.6829419696$

Therefore:

{"