Given:

\[
I = \int_0^1\sqrt[3]{x}\left\lfloor\frac1{\sqrt[3]{x}}\right\rfloor\:\mathrm{d}x
\]

Let's follow the requested steps.

---

**Step 1: Substitution**

Set \( u = \sqrt[3]{x} \implies x = u^3 \), so \( dx = 3u^2 \, du \).
The limits:
- \( x = 0 \to u = 0 \)
- \( x = 1 \to u = 1 \)

The integrand becomes:

\[
I = \int_{u=0}^{u=1} u \left\lfloor \frac{1}{u} \right\rfloor 3u^2 \, du = 3\int_{0}^1 u^3 \left\lfloor \frac{1}{u} \right\rfloor du
\]

---

**Step 2: Break up the integral over intervals**

\(\left\lfloor \frac{1}{u} \right\rfloor\) is piecewise constant for \(u \in \left(\frac{1}{n+1}, \frac{1}{n}\right]\) and takes the value \(n\), for integer \(n \geq 1\).

Thus, the integration is split over intervals:
- For \(u \in \left( \frac{1}{n+1}, \frac{1}{n} \right] \), \(\left\lfloor \frac{1}{u}\right\rfloor = n\)
- The sum goes for \(n=1, 2, \ldots, \infty\), but since \(u \leq 1\), all \(n \geq 1\) are covered.

So,

\[
I = 3 \sum_{n=1}^{\infty} n \int_{u=\frac{1}{n+1}}^{u=\frac{1}{n}} u^3 du
\]

---

**Step 3: Evaluate the inner integral**

\[
\int_{u=\frac{1}{n+1}}^{u=\frac{1}{n}} u^3 du = \left[ \frac{u^4}{4} \right]_{u=\frac{1}{n+1}}^{u=\frac{1}{n}} = \frac{1}{4} \left( \left(\frac{1}{n}\right)^4 - \left(\frac{1}{n+1}\right)^4 \right)
\]

So,

\[
I = 3 \sum_{n=1}^{\infty} n \cdot \frac{1}{4} \left( \frac{1}{n^4} - \frac{1}{(n+1)^4} \right)
= \frac{3}{4} \sum_{n=1}^{\infty} n \left( \frac{1}{n^4} - \frac{1}{(n+1)^4} \right)
\]

Let’s expand \(n \left( \frac{1}{n^4} - \frac{1}{(n+1)^4} \right)\):

\[
n \left( \frac{1}{n^4} - \frac{1}{(n+1)^4} \right) = \frac{1}{n^3} - \frac{n}{(n+1)^4}
\]

Thus:

\[
I = \frac{3}{4} \sum_{n=1}^\infty \left( \frac{1}{n^3} - \frac{n}{(n+1)^4} \right)
= \frac{3}{4} \left( \sum_{n=1}^\infty \frac{1}{n^3} - \sum_{n=1}^\infty \frac{n}{(n+1)^4} \right)
\]

The first term is the Riemann zeta value \(\zeta(3)\).

Now,

\[
\sum_{n=1}^{\infty} \frac{n}{(n+1)^4}
\]

Let’s write \(n = (n+1) - 1\):

\[
\frac{n}{(n+1)^4} = \frac{n+1}{(n+1)^4} - \frac{1}{(n+1)^4} = \frac{1}{(n+1)^3} - \frac{1}{(n+1)^4}
\]

So:

\[
\sum_{n=1}^{\infty} \frac{n}{(n+1)^4} = \sum_{n=1}^{\infty}\left(\frac{1}{(n+1)^3} - \frac{1}{(n+1)^4}\right)
= \sum_{m=2}^{\infty} \left( \frac{1}{m^3} - \frac{1}{m^4} \right)
\]

So, this is:

\[
= \sum_{m=2}^{\infty} \frac{1}{m^3} - \sum_{m=2}^{\infty} \frac{1}{m^4}
= \left( \zeta(3) - 1 \right) - \left( \zeta(4) - 1 \right) = \zeta(3) - \zeta(4)
\]

Thus,

\[
I = \frac{3}{4} \left( \zeta(3) - [\zeta(3) - \zeta(4)] \right )
= \frac{3}{4} \zeta(4)
\]

\[
\boxed{I = \frac{3}{4} \zeta(4)}
\]

Recall,

\(\zeta(4) = \frac{\pi^4}{90}\), so

\[
I = \frac{3}{4} \cdot \frac{\pi^4}{90} = \frac{\pi^4}{120}
\]

---

**Step 4: Numerical Approximation**

\(\pi^4 = (\pi^2)^2 = (9.869604401089358)^2 = 97.40909103400244\)

Thus,

\[
I = \frac{97.40909103400244}{120} = 0.8117424252833537
\]

Rounding to 10 decimal places,

\[
\boxed{0.8117424253}
\]

---

**Final JSON Output:**

```json
{"answer": "\\frac{\\pi^4}{120}", "numerical_answer": "0.8117424253"}
```