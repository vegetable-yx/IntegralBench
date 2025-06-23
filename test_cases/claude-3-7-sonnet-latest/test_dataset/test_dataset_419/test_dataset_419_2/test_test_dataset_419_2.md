# Evaluation of $\int_0^\infty\frac{x}{e^x-1}\,dx$

## Step 1: Recognize the integral

I notice that this integral involves $\frac{x}{e^x-1}$, which is related to the Riemann zeta function and Bernoulli numbers.

## Step 2: Use the known series representation

For $x > 0$, we have the series expansion:
$$\frac{x}{e^x-1} = \sum_{n=0}^{\infty} B_n \frac{x^n}{n!}$$

Where $B_n$ are the Bernoulli numbers with $B_1 = -\frac{1}{2}$.

## Step 3: Integration

Integrating term by term:
$$\int_0^\infty\frac{x}{e^x-1}\,dx = \int_0^\infty \sum_{n=0}^{\infty} B_n \frac{x^n}{n!}\,dx$$

However, a more direct approach is to use the relationship with the Riemann zeta function.

## Step 4: Use the integral representation of $\zeta(s)$

The Riemann zeta function has the integral representation:
$$\zeta(s)\Gamma(s) = \int_0^\infty \frac{x^{s-1}}{e^x-1}\,dx$$

For our integral, we have $s=2$, so:
$$\int_0^\infty\frac{x}{e^x-1}\,dx = \zeta(2)\Gamma(2)$$

## Step 5: Evaluate using known values

We know that:
- $\zeta(2) = \frac{\pi^2}{6}$
- $\Gamma(2) = 1!= 1$

Therefore:
$$\int_0^\infty\frac{x}{e^x-1}\,dx = \frac{\pi^2}{6} \cdot 1 = \frac{\pi^2}{6}$$

## Step 6: Numerical approximation

The numerical approximation of $\frac{\pi^2}{6}$ to 10 decimal places is:
$$\frac{\pi^2}{6} \approx 1.6449340668$$

{"answer": "\\frac{\\pi^2}{6}", "numerical_answer": "1.6449340668"}