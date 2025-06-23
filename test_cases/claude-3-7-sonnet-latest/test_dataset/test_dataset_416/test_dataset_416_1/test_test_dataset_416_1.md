# Computing $\int_0^1\frac{e^{\arctan(x)}}{(x^2+1)^{3/2}}\text{ dx}$

Let's approach this integral step by step.

## Step 1: Substitution

Let's use the substitution $u = \arctan(x)$. From this, we have:
- $x = \tan(u)$
- $dx = \sec^2(u) \, du$
- When $x = 0$, $u = \arctan(0) = 0$
- When $x = 1$, $u = \arctan(1) = \frac{\pi}{4}$

Also, note that $x^2 + 1 = \tan^2(u) + 1 = \sec^2(u)$, so $(x^2 + 1)^{3/2} = (\sec^2(u))^{3/2} = \sec^3(u)$

## Step 2: Rewrite the integral

Substituting these into our integral:

$$\int_0^1\frac{e^{\arctan(x)}}{(x^2+1)^{3/2}}\text{ dx} = \int_0^{\pi/4}\frac{e^u}{\sec^3(u)} \cdot \sec^2(u) \, du = \int_0^{\pi/4}e^u \cdot \cos(u) \, du$$

This is because $\frac{1}{\sec^3(u)} \cdot \sec^2(u) = \frac{1}{\sec(u)} = \cos(u)$

## Step 3: Integration by parts

Now we use integration by parts with $f(u) = e^u$ and $g'(u) = \cos(u)$:

$$\int e^u \cos(u) \, du = e^u \sin(u) - \int e^u \sin(u) \, du$$

Let's apply integration by parts again with $f(u) = e^u$ and $g'(u) = \sin(u)$:

$$\int e^u \sin(u) \, du = -e^u \cos(u) + \int e^u \cos(u) \, du$$

Let's define $I = \int e^u \cos(u) \, du$. Then:

$$I = e^u \sin(u) - (-e^u \cos(u) + I)$$

Solving for $I$:

$$2I = e^u \sin(u) + e^u \cos(u)$$

$$I = \frac{e^u(\sin(u) + \cos(u))}{2}$$

## Step 4: Apply the limits

Now, we evaluate our original integral:

$$\int_0^{\pi/4}e^u \cdot \cos(u) \, du = \left[ \frac{e^u(\sin(u) + \cos(u))}{2} \right]_0^{\pi/4}$$

At $u = 0$: $\sin(0) = 0$ and $\cos(0) = 1$, so we get $\frac{e^0 \cdot 1}{2} = \frac{1}{2}$

At $u = \frac{\pi}{4}$: $\sin(\frac{\pi}{4}) = \frac{1}{\sqrt{2}}$ and $\cos(\frac{\pi}{4}) = \frac{1}{\sqrt{2}}$, so we get:
$$\frac{e^{\pi/4}(\frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}})}{2} = \frac{e^{\pi/4} \cdot \frac{2}{\sqrt{2}}}{2} = \frac{e^{\pi/4}}{\sqrt{2}}$$

## Step 5: Final result

$$\int_0^1\frac{e^{\arctan(x)}}{(x^2+1)^{3/2}}\text{ dx} = \frac{e^{\pi/4}}{\sqrt{2}} - \frac{1}{2} = \frac{e^{\pi/4}}{\sqrt{2}} - \frac{1}{2}$$

The exact answer is $\frac{e^{\pi/4}}{\sqrt{2}} - \frac{1}{2}$

## Numerical approximation

To calculate this numerically:
- $\frac{\pi}{4} \approx 0.7853981634$
- $e^{\pi/4} \approx 2.1932800508$
- $\frac{e^{\pi/4}}{\sqrt{2}} \approx 1.5508456944$
- $\frac{e^{\pi/4}}{\sqrt{2}} - \frac{1}{2} \approx 1.0508456944$

Rounded to 10 decimal places: 1.0508456944

{"answer": "\\frac{e^{\\pi/4}}{\\sqrt{2}} - \\frac{1}{2}", "numerical_answer": "1.0508456944"}