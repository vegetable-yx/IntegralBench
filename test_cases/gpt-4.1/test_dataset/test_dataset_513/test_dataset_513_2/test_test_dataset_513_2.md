Let's solve the definite integral:
\[
\int_{-4}^4 |x^3 - x|\,dx
\]

**Step 1: Find where the expression inside the absolute value changes sign.**

Set \( x^3 - x = 0 \implies x(x^2 - 1) = 0 \implies x = 0, x = \pm1 \).

So, the sign of \( x^3-x \) changes at \( x = -1, 0, 1 \). Let's check signs in intervals:

- For \( x < -1 \): pick \( x = -2 \), \( (-2)^3 - (-2) = -8 + 2 = -6 < 0 \)
- For \( -1 < x < 0 \): pick \( x = -0.5 \), \( (-0.5)^3 - (-0.5) = -0.125 + 0.5 = 0.375 > 0 \)
- For \( 0 < x < 1 \): pick \( x = 0.5 \), \( 0.125 - 0.5 = -0.375 < 0 \)
- For \( x > 1 \): pick \( x = 2 \), \( 8 - 2 = 6 > 0 \)

So the sign pattern is:
- \( x^3 - x < 0 \) on \( [-4, -1] \)
- \( x^3 - x > 0 \) on \( [-1, 0] \)
- \( x^3 - x < 0 \) on \( [0,1] \)
- \( x^3 - x > 0 \) on \( [1,4] \)

**Step 2: Break up the integral and remove the absolute value accordingly:**

\[
\begin{align*}
\int_{-4}^4 |x^3 - x|\,dx &= \int_{-4}^{-1} -(x^3 - x)\,dx + \int_{-1}^0 (x^3 - x)\,dx \\
&\quad + \int_0^1 -(x^3 - x)\,dx + \int_1^4 (x^3 - x)\,dx
\end{align*}
\]

**Step 3: Compute the antiderivative**

\[
\int (x^3 - x)\,dx = \frac{x^4}{4} - \frac{x^2}{2} + C
\]
So,
\[
\int -(x^3-x)\,dx = -\frac{x^4}{4} + \frac{x^2}{2} + C
\]

**Step 4: Evaluate each interval**

Let’s compute each term.

---

**A. \(\int_{-4}^{-1} -(x^3-x) dx = [-\frac{x^4}{4} + \frac{x^2}{2}]_{-4}^{-1}\)**

\[
= \left(-\frac{(-1)^4}{4} + \frac{(-1)^2}{2}\right)
- \left(-\frac{(-4)^4}{4} + \frac{(-4)^2}{2}\right)
\]
\[
= \left(-\frac{1}{4} + \frac{1}{2}\right)
- \left(-\frac{256}{4} + \frac{16}{2}\right)
\]
\[
= (0.25) - (-64 + 8)
\]
Let’s compute:

First bracket: \(-\frac{1}{4}+\frac{1}{2} = \frac{-1+2}{4} = \frac{1}{4}\).

Second bracket: \(-\frac{256}{4}+\frac{16}{2} = -64 + 8 = -56\).

So,
\[
= \frac{1}{4} - (-56) = \frac{1}{4} + 56 = \frac{225}{4} = 56.25
\]

---

**B. \(\int_{-1}^{0} (x^3-x) dx = [\frac{x^4}{4} - \frac{x^2}{2}]_{-1}^0\)**
\[
= \left(\frac{0^4}{4} - \frac{0^2}{2}\right)
- \left(\frac{(-1)^4}{4} - \frac{(-1)^2}{2}\right)
= (0 - 0) - \left(\frac{1}{4} - \frac{1}{2} \right)
= 0 - (-\frac{1}{4})
= \frac{1}{4}
\]

---

**C. \(\int_{0}^{1} -(x^3-x) dx = [-\frac{x^4}{4} + \frac{x^2}{2}]_0^1\)**
\[
= \left(-\frac{1}{4} + \frac{1}{2}\right) - \left(-\frac{0}{4} + \frac{0}{2}\right)
= (-\frac{1}{4} + \frac{1}{2}) - 0
= \frac{-1+2}{4} = \frac{1}{4}
\]

---

**D. \(\int_{1}^{4} (x^3-x) dx = [\frac{x^4}{4} - \frac{x^2}{2}]_1^4\)**

\[
= \left(\frac{4^4}{4} - \frac{4^2}{2}\right)
- \left(\frac{1^4}{4} - \frac{1^2}{2}\right)
\]
\[
= \left(\frac{256}{4} - \frac{16}{2}\right)
- \left(\frac{1}{4} - \frac{1}{2}\right)
\]
\[
= (64 - 8)
- (\frac{1}{4} - \frac{1}{2})
\]
\[
= 56 - (-\frac{1}{4})
= 56 + \frac{1}{4} = \frac{225}{4} = 56.25
\]

---

**Step 5: Add up terms**

\[
\text{Total} = 56.25 + \frac{1}{4} + \frac{1}{4} + 56.25 = (56.25 + 56.25) + (\frac{1}{4} + \frac{1}{4}) = 112.5 + 0.5 = 113
\]

---

**Step 6: Numerical approximation**

The answer is exactly \( 113 \). As a decimal to 10 places: \( 113.0000000000 \).

---

**JSON format answer:**

{"answer": "113", "numerical_answer": "113.0000000000"}