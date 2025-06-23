# Evaluating $\int_{1/\sqrt{2}}^1\frac{\arcsin(x)}{x^3}\:dx$

## Step 1: Integration by parts

Let's use integration by parts with:
- $u = \arcsin(x)$
- $dv = \frac{1}{x^3}dx$

This gives:
- $du = \frac{1}{\sqrt{1-x^2}}dx$
- $v = -\frac{1}{2x^2}$

Applying the integration by parts formula $\int u\,dv = uv - \int v\,du$:

$$\int\frac{\arcsin(x)}{x^3}\:dx = -\frac{\arcsin(x)}{2x^2} - \int -\frac{1}{2x^2} \cdot \frac{1}{\sqrt{1-x^2}}dx$$

$$= -\frac{\arcsin(x)}{2x^2} + \frac{1}{2}\int \frac{1}{x^2\sqrt{1-x^2}}dx$$

## Step 2: Evaluate the remaining integral

For the integral $\int \frac{1}{x^2\sqrt{1-x^2}}dx$, I'll make the substitution $x = \sin(t)$.

When $x = \sin(t)$:
- $dx = \cos(t)dt$
- $\sqrt{1-x^2} = \cos(t)$
- $t = \arcsin(x)$

The integral becomes:
$$\int \frac{1}{x^2\sqrt{1-x^2}}dx = \int \frac{1}{\sin^2(t)\cos(t)} \cdot \cos(t)dt = \int \frac{1}{\sin^2(t)}dt = \int \csc^2(t)dt = -\cot(t) + C$$

Substituting back:
$$\int \frac{1}{x^2\sqrt{1-x^2}}dx = -\cot(\arcsin(x)) + C = -\frac{\sqrt{1-x^2}}{x} + C$$

## Step 3: Combine results

Going back to our original integration:
$$\int\frac{\arcsin(x)}{x^3}\:dx = -\frac{\arcsin(x)}{2x^2} + \frac{1}{2}\left(-\frac{\sqrt{1-x^2}}{x}\right) + C$$

$$= -\frac{\arcsin(x)}{2x^2} - \frac{\sqrt{1-x^2}}{2x} + C$$

## Step 4: Evaluate the definite integral

Now I'll evaluate the definite integral from $\frac{1}{\sqrt{2}}$ to $1$:

$$\int_{1/\sqrt{2}}^1\frac{\arcsin(x)}{x^3}\:dx = \left[-\frac{\arcsin(x)}{2x^2} - \frac{\sqrt{1-x^2}}{2x}\right]_{1/\sqrt{2}}^1$$

For the upper limit $x = 1$:
- $\arcsin(1) = \frac{\pi}{2}$
- $\sqrt{1-1^2} = 0$

So:
$$\left[-\frac{\arcsin(1)}{2(1)^2} - \frac{\sqrt{1-1^2}}{2(1)}\right] = -\frac{\pi}{4} - 0 = -\frac{\pi}{4}$$

For the lower limit $x = \frac{1}{\sqrt{2}}$:
- $\arcsin\left(\frac{1}{\sqrt{2}}\right) = \frac{\pi}{4}$
- $\sqrt{1-\left(\frac{1}{\sqrt{2}}\right)^2} = \sqrt{1-\frac{1}{2}} = \sqrt{\frac{1}{2}} = \frac{1}{\sqrt{2}}$

So:
$$\left[-\frac{\arcsin\left(\frac{1}{\sqrt{2}}\right)}{2\left(\frac{1}{\sqrt{2}}\right)^2} - \frac{\sqrt{1-\left(\frac{1}{\sqrt{2}}\right)^2}}{2\left(\frac{1}{\sqrt{2}}\right)}\right] = -\frac{\frac{\pi}{4}}{2 \cdot \frac{1}{2}} - \frac{\frac{1}{\sqrt{2}}}{2 \cdot \frac{1}{\sqrt{2}}} = -\frac{\pi}{4} - \frac{1}{2}$$

Therefore:
$$\int_{1/\sqrt{2}}^1\frac{\arcsin(x)}{x^3}\:dx = \left(-\frac{\pi}{4}\right) - \left(-\frac{\pi}{4} - \frac{1}{2}\right) = \frac{1}{2}$$

## Step 5: Numerical approximation

The exact value is $\frac{1}{2} = 0.5$, which rounded to 10 decimal places is $0.5000000000$.

{"answer": "\\frac{1}{2}", "numerical_answer": "0.5000000000"}