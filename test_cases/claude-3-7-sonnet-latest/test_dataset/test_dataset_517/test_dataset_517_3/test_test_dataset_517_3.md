# Evaluating $\int_{-\infty}^\infty e^{-2x^2-5x-3}dx$

## Step 1: Rewrite the exponent in completed square form

I'll start by rewriting the exponent $-2x^2-5x-3$ in the form $-a(x+b)^2+c$.

$-2x^2-5x-3 = -2(x^2 + \frac{5}{2}x) - 3$
$= -2(x^2 + \frac{5}{2}x + \frac{25}{16} - \frac{25}{16}) - 3$
$= -2(x + \frac{5}{4})^2 + 2 \cdot \frac{25}{16} - 3$
$= -2(x + \frac{5}{4})^2 + \frac{25}{8} - 3$
$= -2(x + \frac{5}{4})^2 + \frac{25-24}{8}$
$= -2(x + \frac{5}{4})^2 + \frac{1}{8}$

## Step 2: Substitute the completed square form into the integral

Now I can rewrite the integral as:
$\int_{-\infty}^\infty e^{-2x^2-5x-3}dx = \int_{-\infty}^\infty e^{-2(x + \frac{5}{4})^2 + \frac{1}{8}}dx$
$= e^{\frac{1}{8}} \int_{-\infty}^\infty e^{-2(x + \frac{5}{4})^2}dx$

## Step 3: Apply substitution

Let's use the substitution $u = x + \frac{5}{4}$, which gives $dx = du$.
When $x \to -\infty$, $u \to -\infty$ and when $x \to \infty$, $u \to \infty$.

The integral becomes:
$e^{\frac{1}{8}} \int_{-\infty}^\infty e^{-2u^2}du$

## Step 4: Use the Gaussian integral formula

We know that $\int_{-\infty}^\infty e^{-ax^2}dx = \sqrt{\frac{\pi}{a}}$ for $a > 0$.

In our case, $a = 2$, so:
$e^{\frac{1}{8}} \int_{-\infty}^\infty e^{-2u^2}du = e^{\frac{1}{8}} \cdot \sqrt{\frac{\pi}{2}}$

## Step 5: Simplify the final result

$\int_{-\infty}^\infty e^{-2x^2-5x-3}dx = e^{\frac{1}{8}} \cdot \sqrt{\frac{\pi}{2}}$
$= e^{\frac{1}{8}} \cdot \frac{\sqrt{\pi}}{\sqrt{2}}$
$= \frac{e^{\frac{1}{8}} \cdot \sqrt{\pi}}{\sqrt{2}}$

## Step 6: Calculate the numerical approximation

$e^{\frac{1}{8}} \approx 1.1331484531$
$\sqrt{\pi} \approx 1.7724538509$
$\sqrt{2} \approx 1.4142135624$

Therefore:
$\frac{e^{\frac{1}{8}} \cdot \sqrt{\pi}}{\sqrt{2}} \approx \frac{1.1331484531 \cdot 1.7724538509}{1.4142135624} \approx 1.4210132090$

## Final Answer
The exact value of the definite integral is $\frac{e^{\frac{1}{8}} \cdot \sqrt{\pi}}{\sqrt{2}}$, which is approximately $1.4210132090$.

{"answer": "\\frac{e^{\\frac{1}{8}} \\cdot \\sqrt{\\pi}}{\\sqrt{2}}", "numerical_answer": "1.4210132090"}