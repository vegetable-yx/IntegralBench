# Evaluating $\int_0^\pi\cos(x)\cos(3x)\cos(5x)dx$

I'll solve this integral using trigonometric identities.

## Step 1: Use the product-to-sum formula
We can use the formula: $\cos(A)\cos(B) = \frac{1}{2}[\cos(A+B) + \cos(A-B)]$

Let's first simplify $\cos(x)\cos(3x)$:
$\cos(x)\cos(3x) = \frac{1}{2}[\cos(x+3x) + \cos(x-3x)] = \frac{1}{2}[\cos(4x) + \cos(-2x)]$

Since $\cos(-2x) = \cos(2x)$, we have:
$\cos(x)\cos(3x) = \frac{1}{2}[\cos(4x) + \cos(2x)]$

## Step 2: Multiply the result by $\cos(5x)$
Now we calculate $\frac{1}{2}[\cos(4x) + \cos(2x)]\cos(5x)$:

$\frac{1}{2}\cos(4x)\cos(5x) = \frac{1}{4}[\cos(4x+5x) + \cos(4x-5x)] = \frac{1}{4}[\cos(9x) + \cos(-x)] = \frac{1}{4}[\cos(9x) + \cos(x)]$

$\frac{1}{2}\cos(2x)\cos(5x) = \frac{1}{4}[\cos(2x+5x) + \cos(2x-5x)] = \frac{1}{4}[\cos(7x) + \cos(-3x)] = \frac{1}{4}[\cos(7x) + \cos(3x)]$

Combining these results:
$\cos(x)\cos(3x)\cos(5x) = \frac{1}{4}[\cos(9x) + \cos(x) + \cos(7x) + \cos(3x)]$

## Step 3: Integrate each term
$\int_0^\pi\cos(x)\cos(3x)\cos(5x)dx = \frac{1}{4}\int_0^\pi[\cos(9x) + \cos(x) + \cos(7x) + \cos(3x)]dx$

For each term, we use $\int\cos(nx)dx = \frac{1}{n}\sin(nx) + C$:

$\frac{1}{4}\int_0^\pi\cos(9x)dx = \frac{1}{4}[\frac{1}{9}\sin(9x)]_0^\pi = \frac{1}{36}[\sin(9\pi) - \sin(0)] = 0$

$\frac{1}{4}\int_0^\pi\cos(x)dx = \frac{1}{4}[\sin(x)]_0^\pi = \frac{1}{4}[\sin(\pi) - \sin(0)] = 0$

$\frac{1}{4}\int_0^\pi\cos(7x)dx = \frac{1}{4}[\frac{1}{7}\sin(7x)]_0^\pi = \frac{1}{28}[\sin(7\pi) - \sin(0)] = 0$

$\frac{1}{4}\int_0^\pi\cos(3x)dx = \frac{1}{4}[\frac{1}{3}\sin(3x)]_0^\pi = \frac{1}{12}[\sin(3\pi) - \sin(0)] = 0$

All the terms evaluate to zero because $\sin(n\pi) = 0$ for any integer $n$.

## Step 4: Final result
$\int_0^\pi\cos(x)\cos(3x)\cos(5x)dx = 0$

## Numerical approximation
The numerical value is exactly 0.0000000000 (rounded to 10 decimal places).

{"answer": "0", "numerical_answer": "0.0000000000"}