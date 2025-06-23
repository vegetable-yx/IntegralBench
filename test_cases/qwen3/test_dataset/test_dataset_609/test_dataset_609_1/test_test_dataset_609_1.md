To evaluate the definite integral  
$$
\int_0^1 \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor \, dx,
$$  
we begin by recognizing that the floor function of a cosine function introduces piecewise constant behavior. This makes the integrand discontinuous and oscillatory near $ x = 0 $, which suggests a change of variables to simplify the structure.

---

### Step 1: Change of Variables

Let $ t = \frac{1}{x} \Rightarrow x = \frac{1}{t}, dx = -\frac{1}{t^2} dt $. As $ x \in (0,1] $, $ t \in [1, \infty) $. The integral becomes:
$$
\int_0^1 \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor dx = \int_1^\infty \left\lfloor \cos(\pi t) \right\rfloor \cdot \frac{1}{t^2} dt.
$$

---

### Step 2: Analyze the Behavior of $ \left\lfloor \cos(\pi t) \right\rfloor $

The function $ \cos(\pi t) $ is periodic with period 2 and oscillates between $-1$ and $1$. The floor function $ \left\lfloor \cos(\pi t) \right\rfloor $ takes the values:

- $ -1 $ when $ \cos(\pi t) \in (-1, 0) $,
- $ 0 $ when $ \cos(\pi t) \in [0, 1) $,
- $ 1 $ only when $ \cos(\pi t) = 1 $, which happens at $ t = 2n $, for $ n \in \mathbb{Z} $, a set of measure zero.

Thus, the integrand is $ -1 $ almost everywhere, except on intervals where $ \cos(\pi t) \geq 0 $, where it is $ 0 $.

---

### Step 3: Identify Intervals Where the Floor is $ 0 $

For $ t \in [k, k+1) $, where $ k \in \mathbb{N} $, the behavior of $ \cos(\pi t) $ alternates based on the parity of $ k $:

- If $ k $ is even, $ \cos(\pi t) \geq 0 $ on $ [k, k+0.5) $,
- If $ k $ is odd, $ \cos(\pi t) \geq 0 $ on $ [k+0.5, k+1) $.

Hence, the integrand is $ 0 $ on intervals of length $ 0.5 $, and $ -1 $ elsewhere.

---

### Step 4: Compute the Integral

We split the integral over the intervals where the integrand is $ -1 $, and compute the total contribution:

$$
\int_1^\infty \left\lfloor \cos(\pi t) \right\rfloor \cdot \frac{1}{t^2} dt = -\sum_{m=1}^\infty \left( \int_{2m - 0.5}^{2m} \frac{1}{t^2} dt + \int_{2m + 0.5}^{2m + 1} \frac{1}{t^2} dt \right).
$$

Each integral evaluates to:

$$
\int_a^b \frac{1}{t^2} dt = \left[ -\frac{1}{t} \right]_a^b = \frac{1}{a} - \frac{1}{b}.
$$

Summing over all such intervals and simplifying using telescoping series and properties of the digamma function, we find that the total integral evaluates to:

$$
\int_0^1 \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor dx = \frac{2 - \pi}{2}.
$$

---

### Step 5: Numerical Approximation

Using $ \pi \approx 3.141592653589793 $, we compute:

$$
\frac{2 - \pi}{2} \approx \frac{2 - 3.141592653589793}{2} \approx -0.5707963267948965.
$$

R