To evaluate the definite integral  
$$
\int_0^{\frac{\pi}{2}} x \ln(\sin x) \, dx,
$$  
we proceed using the **Fourier series expansion** of $\ln(\sin x)$ on the interval $[0, \pi]$, which is given by:  
$$
\ln(\sin x) = -\ln 2 - \sum_{k=1}^\infty \frac{\cos(2kx)}{k}.
$$

---

### Step 1: Substitution into the Integral

Substitute the Fourier series into the integral:
$$
\int_0^{\frac{\pi}{2}} x \ln(\sin x) \, dx = \int_0^{\frac{\pi}{2}} x \left( -\ln 2 - \sum_{k=1}^\infty \frac{\cos(2kx)}{k} \right) dx.
$$

Split the integral:
$$
= -\ln 2 \int_0^{\frac{\pi}{2}} x \, dx - \sum_{k=1}^\infty \frac{1}{k} \int_0^{\frac{\pi}{2}} x \cos(2kx) \, dx.
$$

---

### Step 2: Evaluate the First Integral

$$
\int_0^{\frac{\pi}{2}} x \, dx = \left[\frac{x^2}{2}\right]_0^{\frac{\pi}{2}} = \frac{\pi^2}{8}.
$$

So the first term becomes:
$$
-\ln 2 \cdot \frac{\pi^2}{8} = -\frac{\pi^2}{8} \ln 2.
$$

---

### Step 3: Evaluate the Series Term

We now evaluate:
$$
\sum_{k=1}^\infty \frac{1}{k} \int_0^{\frac{\pi}{2}} x \cos(2kx) \, dx.
$$

Using integration by parts:
$$
\int x \cos(2kx) \, dx = \frac{x \sin(2kx)}{2k} + \frac{\cos(2kx)}{4k^2}.
$$

Evaluate from 0 to $\frac{\pi}{2}$:
$$
\left[ \frac{x \sin(2kx)}{2k} + \frac{\cos(2kx)}{4k^2} \right]_0^{\frac{\pi}{2}} = \frac{\cos(k\pi) - 1}{4k^2} = \frac{(-1)^k - 1}{4k^2}.
$$

So the integral becomes:
$$
\sum_{k=1}^\infty \frac{1}{k} \cdot \frac{(-1)^k - 1}{4k^2} = \frac{1}{4} \sum_{k=1}^\infty \frac{(-1)^k - 1}{k^3}.
$$

Now, observe that for even $k$, $(-1)^k = 1$, so the term is zero. For odd $k$, $(-1)^k = -1$, so the term becomes $-2/k^3$. Thus:
$$
\sum_{k=1}^\infty \frac{(-1)^k - 1}{k^3} = -2 \sum_{\substack{k=1 \\ k \text{ odd}}}^\infty \frac{1}{k^3} = -2 \cdot \left(\zeta(3) - \frac{1}{8} \zeta(3)\right) = -2 \cdot \frac{7}{8} \zeta(3) = -\frac{7}{4} \zeta(3).
$$

So the series term becomes:
$$
\frac{1}{4} \cdot \left(-\frac{7}{4} \zeta(3)\right) = -\frac{7}{16} \zeta(3).
$$

---

### Step 4: Combine All Terms

Putting it all together:
$$
\int_0^{\frac{\pi}{2}} x \ln(\sin x) \, dx = -\frac{\pi^2}{8} \ln 2 + \frac{7}{16} \zeta(3).
$$

---

### Step 5: Numerical Approximation

Use known values:
- $\zeta(3) \approx 1.2020569