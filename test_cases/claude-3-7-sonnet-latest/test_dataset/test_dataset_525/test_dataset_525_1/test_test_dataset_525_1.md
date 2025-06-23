# Calculating $\int_{1/\sqrt{2}}^1\frac{\arcsin(x)}{x^3}\:dx$

## Step 1: Set up the integration

Let's start by making a substitution. Let $u = \arcsin(x)$, then:
- $du = \frac{1}{\sqrt{1-x^2}}dx$
- $x = \sin(u)$

When $x = \frac{1}{\sqrt{2}}$, $u = \arcsin\left(\frac{1}{\sqrt{2}}\right) = \frac{\pi}{4}$
When $x = 1$, $u = \arcsin(1) = \frac{\pi}{2}$

## Step 2: Rewrite the integral in terms of $u$

We need to express $dx$ in terms of $du$:
$dx = \sqrt{1-x^2}du$

And substitute $x = \sin(u)$ into the integrand:
$\frac{\arcsin(x)}{x^3} = \frac{u}{(\sin(u))^3}$

So our integral becomes:
$$\int_{1/\sqrt{2}}^1\frac{\arcsin(x)}{x^3}\:dx = \int_{\pi/4}^{\pi/2}\frac{u}{(\sin(u))^3}\sqrt{1-\sin^2(u)}\:du$$

Using $1-\sin^2(u) = \cos^2(u)$:
$$\int_{\pi/4}^{\pi/2}\frac{u \cdot \cos(u)}{(\sin(u))^3}\:du$$

## Step 3: Further simplification

Let's rewrite this as:
$$\int_{\pi/4}^{\pi/2}u \cdot \frac{\cos(u)}{(\sin(u))^3}\:du$$

For the term $\frac{\cos(u)}{(\sin(u))^3}$, note that:
$$\frac{d}{du}\left(-\frac{1}{2(\sin(u))^2}\right) = \frac{\cos(u)}{(\sin(u))^3}$$

## Step 4: Integration by parts

Let's use integration by parts with:
- $f(u) = u$
- $g'(u) = \frac{\cos(u)}{(\sin(u))^3}$
- $f'(u) = 1$
- $g(u) = -\frac{1}{2(\sin(u))^2}$

Using the formula $\int f(u)g'(u)du = f(u)g(u) - \int f'(u)g(u)du$:

$$\int_{\pi/4}^{\pi/2}u \cdot \frac{\cos(u)}{(\sin(u))^3}\:du = \left[u \cdot \left(-\frac{1}{2(\sin(u))^2}\right)\right]_{\pi/4}^{\pi/2} - \int_{\pi/4}^{\pi/2} \left(-\frac{1}{2(\sin(u))^2}\right) \:du$$

## Step 5: Evaluate the first term

At $u = \frac{\pi}{2}$, $\sin(u) = 1$, so the term becomes $-\frac{\pi}{4}$

At $u = \frac{\pi}{4}$, $\sin(u) = \frac{1}{\sqrt{2}}$, so the term becomes $-\frac{\pi}{4} \cdot \frac{1}{2 \cdot \frac{1}{2}} = -\frac{\pi}{4}$

Therefore:
$$\left[u \cdot \left(-\frac{1}{2(\sin(u))^2}\right)\right]_{\pi/4}^{\pi/2} = -\frac{\pi}{4} - \left(-\frac{\pi}{4} \cdot 2\right) = -\frac{\pi}{4} + \frac{\pi}{2} = \frac{\pi}{4}$$

## Step 6: Evaluate the second term

For the second integral:
$$\int_{\pi/4}^{\pi/2} \frac{1}{2(\sin(u))^2} \:du$$

We know that $\int \csc^2(u) \:du = -\cot(u) + C$, so:
$$\int_{\pi/4}^{\pi/2} \frac{1}{2(\sin(u))^2} \:du = \frac{1}{2}\int_{\pi/4}^{\pi/2} \csc^2(u) \:du = \frac{1}{2}[-\cot(u)]_{\pi/4}^{\pi/2}$$

At $u = \frac{\pi}{2}$, $\cot(u) = 0$
At $u = \frac{\pi}{4}$, $\cot(u) = 1$

Therefore:
$$\frac{1}{2}[-\cot(u)]_{\pi/4}^{\pi/2} = \frac{1}{2}[0 - (-1)] = \frac{1}{2}$$

## Step 7: Combine the results

$$\int_{1/\sqrt{2}}^1\frac{\arcsin(x)}{x^3}\:dx = \frac{\pi}{4} - \frac{1}{2} = \frac{\pi}{4} - \frac{1}{2}$$

## Step 8: Numerical approximation

$\frac{\pi}{4} - \frac{1}{2} ≈ 0.7853981634 - 0.5 ≈ 0.2853981634$

Therefore, the exact answer is $\frac{\pi}{4} - \frac{1}{2}$, which numerically is approximately $0.2853981634$.

{"answer": "\\frac{\\pi}{4} - \\frac{1}{2}", "numerical_answer": "0.2853981634"}