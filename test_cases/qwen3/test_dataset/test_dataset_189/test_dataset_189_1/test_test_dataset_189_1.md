To evaluate the definite integral

$$
\int_0^\infty \frac{1}{x(x^2 + 1)} \arctan\left(\frac{x}{x^2 + 1}\right) \, dx,
$$

we begin by recognizing the complexity of the integrand due to the presence of both a rational function and an inverse trigonometric function. A direct analytical evaluation is non-trivial, but we can simplify the expression by leveraging a clever trigonometric identity.

---

### Step 1: Use of Trigonometric Identity

We use the identity:

$$
\arctan\left(\frac{x}{x^2 + 1}\right) = \arctan(kx) - \arctan(mx),
$$

where $ k = \frac{1 + \sqrt{5}}{2} $ and $ m = \frac{\sqrt{5} - 1}{2} $. This identity is derived from the tangent subtraction formula and is valid for all $ x > 0 $.

This allows us to rewrite the original integral as:

$$
I = \int_0^\infty \frac{1}{x(x^2 + 1)} \left[\arctan(kx) - \arctan(mx)\right] dx.
$$

Splitting the integral:

$$
I = \int_0^\infty \frac{\arctan(kx)}{x(x^2 + 1)} dx - \int_0^\infty \frac{\arctan(mx)}{x(x^2 + 1)} dx.
$$

---

### Step 2: Apply Frullani's Theorem

Frullani's integral theorem states that for a suitable function $ f $, and constants $ a, b > 0 $:

$$
\int_0^\infty \frac{f(ax) - f(bx)}{x} dx = (f(\infty) - f(0)) \ln\left(\frac{a}{b}\right).
$$

In our case, the function $ f(x) = \frac{\arctan(x)}{x^2 + 1} $, and we observe that:

- $ f(0) = 0 $,
- $ f(\infty) = \frac{\pi}{2} \cdot \frac{1}{x^2 + 1} \to 0 $ as $ x \to \infty $,
- The integrand becomes $ \frac{f(kx) - f(mx)}{x} $, so we can apply Frullani's theorem.

Thus:

$$
I = \left(\frac{\pi}{2} - 0\right) \ln\left(\frac{k}{m}\right) = \frac{\pi}{2} \ln\left(\frac{k}{m}\right).
$$

---

### Step 3: Simplify the Logarithmic Term

Recall:

- $ k = \frac{1 + \sqrt{5}}{2} $,
- $ m = \frac{\sqrt{5} - 1}{2} $.

Then:

$$
\frac{k}{m} = \frac{1 + \sqrt{5}}{\sqrt{5} - 1} = \left(\frac{1 + \sqrt{5}}{2}\right)^2 = \phi^2,
$$

where $ \phi = \frac{1 + \sqrt{5}}{2} $ is the **golden ratio**.

So:

$$
\ln\left(\frac{k}{m}\right) = \ln(\phi^2) = 2 \ln(\phi).
$$

Hence:

$$
I = \frac{\pi}{2} \cdot 2 \ln(\phi) = \pi \ln(\phi).
$$

---

### Step 4: Final Answer

The exact value of the integral is:

$$
\boxed{\pi \ln\left(\frac{1 + \sqrt{5}}{2}\right)}
$$

This is equivalent to:

$$
\boxed{\frac{\pi}{2} \ln\left(\frac{3 + \sqrt{5}}{2}\right)}.
$$

Numerically, the golden ratio $ \phi \approx 1.61803398875 $, and $ \ln(\phi) \approx 0.4812118255 $. Therefore:

$$
I \approx \pi \cdot 0.4812118255 \approx 1.5117716734.
$$

Rounded to 10 decimal places:

$$
\boxed{1