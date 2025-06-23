# Evaluating $\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\:dx$

## Step 1: Use the product-to-sum formula

I'll use the trigonometric identity:
$$\cos(a)\sin(b) = \frac{1}{2}[\sin(b+a) - \sin(b-a)]$$

With $a = 20x$ and $b = 25x$:
$$\cos(20x)\sin(25x) = \frac{1}{2}[\sin(45x) - \sin(5x)]$$

## Step 2: Rewrite the integral

$$\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\:dx = \frac{1}{2}\int_{-\pi/2}^{\pi/2}[\sin(45x) - \sin(5x)]\:dx$$

## Step 3: Split the integral

$$\frac{1}{2}\int_{-\pi/2}^{\pi/2}\sin(45x)\:dx - \frac{1}{2}\int_{-\pi/2}^{\pi/2}\sin(5x)\:dx$$

## Step 4: Solve each integral

For the first integral:
$$\frac{1}{2}\int_{-\pi/2}^{\pi/2}\sin(45x)\:dx = \frac{1}{2}\left[-\frac{\cos(45x)}{45}\right]_{-\pi/2}^{\pi/2}$$

At the limits:
- When $x = \pi/2$: $\cos(45\pi/2) = \cos(45\pi/2)$
- When $x = -\pi/2$: $\cos(45(-\pi/2)) = \cos(-45\pi/2) = \cos(45\pi/2)$

Since $\cos$ is an even function, the values at the upper and lower limits are equal, so:
$$\frac{1}{2}\left[-\frac{\cos(45\pi/2)}{45} + \frac{\cos(45\pi/2)}{45}\right] = 0$$

For the second integral:
$$\frac{1}{2}\int_{-\pi/2}^{\pi/2}\sin(5x)\:dx = \frac{1}{2}\left[-\frac{\cos(5x)}{5}\right]_{-\pi/2}^{\pi/2}$$

At the limits:
- When $x = \pi/2$: $\cos(5\pi/2) = \cos(\pi/2 + 2\pi) = \cos(\pi/2) = 0$
- When $x = -\pi/2$: $\cos(5(-\pi/2)) = \cos(-5\pi/2) = \cos(-\pi/2 - 2\pi) = \cos(-\pi/2) = 0$

Therefore:
$$\frac{1}{2}\left[-\frac{0}{5} + \frac{0}{5}\right] = 0$$

## Step 5: Calculate the final result

The definite integral is:
$$\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\:dx = 0 - 0 = 0$$

## Numerical approximation
The numerical value rounded to 10 decimal places is 0.0000000000.

{"answer": "0", "numerical_answer": "0.0000000000"}