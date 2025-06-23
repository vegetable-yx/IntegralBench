To evaluate the definite integral

$$
\int_0^1 \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor \, dx,
$$

we begin by analyzing the behavior of the integrand. The floor function, $ \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor $, is piecewise constant, taking on values $ -1 $, $ 0 $, and $ 1 $ depending on the value of $ \cos\left(\frac{\pi}{x}\right) $. However, since $ \cos\left(\frac{\pi}{x}\right) \in [-1, 1] $, the floor function will only take values $ -1 $ and $ 0 $ almost everywhere, except at discrete points where $ \cos\left(\frac{\pi}{x}\right) = \pm1 $, which have measure zero.

---

### Step 1: Substitution

We perform the substitution $ \theta = \frac{\pi}{x} $, which implies $ x = \frac{\pi}{\theta} $ and $ dx = -\frac{\pi}{\theta^2} \, d\theta $. The limits of integration transform as follows:

- When $ x = 0 $, $ \theta \to \infty $
- When $ x = 1 $, $ \theta = \pi $

Thus, the integral becomes:

$$
\int_0^1 \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor dx = \int_\pi^\infty \left\lfloor \cos(\theta) \right\rfloor \cdot \frac{\pi}{\theta^2} \, d\theta.
$$

---

### Step 2: Analyzing the Floor Function

We observe that $ \left\lfloor \cos(\theta) \right\rfloor = -1 $ when $ \cos(\theta) < 0 $, and $ \left\lfloor \cos(\theta) \right\rfloor = 0 $ when $ \cos(\theta) \geq 0 $. The function $ \cos(\theta) $ is negative on intervals of the form:

$$
\theta \in \left( \frac{\pi}{2} + 2\pi n, \frac{3\pi}{2} + 2\pi n \right), \quad n \in \mathbb{Z}_{\geq 0}.
$$

For $ \theta \geq \pi $, the relevant intervals where $ \cos(\theta) < 0 $ are:

- $ [\pi, \frac{3\pi}{2}) $
- $ [\frac{5\pi}{2}, \frac{7\pi}{2}) $
- $ [\frac{9\pi}{2}, \frac{11\pi}{2}) $, etc.

These intervals correspond to the values of $ x $ where $ \cos\left(\frac{\pi}{x}\right) < 0 $, and hence $ \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor = -1 $.

---

### Step 3: Computing the Integral

We compute the total measure (length) of the set where $ \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor = -1 $, and then multiply by $ -1 $ to get the value of the integral.

The intervals in $ x $ where $ \cos\left(\frac{\pi}{x}\right) < 0 $ are:

$$
x \in \left( \frac{2}{4n + 3}, \frac{2}{4n + 1} \right), \quad n \in \mathbb{Z}_{\geq 0}.
$$

The length of each such interval is:

$$
\frac{2}{4n + 1} - \frac{2}{4n + 3} = \frac{4}{(4n + 1)(4n + 3)}.
$$

Summing over all $ n \geq 0 $, the total measure is:

$$
\sum_{n=0}^\infty \left( \frac{2}{4n + 1} - \frac{2}{4n + 3} \right) = \frac{\pi}{2} - 1.
$$

Thus, the integral becomes:

$$
\int_0^1 \left\lfloor \cos\left(\frac{\pi}{x}\right