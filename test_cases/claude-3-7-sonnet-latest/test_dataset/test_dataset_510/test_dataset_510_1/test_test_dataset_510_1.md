# Evaluating $\int_0^{5\pi/2}\frac{dx}{2+\cos x}$

## Step 1: Setup the integral

I need to evaluate $\int_0^{5\pi/2}\frac{dx}{2+\cos x}$

For integrals of the form $\int\frac{dx}{a+b\cos x}$, I can use the substitution $t = \tan(x/2)$ which transforms the integral into a rational function.

## Step 2: Apply the substitution $t = \tan(x/2)$

With this substitution:
- $\cos x = \frac{1-t^2}{1+t^2}$
- $dx = \frac{2dt}{1+t^2}$

So our integral becomes:
$$\int_0^{5\pi/2}\frac{dx}{2+\cos x} = \int_0^{5\pi/2}\frac{dx}{2+\frac{1-t^2}{1+t^2}} = \int_0^{5\pi/2}\frac{dx}{\frac{2(1+t^2)+(1-t^2)}{1+t^2}} = \int_0^{5\pi/2}\frac{dx}{\frac{3+t^2}{1+t^2}}$$

Continuing with the substitution:
$$\int_0^{5\pi/2}\frac{dx}{2+\cos x} = \int_{t=\tan(0/2)}^{t=\tan(5\pi/4)}\frac{\frac{2dt}{1+t^2}}{\frac{3+t^2}{1+t^2}} = \int_{0}^{\infty}\frac{2dt}{3+t^2}$$

Note that as $x$ goes from $0$ to $5\pi/2$, $t = \tan(x/2)$ goes from $0$ to $\infty$.

## Step 3: Evaluate the resulting integral

$$\int_{0}^{\infty}\frac{2dt}{3+t^2} = 2\int_{0}^{\infty}\frac{dt}{3+t^2}$$

This is a standard integral. I'll use the substitution $t = \sqrt{3}\tan\theta$:
- $dt = \sqrt{3}\sec^2\theta\,d\theta$
- When $t = 0$, $\theta = 0$
- When $t = \infty$, $\theta = \pi/2$

$$2\int_{0}^{\infty}\frac{dt}{3+t^2} = 2\int_{0}^{\pi/2}\frac{\sqrt{3}\sec^2\theta\,d\theta}{3+3\tan^2\theta} = 2\int_{0}^{\pi/2}\frac{\sqrt{3}\sec^2\theta\,d\theta}{3\sec^2\theta} = \frac{2\sqrt{3}}{3}\int_{0}^{\pi/2}d\theta = \frac{2\sqrt{3}}{3} \cdot \frac{\pi}{2}$$

## Step 4: Simplify the final result

$$\int_0^{5\pi/2}\frac{dx}{2+\cos x} = \frac{2\sqrt{3}}{3} \cdot \frac{\pi}{2} = \frac{\pi\sqrt{3}}{3}$$

## Step 5: Numerical approximation

The numerical value of $\frac{\pi\sqrt{3}}{3}$ is approximately $1.8137993642$.

{"answer": "\\frac{\\pi\\sqrt{3}}{3}", "numerical_answer": "1.8137993642"}