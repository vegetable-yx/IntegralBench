# Evaluating $\int_0^\pi\cos(x)\cos(3x)\cos(5x)dx$

## Step 1: Use trigonometric product identities

I'll use the trigonometric identity:
$\cos(A)\cos(B) = \frac{1}{2}[\cos(A+B) + \cos(A-B)]$

First, let's simplify $\cos(x)\cos(3x)$:
$\cos(x)\cos(3x) = \frac{1}{2}[\cos(x+3x) + \cos(x-3x)] = \frac{1}{2}[\cos(4x) + \cos(-2x)] = \frac{1}{2}[\cos(4x) + \cos(2x)]$

Now, I need to multiply this result by $\cos(5x)$:
$\cos(x)\cos(3x)\cos(5x) = \frac{1}{2}[\cos(4x) + \cos(2x)]\cos(5x)$

Let's apply the identity again:
$\frac{1}{2}\cos(4x)\cos(5x) = \frac{1}{4}[\cos(4x+5x) + \cos(4x-5x)] = \frac{1}{4}[\cos(9x) + \cos(-x)] = \frac{1}{4}[\cos(9x) + \cos(x)]$

And:
$\frac{1}{2}\cos(2x)\cos(5x) = \frac{1}{4}[\cos(2x+5x) + \cos(2x-5x)] = \frac{1}{4}[\cos(7x) + \cos(-3x)] = \frac{1}{4}[\cos(7x) + \cos(3x)]$

Therefore:
$\cos(x)\cos(3x)\cos(5x) = \frac{1}{4}[\cos(9x) + \cos(x) + \cos(7x) + \cos(3x)]$

## Step 2: Integrate each term

$\int_0^\pi\cos(x)\cos(3x)\cos(5x)dx = \frac{1}{4}\int_0^\pi[\cos(9x) + \cos(x) + \cos(7x) + \cos(3x)]dx$

For each term, we use $\int\cos(nx)dx = \frac{1}{n}\sin(nx) + C$:

$\frac{1}{4}\int_0^\pi\cos(9x)dx = \frac{1}{4} \cdot \frac{1}{9}[\sin(9x)]_0^\pi = \frac{1}{36}[\sin(9\pi) - \sin(0)] = \frac{1}{36} \cdot 0 = 0$

$\frac{1}{4}\int_0^\pi\cos(x)dx = \frac{1}{4}[\sin(x)]_0^\pi = \frac{1}{4}[\sin(\pi) - \sin(0)] = \frac{1}{4} \cdot 0 = 0$

$\frac{1}{4}\int_0^\pi\cos(7x)dx = \frac{1}{4} \cdot \frac{1}{7}[\sin(7x)]_0^\pi = \frac{1}{28}[\sin(7\pi) - \sin(0)] = \frac{1}{28} \cdot 0 = 0$

$\frac{1}{4}\int_0^\pi\cos(3x)dx = \frac{1}{4} \cdot \frac{1}{3}[\sin(3x)]_0^\pi = \frac{1}{12}[\sin(3\pi) - \sin(0)] = \frac{1}{12} \cdot 0 = 0$

Each term evaluates to zero because $\sin(n\pi) = 0$ for any integer $n$.

## Step 3: Final result

Therefore:
$\int_0^\pi\cos(x)\cos(3x)\cos(5x)dx = 0 + 0 + 0 + 0 = 0$

## Step 4: Numerical approximation

The numerical approximation (rounded to 10 decimal places) is:
$0.0000000000$

{"answer": "0", "numerical_answer": "0.0000000000"}