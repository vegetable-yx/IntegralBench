# Evaluating $\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\:dx$

I'll use the trigonometric product-to-sum identity:
$$\cos(a)\sin(b) = \frac{1}{2}[\sin(b+a) - \sin(b-a)]$$

## Step 1: Apply the trigonometric identity
$$\cos(20x)\sin(25x) = \frac{1}{2}[\sin(25x+20x) - \sin(25x-20x)]$$
$$= \frac{1}{2}[\sin(45x) - \sin(5x)]$$

## Step 2: Rewrite the integral
$$\int_{-\pi/2}^{\pi/2}\cos(20x)\sin(25x)\:dx = \frac{1}{2}\int_{-\pi/2}^{\pi/2}[\sin(45x) - \sin(5x)]\:dx$$

## Step 3: Split the integral
$$\frac{1}{2}\int_{-\pi/2}^{\pi/2}\sin(45x)\:dx - \frac{1}{2}\int_{-\pi/2}^{\pi/2}\sin(5x)\:dx$$

## Step 4: Solve each integral
For the first integral:
$$\int\sin(45x)\:dx = -\frac{\cos(45x)}{45} + C_1$$

For the second integral:
$$\int\sin(5x)\:dx = -\frac{\cos(5x)}{5} + C_2$$

## Step 5: Apply the limits
$$\frac{1}{2}\left[-\frac{\cos(45x)}{45}\right]_{-\pi/2}^{\pi/2} - \frac{1}{2}\left[-\frac{\cos(5x)}{5}\right]_{-\pi/2}^{\pi/2}$$

$$= \frac{1}{2}\left[-\frac{\cos(45\pi/2)}{45} + \frac{\cos(-45\pi/2)}{45}\right] - \frac{1}{2}\left[-\frac{\cos(5\pi/2)}{5} + \frac{\cos(-5\pi/2)}{5}\right]$$

Since $\cos(-\theta) = \cos(\theta)$, we can simplify:
$$= \frac{1}{2}\left[-\frac{\cos(45\pi/2)}{45} + \frac{\cos(45\pi/2)}{45}\right] - \frac{1}{2}\left[-\frac{\cos(5\pi/2)}{5} + \frac{\cos(5\pi/2)}{5}\right]$$

Both terms cancel out to zero:
$$= \frac{1}{2}[0] - \frac{1}{2}[0] = 0$$

## Step 6: Numerical approximation
The exact answer is 0, which gives a numerical approximation of 0.0000000000 (rounded to 10 decimal places).

{"answer": "0", "numerical_answer": "0.0000000000"}