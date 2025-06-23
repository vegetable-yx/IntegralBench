# Evaluating $\int_0^\pi\cos(x)\cos(3x)\cos(5x)dx$

I'll use the trigonometric product-to-sum formulas to solve this integral.

## Step 1: Convert the product of cosines to a sum
Using the identity: $\cos(A)\cos(B) = \frac{1}{2}[\cos(A+B) + \cos(A-B)]$

First, let's work with $\cos(x)\cos(3x)$:
$\cos(x)\cos(3x) = \frac{1}{2}[\cos(x+3x) + \cos(x-3x)] = \frac{1}{2}[\cos(4x) + \cos(-2x)]$

Since $\cos(-2x) = \cos(2x)$, we have:
$\cos(x)\cos(3x) = \frac{1}{2}[\cos(4x) + \cos(2x)]$

Now, multiply by $\cos(5x)$:
$\cos(x)\cos(3x)\cos(5x) = \frac{1}{2}[\cos(4x)\cos(5x) + \cos(2x)\cos(5x)]$

Using the same identity again:
$\cos(4x)\cos(5x) = \frac{1}{2}[\cos(4x+5x) + \cos(4x-5x)] = \frac{1}{2}[\cos(9x) + \cos(-x)]$

$\cos(2x)\cos(5x) = \frac{1}{2}[\cos(2x+5x) + \cos(2x-5x)] = \frac{1}{2}[\cos(7x) + \cos(-3x)]$

Since $\cos(-x) = \cos(x)$ and $\cos(-3x) = \cos(3x)$, we have:
$\cos(x)\cos(3x)\cos(5x) = \frac{1}{4}[\cos(9x) + \cos(x) + \cos(7x) + \cos(3x)]$

## Step 2: Integrate the sum
$\int_0^\pi\cos(x)\cos(3x)\cos(5x)dx = \frac{1}{4}\int_0^\pi[\cos(9x) + \cos(x) + \cos(7x) + \cos(3x)]dx$

We know that $\int\cos(nx)dx = \frac{1}{n}\sin(nx) + C$, so:

$\frac{1}{4}\int_0^\pi[\cos(9x) + \cos(x) + \cos(7x) + \cos(3x)]dx$
$= \frac{1}{4}\left[\frac{\sin(9x)}{9} + \sin(x) + \frac{\sin(7x)}{7} + \frac{\sin(3x)}{3}\right]_0^\pi$

## Step 3: Evaluate at the limits
For any integer $n$, $\sin(n\pi) = 0$ and $\sin(0) = 0$, so:

$\frac{1}{4}\left[\frac{\sin(9\pi)}{9} + \sin(\pi) + \frac{\sin(7\pi)}{7} + \frac{\sin(3\pi)}{3} - \frac{\sin(0)}{9} - \sin(0) - \frac{\sin(0)}{7} - \frac{\sin(0)}{3}\right]$
$= \frac{1}{4}\left[0 + 0 + 0 + 0 - 0 - 0 - 0 - 0\right]$
$= 0$

## Step 4: Verify the result
The definite integral $\int_0^\pi\cos(x)\cos(3x)\cos(5x)dx = 0$

## Numerical approximation
The exact value is 0, so numerically it's 0.0000000000 (rounded to 10 decimal places).

{"answer": "0", "numerical_answer": "0.0000000000"}