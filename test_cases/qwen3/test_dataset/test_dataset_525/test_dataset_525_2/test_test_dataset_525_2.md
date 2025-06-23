To evaluate the definite integral  
$$
\int_{1/\sqrt{2}}^1 \frac{\arcsin(x)}{x^3} \, dx,
$$
we proceed using **integration by parts**, which is suitable for integrals involving products of functions like inverse trigonometric and algebraic functions.

---

### **Step 1: Integration by Parts**

Let:
- $ u = \arcsin(x) \Rightarrow du = \frac{1}{\sqrt{1 - x^2}} \, dx $,
- $ dv = x^{-3} \, dx \Rightarrow v = -\frac{1}{2x^2} $.

Then, applying the integration by parts formula:
$$
\int u \, dv = uv - \int v \, du,
$$
we get:
$$
\int_{1/\sqrt{2}}^1 \frac{\arcsin(x)}{x^3} \, dx = \left[ -\frac{\arcsin(x)}{2x^2} \right]_{1/\sqrt{2}}^1 + \frac{1}{2} \int_{1/\sqrt{2}}^1 \frac{1}{x^2 \sqrt{1 - x^2}} \, dx.
$$

---

### **Step 2: Evaluate the Boundary Terms**

At $ x = 1 $:
- $ \arcsin(1) = \frac{\pi}{2} $,
- $ x^2 = 1 $,
- So, $ -\frac{\arcsin(1)}{2x^2} = -\frac{\pi}{4} $.

At $ x = \frac{1}{\sqrt{2}} $:
- $ \arcsin\left(\frac{1}{\sqrt{2}}\right) = \frac{\pi}{4} $,
- $ x^2 = \frac{1}{2} $,
- So, $ -\frac{\arcsin\left(\frac{1}{\sqrt{2}}\right)}{2x^2} = -\frac{\pi}{4} $.

Thus, the boundary term becomes:
$$
\left[ -\frac{\arcsin(x)}{2x^2} \right]_{1/\sqrt{2}}^1 = -\frac{\pi}{4} - \left( -\frac{\pi}{4} \right) = 0.
$$

---

### **Step 3: Evaluate the Remaining Integral**

We now compute:
$$
\frac{1}{2} \int_{1/\sqrt{2}}^1 \frac{1}{x^2 \sqrt{1 - x^2}} \, dx.
$$

Let’s use the substitution $ x = \sin\theta $, so:
- $ dx = \cos\theta \, d\theta $,
- $ \sqrt{1 - x^2} = \cos\theta $,
- $ x^2 = \sin^2\theta $.

Limits:
- When $ x = \frac{1}{\sqrt{2}} $, $ \theta = \frac{\pi}{4} $,
- When $ x = 1 $, $ \theta = \frac{\pi}{2} $.

So the integral becomes:
$$
\frac{1}{2} \int_{\pi/4}^{\pi/2} \frac{\cos\theta}{\sin^2\theta \cdot \cos\theta} \, d\theta = \frac{1}{2} \int_{\pi/4}^{\pi/2} \csc^2\theta \, d\theta.
$$

The integral of $ \csc^2\theta $ is $ -\cot\theta $, so:
$$
\frac{1}{2} \left[ -\cot\theta \right]_{\pi/4}^{\pi/2} = \frac{1}{2} \left( -\cot\left(\frac{\pi}{2}\right) + \cot\left(\frac{\pi}{4}\right) \right).
$$

Since $ \cot\left(\frac{\pi}{2}\right) = 0 $ and $ \cot\left(\frac{\pi}{4}\right) = 1 $, we get:
$$
\frac{1}{2} (0 + 1) = \frac{1}{2}.
$$

---

### **Step 4: Final Answer and Numerical Approximation**

Thus, the exact value of the integral is:
$$
\boxed{\frac{1}{2}}.
$$