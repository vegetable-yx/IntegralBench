# Evaluating $\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx$

## Step 1: Let's use substitution
Let $u = \sqrt{x}$, which means $x = u^2$ and $dx = 2u\,du$.

The limits change:
- When $x = 0$, $u = 0$
- When $x = 441$, $u = 21$

Substituting into the integral:
$$\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx = \int_0^{21}\frac{\pi\sin(\pi u)}{u} \cdot 2u\,du = 2\pi\int_0^{21}\sin(\pi u)\,du$$

## Step 2: Evaluate the simpler integral
$$2\pi\int_0^{21}\sin(\pi u)\,du = 2\pi \left[-\frac{\cos(\pi u)}{\pi}\right]_0^{21}$$
$$= 2\pi \left[-\frac{\cos(21\pi)}{\pi} + \frac{\cos(0)}{\pi}\right]$$
$$= 2\pi \left[-\frac{\cos(21\pi)}{\pi} + \frac{1}{\pi}\right]$$

Since $21\pi$ is an odd multiple of $\pi$ ($21$ is odd), we have $\cos(21\pi) = -1$

$$= 2\pi \left[-\frac{-1}{\pi} + \frac{1}{\pi}\right] = 2\pi \left[\frac{1}{\pi} + \frac{1}{\pi}\right] = 2\pi \cdot \frac{2}{\pi} = 4$$

## Step 3: Numerical approximation
The exact result is 4, so the numerical approximation rounded to 10 decimal places is 4.0000000000.

## Step 4: Final result

{"answer": "4", "numerical_answer": "4.0000000000"}