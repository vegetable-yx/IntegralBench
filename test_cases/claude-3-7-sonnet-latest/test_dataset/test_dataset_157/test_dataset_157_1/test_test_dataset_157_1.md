# Evaluating $\int\limits_{1.0}^{\infty}(x^2-1.0^2)^{2-1/2}e^{-0.5^2x^2}H_{2 \times 2+1}(0.5x)\:dx$

I'll first simplify the integral by identifying the various components:

- $(x^2-1.0^2)^{2-1/2} = (x^2-1)^{3/2}$
- $e^{-0.5^2x^2} = e^{-0.25x^2}$
- $H_{2 \times 2+1}(0.5x) = H_5(0.5x)$, where $H_5$ is the Hermite polynomial of order 5

## Step 1: Identifying the Hermite polynomial $H_5(x)$
The Hermite polynomial of order 5 is:
$H_5(x) = 32x^5 - 160x^3 + 120x$

So $H_5(0.5x) = 32(0.5x)^5 - 160(0.5x)^3 + 120(0.5x)$
$= 32 \cdot 0.5^5 \cdot x^5 - 160 \cdot 0.5^3 \cdot x^3 + 120 \cdot 0.5 \cdot x$
$= x^5 - 20x^3 + 60x$

## Step 2: Substituting and setting up the integral
Our integral becomes:
$\int\limits_{1.0}^{\infty}(x^2-1)^{3/2}e^{-0.25x^2}(x^5 - 20x^3 + 60x)\:dx$

Let's break this into three parts:
$I_1 = \int\limits_{1.0}^{\infty}(x^2-1)^{3/2}e^{-0.25x^2}x^5\:dx$
$I_2 = -20\int\limits_{1.0}^{\infty}(x^2-1)^{3/2}e^{-0.25x^2}x^3\:dx$
$I_3 = 60\int\limits_{1.0}^{\infty}(x^2-1)^{3/2}e^{-0.25x^2}x\:dx$

## Step 3: Applying the substitution $u = x^2-1$
For each integral, I'll use the substitution $u = x^2-1$, which gives:
- $x^2 = u+1$
- $x = \sqrt{u+1}$
- $dx = \frac{du}{2\sqrt{u+1}}$

### For $I_1$:
$I_1 = \int\limits_{1.0}^{\infty}u^{3/2}e^{-0.25(u+1)}(u+1)^{5/2}\frac{du}{2\sqrt{u+1}}$
$= \frac{1}{2}\int\limits_{0}^{\infty}u^{3/2}e^{-0.25(u+1)}(u+1)^2\:du$
$= \frac{1}{2}e^{-0.25}\int\limits_{0}^{\infty}u^{3/2}e^{-0.25u}(u+1)^2\:du$

### For $I_2$:
$I_2 = -20\int\limits_{1.0}^{\infty}u^{3/2}e^{-0.25(u+1)}(u+1)^{3/2}\frac{du}{2\sqrt{u+1}}$
$= -10\int\limits_{0}^{\infty}u^{3/2}e^{-0.25(u+1)}(u+1)\:du$
$= -10e^{-0.25}\int\limits_{0}^{\infty}u^{3/2}e^{-0.25u}(u+1)\:du$

### For $I_3$:
$I_3 = 60\int\limits_{1.0}^{\infty}u^{3/2}e^{-0.25(u+1)}(u+1)^{1/2}\frac{du}{2\sqrt{u+1}}$
$= 30\int\limits_{0}^{\infty}u^{3/2}e^{-0.25(u+1)}\:du$
$= 30e^{-0.25}\int\limits_{0}^{\infty}u^{3/2}e^{-0.25u}\:du$

## Step 4: Using the gamma function
For the third integral $I_3$, I can use the gamma function directly:
$I_3 = 30e^{-0.25}\int\limits_{0}^{\infty}u^{3/2}e^{-0.25u}\:du$

Using the formula $\int_0^{\infty} x^{n-1}e^{-ax}dx = \frac{\Gamma(n)}{a^n}$, with $n = 3/2 + 1 = 5/2$ and $a = 0.25$:

$I_3 = 30e^{-0.25} \cdot \frac{\Gamma(5/2)}{0.25^{5/2}}$

We know that $\Gamma(5/2) = \frac{3}{2} \cdot \frac{1}{2} \cdot \Gamma(1/2) = \frac{3\sqrt{\pi}}{4}$

$I_3 = 30e^{-0.25} \cdot \frac{3\sqrt{\pi}/4}{0.25^{5/2}} = 30e^{-0.25} \cdot \frac{3\sqrt{\pi}}{4} \cdot 4^{5/2} = 30e^{-0.25} \cdot 3\sqrt{\pi} \cdot 2^5 = 2880\sqrt{\pi}e^{-0.25}$

## Step 5: For $I_1$ and $I_2$, expanding the polynomials

For $I_1$:
$I_1 = \frac{1}{2}e^{-0.25}\int\limits_{0}^{\infty}u^{3/2}e^{-0.25u}(u^2 + 2u + 1)\:du$
$= \frac{1}{2}e^{-0.25}\int\limits_{0}^{\infty}(u^{7/2} + 2u^{5/2} + u^{3/2})e^{-0.25u}\:du$

Using the gamma function for each term:
$I_1 = \frac{1}{2}e^{-0.25}[\frac{\Gamma(9/2)}{0.25^{9/2}} + 2\frac{\Gamma(7/2)}{0.25^{7/2}} + \frac{\Gamma(5/2)}{0.25^{5/2}}]$

We know:
- $\Gamma(9/2) = \frac{7}{2} \cdot \frac{5}{2} \cdot \frac{3}{2} \cdot \frac{1}{2} \cdot \Gamma(1/2) = \frac{105\sqrt{\pi}}{16}$
- $\Gamma(7/2) = \frac{5}{2} \cdot \frac{3}{2} \cdot \frac{1}{2} \cdot \Gamma(1/2) = \frac{15\sqrt{\pi}}{8}$
- $\Gamma(5/2) = \frac{3\sqrt{\pi}}{4}$

Therefore:
$I_1 = \frac{1}{2}e^{-0.25}[\frac{105\sqrt{\pi}/16}{0.25^{9/2}} + 2\frac{15\sqrt{\pi}/8}{0.25^{7/2}} + \frac{3\sqrt{\pi}/4}{0.25^{5/2}}]$
$= \frac{1}{2}e^{-0.25}\sqrt{\pi}[\frac{105}{16} \cdot 4^{9/2} + 2 \cdot \frac{15}{8} \cdot 4^{7/2} + \frac{3}{4} \cdot 4^{5/2}]$
$= \frac{1}{2}e^{-0.25}\sqrt{\pi}[105 \cdot 2^9 + 30 \cdot 2^7 + 3 \cdot 2^5]$
$= \frac{1}{2}e^{-0.25}\sqrt{\pi}[105 \cdot 512 + 30 \cdot 128 + 3 \cdot 32]$
$= \frac{1}{2}e^{-0.25}\sqrt{\pi}[53760 + 3840 + 96]$
$= \frac{1}{2}e^{-0.25}\sqrt{\pi} \cdot 57696 = 28848\sqrt{\pi}e^{-0.25}$

For $I_2$:
$I_2 = -10e^{-0.25}\int\limits_{0}^{\infty}u^{3/2}e^{-0.25u}(u+1)\:du$
$= -10e^{-0.25}\int\limits_{0}^{\infty}(u^{5/2} + u^{3/2})e^{-0.25u}\:du$

Using the gamma function for each term:
$I_2 = -10e^{-0.25}[\frac{\Gamma(7/2)}{0.25^{7/2}} + \frac{\Gamma(5/2)}{0.25^{5/2}}]$
$= -10e^{-0.25}[\frac{15\sqrt{\pi}/8}{0.25^{7/2}} + \frac{3\sqrt{\pi}/4}{0.25^{5/2}}]$
$= -10e^{-0.25}\sqrt{\pi}[\frac{15}{8} \cdot 4^{7/2} + \frac{3}{4} \cdot 4^{5/2}]$
$= -10e^{-0.25}\sqrt{\pi}[15 \cdot 2^7 + 3 \cdot 2^5]$
$= -10e^{-0.25}\sqrt{\pi}[15 \cdot 128 + 3 \cdot 32]$
$= -10e^{-0.25}\sqrt{\pi}[1920 + 96]$
$= -10e^{-0.25}\sqrt{\pi} \cdot 2016 = -20160\sqrt{\pi}e^{-0.25}$

## Step 6: Combining the results
$I = I_1 + I_2 + I_3$
$= 28848\sqrt{\pi}e^{-0.25} - 20160\sqrt{\pi}e^{-0.25} + 2880\sqrt{\pi}e^{-0.25}$
$= \sqrt{\pi}e^{-0.25}(28848 - 20160 + 2880)$
$= \sqrt{\pi}e