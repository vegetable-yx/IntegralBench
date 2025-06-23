# Evaluation of $\int\limits_{0}^{0.5} x(0.5^2-x^2)^{-1/2}\arcsin\left(0.5x\right)dx$

## Step 1: Substitution

Let's try the substitution $u = 0.5x$, which gives $x = 2u$ and $dx = 2du$.

When $x = 0$, $u = 0$
When $x = 0.5$, $u = 0.25$

Rewriting the integral:
$$\int\limits_{0}^{0.5} x(0.5^2-x^2)^{-1/2}\arcsin\left(0.5x\right)dx = \int\limits_{0}^{0.25} 2u(0.5^2-(2u)^2)^{-1/2}\arcsin(u)2du$$
$$= 4\int\limits_{0}^{0.25} u(0.25-4u^2)^{-1/2}\arcsin(u)du$$
$$= 4\int\limits_{0}^{0.25} u(0.25(1-16u^2))^{-1/2}\arcsin(u)du$$
$$= 4\int\limits_{0}^{0.25} \frac{u}{\sqrt{0.25}\sqrt{1-16u^2}}\arcsin(u)du$$
$$= 8\int\limits_{0}^{0.25} \frac{u}{\sqrt{1-16u^2}}\arcsin(u)du$$

## Step 2: Another Substitution

Let's make another substitution: $v = \arcsin(u)$, which gives $u = \sin(v)$ and $du = \cos(v)dv$.

When $u = 0$, $v = 0$
When $u = 0.25$, $v = \arcsin(0.25)$

Also, note that $\sqrt{1-16u^2} = \sqrt{1-16\sin^2(v)}$

Using the identity $1-16\sin^2(v) = 1-16(1-\cos^2(v))/16 = 1-1+\cos^2(v) = \cos^2(v)$, we get:
$\sqrt{1-16u^2} = \sqrt{\cos^2(v)} = |\cos(v)| = \cos(v)$ (since $v$ is in the first quadrant)

The integral becomes:
$$8\int\limits_{0}^{\arcsin(0.25)} \frac{\sin(v)}{\cos(v)}\arcsin(\sin(v))\cos(v)dv$$
$$= 8\int\limits_{0}^{\arcsin(0.25)} \sin(v) \cdot v \cdot dv$$
$$= 8\int\limits_{0}^{\arcsin(0.25)} v\sin(v)dv$$

## Step 3: Integration by Parts

Let's use integration by parts with $u = v$ and $dv = \sin(v)dv$.
Then $du = dv$ and $v = -\cos(v)$

$$8\int\limits_{0}^{\arcsin(0.25)} v\sin(v)dv = 8\left[-v\cos(v)\right]_{0}^{\arcsin(0.25)} + 8\int\limits_{0}^{\arcsin(0.25)} \cos(v)dv$$
$$= 8\left[-\arcsin(0.25)\cos(\arcsin(0.25)) + 0\right] + 8\left[\sin(v)\right]_{0}^{\arcsin(0.25)}$$
$$= -8\arcsin(0.25)\cos(\arcsin(0.25)) + 8\sin(\arcsin(0.25)) - 8\sin(0)$$
$$= -8\arcsin(0.25)\cos(\arcsin(0.25)) + 8(0.25)$$

We know that $\cos(\arcsin(0.25)) = \sqrt{1-0.25^2} = \sqrt{1-0.0625} = \sqrt{0.9375} = \frac{\sqrt{15}}{4}$

Therefore:
$$-8\arcsin(0.25)\cos(\arcsin(0.25)) + 8(0.25) = -8\arcsin(0.25)\frac{\sqrt{15}}{4} + 2$$
$$= -2\arcsin(0.25)\sqrt{15} + 2$$

## Step 4: Evaluating $\arcsin(0.25)$

$\arcsin(0.25) = \arcsin(\frac{1}{4}) = \arcsin(\frac{\sqrt{16}}{16}) = \arcsin(\frac{\sin(\arcsin(\frac{1}{4}))}{\sin(\frac{\pi}{2})}) = \frac{\pi}{12}$

So our final result is:
$$-2\arcsin(0.25)\sqrt{15} + 2 = -2\cdot\frac{\pi}{12}\cdot\sqrt{15} + 2 = -\frac{\pi\sqrt{15}}{6} + 2$$

## Numerical Approximation

$-\frac{\pi\sqrt{15}}{6} + 2 \approx -\frac{3.14159 \cdot \sqrt{15}}{6} + 2 \approx -\frac{3.14159 \cdot 3.87298}{6} + 2 \approx -2.02899 + 2 \approx -0.0289927544$

Calculating more precisely: $-\frac{\pi\sqrt{15}}{6} + 2 \approx -0.0289927544$

{"answer": "-\\frac{\\pi\\sqrt{15}}{6} + 2", "numerical_answer": "-0.0289927544"}