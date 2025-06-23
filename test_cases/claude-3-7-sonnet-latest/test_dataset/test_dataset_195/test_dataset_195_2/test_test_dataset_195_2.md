# Evaluating $\int_{0}^{1}\arcsin(x)\arccos(x)dx$

I'll compute this definite integral step by step.

## Step 1: Set up substitutions
Note that $\arccos(x) = \frac{\pi}{2} - \arcsin(x)$ for $x \in [0,1]$

## Step 2: Substitute into the integral
$$\int_{0}^{1}\arcsin(x)\arccos(x)dx = \int_{0}^{1}\arcsin(x)\left(\frac{\pi}{2} - \arcsin(x)\right)dx$$

$$= \int_{0}^{1}\left[\frac{\pi}{2}\arcsin(x) - \arcsin^2(x)\right]dx$$

$$= \frac{\pi}{2}\int_{0}^{1}\arcsin(x)dx - \int_{0}^{1}\arcsin^2(x)dx$$

## Step 3: Evaluate each part separately

### Part 1: $\frac{\pi}{2}\int_{0}^{1}\arcsin(x)dx$
For this part, I'll use integration by parts with:
- $u = \arcsin(x)$
- $dv = dx$
- $du = \frac{1}{\sqrt{1-x^2}}dx$
- $v = x$

$$\int\arcsin(x)dx = x\arcsin(x) - \int\frac{x}{\sqrt{1-x^2}}dx$$

To evaluate $\int\frac{x}{\sqrt{1-x^2}}dx$, I'll substitute $x = \sin t$, which gives $dx = \cos t \, dt$:
$$\int\frac{x}{\sqrt{1-x^2}}dx = \int\frac{\sin t}{\sqrt{1-\sin^2 t}}\cos t \, dt = \int\frac{\sin t}{\cos t}\cos t \, dt = \int\sin t \, dt = -\cos t = -\sqrt{1-x^2}$$

Therefore:
$$\int\arcsin(x)dx = x\arcsin(x) + \sqrt{1-x^2} + C$$

Evaluating at the bounds:
$$\left[x\arcsin(x) + \sqrt{1-x^2}\right]_{0}^{1} = 1 \cdot \frac{\pi}{2} + 0 - 0 \cdot 0 - 1 = \frac{\pi}{2} - 1$$

So $\frac{\pi}{2}\int_{0}^{1}\arcsin(x)dx = \frac{\pi}{2} \cdot \left(\frac{\pi}{2} - 1\right) = \frac{\pi^2}{4} - \frac{\pi}{2}$

### Part 2: $\int_{0}^{1}\arcsin^2(x)dx$
For this part, I'll use integration by parts with:
- $u = \arcsin^2(x)$
- $dv = dx$
- $du = 2\arcsin(x) \cdot \frac{1}{\sqrt{1-x^2}}dx$
- $v = x$

$$\int\arcsin^2(x)dx = x\arcsin^2(x) - \int 2x\arcsin(x)\frac{1}{\sqrt{1-x^2}}dx$$

Let's simplify the remaining integral:
$$\int 2x\arcsin(x)\frac{1}{\sqrt{1-x^2}}dx$$

I'll use the substitution $t = \arcsin(x)$, which gives $x = \sin t$ and $dx = \cos t \, dt$:
$$\int 2x\arcsin(x)\frac{1}{\sqrt{1-x^2}}dx = \int 2\sin t \cdot t \cdot \frac{1}{\cos t} \cdot \cos t \, dt = \int 2t\sin t \, dt$$

Integrating by parts again with $u = t$ and $dv = 2\sin t \, dt$:
$$\int 2t\sin t \, dt = -2t\cos t + \int 2\cos t \, dt = -2t\cos t + 2\sin t + C$$

Substituting back:
$$\int 2t\sin t \, dt = -2\arcsin(x)\cos(\arcsin(x)) + 2\sin(\arcsin(x)) + C$$

Since $\cos(\arcsin(x)) = \sqrt{1-x^2}$ and $\sin(\arcsin(x)) = x$:
$$\int 2t\sin t \, dt = -2\arcsin(x)\sqrt{1-x^2} + 2x + C$$

Therefore:
$$\int\arcsin^2(x)dx = x\arcsin^2(x) + 2\arcsin(x)\sqrt{1-x^2} - 2x + C$$

Evaluating at the bounds:
$$\left[x\arcsin^2(x) + 2\arcsin(x)\sqrt{1-x^2} - 2x\right]_{0}^{1}$$
$$= 1 \cdot \left(\frac{\pi}{2}\right)^2 + 2\cdot\frac{\pi}{2}\cdot 0 - 2 \cdot 1 - 0 \cdot 0 - 2 \cdot 0 \cdot 1 + 2 \cdot 0$$
$$= \frac{\pi^2}{4} - 2$$

## Step 4: Combine the results
$$\int_{0}^{1}\arcsin(x)\arccos(x)dx = \frac{\pi}{2}\int_{0}^{1}\arcsin(x)dx - \int_{0}^{1}\arcsin^2(x)dx$$
$$= \left(\frac{\pi^2}{4} - \frac{\pi}{2}\right) - \left(\frac{\pi^2}{4} - 2\right)$$
$$= \frac{\pi^2}{4} - \frac{\pi}{2} - \frac{\pi^2}{4} + 2$$
$$= 2 - \frac{\pi}{2}$$

## Step 5: Numerical approximation
$2 - \frac{\pi}{2} \approx 2 - 1.5707963268 \approx 0.4292036732$

{"answer": "2 - \\frac{\\pi}{2}", "numerical_answer": "0.4292036732"}