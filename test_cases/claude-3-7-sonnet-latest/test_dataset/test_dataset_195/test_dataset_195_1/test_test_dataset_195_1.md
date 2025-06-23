# Evaluating $\int\limits_{0}^{1}\arcsin(x)\arccos(x)dx$

## Step 1: Substitute $\arccos(x) = \frac{\pi}{2} - \arcsin(x)$

Let's rewrite the integral:
$$\int\limits_{0}^{1}\arcsin(x)\arccos(x)dx = \int\limits_{0}^{1}\arcsin(x) \left(\frac{\pi}{2} - \arcsin(x)\right)dx$$

Distributing:
$$\int\limits_{0}^{1}\arcsin(x) \cdot \frac{\pi}{2}dx - \int\limits_{0}^{1}\arcsin^2(x)dx$$

## Step 2: Let's evaluate each integral separately

### For $\int\limits_{0}^{1}\arcsin(x) \cdot \frac{\pi}{2}dx$:
$$\frac{\pi}{2}\int\limits_{0}^{1}\arcsin(x)dx$$

To evaluate $\int\arcsin(x)dx$, we use integration by parts:
Let $u = \arcsin(x)$ and $dv = dx$
Then $du = \frac{1}{\sqrt{1-x^2}}dx$ and $v = x$

$$\int\arcsin(x)dx = x\arcsin(x) - \int\frac{x}{\sqrt{1-x^2}}dx$$

The integral $\int\frac{x}{\sqrt{1-x^2}}dx$ can be evaluated with the substitution $x = \sin(t)$, which gives $-\sqrt{1-x^2}$.

Therefore:
$$\int\arcsin(x)dx = x\arcsin(x) + \sqrt{1-x^2} + C$$

Evaluating from 0 to 1:
$$\left[x\arcsin(x) + \sqrt{1-x^2}\right]_0^1 = 1 \cdot \frac{\pi}{2} + 0 - (0 \cdot 0 + 1) = \frac{\pi}{2} - 1$$

So $\frac{\pi}{2}\int\limits_{0}^{1}\arcsin(x)dx = \frac{\pi}{2} \cdot \left(\frac{\pi}{2} - 1\right) = \frac{\pi^2}{4} - \frac{\pi}{2}$

### For $\int\limits_{0}^{1}\arcsin^2(x)dx$:

We can use integration by parts:
Let $u = \arcsin^2(x)$ and $dv = dx$
Then $du = 2\arcsin(x) \cdot \frac{1}{\sqrt{1-x^2}}dx$ and $v = x$

$$\int\arcsin^2(x)dx = x\arcsin^2(x) - \int 2x\arcsin(x) \cdot \frac{1}{\sqrt{1-x^2}}dx$$

For the second integral, let's substitute $x = \sin(t)$, then $dx = \cos(t)dt$ and $\arcsin(x) = t$:

$$\int 2x\arcsin(x) \cdot \frac{1}{\sqrt{1-x^2}}dx = \int 2\sin(t) \cdot t \cdot \frac{1}{\cos(t)} \cdot \cos(t)dt = \int 2t\sin(t)dt$$

Using integration by parts again:
$$\int t\sin(t)dt = -t\cos(t) + \int\cos(t)dt = -t\cos(t) + \sin(t) + C$$

Therefore:
$$\int 2t\sin(t)dt = -2t\cos(t) + 2\sin(t) + C$$

Substituting back:
$$\int\arcsin^2(x)dx = x\arcsin^2(x) + 2\sqrt{1-x^2}\arcsin(x) - 2x + C$$

Evaluating from 0 to 1:
$$\left[x\arcsin^2(x) + 2\sqrt{1-x^2}\arcsin(x) - 2x\right]_0^1 = 1 \cdot \frac{\pi^2}{4} + 0 - 2 - (0 + 0 - 0) = \frac{\pi^2}{4} - 2$$

## Step 3: Combining the results

$$\int\limits_{0}^{1}\arcsin(x)\arccos(x)dx = \frac{\pi^2}{4} - \frac{\pi}{2} - \left(\frac{\pi^2}{4} - 2\right) = \frac{\pi^2}{4} - \frac{\pi}{2} - \frac{\pi^2}{4} + 2 = 2 - \frac{\pi}{2}$$

## Step 4: Numerical approximation
$2 - \frac{\pi}{2} = 2 - 1.5707963268 = 0.4292036732$

Therefore, $\int\limits_{0}^{1}\arcsin(x)\arccos(x)dx = 2 - \frac{\pi}{2}$.

{"answer": "2 - \\frac{\\pi}{2}", "numerical_answer": "0.4292036732"}