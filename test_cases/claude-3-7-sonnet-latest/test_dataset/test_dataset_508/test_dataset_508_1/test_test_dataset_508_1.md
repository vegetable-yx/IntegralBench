# Evaluating $\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx$

I'll approach this by using a substitution to simplify the integral.

## Step 1: Substitution
Let $u = \sqrt{x}$, which gives us:
- $x = u^2$
- $dx = 2u \, du$
- When $x = 0$, $u = 0$
- When $x = 441$, $u = 21$

Rewriting the integral:
$$\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx = \int_0^{21}\frac{\pi\sin(\pi u)}{u} \cdot 2u \, du = 2\pi\int_0^{21}\sin(\pi u) \, du$$

## Step 2: Evaluate the simplified integral
$$2\pi\int_0^{21}\sin(\pi u) \, du = 2\pi \left[-\frac{\cos(\pi u)}{\pi}\right]_0^{21}$$
$$= 2\pi \left[-\frac{\cos(21\pi)}{\pi} + \frac{\cos(0)}{\pi}\right]$$
$$= 2\pi \left[-\frac{\cos(21\pi)}{\pi} + \frac{1}{\pi}\right]$$

Since $21 = 10.5 \cdot 2$, we know that $21\pi$ represents $10.5$ complete rotations around the unit circle. Half a rotation from $0$ gives us $\pi$, which means $\cos(21\pi) = \cos(\pi) = -1$.

$$= 2\pi \left[-\frac{-1}{\pi} + \frac{1}{\pi}\right] = 2\pi \left[\frac{1}{\pi} + \frac{1}{\pi}\right] = 2\pi \cdot \frac{2}{\pi} = 4$$

## Step 3: Numerical approximation
The exact answer is 4, so the numerical approximation rounded to 10 decimal places is 4.0000000000.

## Final result
The definite integral $\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx = 4$

{"answer": "4", "numerical_answer": "4.0000000000"}