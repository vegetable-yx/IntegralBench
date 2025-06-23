To evaluate the definite integral  
$$
\int_0^2 x \arctan\left(\sqrt{x(2 - x)}\right) dx,
$$  
we proceed through a series of carefully chosen substitutions and analytical techniques.

---

### **Step 1: Simplify the Square Root Expression**

The expression inside the square root, $ x(2 - x) $, simplifies to:
$$
x(2 - x) = 2x - x^2 = 1 - (x - 1)^2.
$$
Thus, the square root becomes:
$$
\sqrt{x(2 - x)} = \sqrt{1 - (x - 1)^2}.
$$
This suggests a substitution centered at $ x = 1 $, which simplifies the integrand.

---

### **Step 2: Substitution to Exploit Symmetry**

Let:
$$
t = x - 1 \quad \Rightarrow \quad x = t + 1, \quad dx = dt.
$$
When $ x = 0 $, $ t = -1 $; and when $ x = 2 $, $ t = 1 $. The integral becomes:
$$
\int_0^2 x \arctan\left(\sqrt{1 - (x - 1)^2}\right) dx = \int_{-1}^1 (t + 1) \arctan\left(\sqrt{1 - t^2}\right) dt.
$$

Now split the integral:
$$
\int_{-1}^1 (t + 1) \arctan\left(\sqrt{1 - t^2}\right) dt = \int_{-1}^1 t \arctan\left(\sqrt{1 - t^2}\right) dt + \int_{-1}^1 \arctan\left(\sqrt{1 - t^2}\right) dt.
$$

Note that $ \arctan(\sqrt{1 - t^2}) $ is an even function, and $ t $ is odd. Therefore, the first integral over $ [-1, 1] $ is zero due to symmetry.

Thus, the integral reduces to:
$$
\int_{-1}^1 \arctan\left(\sqrt{1 - t^2}\right) dt = 2 \int_0^1 \arctan\left(\sqrt{1 - t^2}\right) dt.
$$

---

### **Step 3: Trigonometric Substitution**

Let:
$$
t = \sin\theta \quad \Rightarrow \quad dt = \cos\theta\, d\theta, \quad \sqrt{1 - t^2} = \cos\theta.
$$
When $ t = 0 $, $ \theta = 0 $; and when $ t = 1 $, $ \theta = \frac{\pi}{2} $. The integral becomes:
$$
2 \int_0^1 \arctan\left(\sqrt{1 - t^2}\right) dt = 2 \int_0^{\pi/2} \arctan(\cos\theta) \cdot \cos\theta\, d\theta.
$$

---

### **Step 4: Integration by Parts**

Let:
- $ u = \arctan(\cos\theta) \Rightarrow du = \frac{-\sin\theta}{1 + \cos^2\theta} d\theta $,
- $ dv = \cos\theta\, d\theta \Rightarrow v = \sin\theta $.

Then:
$$
\int \arctan(\cos\theta) \cos\theta\, d\theta = \arctan(\cos\theta)\sin\theta - \int \sin\theta \cdot \left( \frac{-\sin\theta}{1 + \cos^2\theta} \right) d\theta.
$$
$$
= \arctan(\cos\theta)\sin\theta + \int \frac{\sin^2\theta}{1 + \cos^2\theta} d\theta.
$$

Evaluate the boundary terms:
- At $ \theta = 0 $, $ \cos\theta = 1 $, $ \sin\theta = 0 $, so the term is 0.
- At $ \theta = \frac{\pi}{2} $, $ \cos\theta = 0 $, $ \sin\theta = 1 $, so the term is 0.

Thus, the integral becomes:
$$
\int_0^{\pi/2} \frac{\sin^2\theta}{1 + \cos^2\theta