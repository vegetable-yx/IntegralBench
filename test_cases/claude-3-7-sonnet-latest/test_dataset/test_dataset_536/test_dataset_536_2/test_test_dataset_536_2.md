# Evaluating $\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\:dx$

I'll use the product-to-sum identity for trigonometric functions:

$$\cos(a)\sin(b) = \frac{1}{2}[\sin(b+a) - \sin(b-a)]$$

Applying this identity with $a = 20x$ and $b = 25x$:

$$\cos(20x)\sin(25x) = \frac{1}{2}[\sin(25x+20x) - \sin(25x-20x)] = \frac{1}{2}[\sin(45x) - \sin(5x)]$$

So the integral becomes:

$$\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\:dx = \frac{1}{2}\int_{-\pi/2}^{\pi/2}[\sin(45x) - \sin(5x)]\:dx$$

Let's evaluate each part separately:

1. For $\int_{-\pi/2}^{\pi/2}\sin(45x)\:dx$:
   $$\int\sin(45x)\:dx = -\frac{1}{45}\cos(45x) + C$$
   
   Evaluating at the bounds:
   $$\left[-\frac{1}{45}\cos(45x)\right]_{-\pi/2}^{\pi/2} = -\frac{1}{45}\cos\left(45 \cdot \frac{\pi}{2}\right) + \frac{1}{45}\cos\left(45 \cdot \left(-\frac{\pi}{2}\right)\right)$$
   
   Since $45 \cdot \frac{\pi}{2} = \frac{45\pi}{2}$ and $\cos\left(\frac{45\pi}{2}\right) = \cos\left(\frac{-45\pi}{2}\right)$, we get:
   $$-\frac{1}{45}\cos\left(\frac{45\pi}{2}\right) + \frac{1}{45}\cos\left(\frac{-45\pi}{2}\right) = 0$$

2. For $\int_{-\pi/2}^{\pi/2}\sin(5x)\:dx$:
   $$\int\sin(5x)\:dx = -\frac{1}{5}\cos(5x) + C$$
   
   Evaluating at the bounds:
   $$\left[-\frac{1}{5}\cos(5x)\right]_{-\pi/2}^{\pi/2} = -\frac{1}{5}\cos\left(5 \cdot \frac{\pi}{2}\right) + \frac{1}{5}\cos\left(5 \cdot \left(-\frac{\pi}{2}\right)\right)$$
   
   Since $5 \cdot \frac{\pi}{2} = \frac{5\pi}{2}$ and $\cos\left(\frac{5\pi}{2}\right) = \cos\left(\frac{-5\pi}{2}\right) = 0$, we get:
   $$-\frac{1}{5}\cos\left(\frac{5\pi}{2}\right) + \frac{1}{5}\cos\left(\frac{-5\pi}{2}\right) = 0$$

Therefore:
$$\frac{1}{2}\int_{-\pi/2}^{\pi/2}[\sin(45x) - \sin(5x)]\:dx = \frac{1}{2}(0 - 0) = 0$$

The exact value of the definite integral is 0.

## Numerical Approximation
The numerical approximation is simply 0.0000000000 (10 decimal places).

{"answer": "0", "numerical_answer": "0.0000000000"}