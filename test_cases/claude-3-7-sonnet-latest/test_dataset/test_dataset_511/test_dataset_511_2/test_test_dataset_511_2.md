# Evaluating $\int_0^8\frac{\cos\sqrt{x}}{\sqrt{x}}dx$

## Step 1: Substitution
Let's use the substitution $u = \sqrt{x}$, which gives:
- $u = \sqrt{x}$
- $x = u^2$
- $dx = 2u \, du$
- When $x = 0$, $u = 0$
- When $x = 8$, $u = 2\sqrt{2}$

Substituting into the integral:
$$\int_0^8\frac{\cos\sqrt{x}}{\sqrt{x}}dx = \int_0^{2\sqrt{2}}\frac{\cos(u)}{u} \cdot 2u \, du = 2\int_0^{2\sqrt{2}}\cos(u) \, du$$

## Step 2: Evaluate the new integral
$$2\int_0^{2\sqrt{2}}\cos(u) \, du = 2[\sin(u)]_0^{2\sqrt{2}} = 2[\sin(2\sqrt{2}) - \sin(0)] = 2\sin(2\sqrt{2})$$

## Step 3: Simplify the result
The exact answer is $2\sin(2\sqrt{2})$.

## Step 4: Numerical approximation
To compute the numerical value:
$2\sin(2\sqrt{2}) \approx 2 \cdot \sin(2.8284271247) \approx 2 \cdot 0.3246994692 \approx 0.6493989384$

Rounding to 10 decimal places: $0.6493989384$

{"answer": "2\\sin(2\\sqrt{2})", "numerical_answer": "0.6493989384"}