# Evaluating $\int\limits_{0}^{2.0}x^{1/2}(2.0-x)^{-1/2}\arcsin(0.5\sqrt{x(2.0-x)})\:dx$

## Step 1: Make a substitution to simplify the integral

Let's try the substitution $x = 2\sin^2(t)$ for $0 \leq t \leq \pi/2$. This gives:
- $dx = 4\sin(t)\cos(t)\,dt = 2\sin(2t)\,dt$
- When $x = 0$, $t = 0$
- When $x = 2$, $t = \pi/2$

Now let's compute the transformed terms:
- $x^{1/2} = (2\sin^2(t))^{1/2} = \sqrt{2}\sin(t)$
- $(2.0-x)^{-1/2} = (2-2\sin^2(t))^{-1/2} = (2\cos^2(t))^{-1/2} = \frac{1}{\sqrt{2}|\cos(t)|} = \frac{1}{\sqrt{2}\cos(t)}$ since $0 \leq t \leq \pi/2$

Now for the arcsin term:
$\arcsin(0.5\sqrt{x(2.0-x)}) = \arcsin(0.5\sqrt{2\sin^2(t) \cdot 2\cos^2(t)}) = \arcsin(\sin(t)\cos(t)) = \arcsin(\frac{\sin(2t)}{2})$

For $0 \leq t \leq \pi/2$, we have $0 \leq \sin(2t) \leq 1$, so $\arcsin(\frac{\sin(2t)}{2}) = \arcsin(\frac{\sin(2t)}{2})$

## Step 2: Substitute all terms and simplify

The integral becomes:
$$\int_{0}^{\pi/2} \sqrt{2}\sin(t) \cdot \frac{1}{\sqrt{2}\cos(t)} \cdot \arcsin(\frac{\sin(2t)}{2}) \cdot 2\sin(2t)\,dt$$

This simplifies to:
$$\int_{0}^{\pi/2} 2\sin(t) \cdot \frac{1}{\cos(t)} \cdot \arcsin(\frac{\sin(2t)}{2}) \cdot \sin(2t)\,dt$$

Using $\sin(2t) = 2\sin(t)\cos(t)$:
$$\int_{0}^{\pi/2} 2\sin(t) \cdot \frac{1}{\cos(t)} \cdot \arcsin(\sin(t)\cos(t)) \cdot 2\sin(t)\cos(t)\,dt$$

$$\int_{0}^{\pi/2} 4\sin^2(t) \cdot \arcsin(\sin(t)\cos(t))\,dt$$

## Step 3: Further manipulation of the arcsin term

For $0 \leq t \leq \pi/2$, we can simplify $\arcsin(\sin(t)\cos(t))$ as follows:

Since $\sin(t)\cos(t) = \frac{\sin(2t)}{2}$ and for $0 \leq t \leq \pi/2$, we have $0 \leq 2t \leq \pi$, so $\sin(2t)$ increases from 0 to 1 and then decreases back to 0.

This means $0 \leq \frac{\sin(2t)}{2} \leq \frac{1}{2}$, and $\arcsin(\frac{\sin(2t)}{2}) = t$ for $0 \leq t \leq \frac{\pi}{4}$, and $\arcsin(\frac{\sin(2t)}{2}) = \frac{\pi}{2} - t$ for $\frac{\pi}{4} \leq t \leq \frac{\pi}{2}$.

Let's split the integral:
$$\int_{0}^{\pi/4} 4\sin^2(t) \cdot t\,dt + \int_{\pi/4}^{\pi/2} 4\sin^2(t) \cdot (\frac{\pi}{2} - t)\,dt$$

## Step 4: Evaluate each part

Using the identity $\sin^2(t) = \frac{1-\cos(2t)}{2}$:

First integral:
$$\int_{0}^{\pi/4} 4\sin^2(t) \cdot t\,dt = \int_{0}^{\pi/4} 4 \cdot \frac{1-\cos(2t)}{2} \cdot t\,dt = \int_{0}^{\pi/4} 2(1-\cos(2t))t\,dt$$

$$= 2\int_{0}^{\pi/4} t\,dt - 2\int_{0}^{\pi/4} t\cos(2t)\,dt$$

Second integral:
$$\int_{\pi/4}^{\pi/2} 4\sin^2(t) \cdot (\frac{\pi}{2} - t)\,dt = \int_{\pi/4}^{\pi/2} 2(1-\cos(2t))(\frac{\pi}{2} - t)\,dt$$

$$= 2\int_{\pi/4}^{\pi/2} (\frac{\pi}{2} - t)\,dt - 2\int_{\pi/4}^{\pi/2} (\frac{\pi}{2} - t)\cos(2t)\,dt$$

After evaluating all these integrals and combining the results, we get:

$$\int_{0}^{2.0}x^{1/2}(2.0-x)^{-1/2}\arcsin(0.5\sqrt{x(2.0-x)})\:dx = \frac{\pi^2}{8}$$

## Numerical approximation
$\frac{\pi^2}{8} \approx 1.2337005501$

{"answer": "\\frac{\\pi^2}{8}", "numerical_answer": "1.2337005501"}