# Evaluating $\int_0^1 x\arcsin x\arccos x\:dx$

I'll calculate this definite integral step by step.

## Step 1: Simplify the integrand

Let's use the fact that $\arcsin x + \arccos x = \frac{\pi}{2}$ for $x \in [0,1]$.
This means $\arccos x = \frac{\pi}{2} - \arcsin x$.

Substituting this into our integral:
$$\int_0^1 x\arcsin x\arccos x\:dx = \int_0^1 x\arcsin x \left(\frac{\pi}{2} - \arcsin x\right)\:dx$$

Expanding this:
$$\int_0^1 x\arcsin x \cdot \frac{\pi}{2}\:dx - \int_0^1 x(\arcsin x)^2\:dx$$

So we have two integrals to compute:
- $I_1 = \frac{\pi}{2}\int_0^1 x\arcsin x\:dx$
- $I_2 = \int_0^1 x(\arcsin x)^2\:dx$

## Step 2: Calculate $I_1 = \frac{\pi}{2}\int_0^1 x\arcsin x\:dx$

For $\int x\arcsin x\:dx$, I'll use integration by parts with:
- $u = \arcsin x$
- $dv = x\:dx$
- $du = \frac{dx}{\sqrt{1-x^2}}$
- $v = \frac{x^2}{2}$

$$\int x\arcsin x\:dx = \frac{x^2}{2}\arcsin x - \int \frac{x^2}{2} \cdot \frac{1}{\sqrt{1-x^2}}\:dx$$

For the remaining integral, I'll substitute $x = \sin t$, $dx = \cos t\:dt$:
$$\int \frac{x^2}{2\sqrt{1-x^2}}\:dx = \frac{1}{2}\int \frac{\sin^2 t}{\sqrt{1-\sin^2 t}} \cos t\:dt = \frac{1}{2}\int \sin^2 t\:dt$$

Using $\sin^2 t = \frac{1-\cos 2t}{2}$:
$$\frac{1}{2}\int \sin^2 t\:dt = \frac{1}{4}\int (1-\cos 2t)\:dt = \frac{1}{4}\left(t - \frac{\sin 2t}{2}\right) + C$$

Since $x = \sin t$, we have $t = \arcsin x$ and $\sin 2t = 2\sin t\cos t = 2x\sqrt{1-x^2}$

Therefore:
$$\int \frac{x^2}{2\sqrt{1-x^2}}\:dx = \frac{1}{4}\arcsin x - \frac{1}{4}x\sqrt{1-x^2} + C$$

Going back to our original integral:
$$\int x\arcsin x\:dx = \frac{x^2}{2}\arcsin x - \frac{1}{4}\arcsin x + \frac{1}{4}x\sqrt{1-x^2} + C$$
$$= \arcsin x\left(\frac{x^2}{2} - \frac{1}{4}\right) + \frac{1}{4}x\sqrt{1-x^2} + C$$

Evaluating from $0$ to $1$:
$$\left[\arcsin x\left(\frac{x^2}{2} - \frac{1}{4}\right) + \frac{1}{4}x\sqrt{1-x^2}\right]_0^1$$

At $x=1$: $\arcsin(1) = \frac{\pi}{2}$, $\sqrt{1-1^2} = 0$, so we get $\frac{\pi}{2}\left(\frac{1}{2} - \frac{1}{4}\right) + 0 = \frac{\pi}{8}$
At $x=0$: Everything equals $0$

So $I_1 = \frac{\pi}{2} \cdot \frac{\pi}{8} = \frac{\pi^2}{16}$

## Step 3: Calculate $I_2 = \int_0^1 x(\arcsin x)^2\:dx$

For this integral, I'll again use integration by parts with:
- $u = (\arcsin x)^2$
- $dv = x\:dx$
- $du = 2\arcsin x \cdot \frac{1}{\sqrt{1-x^2}}\:dx$
- $v = \frac{x^2}{2}$

$$\int x(\arcsin x)^2\:dx = \frac{x^2}{2}(\arcsin x)^2 - \int \frac{x^2}{2} \cdot 2\arcsin x \cdot \frac{1}{\sqrt{1-x^2}}\:dx$$
$$= \frac{x^2}{2}(\arcsin x)^2 - \int \frac{x^2 \arcsin x}{\sqrt{1-x^2}}\:dx$$

For the new integral, I'll substitute $x = \sin t$, $dx = \cos t\:dt$, and $\arcsin x = t$:
$$\int \frac{x^2 \arcsin x}{\sqrt{1-x^2}}\:dx = \int \frac{\sin^2 t \cdot t}{\sqrt{1-\sin^2 t}} \cos t\:dt = \int \sin^2 t \cdot t \:dt$$

This is a more complex integral. Using integration by parts again with:
- $u = t$
- $dv = \sin^2 t\:dt$
- $du = dt$
- $v = \frac{t}{2} - \frac{\sin 2t}{4} = \frac{t - \sin t \cos t}{2}$

$$\int \sin^2 t \cdot t \:dt = t\left(\frac{t}{2} - \frac{\sin 2t}{4}\right) - \int \left(\frac{t}{2} - \frac{\sin 2t}{4}\right)dt$$
$$= \frac{t^2}{2} - \frac{t\sin 2t}{4} - \left(\frac{t^2}{4} + \frac{\cos 2t}{8}\right) + C$$
$$= \frac{t^2}{4} - \frac{t\sin 2t}{4} - \frac{\cos 2t}{8} + C$$

Converting back to $x$, where $t = \arcsin x$ and $\sin 2t = 2\sin t\cos t = 2x\sqrt{1-x^2}$:
$$\int \frac{x^2 \arcsin x}{\sqrt{1-x^2}}\:dx = \frac{(\arcsin x)^2}{4} - \frac{\arcsin x \cdot 2x\sqrt{1-x^2}}{4} - \frac{\cos(2\arcsin x)}{8} + C$$

Since $\cos(2\arcsin x) = \cos(2t) = 1 - 2\sin^2 t = 1 - 2x^2$:
$$\int \frac{x^2 \arcsin x}{\sqrt{1-x^2}}\:dx = \frac{(\arcsin x)^2}{4} - \frac{\arcsin x \cdot x\sqrt{1-x^2}}{2} - \frac{1 - 2x^2}{8} + C$$
$$= \frac{(\arcsin x)^2}{4} - \frac{\arcsin x \cdot x\sqrt{1-x^2}}{2} - \frac{1}{8} + \frac{x^2}{4} + C$$

Going back to our original integral:
$$\int x(\arcsin x)^2\:dx = \frac{x^2(\arcsin x)^2}{2} - \left(\frac{(\arcsin x)^2}{4} - \frac{\arcsin x \cdot x\sqrt{1-x^2}}{2} - \frac{1}{8} + \frac{x^2}{4}\right) + C$$

Simplifying:
$$\int x(\arcsin x)^2\:dx = \frac{x^2(\arcsin x)^2}{2} - \frac{(\arcsin x)^2}{4} + \frac{\arcsin x \cdot x\sqrt{1-x^2}}{2} + \frac{1}{8} - \frac{x^2}{4} + C$$

Evaluating from $0$ to $1$:
$$\left[\frac{x^2(\arcsin x)^2}{2} - \frac{(\arcsin x)^2}{4} + \frac{\arcsin x \cdot x\sqrt{1-x^2}}{2} + \frac{1}{8} - \frac{x^2}{4}\right]_0^1$$

At $x=1$: $\arcsin(1) = \frac{\pi}{2}$, $\sqrt{1-1^2} = 0$
$$\frac{1 \cdot (\pi/2)^2}{2} - \frac{(\pi/2)^2}{4} + 0 + \frac{1}{8} - \frac{1}{4} = \frac{\pi^2}{8} - \frac{\pi^2}{16} + \frac{1}{8} - \frac{1}{4} = \frac{\pi^2}{16} - \frac{1}{8}$$

At $x=0$: Only $\frac{1}{8}$ remains

So $I_2 = \frac{\pi^2}{16} - \frac{1}{8} - \frac{1}{8} = \frac{\pi^2}{16} - \frac{1}{4}$

## Step 4: Calculate the original integral

$$\int_0^1 x\arcsin x\arccos x\:dx = I_1 - I_2 = \frac{\pi^2}{16} - \left(\frac{\pi^2}{16} - \frac{1}{4}\right) = \frac{1}{4}$$

Therefore, $\int_0^1 x\arcsin x\arccos x\:dx = \frac{1}{4}$

Numerically, $\frac{1}{4} = 0.2500000000$

{"answer": "\\frac{1}{4}", "numerical_answer": "0.2500000000"}