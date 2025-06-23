To evaluate the definite integral

$$
\int_{0}^{7}\left(\sqrt[3]{\sqrt{x^{2}+1}+x}-\sqrt[3]{\sqrt{x^{2}+1}-x}\right)\:\mathrm{d}x,
$$

we begin by analyzing the structure of the integrand. Let us define:

- $ u = \sqrt[3]{\sqrt{x^2 + 1} + x} $,
- $ v = \sqrt[3]{\sqrt{x^2 + 1} - x} $.

Then the integrand becomes $ u - v $.

---

### Step 1: Key Identity

We observe that:

$$
u^3 = \sqrt{x^2 + 1} + x,\quad v^3 = \sqrt{x^2 + 1} - x.
$$

Adding and subtracting these:

$$
u^3 + v^3 = 2\sqrt{x^2 + 1},\quad u^3 - v^3 = 2x.
$$

Also, multiplying $ u $ and $ v $:

$$
uv = \sqrt[3]{(\sqrt{x^2 + 1} + x)(\sqrt{x^2 + 1} - x)} = \sqrt[3]{x^2 + 1 - x^2} = \sqrt[3]{1} = 1.
$$

Thus, $ v = \frac{1}{u} $, and the integrand becomes:

$$
u - v = u - \frac{1}{u}.
$$

---

### Step 2: Substitution and Simplification

Let us now consider the substitution $ u = \sqrt[3]{\sqrt{x^2 + 1} + x} $, which implies:

$$
u^3 = \sqrt{x^2 + 1} + x \Rightarrow x = \frac{u^3 - u^{-3}}{2}.
$$

Differentiating both sides with respect to $ u $:

$$
dx = \frac{d}{du} \left( \frac{u^3 - u^{-3}}{2} \right) du = \frac{3(u^2 + u^{-4})}{2} du.
$$

Now the integral becomes:

$$
\int_{u=1}^{u=U} \left( u - \frac{1}{u} \right) \cdot \frac{3(u^2 + u^{-4})}{2} \, du,
$$

where $ U = \sqrt[3]{\sqrt{7^2 + 1} + 7} = \sqrt[3]{5\sqrt{2} + 7} $.

---

### Step 3: Evaluate the Integral

Expanding the integrand:

$$
\left( u - \frac{1}{u} \right) \cdot \left( u^2 + u^{-4} \right) = u^3 + u^{-3} - u - u^{-5}.
$$

So the integral becomes:

$$
\frac{3}{2} \int_{1}^{U} \left( u^3 + u^{-3} - u - u^{-5} \right) du.
$$

Integrating term-by-term:

$$
\int u^3 \, du = \frac{u^4}{4},\quad \int u^{-3} \, du = \frac{u^{-2}}{-2},\quad \int u \, du = \frac{u^2}{2},\quad \int u^{-5} \, du = \frac{u^{-4}}{-4}.
$$

Thus, the antiderivative is:

$$
\frac{3}{2} \left[ \frac{u^4}{4} - \frac{u^{-2}}{2} - \frac{u^2}{2} + \frac{u^{-4}}{4} \right] \Bigg|_{1}^{U}.
$$

Evaluating at $ u = 1 $:

$$
\frac{1}{4} - \frac{1}{2} - \frac{1}{2} + \frac{1}{4} = -0.5.
$$

Evaluating at $ u = U = 1 + \sqrt{2} $:

We compute:

- $ U^2 = (1 + \sqrt{2})^2 = 3 + 2\sqrt{2} $,
- $ U^4 = (3 + 2\sqrt{2})^2 = 17 + 12\sqrt{2} $,
- $ U