# Evaluating $\int_0^\infty e^{-x^2}\cos(2x)\text{ dx}$

I'll evaluate this integral using complex analysis techniques, specifically by considering the Gaussian integral with a complex parameter.

## Step 1: Set up the approach
Let's define the function:
$$F(t) = \int_0^\infty e^{-x^2}e^{itx}\text{ dx}$$

Note that our original integral can be expressed as:
$$\int_0^\infty e^{-x^2}\cos(2x)\text{ dx} = \text{Re}\left[F(2)\right]$$

## Step 2: Evaluate $F(t)$
First, I'll relate $F(t)$ to the standard Gaussian integral. We know that:
$$\int_{-\infty}^{\infty} e^{-x^2}\text{ dx} = \sqrt{\pi}$$

For the complex version, we have:
$$\int_{-\infty}^{\infty} e^{-x^2}e^{itx}\text{ dx} = \sqrt{\pi}e^{-t^2/4}$$

This can be verified by completing the square in the exponent: $-x^2 + itx = -(x^2 - itx) = -(x - \frac{it}{2})^2 - \frac{t^2}{4}$

Now, due to the even nature of $e^{-x^2}$ and odd nature of $\sin(tx)$:
$$\int_{-\infty}^{\infty} e^{-x^2}\cos(tx)\text{ dx} = 2\int_0^{\infty} e^{-x^2}\cos(tx)\text{ dx}$$
$$\int_{-\infty}^{\infty} e^{-x^2}\sin(tx)\text{ dx} = 0$$

Therefore:
$$\int_{-\infty}^{\infty} e^{-x^2}e^{itx}\text{ dx} = \int_{-\infty}^{\infty} e^{-x^2}\cos(tx)\text{ dx} + i\int_{-\infty}^{\infty} e^{-x^2}\sin(tx)\text{ dx}$$
$$= 2\int_0^{\infty} e^{-x^2}\cos(tx)\text{ dx}$$

Which means:
$$F(t) = \int_0^{\infty} e^{-x^2}\cos(tx)\text{ dx} = \frac{\sqrt{\pi}}{2}e^{-t^2/4}$$

## Step 3: Substitute $t = 2$ to get our answer
$$\int_0^\infty e^{-x^2}\cos(2x)\text{ dx} = F(2) = \frac{\sqrt{\pi}}{2}e^{-2^2/4} = \frac{\sqrt{\pi}}{2}e^{-1} = \frac{\sqrt{\pi}}{2e}$$

## Step 4: Numerical approximation
$$\frac{\sqrt{\pi}}{2e} \approx \frac{1.7724538509055160273}{5.4365636569180982490} \approx 0.3262902569$$

The numerical value, rounded to 10 decimal places, is 0.3262902569.

{"answer": "\\frac{\\sqrt{\\pi}}{2e}", "numerical_answer": "0.3262902569"}