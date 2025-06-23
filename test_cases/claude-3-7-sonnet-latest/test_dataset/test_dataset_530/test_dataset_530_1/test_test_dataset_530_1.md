# Calculating the definite integral $\int_0^1\left(\frac{x^2}{2-x^2}+\sqrt{\frac{2x}{x+1}}\right)\:dx$

I'll split this into two parts:
$$I = \int_0^1\frac{x^2}{2-x^2}dx + \int_0^1\sqrt{\frac{2x}{x+1}}dx$$

## Part 1: $\int_0^1\frac{x^2}{2-x^2}dx$

First, I'll rewrite this:
$$\frac{x^2}{2-x^2} = \frac{x^2}{2-x^2} = \frac{2-(2-x^2)}{2-x^2} = \frac{2}{2-x^2} - 1$$

So:
$$\int_0^1\frac{x^2}{2-x^2}dx = \int_0^1\frac{2}{2-x^2}dx - \int_0^1 1 \,dx$$

For the first integral, let $u = 2-x^2$, then $du = -2x\,dx$, so $dx = -\frac{du}{2x}$:

$$\int_0^1\frac{2}{2-x^2}dx = \int_0^1\frac{2}{u}\left(-\frac{du}{2x}\right) = -\int_0^1\frac{1}{x}\frac{du}{u}$$

When $x=0$, $u=2$
When $x=1$, $u=1$

This substitution approach is problematic at $x=0$. Let me try a different method.

For $\int_0^1\frac{x^2}{2-x^2}dx$, I'll use partial fractions:

$$\frac{x^2}{2-x^2} = \frac{x^2}{2-x^2} = -1 + \frac{2}{2-x^2}$$

So:
$$\int_0^1\frac{x^2}{2-x^2}dx = -\int_0^1 dx + \int_0^1\frac{2}{2-x^2}dx = -1 + \int_0^1\frac{2}{2-x^2}dx$$

For $\int_0^1\frac{2}{2-x^2}dx$, I'll use the substitution $x = \sqrt{2}\sin\theta$:
- When $x=0$, $\theta=0$
- When $x=1$, $\theta=\arcsin\frac{1}{\sqrt{2}}$
- $dx = \sqrt{2}\cos\theta\,d\theta$

$$\int_0^1\frac{2}{2-x^2}dx = \int_0^{\arcsin\frac{1}{\sqrt{2}}}\frac{2}{2-2\sin^2\theta}\sqrt{2}\cos\theta\,d\theta$$
$$= \int_0^{\arcsin\frac{1}{\sqrt{2}}}\frac{2\sqrt{2}\cos\theta}{2\cos^2\theta}\,d\theta = \int_0^{\arcsin\frac{1}{\sqrt{2}}}\frac{\sqrt{2}}{\cos\theta}\,d\theta$$
$$= \sqrt{2}\int_0^{\arcsin\frac{1}{\sqrt{2}}}\sec\theta\,d\theta = \sqrt{2}[\ln|\sec\theta + \tan\theta|]_0^{\arcsin\frac{1}{\sqrt{2}}}$$

When $\theta=0$, $\sec\theta + \tan\theta = 1 + 0 = 1$
When $\theta=\arcsin\frac{1}{\sqrt{2}}$, $\sin\theta = \frac{1}{\sqrt{2}}$, $\cos\theta = \frac{1}{\sqrt{2}}$
So $\sec\theta = \sqrt{2}$ and $\tan\theta = 1$

$$= \sqrt{2}[\ln(\sqrt{2} + 1) - \ln(1)] = \sqrt{2}\ln(\sqrt{2} + 1)$$

Therefore:
$$\int_0^1\frac{x^2}{2-x^2}dx = -1 + \sqrt{2}\ln(\sqrt{2} + 1)$$

## Part 2: $\int_0^1\sqrt{\frac{2x}{x+1}}dx$

Let's use the substitution $u = x+1$, so $x = u-1$ and $dx = du$:
- When $x=0$, $u=1$
- When $x=1$, $u=2$

$$\int_0^1\sqrt{\frac{2x}{x+1}}dx = \int_1^2\sqrt{\frac{2(u-1)}{u}}du = \int_1^2\sqrt{\frac{2u-2}{u}}du = \sqrt{2}\int_1^2\sqrt{\frac{u-1}{u}}du$$

Now let's use $t^2 = \frac{u-1}{u}$, which gives $u = \frac{1}{1-t^2}$ for $t \in [0,\frac{1}{\sqrt{2}}]$:
- When $u=1$, $t=0$
- When $u=2$, $t=\frac{1}{\sqrt{2}}$

With this substitution:
$$\frac{du}{dt} = \frac{2t}{(1-t^2)^2}$$

So:
$$\sqrt{2}\int_1^2\sqrt{\frac{u-1}{u}}du = \sqrt{2}\int_0^{1/\sqrt{2}} t \cdot \frac{2t}{(1-t^2)^2}dt = 2\sqrt{2}\int_0^{1/\sqrt{2}} \frac{t^2}{(1-t^2)^2}dt$$

Let's try a different approach. Starting with $\int_0^1\sqrt{\frac{2x}{x+1}}dx$:

Let $t^2 = \frac{2x}{x+1}$, then $x = \frac{t^2}{2-t^2}$ for $t \in [0, \sqrt{\frac{2}{3}}]$:
- When $x=0$, $t=0$
- When $x=1$, $t=1$

This gives $dx = \frac{4t}{(2-t^2)^2}dt$

$$\int_0^1\sqrt{\frac{2x}{x+1}}dx = \int_0^1 t \cdot \frac{4t}{(2-t^2)^2}dt = 4\int_0^1 \frac{t^2}{(2-t^2)^2}dt$$

Let $v = 2-t^2$, then $dv = -2t\,dt$ and $t^2 = 2-v$:
- When $t=0$, $v=2$
- When $t=1$, $v=1$

$$4\int_0^1 \frac{t^2}{(2-t^2)^2}dt = 4\int_2^1 \frac{2-v}{v^2} \cdot \frac{-dv}{2t} = -2\int_2^1 \frac{2-v}{v^2 \cdot t}dv$$

Since $t = \sqrt{2-v}$:

$$-2\int_2^1 \frac{2-v}{v^2 \cdot \sqrt{2-v}}dv = 2\int_1^2 \frac{2-v}{v^2 \cdot \sqrt{2-v}}dv$$

Let's separate this:
$$2\int_1^2 \frac{2-v}{v^2 \cdot \sqrt{2-v}}dv = 2\int_1^2 \frac{2}{v^2 \cdot \sqrt{2-v}}dv - 2\int_1^2 \frac{v}{v^2 \cdot \sqrt{2-v}}dv$$
$$= 4\int_1^2 \frac{1}{v^2 \cdot \sqrt{2-v}}dv - 2\int_1^2 \frac{1}{v \cdot \sqrt{2-v}}dv$$

For the second integral, we use $w = 2-v$ to get:
$$-2\int_1^2 \frac{1}{v \cdot \sqrt{2-v}}dv = -2\int_1^0 \frac{1}{(2-w) \cdot \sqrt{w}}(-dw) = 2\int_0^1 \frac{1}{(2-w) \cdot \sqrt{w}}dw$$

This is a standard form that evaluates to:
$$2[2\arctan\sqrt{w}]_0^1 = 2[2\arctan(1) - 2\arctan(0)] = 2[2 \cdot \frac{\pi}{4} - 0] = 2 \cdot \frac{\pi}{2} = \pi$$

For the first part, let's use a different approach:
$$4\int_1^2 \frac{1}{v^2 \cdot \sqrt{2-v}}dv$$

Let $s = \sqrt{2-v}$, then $v = 2-s^2$ and $dv = -2s\,ds$:
- When $v=1$, $s=1$
- When $v=2$, $s=0$

$$4\int_1^2 \frac{1}{v^2 \cdot \sqrt{2-v}}dv = 4\int_1^0 \frac{1}{(2-s^2)^2 \cdot s}(-2s\,ds) = -8\int_1^0 \frac{1}{(2-s^2)^2}ds$$
$$= 8\int_0^1 \frac{1}{(2-s^2)^2}ds$$

Let's use partial fractions:
$$\frac{1}{(2-s^2)^2} = \frac{1}{(2-s^2)^2} = \frac{1}{4}\frac{1}{(1-\frac{s^2}{2})^2}$$

With $u = \frac{s^2}{2}$, we get $du = s\,ds$ and $s\,ds = du$:
- When $s=0$, $u=0$
- When $s=1$, $u=\frac{1}{2}$

$$8\int_0^1 \frac{1}{(2-s^2)^2}ds = 8 \cdot \frac{1}{4}\int_0^1 \frac{1}{(1-\frac{s^2}{2})^2}ds = 2\int_0^1 \frac{1}{(1-\frac{s^2}{2})^2}ds$$

$$= 2\int_0^{1/2} \frac{1}{(1-u)^2} \cdot \frac{du}{s} = 2\int_0^{1/2} \frac{1}{(1-u)^2} \cdot \frac{du}{\sqrt{2u}}$$

This integral is challenging in this form. Let me revisit the original approach.

After