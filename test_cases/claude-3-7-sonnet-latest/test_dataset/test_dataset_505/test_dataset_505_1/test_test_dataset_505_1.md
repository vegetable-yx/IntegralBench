# Evaluating $\int_0^1\sin(\cos^{-1}(x))\:dx$

I'll solve this definite integral step by step.

## Step 1: Make a substitution
Let's substitute $u = \cos^{-1}(x)$, which means $x = \cos(u)$.

When $x = 0$, $u = \cos^{-1}(0) = \frac{\pi}{2}$
When $x = 1$, $u = \cos^{-1}(1) = 0$

For the differential, we have:
$dx = -\sin(u)\:du$

## Step 2: Rewrite the integral in terms of $u$
$$\int_0^1\sin(\cos^{-1}(x))\:dx = \int_{\frac{\pi}{2}}^{0}\sin(u) \cdot (-\sin(u))\:du = \int_{0}^{\frac{\pi}{2}}\sin^2(u)\:du$$

Note that I changed the limits and the sign when reversing the bounds of integration.

## Step 3: Use the identity $\sin^2(u) = \frac{1-\cos(2u)}{2}$
$$\int_{0}^{\frac{\pi}{2}}\sin^2(u)\:du = \int_{0}^{\frac{\pi}{2}}\frac{1-\cos(2u)}{2}\:du = \frac{1}{2}\int_{0}^{\frac{\pi}{2}}(1-\cos(2u))\:du$$
$$= \frac{1}{2}\left[u - \frac{\sin(2u)}{2}\right]_{0}^{\frac{\pi}{2}}$$

## Step 4: Evaluate at the limits
$$\frac{1}{2}\left[u - \frac{\sin(2u)}{2}\right]_{0}^{\frac{\pi}{2}} = \frac{1}{2}\left[\frac{\pi}{2} - \frac{\sin(\pi)}{2} - \left(0 - \frac{\sin(0)}{2}\right)\right]$$
$$= \frac{1}{2}\left[\frac{\pi}{2} - 0 - 0\right] = \frac{1}{2} \cdot \frac{\pi}{2} = \frac{\pi}{4}$$

## Step 5: Numerical approximation
$\frac{\pi}{4} \approx 0.7853981634$

{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}