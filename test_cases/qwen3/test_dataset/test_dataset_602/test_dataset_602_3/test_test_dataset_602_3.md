To evaluate the definite integral

$$
\int_0^1 \sqrt[3]{x} \left\lfloor \frac{1}{\sqrt[3]{x}} \right\rfloor \, dx,
$$

we begin by making the substitution:

$$
t = \frac{1}{\sqrt[3]{x}} \quad \Rightarrow \quad x = \frac{1}{t^3}, \quad dx = -\frac{3}{t^4} dt.
$$

As $ x \to 0^+ $, $ t \to \infty $, and as $ x = 1 $, $ t = 1 $. The integral becomes:

$$
\int_0^1 \sqrt[3]{x} \left\lfloor \frac{1}{\sqrt[3]{x}} \right\rfloor dx = \int_1^\infty \left( \frac{1}{t} \right) \left\lfloor t \right\rfloor \cdot \frac{3}{t^4} dt = 3 \int_1^\infty \frac{\left\lfloor t \right\rfloor}{t^5} dt.
$$

---

### Step 1: Break the integral into a sum

We use the fact that $ \left\lfloor t \right\rfloor = n $ on the interval $ t \in [n, n+1) $, for each integer $ n \geq 1 $. Thus:

$$
\int_1^\infty \frac{\left\lfloor t \right\rfloor}{t^5} dt = \sum_{n=1}^\infty \int_n^{n+1} \frac{n}{t^5} dt.
$$

Compute the inner integral:

$$
\int_n^{n+1} \frac{n}{t^5} dt = n \left[ -\frac{1}{4t^4} \right]_n^{n+1} = n \left( \frac{1}{4n^4} - \frac{1}{4(n+1)^4} \right).
$$

So the full integral becomes:

$$
3 \sum_{n=1}^\infty \left( \frac{1}{4n^3} - \frac{n}{4(n+1)^4} \right) = \frac{3}{4} \sum_{n=1}^\infty \left( \frac{1}{n^3} - \frac{n}{(n+1)^4} \right).
$$

---

### Step 2: Evaluate the infinite sum

Split the sum:

$$
\sum_{n=1}^\infty \left( \frac{1}{n^3} - \frac{n}{(n+1)^4} \right) = \sum_{n=1}^\infty \frac{1}{n^3} - \sum_{n=1}^\infty \frac{n}{(n+1)^4}.
$$

Reindex the second sum by letting $ m = n+1 $, so $ n = m - 1 $, and $ n+1 = m $:

$$
\sum_{n=1}^\infty \frac{n}{(n+1)^4} = \sum_{m=2}^\infty \frac{m-1}{m^4} = \sum_{m=2}^\infty \left( \frac{1}{m^3} - \frac{1}{m^4} \right).
$$

This becomes:

$$
\sum_{m=2}^\infty \frac{1}{m^3} - \sum_{m=2}^\infty \frac{1}{m^4} = \left( \zeta(3) - 1 \right) - \left( \zeta(4) - 1 \right) = \zeta(3) - \zeta(4).
$$

Therefore, the original sum is:

$$
\sum_{n=1}^\infty \left( \frac{1}{n^3} - \frac{n}{(n+1)^4} \right) = \zeta(3) - (\zeta(3) - \zeta(4)) = \zeta(4).
$$

---

### Step 3: Final expression

Thus, the integral becomes:

$$
\frac{3}{4} \zeta(4).
$$

Using the known value:

$$
\zeta(4) = \frac{\pi^4}{90},
$$