# Evaluating $\int_0^\infty\frac{\sin\sqrt{3}x-\sin\frac{x}{\sqrt{3}}}{x}e^{-x^2}\text{ dx}$

I'll calculate this definite integral using analytical methods.

## Step 1: Let's separate the integral into two parts

$$I = \int_0^\infty\frac{\sin\sqrt{3}x}{x}e^{-x^2}\text{ dx} - \int_0^\infty\frac{\sin\frac{x}{\sqrt{3}}}{x}e^{-x^2}\text{ dx}$$

Let's call these $I_1$ and $I_2$ respectively.

## Step 2: Use a known result for integrals of this form

For integrals of the form $\int_0^\infty \frac{\sin(ax)}{x}e^{-b^2x^2}dx$, there is a standard result:

$$\int_0^\infty \frac{\sin(ax)}{x}e^{-b^2x^2}dx = \frac{1}{2}\arctan\left(\frac{a}{b^2}\right)$$

## Step 3: Apply the formula to each part

For $I_1$, we have $a = \sqrt{3}$ and $b^2 = 1$:
$$I_1 = \int_0^\infty\frac{\sin\sqrt{3}x}{x}e^{-x^2}\text{ dx} = \frac{1}{2}\arctan\left(\frac{\sqrt{3}}{1}\right) = \frac{1}{2}\arctan(\sqrt{3})$$

For $I_2$, we have $a = \frac{1}{\sqrt{3}}$ and $b^2 = 1$:
$$I_2 = \int_0^\infty\frac{\sin\frac{x}{\sqrt{3}}}{x}e^{-x^2}\text{ dx} = \frac{1}{2}\arctan\left(\frac{1}{\sqrt{3}}\right)$$

## Step 4: Combine the results

$$I = I_1 - I_2 = \frac{1}{2}\arctan(\sqrt{3}) - \frac{1}{2}\arctan\left(\frac{1}{\sqrt{3}}\right)$$

## Step 5: Simplify using properties of arctangent

Note that $\arctan\left(\frac{1}{x}\right) = \frac{\pi}{2} - \arctan(x)$ for $x > 0$

So, $\arctan\left(\frac{1}{\sqrt{3}}\right) = \frac{\pi}{2} - \arctan(\sqrt{3})$

Substituting:
$$I = \frac{1}{2}\arctan(\sqrt{3}) - \frac{1}{2}\left(\frac{\pi}{2} - \arctan(\sqrt{3})\right)$$
$$I = \frac{1}{2}\arctan(\sqrt{3}) - \frac{\pi}{4} + \frac{1}{2}\arctan(\sqrt{3})$$
$$I = \arctan(\sqrt{3}) - \frac{\pi}{4}$$

We know that $\arctan(\sqrt{3}) = \frac{\pi}{3}$, so:
$$I = \frac{\pi}{3} - \frac{\pi}{4} = \frac{4\pi - 3\pi}{12} = \frac{\pi}{12}$$

## Step 6: Numerical approximation

$\frac{\pi}{12} \approx 0.2617993878$ (rounded to 10 decimal places)

{"answer": "\\frac{\\pi}{12}", "numerical_answer": "0.2617993878"}