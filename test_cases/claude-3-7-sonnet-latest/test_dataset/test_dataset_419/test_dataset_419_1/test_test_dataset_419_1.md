# Evaluating $\int_0^\infty\frac{x}{e^x-1}\text{ dx}$

## Step 1: Recognize the integral

The integral $\int_0^\infty\frac{x}{e^x-1}\text{ dx}$ is related to the Riemann zeta function. Specifically, it's connected to $\zeta(2)$.

## Step 2: Make a substitution

Let's set $u = e^x - 1$, which gives:
- $e^x = u + 1$
- $x = \ln(u + 1)$
- $dx = \frac{du}{u + 1}$

When $x = 0$, $u = 0$
When $x \to \infty$, $u \to \infty$

## Step 3: Transform the integral

Substituting these values:
$$\int_0^\infty\frac{x}{e^x-1}\text{ dx} = \int_0^\infty\frac{\ln(u+1)}{u}\frac{du}{u+1} = \int_0^\infty\frac{\ln(u+1)}{u(u+1)}\text{ du}$$

## Step 4: Apply partial fractions

We can write:
$$\frac{1}{u(u+1)} = \frac{1}{u} - \frac{1}{u+1}$$

So our integral becomes:
$$\int_0^\infty\ln(u+1)\left(\frac{1}{u} - \frac{1}{u+1}\right)\text{ du}$$

This can be split as:
$$\int_0^\infty\frac{\ln(u+1)}{u}\text{ du} - \int_0^\infty\frac{\ln(u+1)}{u+1}\text{ du}$$

## Step 5: Evaluate the second integral

For the second integral, substitute $v = u+1$:
$$\int_0^\infty\frac{\ln(u+1)}{u+1}\text{ du} = \int_1^\infty\frac{\ln(v)}{v}\text{ dv} = \left.\frac{(\ln v)^2}{2}\right|_1^\infty$$

The upper limit gives 0 (using L'Hôpital's rule), and at $v=1$, $\ln(1)=0$, so this integral equals 0.

## Step 6: Evaluate the first integral

For the first integral $\int_0^\infty\frac{\ln(u+1)}{u}\text{ du}$, we can use the known result:
$$\int_0^\infty\frac{\ln(1+ax)}{x}\text{ dx} = \frac{\pi^2}{6} \quad \text{for } a > 0$$

With $a = 1$, our integral equals $\frac{\pi^2}{6}$.

## Step 7: Combine results

Therefore:
$$\int_0^\infty\frac{x}{e^x-1}\text{ dx} = \frac{\pi^2}{6} - 0 = \frac{\pi^2}{6}$$

## Numerical approximation

The numerical value of $\frac{\pi^2}{6}$ is approximately 1.6449340668.

{"answer": "\\frac{\\pi^2}{6}", "numerical_answer": "1.6449340668"}