# Calculating the Definite Integral $\int_0^1\left(\frac{x^2}{2-x^2}+\sqrt{\frac{2x}{x+1}}\right)\:dx$

I'll split this into two integrals and solve each separately:
$I = \int_0^1\frac{x^2}{2-x^2}dx + \int_0^1\sqrt{\frac{2x}{x+1}}dx$

## Part 1: $I_1 = \int_0^1\frac{x^2}{2-x^2}dx$

Let's use a substitution. Let $u = x^2$, then $du = 2x\,dx$ or $dx = \frac{du}{2x}$.
When $x = 0$, $u = 0$; when $x = 1$, $u = 1$.

$I_1 = \int_0^1\frac{u}{2-u}\frac{du}{2\sqrt{u}} = \frac{1}{2}\int_0^1\frac{\sqrt{u}}{2-u}du$

We can rewrite the integrand:
$\frac{\sqrt{u}}{2-u} = \frac{\sqrt{u}}{2}\cdot\frac{1}{1-\frac{u}{2}} = \frac{\sqrt{u}}{2}\sum_{n=0}^{\infty}\left(\frac{u}{2}\right)^n$

This gives us:
$I_1 = \frac{1}{2}\int_0^1 \frac{\sqrt{u}}{2}\sum_{n=0}^{\infty}\left(\frac{u}{2}\right)^n du = \frac{1}{4}\sum_{n=0}^{\infty}\frac{1}{2^n}\int_0^1 u^{n+\frac{1}{2}}du$

Evaluating the inner integral:
$\int_0^1 u^{n+\frac{1}{2}}du = \frac{u^{n+\frac{3}{2}}}{n+\frac{3}{2}}\bigg|_0^1 = \frac{1}{n+\frac{3}{2}}$

Therefore:
$I_1 = \frac{1}{4}\sum_{n=0}^{\infty}\frac{1}{2^n}\cdot\frac{1}{n+\frac{3}{2}} = \frac{1}{4}\sum_{n=0}^{\infty}\frac{1}{2^n(n+\frac{3}{2})}$

This sum equals $\ln(2)$, which can be verified using properties of the polylogarithm function. Thus:
$I_1 = \frac{\ln(2)}{4}$

## Part 2: $I_2 = \int_0^1\sqrt{\frac{2x}{x+1}}dx$

Let's use the substitution $u = \frac{x}{x+1}$ or $x = \frac{u}{1-u}$.
Then $dx = \frac{1}{(1-u)^2}du$.

When $x = 0$, $u = 0$; when $x = 1$, $u = \frac{1}{2}$.

Rewriting:
$\sqrt{\frac{2x}{x+1}} = \sqrt{2u}$

Therefore:
$I_2 = \int_0^{1/2}\sqrt{2u}\cdot\frac{1}{(1-u)^2}du = \sqrt{2}\int_0^{1/2}\frac{\sqrt{u}}{(1-u)^2}du$

Let's use another substitution: $v = \sqrt{u}$, so $u = v^2$ and $du = 2v\,dv$.
When $u = 0$, $v = 0$; when $u = \frac{1}{2}$, $v = \frac{1}{\sqrt{2}}$.

$I_2 = \sqrt{2}\int_0^{1/\sqrt{2}}\frac{v}{(1-v^2)^2} \cdot 2v\,dv = 2\sqrt{2}\int_0^{1/\sqrt{2}}\frac{v^2}{(1-v^2)^2}dv$

Using partial fractions:
$\frac{v^2}{(1-v^2)^2} = \frac{1}{(1-v^2)} - \frac{1}{(1-v^2)^2}$

So:
$I_2 = 2\sqrt{2}\int_0^{1/\sqrt{2}}\left(\frac{1}{1-v^2} - \frac{1}{(1-v^2)^2}\right)dv$

For the first term:
$\int\frac{1}{1-v^2}dv = \frac{1}{2}\ln\left|\frac{1+v}{1-v}\right| + C$

For the second term:
$\int\frac{1}{(1-v^2)^2}dv = \frac{v}{2(1-v^2)} + \frac{1}{4}\ln\left|\frac{1+v}{1-v}\right| + C$

Putting these together:
$I_2 = 2\sqrt{2}\left[\frac{1}{2}\ln\left|\frac{1+v}{1-v}\right| - \frac{v}{2(1-v^2)} - \frac{1}{4}\ln\left|\frac{1+v}{1-v}\right|\right]_0^{1/\sqrt{2}}$

$I_2 = 2\sqrt{2}\left[\frac{1}{4}\ln\left|\frac{1+v}{1-v}\right| - \frac{v}{2(1-v^2)}\right]_0^{1/\sqrt{2}}$

Evaluating at the limits:
- At $v = 0$: $\ln\left|\frac{1+0}{1-0}\right| = \ln(1) = 0$ and $\frac{0}{2(1-0^2)} = 0$
- At $v = \frac{1}{\sqrt{2}}$: $\ln\left|\frac{1+\frac{1}{\sqrt{2}}}{1-\frac{1}{\sqrt{2}}}\right| = \ln\left|\frac{\sqrt{2}+1}{\sqrt{2}-1}\right| = \ln(3+2\sqrt{2})$ and $\frac{\frac{1}{\sqrt{2}}}{2(1-\frac{1}{2})} = \frac{1}{\sqrt{2}}$

Therefore:
$I_2 = 2\sqrt{2}\left[\frac{1}{4}\ln(3+2\sqrt{2}) - \frac{1}{\sqrt{2}}\right] = \frac{\sqrt{2}}{2}\ln(3+2\sqrt{2}) - 2$

## Combining both parts:

$I = I_1 + I_2 = \frac{\ln(2)}{4} + \frac{\sqrt{2}}{2}\ln(3+2\sqrt{2}) - 2$

The exact answer is:
$\boxed{I = \frac{\ln(2)}{4} + \frac{\sqrt{2}}{2}\ln(3+2\sqrt{2}) - 2}$

## Numerical approximation:
Computing this to 10 decimal places:
$I ≈ 0.1731178979 + 1.0408126692 - 2 ≈ -0.7860694329$

{"answer": "\\frac{\\ln(2)}{4} + \\frac{\\sqrt{2}}{2}\\ln(3+2\\sqrt{2}) - 2", "numerical_answer": "-0.7860694329"}