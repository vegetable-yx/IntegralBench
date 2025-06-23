To evaluate the definite integral

$$
\int_0^\infty \frac{\{x\}^{\lceil x \rceil}}{1 + \lceil x \rceil} \, dx,
$$

we begin by analyzing the structure of the integrand. The fractional part $\{x\}$ is defined as $x - \lfloor x \rfloor$, and the ceiling function $\lceil x \rceil$ is the smallest integer greater than or equal to $x$. These functions are piecewise constant on intervals between consecutive integers.

---

### Step 1: Partition the Interval

We partition the domain $[0, \infty)$ into intervals $[n, n+1)$ for $n = 0, 1, 2, \ldots$. On each such interval:

- $\{x\} = x - n$,
- $\lceil x \rceil = n + 1$ (except at the point $x = n$, which has measure zero),
- The integrand becomes:
  $$
  \frac{(x - n)^{n+1}}{1 + (n+1)} = \frac{(x - n)^{n+1}}{n + 2}.
  $$

---

### Step 2: Change of Variables

Let $t = x - n$, so $x = t + n$ and $dx = dt$. When $x$ ranges from $n$ to $n+1$, $t$ ranges from $0$ to $1$. The integral over $[n, n+1)$ becomes:

$$
\int_n^{n+1} \frac{(x - n)^{n+1}}{n + 2} \, dx = \int_0^1 \frac{t^{n+1}}{n + 2} \, dt.
$$

This simplifies to:

$$
\frac{1}{n + 2} \int_0^1 t^{n+1} \, dt = \frac{1}{n + 2} \cdot \frac{1}{n + 2} = \frac{1}{(n + 2)^2}.
$$

---

### Step 3: Sum the Series

The total integral is the sum over all $n \geq 0$ of the contributions from each interval:

$$
\sum_{n=0}^{\infty} \frac{1}{(n + 2)^2} = \sum_{k=2}^{\infty} \frac{1}{k^2},
$$

where we substituted $k = n + 2$. This is a well-known series:

$$
\sum_{k=1}^{\infty} \frac{1}{k^2} = \frac{\pi^2}{6},
$$

so

$$
\sum_{k=2}^{\infty} \frac{1}{k^2} = \frac{\pi^2}{6} - 1.
$$

---

### Step 4: Final Answer

Thus, the exact value of the integral is:

$$
\boxed{\frac{\pi^2}{6} - 1}
$$

Numerically, this evaluates to approximately:

$$
0.6449340668
$$

---

### Final Output

$$
\boxed{\frac{\pi^2}{6} - 1}
$$

```json
{"answer": "\\boxed{\\frac{\\pi^2}{6} - 1}", "numerical_answer": "0.6449340668"}
```