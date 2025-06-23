# Evaluating $\int_{-\infty}^{\infty} e^{-(x-2024)^2/4}\:dx$

## Step 1: Recognize the form of the integral
The integral has the form of a Gaussian integral with:
- Mean $\mu = 2024$
- Variance $\sigma^2 = 2$ (since the exponent has denominator 4 = 2²)

## Step 2: Apply the Gaussian integral formula
The general formula for a Gaussian integral is:
$$\int_{-\infty}^{\infty} e^{-(x-\mu)^2/(2\sigma^2)}\:dx = \sigma\sqrt{2\pi}$$

In our case:
- $\mu = 2024$
- $\sigma^2 = 2$, so $\sigma = \sqrt{2}$

## Step 3: Substitute into the formula
$$\int_{-\infty}^{\infty} e^{-(x-2024)^2/4}\:dx = \sqrt{2} \cdot \sqrt{2\pi} = 2\sqrt{\pi}$$

## Step 4: Calculate the numerical value
$2\sqrt{\pi} \approx 2 \cdot 1.7724538509 \approx 3.5449077018$

The exact answer is $2\sqrt{\pi}$, and the numerical approximation rounded to 10 decimal places is 3.5449077018.

{"answer": "2\\sqrt{\\pi}", "numerical_answer": "3.5449077018"}