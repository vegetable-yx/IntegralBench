# Evaluating $\int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx$

## Step 1: Set up a substitution
Let's start by setting $t = \frac{\pi}{2} - x$. When $x = 0$, $t = \frac{\pi}{2}$, and when $x = \frac{\pi}{2}$, $t = 0$.

Under this substitution:
- $\sin x = \cos t$
- $\cos x = \sin t$
- $dx = -dt$

## Step 2: Transform the integral
Applying this substitution:

$$\int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx = \int\limits_{\pi/2}^{0}\frac{\cos^{2n}t}{\cos^{2n}t+\sin^{2n}t}\:(-dt) = \int\limits_{0}^{\pi/2}\frac{\cos^{2n}t}{\cos^{2n}t+\sin^{2n}t}\:dt$$

## Step 3: Add the original and transformed integrals
Now we have:

$$\int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx + \int\limits_{0}^{\pi/2}\frac{\cos^{2n}t}{\cos^{2n}t+\sin^{2n}t}\:dt$$

Since $t$ is just a dummy variable, we can rewrite the second integral using $x$:

$$\int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx + \int\limits_{0}^{\pi/2}\frac{\cos^{2n}x}{\cos^{2n}x+\sin^{2n}x}\:dx$$

This simplifies to:

$$\int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx + \int\limits_{0}^{\pi/2}\frac{\cos^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx = \int\limits_{0}^{\pi/2}\frac{\sin^{2n}x + \cos^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx = \int\limits_{0}^{\pi/2}1\:dx = \frac{\pi}{2}$$

## Step 4: Solve for our original integral
Since the sum of our original integral and the transformed integral equals $\frac{\pi}{2}$, and they are equal to each other by symmetry, we have:

$$2 \cdot \int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx = \frac{\pi}{2}$$

Therefore:

$$\int\limits_{0}^{\pi/2}\frac{\sin^{2n}x}{\sin^{2n}x+\cos^{2n}x}\:dx = \frac{\pi}{4}$$

## Step 5: Numerical approximation
The exact answer is $\frac{\pi}{4}$, which numerically equals:

$$\frac{\pi}{4} \approx 0.7853981634$$

## Final Answer

{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}