# Evaluating $\int_{-\infty}^\infty e^{-(x-2024)^2/4}\:dx$

## Step 1: Recognize the form of the integral
The given integral is of the form $\int_{-\infty}^\infty e^{-(x-\mu)^2/(2\sigma^2)}\:dx$ where $\mu = 2024$ and $2\sigma^2 = 4$, so $\sigma^2 = 2$ and $\sigma = \sqrt{2}$.

This is related to the standard Gaussian integral formula:
$$\int_{-\infty}^\infty e^{-x^2/(2\sigma^2)}\:dx = \sigma\sqrt{2\pi}$$

## Step 2: Apply substitution
Let's make a substitution to put our integral in the standard form:
Let $u = x - 2024$, then $dx = du$ and the limits remain the same.

So our integral becomes:
$$\int_{-\infty}^\infty e^{-u^2/4}\:du$$

## Step 3: Compare with standard form
We can rewrite this as:
$$\int_{-\infty}^\infty e^{-u^2/(2(2))}\:du$$

Comparing with the standard formula where $\sigma^2 = 2$, we get:
$$\int_{-\infty}^\infty e^{-u^2/(2(2))}\:du = \sigma\sqrt{2\pi} = \sqrt{2}\sqrt{2\pi} = 2\sqrt{\pi}$$

## Step 4: Final answer
Therefore:
$$\int_{-\infty}^\infty e^{-(x-2024)^2/4}\:dx = 2\sqrt{\pi}$$

## Numerical approximation
$2\sqrt{\pi} \approx 2 \times 1.7724538509 \approx 3.5449077018$

{"answer": "2\\sqrt{\\pi}", "numerical_answer": "3.5449077018"}