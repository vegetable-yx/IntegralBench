# Evaluating $\int_{-\infty}^{\infty} e^{-2x^2-5x-3}dx$

I need to evaluate the definite integral $\int_{-\infty}^{\infty} e^{-2x^2-5x-3}dx$.

## Step 1: Rewrite the exponent to complete the square
Let's look at the exponent $-2x^2-5x-3$:

$-2x^2-5x-3 = -2(x^2 + \frac{5}{2}x) - 3$

$= -2(x^2 + \frac{5}{2}x + \frac{25}{16} - \frac{25}{16}) - 3$

$= -2(x + \frac{5}{4})^2 + 2 \cdot \frac{25}{16} - 3$

$= -2(x + \frac{5}{4})^2 + \frac{25}{8} - 3$

$= -2(x + \frac{5}{4})^2 + \frac{25-24}{8}$

$= -2(x + \frac{5}{4})^2 + \frac{1}{8}$

## Step 2: Substitute into the integral
Now I can rewrite the integral:

$\int_{-\infty}^{\infty} e^{-2x^2-5x-3}dx = \int_{-\infty}^{\infty} e^{-2(x + \frac{5}{4})^2 + \frac{1}{8}}dx$

$= e^{\frac{1}{8}} \int_{-\infty}^{\infty} e^{-2(x + \frac{5}{4})^2}dx$

## Step 3: Use substitution 
Let $u = x + \frac{5}{4}$, so $dx = du$

When $x \to -\infty$, $u \to -\infty$
When $x \to \infty$, $u \to \infty$

So the integral becomes:
$e^{\frac{1}{8}} \int_{-\infty}^{\infty} e^{-2u^2}du$

## Step 4: Apply the Gaussian integral formula
I know that $\int_{-\infty}^{\infty} e^{-ax^2}dx = \sqrt{\frac{\pi}{a}}$ for $a > 0$

In our case, $a = 2$, so:
$\int_{-\infty}^{\infty} e^{-2u^2}du = \sqrt{\frac{\pi}{2}}$

## Step 5: Substitute back
$\int_{-\infty}^{\infty} e^{-2x^2-5x-3}dx = e^{\frac{1}{8}} \cdot \sqrt{\frac{\pi}{2}}$

$= \sqrt{\frac{\pi}{2}} \cdot e^{\frac{1}{8}}$

## Step 6: Calculate the numerical value
$\sqrt{\frac{\pi}{2}} \approx 1.2533141373$
$e^{\frac{1}{8}} \approx 1.1331484531$

$\sqrt{\frac{\pi}{2}} \cdot e^{\frac{1}{8}} \approx 1.2533141373 \cdot 1.1331484531 \approx 1.4201269047$

Therefore, the exact answer is $\sqrt{\frac{\pi}{2}} \cdot e^{\frac{1}{8}}$ and the numerical approximation is $1.4201269047$.

{"answer": "\\sqrt{\\frac{\\pi}{2}} \\cdot e^{\\frac{1}{8}}", "numerical_answer": "1.4201269047"}