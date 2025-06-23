# Definite Integral Evaluation: $\int_0^\infty\frac{\sin\sqrt{3}x-\sin\frac{x}{\sqrt{3}}}{x}e^{-x^2}dx$

I'll evaluate this definite integral step by step.

## Step 1: Initial Setup
Let's denote our integral as $I$:
$$I = \int_0^\infty\frac{\sin\sqrt{3}x-\sin\frac{x}{\sqrt{3}}}{x}e^{-x^2}dx$$

## Step 2: Using a Known Result
I'll use the following standard result for this type of integral:
$$\int_0^\infty \frac{\sin(ax)}{x}e^{-b^2x^2}dx = \frac{1}{2}\arctan\left(\frac{a}{b^2}\right)$$

This can be applied to both terms in our integral.

## Step 3: Applying the Formula
For the first term with $a=\sqrt{3}$ and $b=1$:
$$\int_0^\infty \frac{\sin(\sqrt{3}x)}{x}e^{-x^2}dx = \frac{1}{2}\arctan\left(\frac{\sqrt{3}}{1}\right) = \frac{1}{2}\arctan(\sqrt{3})$$

For the second term with $a=\frac{1}{\sqrt{3}}$ and $b=1$:
$$\int_0^\infty \frac{\sin\left(\frac{x}{\sqrt{3}}\right)}{x}e^{-x^2}dx = \frac{1}{2}\arctan\left(\frac{1}{\sqrt{3}}\right)$$

## Step 4: Combining the Results
The original integral is the difference of these two terms:
$$I = \frac{1}{2}\arctan(\sqrt{3}) - \frac{1}{2}\arctan\left(\frac{1}{\sqrt{3}}\right)$$

## Step 5: Simplifying Using Arctangent Properties
We can use the property $\arctan(x) + \arctan\left(\frac{1}{x}\right) = \frac{\pi}{2}$ for $x > 0$.

Since $\sqrt{3} > 0$, we have:
$$\arctan(\sqrt{3}) + \arctan\left(\frac{1}{\sqrt{3}}\right) = \frac{\pi}{2}$$

Therefore:
$$\arctan\left(\frac{1}{\sqrt{3}}\right) = \frac{\pi}{2} - \arctan(\sqrt{3})$$

Substituting this into our integral:
$$I = \frac{1}{2}\arctan(\sqrt{3}) - \frac{1}{2}\left(\frac{\pi}{2} - \arctan(\sqrt{3})\right)$$
$$I = \frac{1}{2}\arctan(\sqrt{3}) - \frac{\pi}{4} + \frac{1}{2}\arctan(\sqrt{3})$$
$$I = \arctan(\sqrt{3}) - \frac{\pi}{4}$$

## Step 6: Final Simplification
We know that $\arctan(\sqrt{3}) = \frac{\pi}{3}$ (this is a standard value).

Therefore:
$$I = \frac{\pi}{3} - \frac{\pi}{4} = \frac{4\pi}{12} - \frac{3\pi}{12} = \frac{\pi}{12}$$

## Numerical Approximation
$\frac{\pi}{12} \approx 0.2617993878$ (rounded to 10 decimal places)

{"answer": "\\frac{\\pi}{12}", "numerical_answer": "0.2617993878"}