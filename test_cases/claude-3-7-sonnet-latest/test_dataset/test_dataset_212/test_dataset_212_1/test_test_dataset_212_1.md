# Calculating $\int\limits_0^{2.0}x^{1/2}(2.0-x)^{1/2}\cos\left(1.0\sqrt{x(2.0-x)}\right)dx$

## Step 1: Substitution
Let's make a substitution to simplify this integral. Notice that we have $x(2.0-x)$ inside the cosine function. 

Let's set $u = \sqrt{x(2.0-x)}$, which gives us $u^2 = x(2.0-x) = 2.0x - x^2$

We need to find $dx$ in terms of $du$. Differentiating both sides:
$2u \, du = 2.0 - 2x$

Solving for $x$ from $u^2 = 2.0x - x^2$:
$x^2 - 2.0x + u^2 = 0$

Using the quadratic formula:
$x = \frac{2.0 \pm \sqrt{4.0 - 4u^2}}{2} = 1.0 \pm \sqrt{1.0 - u^2}$

Since $x$ ranges from 0 to 2.0, and considering the domain constraints, we have:
$x = 1.0 - \sqrt{1.0 - u^2}$

Differentiating this expression:
$dx = \frac{u}{\sqrt{1.0 - u^2}} \, du$

## Step 2: Rewriting the integral
When $x = 0$, $u = 0$
When $x = 2.0$, $u = 0$

Also, $x^{1/2}(2.0-x)^{1/2} = \sqrt{x(2.0-x)} = u$

Our integral becomes:
$\int_{0}^{0} u \cdot \cos(1.0 \cdot u) \cdot \frac{u}{\sqrt{1.0 - u^2}} \, du$

But this is incorrect since the upper limit of $u$ should not be 0. Let's analyze the range of $u$ more carefully.

When $x$ increases from 0 to 1.0, $u$ increases from 0 to 1.0
When $x$ increases from 1.0 to 2.0, $u$ decreases from 1.0 to 0

So our integral needs to be split:
$\int_{0}^{1.0} u \cdot \cos(1.0 \cdot u) \cdot \frac{u}{\sqrt{1.0 - u^2}} \, du + \int_{1.0}^{0} u \cdot \cos(1.0 \cdot u) \cdot \frac{u}{\sqrt{1.0 - u^2}} \, du$

## Step 3: Alternative approach using symmetry
Let's take a step back and use the symmetry of the integrand. If we substitute $y = 2.0 - x$, we can show that the integral is symmetric around $x = 1.0$.

This means:
$\int_{0}^{2.0} x^{1/2}(2.0-x)^{1/2}\cos\left(1.0\sqrt{x(2.0-x)}\right)dx = 2 \int_{0}^{1.0} x^{1/2}(2.0-x)^{1/2}\cos\left(1.0\sqrt{x(2.0-x)}\right)dx$

## Step 4: Using polar coordinates
Let's use the substitution $x = 1.0 - \cos\theta$ or equivalently $x = 1.0 + \cos(\theta+\pi)$

With this substitution:
- When $x = 0$, $\theta = \arccos(1.0) = 0$
- When $x = 1.0$, $\theta = \arccos(0) = \pi/2$
- When $x = 2.0$, $\theta = \arccos(-1.0) = \pi$

Also:
$x(2.0-x) = (1.0-\cos\theta)(1.0+\cos\theta) = 1.0-\cos^2\theta = \sin^2\theta$

So $\sqrt{x(2.0-x)} = \sin\theta$

And:
$x^{1/2}(2.0-x)^{1/2} = \sqrt{(1.0-\cos\theta)(1.0+\cos\theta)} = \sin\theta$

$dx = \sin\theta \, d\theta$

The integral becomes:
$\int_{0}^{\pi} \sin\theta \cdot \cos(1.0 \cdot \sin\theta) \cdot \sin\theta \, d\theta = \int_{0}^{\pi} \sin^2\theta \cdot \cos(\sin\theta) \, d\theta$

Due to symmetry around $\theta = \pi/2$, this equals:
$2 \int_{0}^{\pi/2} \sin^2\theta \cdot \cos(\sin\theta) \, d\theta$

## Step 5: Evaluation using Bessel functions
This integral can be expressed in terms of the Bessel function of the first kind:
$\int_{0}^{\pi} \sin^2\theta \cdot \cos(\sin\theta) \, d\theta = \pi J_1(1)$

Where $J_1(1)$ is the Bessel function of the first kind of order 1 evaluated at 1.

## Step 6: Numerical evaluation
$J_1(1) \approx 0.4400505857$

Therefore:
$\int_{0}^{2.0} x^{1/2}(2.0-x)^{1/2}\cos\left(1.0\sqrt{x(2.0-x)}\right)dx = \pi J_1(1) \approx \pi \cdot 0.4400505857 \approx 1.3825692956$

The exact answer is $\pi J_1(1)$.

{"answer": "\\pi J_1(1)", "numerical_answer": "1.3825692956"}