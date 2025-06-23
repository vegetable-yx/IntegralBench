# Evaluating $\int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx$

## Step 1: Analyze the integrand
The integrand is $\frac{\cos(x)}{2-\cos^2(x)}$. I'll use the substitution $u = \cos(x)$ to simplify this.

When $x = 0$, $u = \cos(0) = 1$
When $x = \pi/2$, $u = \cos(\pi/2) = 0$

For the substitution:
$u = \cos(x)$
$du = -\sin(x)dx$
$dx = -\frac{du}{\sin(x)}$

Since $\sin^2(x) + \cos^2(x) = 1$, we have $\sin(x) = \sqrt{1-\cos^2(x)} = \sqrt{1-u^2}$

Therefore:
$dx = -\frac{du}{\sqrt{1-u^2}}$

## Step 2: Rewrite the integral with the substitution
$\int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx = \int_1^0\frac{u}{2-u^2}\left(-\frac{du}{\sqrt{1-u^2}}\right) = \int_0^1\frac{u}{2-u^2}\cdot\frac{du}{\sqrt{1-u^2}}$

## Step 3: Simplify the integrand further
$\frac{u}{2-u^2}\cdot\frac{1}{\sqrt{1-u^2}} = \frac{u}{(2-u^2)\sqrt{1-u^2}}$

Let's factor the denominator $2-u^2$ as $2-(1-(1-u^2)) = 1+(1-u^2)$

This gives us:
$\frac{u}{(1+(1-u^2))\sqrt{1-u^2}} = \frac{u}{(1+v)\sqrt{v}}$ where $v = 1-u^2$

## Step 4: Make another substitution
Let $v = 1-u^2$
When $u = 0$, $v = 1$
When $u = 1$, $v = 0$
$dv = -2u\,du$
$du = -\frac{dv}{2u}$

Also, $u = \sqrt{1-v}$

Therefore:
$\int_0^1\frac{u}{(1+(1-u^2))\sqrt{1-u^2}}du = \int_1^0\frac{\sqrt{1-v}}{(1+v)\sqrt{v}}\left(-\frac{dv}{2\sqrt{1-v}}\right) = \frac{1}{2}\int_0^1\frac{dv}{(1+v)\sqrt{v}}$

## Step 5: Evaluate the resulting integral
We need to compute $\frac{1}{2}\int_0^1\frac{dv}{(1+v)\sqrt{v}}$

Let $w = \sqrt{v}$, so $v = w^2$ and $dv = 2w\,dw$
When $v = 0$, $w = 0$
When $v = 1$, $w = 1$

This gives us:
$\frac{1}{2}\int_0^1\frac{dv}{(1+v)\sqrt{v}} = \frac{1}{2}\int_0^1\frac{2w\,dw}{(1+w^2)w} = \int_0^1\frac{dw}{1+w^2}$

This is now in the form of $\int\frac{dx}{1+x^2} = \arctan(x) + C$

So we have:
$\int_0^1\frac{dw}{1+w^2} = [\arctan(w)]_0^1 = \arctan(1) - \arctan(0) = \frac{\pi}{4} - 0 = \frac{\pi}{4}$

## Step 6: Numerical approximation
$\frac{\pi}{4} \approx 0.7853981634$ (rounded to 10 decimal places)

Therefore, the definite integral $\int_0^{\pi/2}\frac{\cos(x)}{2-\cos^2(x)}dx = \frac{\pi}{4}$.

{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}