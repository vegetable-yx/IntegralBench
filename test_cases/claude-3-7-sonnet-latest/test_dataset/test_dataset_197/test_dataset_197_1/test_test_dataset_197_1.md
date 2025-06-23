# Evaluating $\int_0^1 x\arcsin x\arccos x\,dx$

First, I'll note that $\arcsin x + \arccos x = \frac{\pi}{2}$ for $x \in [0,1]$. This gives:

$\arcsin x \cdot \arccos x = \arcsin x \cdot (\frac{\pi}{2} - \arcsin x) = \frac{\pi}{2}\arcsin x - (\arcsin x)^2$

So our integral becomes:
$$\int_0^1 x\arcsin x\arccos x\,dx = \int_0^1 x\arcsin x \cdot (\frac{\pi}{2} - \arcsin x)\,dx = \frac{\pi}{2}\int_0^1 x\arcsin x\,dx - \int_0^1 x(\arcsin x)^2\,dx$$

Let's solve each part separately:

## Part 1: $\frac{\pi}{2}\int_0^1 x\arcsin x\,dx$

I'll use integration by parts with:
- $u = \arcsin x$, $du = \frac{1}{\sqrt{1-x^2}}dx$
- $dv = x\,dx$, $v = \frac{x^2}{2}$

$$\int x\arcsin x\,dx = \frac{x^2}{2}\arcsin x - \int \frac{x^2}{2} \cdot \frac{1}{\sqrt{1-x^2}}\,dx$$

For the remaining integral, I'll substitute $x = \sin t$, giving $dx = \cos t\,dt$:
$$\int \frac{x^2}{2\sqrt{1-x^2}}\,dx = \frac{1}{2}\int \frac{\sin^2 t}{\sqrt{1-\sin^2 t}} \cos t\,dt = \frac{1}{2}\int \sin^2 t\,dt$$

Using $\sin^2 t = \frac{1-\cos 2t}{2}$:
$$\frac{1}{2}\int \sin^2 t\,dt = \frac{1}{4}\int (1-\cos 2t)\,dt = \frac{t}{4} - \frac{\sin 2t}{8} + C$$

Substituting back $t = \arcsin x$, we get:
$$\frac{\arcsin x}{4} - \frac{\sin(2\arcsin x)}{8} + C$$

Since $\sin(2\arcsin x) = 2\sin(\arcsin x)\cos(\arcsin x) = 2x\sqrt{1-x^2}$, we have:
$$\int \frac{x^2}{2\sqrt{1-x^2}}\,dx = \frac{\arcsin x}{4} - \frac{x\sqrt{1-x^2}}{4} + C$$

Therefore:
$$\int x\arcsin x\,dx = \frac{x^2}{2}\arcsin x - \frac{\arcsin x}{4} + \frac{x\sqrt{1-x^2}}{4} + C$$

Evaluating at bounds:
$$\left[\frac{x^2}{2}\arcsin x - \frac{\arcsin x}{4} + \frac{x\sqrt{1-x^2}}{4}\right]_0^1 = \frac{\pi}{4} - 0 = \frac{\pi}{4}$$

So $\frac{\pi}{2}\int_0^1 x\arcsin x\,dx = \frac{\pi}{2} \cdot \frac{\pi}{4} = \frac{\pi^2}{8}$

## Part 2: $\int_0^1 x(\arcsin x)^2\,dx$

Using integration by parts with:
- $u = (\arcsin x)^2$, $du = \frac{2\arcsin x}{\sqrt{1-x^2}}dx$
- $dv = x\,dx$, $v = \frac{x^2}{2}$

$$\int x(\arcsin x)^2\,dx = \frac{x^2}{2}(\arcsin x)^2 - \int \frac{x^2}{2} \cdot \frac{2\arcsin x}{\sqrt{1-x^2}}\,dx$$
$$= \frac{x^2}{2}(\arcsin x)^2 - \int \frac{x^2 \arcsin x}{\sqrt{1-x^2}}\,dx$$

For this integral, I'll use substitution $x = \sin t$, giving $dx = \cos t\,dt$ and $\arcsin x = t$:
$$\int \frac{x^2 \arcsin x}{\sqrt{1-x^2}}\,dx = \int \sin^2 t \cdot t \cdot dt$$

Using $\sin^2 t = \frac{1-\cos 2t}{2}$:
$$\int \sin^2 t \cdot t \cdot dt = \frac{1}{2}\int t\,dt - \frac{1}{2}\int t\cos 2t\,dt$$

The first part is $\frac{t^2}{4}$. For the second part, I'll use integration by parts:
- $u = t$, $du = dt$
- $dv = \cos 2t\,dt$, $v = \frac{\sin 2t}{2}$

$$\int t\cos 2t\,dt = \frac{t\sin 2t}{2} - \int \frac{\sin 2t}{2}\,dt = \frac{t\sin 2t}{2} + \frac{\cos 2t}{4} + C$$

Thus:
$$\int \sin^2 t \cdot t \cdot dt = \frac{t^2}{4} - \frac{t\sin 2t}{4} - \frac{\cos 2t}{8} + C$$

Substituting back $t = \arcsin x$:
$$\int \frac{x^2 \arcsin x}{\sqrt{1-x^2}}\,dx = \frac{(\arcsin x)^2}{4} - \frac{\arcsin x \cdot \sin(2\arcsin x)}{4} - \frac{\cos(2\arcsin x)}{8} + C$$

Using $\sin(2\arcsin x) = 2x\sqrt{1-x^2}$ and $\cos(2\arcsin x) = 1-2x^2$:
$$\int \frac{x^2 \arcsin x}{\sqrt{1-x^2}}\,dx = \frac{(\arcsin x)^2}{4} - \frac{\arcsin x \cdot 2x\sqrt{1-x^2}}{4} - \frac{1-2x^2}{8} + C$$
$$= \frac{(\arcsin x)^2}{4} - \frac{\arcsin x \cdot x\sqrt{1-x^2}}{2} - \frac{1}{8} + \frac{x^2}{4} + C$$

Therefore:
$$\int x(\arcsin x)^2\,dx = \frac{x^2(\arcsin x)^2}{2} - \left[\frac{(\arcsin x)^2}{4} - \frac{\arcsin x \cdot x\sqrt{1-x^2}}{2} - \frac{1}{8} + \frac{x^2}{4}\right] + C$$
$$= \frac{x^2(\arcsin x)^2}{2} - \frac{(\arcsin x)^2}{4} + \frac{\arcsin x \cdot x\sqrt{1-x^2}}{2} + \frac{1}{8} - \frac{x^2}{4} + C$$

Evaluating at bounds:
$$\left[\frac{x^2(\arcsin x)^2}{2} - \frac{(\arcsin x)^2}{4} + \frac{\arcsin x \cdot x\sqrt{1-x^2}}{2} + \frac{1}{8} - \frac{x^2}{4}\right]_0^1$$

At $x=1$: $\frac{\pi^2}{8} - \frac{\pi^2}{16} + 0 + \frac{1}{8} - \frac{1}{4} = \frac{\pi^2}{16} - \frac{1}{8}$
At $x=0$: $0 - 0 + 0 + \frac{1}{8} - 0 = \frac{1}{8}$

So $\int_0^1 x(\arcsin x)^2\,dx = \frac{\pi^2}{16} - \frac{1}{8} - \frac{1}{8} = \frac{\pi^2}{16} - \frac{1}{4}$

## Combining the parts

The original integral equals:
$$\frac{\pi}{2}\int_0^1 x\arcsin x\,dx - \int_0^1 x(\arcsin x)^2\,dx = \frac{\pi^2}{8} - \left(\frac{\pi^2}{16} - \frac{1}{4}\right) = \frac{\pi^2}{8} - \frac{\pi^2}{16} + \frac{1}{4} = \frac{\pi^2}{16} + \frac{1}{4}$$

## Numerical approximation
$\frac{\pi^2}{16} + \frac{1}{4} ≈ 0.6177323193 + 0.25 = 0.8677323193$

{"answer": "\\frac{\\pi^2}{16} + \\frac{1}{4}", "numerical_answer": "0.8677323193"}