# Evaluating $\int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx$

## Step 1: Set up a substitution
Let's use the substitution $u = \cos(x)$ to simplify this integral.

When $u = \cos(x)$:
- $du = -\sin(x)dx$
- $dx = -\frac{du}{\sin(x)}$

Also, when $x = 0$, $u = \cos(0) = 1$
When $x = \pi/2$, $u = \cos(\pi/2) = 0$

## Step 2: Transform the integral
$\int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx = \int_1^0\frac{u}{2-u^2}\left(-\frac{1}{\sin(x)}\right)du$

Since $\sin(x) = \sqrt{1-\cos^2(x)} = \sqrt{1-u^2}$, we have:

$\int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx = \int_1^0\frac{-u}{(2-u^2)\sqrt{1-u^2}}du = \int_0^1\frac{u}{(2-u^2)\sqrt{1-u^2}}du$

## Step 3: Further simplify the integral
Let's rewrite the denominator:
$2-u^2 = 2-(1-(1-u^2)) = 2-1+(1-u^2) = 1+(1-u^2)$

So our integral becomes:
$\int_0^1\frac{u}{(1+(1-u^2))\sqrt{1-u^2}}du = \int_0^1\frac{u}{(1+\sqrt{1-u^2}^2)\sqrt{1-u^2}}du$

## Step 4: Try another approach
Let's start fresh with a different substitution. Let $u = \sin(x)$, so $du = \cos(x)dx$.

When $x = 0$, $u = \sin(0) = 0$
When $x = \pi/2$, $u = \sin(\pi/2) = 1$

With this substitution:
$\int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx = \int_0^1\frac{1}{2-\cos^2(x)}du = \int_0^1\frac{1}{2-(1-\sin^2(x))}du$

$= \int_0^1\frac{1}{2-(1-u^2)}du = \int_0^1\frac{1}{1+u^2}du$

## Step 5: Evaluate the simplified integral
$\int_0^1\frac{1}{1+u^2}du = \left[ \arctan(u) \right]_0^1 = \arctan(1) - \arctan(0) = \frac{\pi}{4} - 0 = \frac{\pi}{4}$

## Step 6: Verify the result
Let's double-check by using another approach. 

Note that $2-\cos^2(x) = 1+\sin^2(x)$, so:
$\int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx = \int_0^{\pi/2}\frac{\cos(x)}{1+\sin^2(x)}dx$

With the substitution $u = \sin(x)$, $du = \cos(x)dx$, we get:
$\int_0^1\frac{1}{1+u^2}du = \arctan(u)\big|_0^1 = \arctan(1) - \arctan(0) = \frac{\pi}{4}$

## Numerical approximation
$\frac{\pi}{4} \approx 0.7853981634$

{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}