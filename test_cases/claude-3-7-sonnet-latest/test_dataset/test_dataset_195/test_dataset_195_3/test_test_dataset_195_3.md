# Evaluating $\int\limits_{0}^{1}\arcsin\left(x\right)\arccos(x)dx$

I'll approach this integral by using the relationship between $\arcsin(x)$ and $\arccos(x)$.

## Step 1: Use the relationship between $\arcsin(x)$ and $\arccos(x)$

Recall that $\arcsin(x) + \arccos(x) = \frac{\pi}{2}$ for $x \in [0,1]$.

This means $\arccos(x) = \frac{\pi}{2} - \arcsin(x)$

## Step 2: Substitute this relationship into the integral

$$\int\limits_{0}^{1}\arcsin\left(x\right)\arccos(x)dx = \int\limits_{0}^{1}\arcsin\left(x\right)\left(\frac{\pi}{2} - \arcsin(x)\right)dx$$

$$= \int\limits_{0}^{1}\left[\frac{\pi}{2}\arcsin(x) - \arcsin^2(x)\right]dx$$

$$= \frac{\pi}{2}\int\limits_{0}^{1}\arcsin(x)dx - \int\limits_{0}^{1}\arcsin^2(x)dx$$

## Step 3: Evaluate each integral separately

For the first integral, $\int\arcsin(x)dx = x\arcsin(x) + \sqrt{1-x^2} + C$

So $\int\limits_{0}^{1}\arcsin(x)dx = [x\arcsin(x) + \sqrt{1-x^2}]_{0}^{1} = 1 \cdot \frac{\pi}{2} + 0 - (0 + 1) = \frac{\pi}{2} - 1$

For the second integral, let's use integration by parts.

Let $u = \arcsin^2(x)$ and $dv = dx$
Then $du = 2\arcsin(x) \cdot \frac{1}{\sqrt{1-x^2}}dx$ and $v = x$

$$\int\arcsin^2(x)dx = x\arcsin^2(x) - \int x \cdot 2\arcsin(x) \cdot \frac{1}{\sqrt{1-x^2}}dx$$

$$= x\arcsin^2(x) - 2\int \frac{x\arcsin(x)}{\sqrt{1-x^2}}dx$$

For the remaining integral, let's use substitution:
Let $t = \arcsin(x)$, then $x = \sin(t)$ and $dx = \cos(t)dt$

$$\int \frac{x\arcsin(x)}{\sqrt{1-x^2}}dx = \int \frac{\sin(t) \cdot t}{\sqrt{1-\sin^2(t)}} \cdot \cos(t)dt$$

$$= \int \frac{\sin(t) \cdot t}{\cos(t)} \cdot \cos(t)dt = \int t\sin(t)dt$$

Using integration by parts again:
Let $u = t$ and $dv = \sin(t)dt$
Then $du = dt$ and $v = -\cos(t)$

$$\int t\sin(t)dt = -t\cos(t) - \int (-\cos(t))dt = -t\cos(t) + \int \cos(t)dt$$

$$= -t\cos(t) + \sin(t) + C$$

Substituting back $t = \arcsin(x)$, we get:
$$\int \frac{x\arcsin(x)}{\sqrt{1-x^2}}dx = -\arcsin(x)\cos(\arcsin(x)) + \sin(\arcsin(x)) + C$$

$$= -\arcsin(x) \cdot \sqrt{1-x^2} + x + C$$

Now returning to our original calculation:
$$\int\arcsin^2(x)dx = x\arcsin^2(x) - 2[-\arcsin(x) \cdot \sqrt{1-x^2} + x] + C$$

$$= x\arcsin^2(x) + 2\arcsin(x) \cdot \sqrt{1-x^2} - 2x + C$$

Evaluating at the limits:
$$\int\limits_{0}^{1}\arcsin^2(x)dx = [x\arcsin^2(x) + 2\arcsin(x) \cdot \sqrt{1-x^2} - 2x]_{0}^{1}$$

At $x = 1$: $1 \cdot (\frac{\pi}{2})^2 + 2 \cdot \frac{\pi}{2} \cdot 0 - 2 \cdot 1 = \frac{\pi^2}{4} - 2$

At $x = 0$: $0 + 0 - 0 = 0$

Therefore, $\int\limits_{0}^{1}\arcsin^2(x)dx = \frac{\pi^2}{4} - 2$

## Step 4: Combine the results

$$\int\limits_{0}^{1}\arcsin\left(x\right)\arccos(x)dx = \frac{\pi}{2}\int\limits_{0}^{1}\arcsin(x)dx - \int\limits_{0}^{1}\arcsin^2(x)dx$$

$$= \frac{\pi}{2} \cdot (\frac{\pi}{2} - 1) - (\frac{\pi^2}{4} - 2)$$

$$= \frac{\pi^2}{4} - \frac{\pi}{2} - \frac{\pi^2}{4} + 2$$

$$= 2 - \frac{\pi}{2}$$

## Step 5: Calculate the numerical approximation

$2 - \frac{\pi}{2} = 2 - 1.5707963268 = 0.4292036732$

Therefore, the value of the integral is $2 - \frac{\pi}{2} \approx 0.4292036732$.

{"answer": "2 - \\frac{\\pi}{2}", "numerical_answer": "0.4292036732"}