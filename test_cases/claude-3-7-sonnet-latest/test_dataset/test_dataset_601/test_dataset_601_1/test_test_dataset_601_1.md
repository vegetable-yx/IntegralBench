# Evaluating $\int_{\frac{1}{4}}^{4}\frac{\tan^{-1}(x)}{x}\,\mathrm{d}x$

## Step 1: Substitution

Let's make a substitution to take advantage of the symmetry. Consider $u = \frac{1}{x}$. Then:
- $x = \frac{1}{u}$
- $dx = -\frac{1}{u^2}\,du$

When $x = \frac{1}{4}$, $u = 4$
When $x = 4$, $u = \frac{1}{4}$

The integral becomes:
$$\int_{\frac{1}{4}}^{4}\frac{\tan^{-1}(x)}{x}\,\mathrm{d}x = \int_{4}^{\frac{1}{4}}\frac{\tan^{-1}\left(\frac{1}{u}\right)}{\frac{1}{u}}\left(-\frac{1}{u^2}\right)\,\mathrm{d}u = -\int_{4}^{\frac{1}{4}}\tan^{-1}\left(\frac{1}{u}\right)\,\mathrm{d}u$$

## Step 2: Use the Identity $\tan^{-1}\left(\frac{1}{u}\right) = \frac{\pi}{2} - \tan^{-1}(u)$ for $u > 0$

$$-\int_{4}^{\frac{1}{4}}\tan^{-1}\left(\frac{1}{u}\right)\,\mathrm{d}u = -\int_{4}^{\frac{1}{4}}\left(\frac{\pi}{2} - \tan^{-1}(u)\right)\,\mathrm{d}u$$

$$= -\left[\frac{\pi}{2}u - \int \tan^{-1}(u)\,\mathrm{d}u\right]_{4}^{\frac{1}{4}}$$

## Step 3: Find $\int \tan^{-1}(u)\,\mathrm{d}u$ using integration by parts

Let $f(u) = \tan^{-1}(u)$ and $g'(u) = 1$, then $f'(u) = \frac{1}{1+u^2}$ and $g(u) = u$

$$\int \tan^{-1}(u)\,\mathrm{d}u = u\tan^{-1}(u) - \int \frac{u}{1+u^2}\,\mathrm{d}u$$

$$= u\tan^{-1}(u) - \frac{1}{2}\int \frac{2u}{1+u^2}\,\mathrm{d}u$$

$$= u\tan^{-1}(u) - \frac{1}{2}\ln(1+u^2) + C$$

## Step 4: Substitute back into our integral

$$-\left[\frac{\pi}{2}u - u\tan^{-1}(u) + \frac{1}{2}\ln(1+u^2)\right]_{4}^{\frac{1}{4}}$$

We need to reverse the limits since we negated the integral:
$$\left[\frac{\pi}{2}u - u\tan^{-1}(u) + \frac{1}{2}\ln(1+u^2)\right]_{4}^{\frac{1}{4}}$$

## Step 5: Evaluate the definite integral

At $u = \frac{1}{4}$:
$$\frac{\pi}{8} - \frac{1}{4}\tan^{-1}\left(\frac{1}{4}\right) + \frac{1}{2}\ln\left(1+\frac{1}{16}\right)$$

At $u = 4$:
$$2\pi - 4\tan^{-1}(4) + \frac{1}{2}\ln(17)$$

The result is:
$$\left[\frac{\pi}{8} - \frac{1}{4}\tan^{-1}\left(\frac{1}{4}\right) + \frac{1}{2}\ln\left(\frac{17}{16}\right)\right] - \left[2\pi - 4\tan^{-1}(4) + \frac{1}{2}\ln(17)\right]$$

## Step 6: Simplification

Note that $\tan^{-1}(4) + \tan^{-1}\left(\frac{1}{4}\right) = \frac{\pi}{2}$ for positive values.

Therefore:
$$\frac{\pi}{8} - \frac{1}{4}\left(\frac{\pi}{2} - \tan^{-1}(4)\right) + \frac{1}{2}\ln\left(\frac{17}{16}\right) - 2\pi + 4\tan^{-1}(4) - \frac{1}{2}\ln(17)$$

$$= \frac{\pi}{8} - \frac{\pi}{8} + \frac{1}{4}\tan^{-1}(4) + \frac{1}{2}\ln\left(\frac{17}{16}\right) - 2\pi + 4\tan^{-1}(4) - \frac{1}{2}\ln(17)$$

$$= -2\pi + \frac{17}{4}\tan^{-1}(4) + \frac{1}{2}\ln\left(\frac{17}{16}\right) - \frac{1}{2}\ln(17)$$

$$= -2\pi + \frac{17}{4}\tan^{-1}(4) + \frac{1}{2}\ln\left(\frac{17}{16 \cdot 17}\right)$$

$$= -2\pi + \frac{17}{4}\tan^{-1}(4) + \frac{1}{2}\ln\left(\frac{1}{16}\right)$$

$$= -2\pi + \frac{17}{4}\tan^{-1}(4) - 2\ln(2)$$

Since $\tan^{-1}(4) = \arctan(4) \approx 1.3258177$, we can compute the numerical value.

## Step 7: Numerical Approximation

The exact answer is $-2\pi + \frac{17}{4}\tan^{-1}(4) - 2\ln(2)$

Calculating the numerical approximation to 10 decimal places:
$-2\pi + \frac{17}{4} \cdot 1.3258177 - 2\ln(2) \approx -0.1485429486$

{"answer": "-2\\pi + \\frac{17}{4}\\tan^{-1}(4) - 2\\ln(2)", "numerical_answer": "-0.1485429486"}