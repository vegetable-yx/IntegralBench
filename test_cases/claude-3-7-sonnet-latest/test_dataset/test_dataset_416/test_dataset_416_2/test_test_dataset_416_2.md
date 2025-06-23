# Evaluating $\int_0^1\frac{e^{\arctan(x)}}{(x^2+1)^{3/2}}\text{ dx}$

## Step 1: Make a substitution

Let's set $u = \arctan(x)$. Then:
- $x = \tan(u)$
- $dx = \sec^2(u) \, du$
- When $x = 0$, $u = 0$
- When $x = 1$, $u = \arctan(1) = \frac{\pi}{4}$

Also, note that $x^2 + 1 = \tan^2(u) + 1 = \sec^2(u)$, so $(x^2 + 1)^{3/2} = (\sec^2(u))^{3/2} = \sec^3(u)$

## Step 2: Rewrite the integral

Substituting these values:

$$\int_0^1\frac{e^{\arctan(x)}}{(x^2+1)^{3/2}}\text{ dx} = \int_0^{\pi/4}\frac{e^u}{\sec^3(u)}\sec^2(u) \, du = \int_0^{\pi/4}\frac{e^u}{\sec(u)} \, du$$

Since $\frac{1}{\sec(u)} = \cos(u)$, we have:

$$\int_0^{\pi/4} e^u \cos(u) \, du$$

## Step 3: Solve the integral

For integrals of the form $\int e^{ax}\cos(bx)\,dx$, we can use the formula:

$$\int e^{ax}\cos(bx)\,dx = \frac{e^{ax}}{a^2+b^2}[a\cos(bx) + b\sin(bx)] + C$$

In our case, $a = 1$ and $b = 1$, so:

$$\int e^u \cos(u) \, du = \frac{e^u}{1^2+1^2}[\cos(u) + \sin(u)] + C = \frac{e^u}{2}[\cos(u) + \sin(u)] + C$$

## Step 4: Apply the limits

$$\int_0^{\pi/4} e^u \cos(u) \, du = \left.\frac{e^u}{2}[\cos(u) + \sin(u)]\right|_0^{\pi/4}$$

At $u = \pi/4$:
- $\cos(\pi/4) = \sin(\pi/4) = \frac{1}{\sqrt{2}}$
- $\cos(\pi/4) + \sin(\pi/4) = \frac{2}{\sqrt{2}} = \sqrt{2}$
- $e^{\pi/4} \approx e^{0.7853981634} \approx 2.1932800507$

At $u = 0$:
- $\cos(0) = 1$, $\sin(0) = 0$
- $\cos(0) + \sin(0) = 1$
- $e^0 = 1$

So:
$$\left.\frac{e^u}{2}[\cos(u) + \sin(u)]\right|_0^{\pi/4} = \frac{e^{\pi/4}}{2}\sqrt{2} - \frac{1}{2} = \frac{e^{\pi/4}\sqrt{2} - 1}{2}$$

## Step 5: Simplify the answer

Our final exact answer is:
$$\int_0^1\frac{e^{\arctan(x)}}{(x^2+1)^{3/2}}\text{ dx} = \frac{e^{\pi/4}\sqrt{2} - 1}{2}$$

## Step 6: Numerical approximation

Computing the numerical value:
- $e^{\pi/4} \approx 2.1932800507$
- $e^{\pi/4}\sqrt{2} \approx 2.1932800507 \times 1.4142135624 \approx 3.1016176731$
- $\frac{e^{\pi/4}\sqrt{2} - 1}{2} \approx \frac{3.1016176731 - 1}{2} \approx \frac{2.1016176731}{2} \approx 1.0508088366$

Therefore, the numerical approximation rounded to 10 decimal places is: 1.0508088366

{"answer": "\\frac{e^{\\pi/4}\\sqrt{2} - 1}{2}", "numerical_answer": "1.0508088366"}