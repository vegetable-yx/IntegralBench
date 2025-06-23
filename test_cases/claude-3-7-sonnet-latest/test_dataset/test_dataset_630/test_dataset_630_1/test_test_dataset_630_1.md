# Calculating $\int_1^3\frac{\ln(x)}{x^2+3}\mathrm{d}x$

To evaluate this definite integral, I'll first find the antiderivative and then apply the fundamental theorem of calculus.

## Step 1: Find the antiderivative of $\frac{\ln(x)}{x^2+3}$

This integral doesn't have an elementary antiderivative through standard methods like substitution or integration by parts. I'll approach it using the properties of arctangent derivatives and logarithms.

First, I'll make the substitution $x = \sqrt{3}\tan\theta$ to transform the denominator.

When $x = \sqrt{3}\tan\theta$:
- $dx = \sqrt{3}\sec^2\theta\,d\theta$
- $x^2 + 3 = 3\tan^2\theta + 3 = 3(1 + \tan^2\theta) = 3\sec^2\theta$

The integral becomes:
$$\int\frac{\ln(x)}{x^2+3}\mathrm{d}x = \int\frac{\ln(\sqrt{3}\tan\theta)}{3\sec^2\theta}\sqrt{3}\sec^2\theta\,d\theta = \frac{1}{\sqrt{3}}\int\ln(\sqrt{3}\tan\theta)\,d\theta$$

Now, $\ln(\sqrt{3}\tan\theta) = \ln(\sqrt{3}) + \ln(\tan\theta)$, so:
$$\frac{1}{\sqrt{3}}\int\ln(\sqrt{3}\tan\theta)\,d\theta = \frac{1}{\sqrt{3}}\int[\ln(\sqrt{3}) + \ln(\tan\theta)]\,d\theta$$

This becomes:
$$\frac{\ln(\sqrt{3})}{\sqrt{3}}\int d\theta + \frac{1}{\sqrt{3}}\int\ln(\tan\theta)\,d\theta$$

The first part is $\frac{\ln(\sqrt{3})}{\sqrt{3}}\theta$. For the second part, we use the known result:
$$\int\ln(\tan\theta)\,d\theta = \theta\ln(\sin\theta) - \theta\ln(\cos\theta) - \theta$$

So our integral is:
$$\frac{\ln(\sqrt{3})}{\sqrt{3}}\theta + \frac{1}{\sqrt{3}}[\theta\ln(\sin\theta) - \theta\ln(\cos\theta) - \theta]$$

Simplifying:
$$\frac{\theta}{\sqrt{3}}[\ln(\sqrt{3}) + \ln(\sin\theta) - \ln(\cos\theta) - 1]$$

Now we need to convert back to the variable $x$. Since $x = \sqrt{3}\tan\theta$, we have:
- $\tan\theta = \frac{x}{\sqrt{3}}$
- $\theta = \arctan\left(\frac{x}{\sqrt{3}}\right)$
- $\sin\theta = \frac{\tan\theta}{\sqrt{1+\tan^2\theta}} = \frac{x/\sqrt{3}}{\sqrt{1+(x/\sqrt{3})^2}} = \frac{x}{\sqrt{x^2+3}}$
- $\cos\theta = \frac{1}{\sqrt{1+\tan^2\theta}} = \frac{1}{\sqrt{1+(x/\sqrt{3})^2}} = \frac{\sqrt{3}}{\sqrt{x^2+3}}$

Substituting these back:
$$F(x) = \frac{1}{\sqrt{3}}\arctan\left(\frac{x}{\sqrt{3}}\right)\left[\ln(\sqrt{3}) + \ln\left(\frac{x}{\sqrt{x^2+3}}\right) - \ln\left(\frac{\sqrt{3}}{\sqrt{x^2+3}}\right) - 1\right]$$

Simplifying:
$$F(x) = \frac{1}{\sqrt{3}}\arctan\left(\frac{x}{\sqrt{3}}\right)\left[\ln\left(\frac{x}{\sqrt{3}}\right) - 1\right]$$

## Step 2: Evaluate the definite integral

Now I'll evaluate $F(3) - F(1)$:

For $x = 3$:
$$F(3) = \frac{1}{\sqrt{3}}\arctan\left(\frac{3}{\sqrt{3}}\right)\left[\ln\left(\frac{3}{\sqrt{3}}\right) - 1\right]$$
$$= \frac{1}{\sqrt{3}}\arctan\left(\sqrt{3}\right)\left[\ln\left(\frac{3}{\sqrt{3}}\right) - 1\right]$$

For $x = 1$:
$$F(1) = \frac{1}{\sqrt{3}}\arctan\left(\frac{1}{\sqrt{3}}\right)\left[\ln\left(\frac{1}{\sqrt{3}}\right) - 1\right]$$

Therefore:
$$\int_1^3\frac{\ln(x)}{x^2+3}\mathrm{d}x = F(3) - F(1)$$
$$= \frac{1}{\sqrt{3}}\arctan\left(\sqrt{3}\right)\left[\ln\left(\frac{3}{\sqrt{3}}\right) - 1\right] - \frac{1}{\sqrt{3}}\arctan\left(\frac{1}{\sqrt{3}}\right)\left[\ln\left(\frac{1}{\sqrt{3}}\right) - 1\right]$$

Since $\arctan(\sqrt{3}) = \frac{\pi}{3}$ and $\arctan\left(\frac{1}{\sqrt{3}}\right) = \frac{\pi}{6}$, and simplifying the logarithms:
$$= \frac{\pi}{3\sqrt{3}}\left[\ln(3) - \ln(\sqrt{3}) - 1\right] - \frac{\pi}{6\sqrt{3}}\left[\ln(1) - \ln(\sqrt{3}) - 1\right]$$

Since $\ln(1) = 0$:
$$= \frac{\pi}{3\sqrt{3}}\left[\ln(3) - \frac{1}{2}\ln(3) - 1\right] - \frac{\pi}{6\sqrt{3}}\left[- \frac{1}{2}\ln(3) - 1\right]$$
$$= \frac{\pi}{3\sqrt{3}}\left[\frac{1}{2}\ln(3) - 1\right] - \frac{\pi}{6\sqrt{3}}\left[- \frac{1}{2}\ln(3) - 1\right]$$
$$= \frac{\pi}{3\sqrt{3}}\left[\frac{1}{2}\ln(3) - 1\right] + \frac{\pi}{6\sqrt{3}}\left[\frac{1}{2}\ln(3) + 1\right]$$

Simplifying further:
$$= \frac{\pi}{6\sqrt{3}}\left[2\left(\frac{1}{2}\ln(3) - 1\right) + \frac{1}{2}\ln(3) + 1\right]$$
$$= \frac{\pi}{6\sqrt{3}}\left[\ln(3) - 2 + \frac{1}{2}\ln(3) + 1\right]$$
$$= \frac{\pi}{6\sqrt{3}}\left[\frac{3}{2}\ln(3) - 1\right]$$

## Step 3: Calculate the numerical approximation

Substituting values:
- $\pi \approx 3.14159265359$
- $\sqrt{3} \approx 1.73205080757$
- $\ln(3) \approx 1.09861228867$

$$\frac{\pi}{6\sqrt{3}}\left[\frac{3}{2}\ln(3) - 1\right] \approx \frac{3.14159265359}{6 \times 1.73205080757}\left[\frac{3}{2} \times 1.09861228867 - 1\right]$$
$$\approx 0.3025850930 \times (1.6479184330 - 1)$$
$$\approx 0.3025850930 \times 0.6479184330$$
$$\approx 0.1960459625$$

## Final Result

The exact value of the integral is:
$$\int_1^3\frac{\ln(x)}{x^2+3}\mathrm{d}x = \frac{\pi}{6\sqrt{3}}\left[\frac{3}{2}\ln(3) - 1\right]$$

The numerical approximation rounded to 10 decimal places is 0.1960459625.

{"answer": "\\frac{\\pi}{6\\sqrt{3}}\\left[\\frac{3}{2}\\ln(3) - 1\\right]", "numerical_answer": "0.1960459625"}