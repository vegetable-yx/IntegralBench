# Evaluating $\int_0^1\frac{e^{\arctan(x)}}{(x^2+1)^{3/2}}\text{ dx}$

I'll compute this definite integral step by step.

## Step 1: Let's make a substitution
Let $u = \arctan(x)$, then:
- $\frac{du}{dx} = \frac{1}{1+x^2}$
- $dx = (1+x^2)du$
- When $x = 0$, $u = \arctan(0) = 0$
- When $x = 1$, $u = \arctan(1) = \frac{\pi}{4}$

Also note that $x = \tan(u)$ for this substitution.

## Step 2: Rewrite the integral with this substitution

$\int_0^1\frac{e^{\arctan(x)}}{(x^2+1)^{3/2}}\text{ dx}$

$= \int_0^{\pi/4}\frac{e^u}{((\tan^2(u))+1)^{3/2}} \cdot (1+\tan^2(u))du$

$= \int_0^{\pi/4}\frac{e^u}{((\tan^2(u))+1)^{3/2}} \cdot \frac{1}{\cos^2(u)}du$

Using the identity $1+\tan^2(u) = \frac{1}{\cos^2(u)}$, we get:

$= \int_0^{\pi/4}\frac{e^u}{(\frac{1}{\cos^2(u)})^{3/2}} \cdot \frac{1}{\cos^2(u)}du$

$= \int_0^{\pi/4}\frac{e^u}{\frac{1}{\cos^3(u)}} \cdot \frac{1}{\cos^2(u)}du$

$= \int_0^{\pi/4}e^u \cdot \cos^3(u) \cdot \frac{1}{\cos^2(u)}du$

$= \int_0^{\pi/4}e^u \cdot \cos(u)du$

## Step 3: Solve this simplified integral
We can use integration by parts with:
- $f(u) = e^u$, so $f'(u) = e^u$
- $g'(u) = \cos(u)$, so $g(u) = \sin(u)$

The integration by parts formula gives:
$\int f(u)g'(u)du = f(u)g(u) - \int f'(u)g(u)du$

So:
$\int e^u\cos(u)du = e^u\sin(u) - \int e^u\sin(u)du$

For $\int e^u\sin(u)du$, let's use integration by parts again:
- $f(u) = e^u$, so $f'(u) = e^u$
- $g'(u) = \sin(u)$, so $g(u) = -\cos(u)$

Thus:
$\int e^u\sin(u)du = -e^u\cos(u) + \int e^u\cos(u)du$

Let's denote $I = \int e^u\cos(u)du$. Then:
$I = e^u\sin(u) - (-e^u\cos(u) + I)$

$2I = e^u\sin(u) + e^u\cos(u)$

$I = \frac{e^u(\sin(u) + \cos(u))}{2}$

## Step 4: Apply the limits of integration
Now we evaluate the definite integral by applying the limits $u = 0$ and $u = \frac{\pi}{4}$:

$\int_0^{\pi/4}e^u\cos(u)du = \left[ \frac{e^u(\sin(u) + \cos(u))}{2} \right]_0^{\pi/4}$

$= \frac{e^{\pi/4}(\sin(\pi/4) + \cos(\pi/4))}{2} - \frac{e^0(\sin(0) + \cos(0))}{2}$

$= \frac{e^{\pi/4}(\frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2})}{2} - \frac{1 \cdot (0 + 1)}{2}$

$= \frac{e^{\pi/4} \cdot \sqrt{2}}{2} - \frac{1}{2}$

$= \frac{\sqrt{2} \cdot e^{\pi/4} - 1}{2}$

## Step 5: Numerical approximation
The numerical value of $\frac{\sqrt{2} \cdot e^{\pi/4} - 1}{2}$ is approximately:
$\frac{\sqrt{2} \cdot e^{0.7853981634} - 1}{2} \approx \frac{\sqrt{2} \cdot 2.1932800507 - 1}{2} \approx 1.0518599404$

## Final answer
The exact answer is $\frac{\sqrt{2} \cdot e^{\pi/4} - 1}{2}$

{"answer": "\\frac{\\sqrt{2} \\cdot e^{\\pi/4} - 1}{2}", "numerical_answer": "1.0518599404"}