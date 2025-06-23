# Evaluation of $\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx$

## Step 1: Substitution
Let's use the substitution $u = \sqrt{x}$, which gives:
- $x = u^2$
- $dx = 2u\,du$
- When $x = 0$, $u = 0$
- When $x = 441$, $u = 21$

Substituting these values:

$$\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx = \int_0^{21}\frac{\pi\sin(\pi u)}{u} \cdot 2u\,du = 2\pi\int_0^{21}\sin(\pi u)\,du$$

## Step 2: Evaluate the resulting integral
For the integral $\int\sin(\pi u)\,du$, we know that:
$$\int\sin(\pi u)\,du = -\frac{1}{\pi}\cos(\pi u) + C$$

Applying the limits:
$$2\pi\int_0^{21}\sin(\pi u)\,du = 2\pi\left[-\frac{1}{\pi}\cos(\pi u)\right]_0^{21} = -2\cos(\pi u)\Big|_0^{21}$$

## Step 3: Evaluate at the limits
$$-2\cos(\pi u)\Big|_0^{21} = -2\cos(21\pi) - (-2\cos(0))$$

We know that:
- $\cos(0) = 1$
- $\cos(21\pi) = \cos(\pi) = -1$ (since $\cos$ has period $2\pi$ and $21\pi = 20\pi + \pi$)

Therefore:
$$-2\cos(21\pi) - (-2\cos(0)) = -2(-1) - (-2)(1) = 2 + 2 = 4$$

## Step 4: Final result
The exact value of the integral is:
$$\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx = 4$$

The numerical approximation, rounded to 10 decimal places, is $4.0000000000$.

{"answer": "4", "numerical_answer": "4.0000000000"}