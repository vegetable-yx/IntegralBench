Given the integral:
\[
I = \int_{0}^{1} x^3 \arccos(x) \arcsin^2(x)\, dx
\]

Let's proceed step by step:

---

### Step 1: Make a substitution to simplify the integral.

Let us use the substitution:
\[
x = \sin\theta \quad \Rightarrow \quad dx = \cos\theta\, d\theta
\]
When \(x=0:\ \theta=0\) \\
When \(x=1:\ \theta=\frac{\pi}{2}\)

Now, rewrite the integral in terms of \(\theta\):

\[
I = \int_{x=0}^{x=1} x^3 \arccos(x) \arcsin^2(x)\, dx = \int_{\theta=0}^{\theta=\frac{\pi}{2}} \sin^3\theta \arccos(\sin\theta) \arcsin^2(\sin\theta) \cos\theta\, d\theta
\]

We know:
- \(\arcsin(\sin\theta) = \theta\) on \([0, \pi/2]\)
- \(\arccos(\sin\theta) = \frac{\pi}{2} - \theta\)

So the integrand simplifies:
- \(x^3 = \sin^3\theta\)
- \(\arccos x = \frac{\pi}{2} - \theta\)
- \(\arcsin^2 x = \theta^2\)

Then:

\[
I = \int_{0}^{\frac{\pi}{2}} \sin^3\theta \left(\frac{\pi}{2} - \theta\right) \theta^2 \cos\theta\, d\theta
\]

---

### Step 2: Expand and separate the integral.

\[
I = \int_{0}^{\frac{\pi}{2}} \sin^3\theta\, \cos\theta\, \left(\frac{\pi}{2} \theta^2 - \theta^3\right) d\theta
= \frac{\pi}{2} \int_{0}^{\frac{\pi}{2}} \sin^3\theta\, \cos\theta\, \theta^2\, d\theta - \int_{0}^{\frac{\pi}{2}} \sin^3\theta\, \cos\theta\, \theta^3\, d\theta
\]

Let
\[
I_1 = \int_{0}^{\frac{\pi}{2}} \sin^3\theta\, \cos\theta\, \theta^2\, d\theta \\
I_2 = \int_{0}^{\frac{\pi}{2}} \sin^3\theta\, \cos\theta\, \theta^3\, d\theta
\]

So,
\[
I = \frac{\pi}{2} I_1 - I_2
\]

---

### Step 3: Integration by parts (for \(I_1\))

Let’s focus on \(I_1\):

Let
- \(u = \theta^2\) \(\Rightarrow du = 2\theta d\theta\)
- \(dv = \sin^3\theta\, \cos\theta\, d\theta\) \(\Rightarrow v = \int \sin^3\theta\, \cos\theta\, d\theta\)

Let’s compute \(v\):

Let \(w = \sin\theta \implies dw = \cos\theta d\theta\) \\
Then, \(\sin^3\theta \cos\theta d\theta = w^3\, dw\)

So,
\[
v = \int \sin^3\theta \cos\theta\, d\theta = \int w^3\, dw = \frac{1}{4} w^4 = \frac{1}{4} \sin^4\theta
\]

Now, use integration by parts:
\[
I_1 = \int_{0}^{\frac{\pi}{2}} \sin^3\theta \cos\theta \theta^2\, d\theta
= \left[ \frac{1}{4} \sin^4\theta\, \theta^2 \right]_{0}^{\frac{\pi}{2}} - \int_{0}^{\frac{\pi}{2}} \frac{1}{4} \sin^4\theta\, (2\theta)\, d\theta
\]

But \(\sin^4(0) = 0\), \(\sin^4(\pi/2) = 1\). So:

\[
I_1 = \frac{1}{4} \cdot 1 \cdot \left(\frac{\pi}{2}\right)^2 - \frac{1}{2} \int_{0}^{\frac{\pi}{2}} \sin^4\theta\, \theta\, d\theta
= \frac{\pi^2}{16} - \frac{1}{2} J_1
\]
where \(J_1 = \int_{0}^{\frac{\pi}{2}} \sin^4\theta\, \theta\, d\theta\).

---

### Step 4: Integration by parts (for \(I_2\))

Let \(u = \theta^3\), \(dv = \sin^3\theta \cos\theta d\theta\):

\(v\) is as above, \(\frac{1}{4} \sin^4\theta\), \(du = 3\theta^2 d\theta\):

\[
I_2 = \left[ \frac{1}{4} \sin^4\theta\, \theta^3 \right]_{0}^{\frac{\pi}{2}} - \int_{0}^{\frac{\pi}{2}} \frac{1}{4} \sin^4\theta\, (3\theta^2)\, d\theta
\]
Again, at the endpoints \(\theta=0, \sin^4\theta = 0\); \(\theta=\frac{\pi}{2}, \sin^4(\frac{\pi}{2}) = 1\):

\[
I_2 = \frac{1}{4} \left(\frac{\pi}{2}\right)^3 - \frac{3}{4} J_2
= \frac{\pi^3}{32} - \frac{3}{4} J_2
\]
where \(J_2 = \int_{0}^{\frac{\pi}{2}} \sin^4\theta\, \theta^2\, d\theta\).

---

### Step 5: Substitute back into the original expression

Recall:
\[
I = \frac{\pi}{2} I_1 - I_2
\]

Substitute the expressions for \(I_1, I_2\):

\[
I = \frac{\pi}{2} \left( \frac{\pi^2}{16} - \frac{1}{2}J_1 \right) - \left( \frac{\pi^3}{32} - \frac{3}{4} J_2 \right)
= \frac{\pi^3}{32} - \frac{\pi}{4} J_1 - \frac{\pi^3}{32} + \frac{3}{4} J_2
\]
The \(\frac{\pi^3}{32}\) terms cancel:

\[
I = -\frac{\pi}{4} J_1 + \frac{3}{4} J_2
= \frac{3}{4} J_2 - \frac{\pi}{4} J_1
\]
where:
\[
J_1 = \int_{0}^{\frac{\pi}{2}} \sin^4\theta\, \theta\, d\theta \\
J_2 = \int_{0}^{\frac{\pi}{2}} \sin^4\theta\, \theta^2\, d\theta
\]

---

### Step 6: Express \( \sin^4\theta \) in terms of cosines

Recall:
\[
\sin^4\theta = \left(\sin^2\theta\right)^2 = \left(\frac{1-\cos 2\theta}{2}\right)^2 = \frac{1}{4}(1 - 2\cos 2\theta + \cos^2 2\theta)
\]
But
\[
\cos^2 2\theta = \frac{1+\cos 4\theta}{2}
\]
Therefore
\[
\sin^4\theta = \frac{1}{4}\left(1 - 2\cos 2\theta + \frac{1}{2}(1+\cos 4\theta)\right) = \frac{1}{4}\left(\frac{3}{2} - 2\cos 2\theta + \frac{1}{2}\cos 4\theta\right) = \frac{3}{8} - \frac{1}{2}\cos 2\theta + \frac{1}{8}\cos 4\theta
\]

Thus,
\[
J_k := \int_{0}^{\pi/2} \sin^4\theta\, \theta^k\, d\theta = \int_{0}^{\pi/2} \left( \frac{3}{8} - \frac{1}{2}\cos 2\theta + \frac{1}{8}\cos 4\theta \right)\theta^k\, d\theta
\]
This splits up as:
\[
J_k = \frac{3}{8} \int_{0}^{\frac{\pi}{2}} \theta^k\, d\theta - \frac{1}{2} \int_{0}^{\frac{\pi}{2}} \theta^k\, \cos 2\theta\, d\theta + \frac{1}{8} \int_{0}^{\frac{\pi}{2}} \theta^k\, \cos 4\theta\, d\theta
\]

---

Now, write out for \(J_1\) and \(J_2\):

\[
J_1 = \frac{3}{8} \int_{0}^{\frac{\pi}{2}} \theta\, d\theta - \frac{1}{2} \int_{0}^{\frac{\pi}{2}} \theta\, \cos 2\theta\, d\theta + \frac{1}{8} \int_{0}^{\frac{\pi}{2}} \theta\, \cos 4\theta\, d\theta
\]
Similarly for \(J_2\):
\[
J_2 = \frac{3}{8} \int_{0}^{\frac{\pi}{2}} \theta^2\, d\theta - \frac{1}{2} \int_{0}^{\frac{\pi}{2}} \theta^2\, \cos 2\theta\, d\theta + \frac{1}{8} \int_{0}^{\frac{\pi}{2}} \theta^2\, \cos 4\theta\, d\theta
\]

Define for \(k = 1, 2\):
\[
A_k = \int_{0}^{\frac{\pi}{2}} \theta^k\, d\theta \\
B_k = \int_{0}^{\frac{\pi}{2}} \theta^k\, \cos 2\theta\, d\theta \\
C_k = \int_{0}^{\frac{\pi}{2}} \theta^k\, \cos 4\theta\, d\theta
\]
So:

\[
J_k = \frac{3}{8} A_k - \frac{1}{2} B_k + \frac{1}{8} C_k
\]

Specifically:
\[
J_1 = \frac{3}{8} A_1 - \frac{1}{2} B_1 + \frac{1}{8} C_1
\]
\[
J_2 = \frac{3}{8} A_2 - \frac{1}{2} B_2 + \frac{1}{8} C_2
\]

Therefore, the original integral becomes:

\[
I = \frac{3}{4} J_2 - \frac{\pi}{4} J_1
\]

---

### Step 7: Compute the elementary integrals

First, \(A_k\):

**For \(A_1\):**

\[
A_1 = \int_{0}^{\frac{\pi}{2}} \theta\, d\theta = \left. \frac{1}{2} \theta^2 \right|_0^{\frac{\pi}{2}} = \frac{1}{2} \left( \frac{\pi}{2} \right)^2 = \frac{\pi^2}{8}
\]

**For \(A_2\):**
\[
A_2 = \int_{0}^{\frac{\pi}{2}} \theta^2\, d\theta = \left. \frac{1}{3} \theta^3 \right|_0^{\frac{\pi}{2}} = \frac{1}{3} \left( \frac{\pi}{2} \right)^3 = \frac{\pi^3}{24}
\]

Now, \(B_1, B_2\) and \(C_1, C_2\):

#### Compute \(B_1 = \int_{0}^{\frac{\pi}{2}} \theta\, \cos 2\theta\, d\theta\):

Integration by parts:
Let \(u = \theta\), \(dv = \cos 2\theta\, d\theta\), \\
then \(du = d\theta, v = \frac{1}{2} \sin 2\theta\):

\[
B_1 = \left.\theta \frac{1}{2} \sin 2\theta \right|_0^{\frac{\pi}{2}} - \int_{0}^{\frac{\pi}{2}} \frac{1}{2} \sin 2\theta\, d\theta
\]
\[
= \frac{1}{2} \left[ \frac{\pi}{2} \sin \pi - 0 \cdot \sin 0 \right] - \frac{1}{2} \int_{0}^{\frac{\pi}{2}} \sin 2\theta\, d\theta
\]
\[
\sin \pi = 0, \sin 0 = 0
\]
\[
\int \sin 2\theta\, d\theta = -\frac{1}{2} \cos 2\theta
\]

So,
\[
B_1 = 0 - \frac{1}{2} \left[ -\frac{1}{2} \cos 2\theta \right]_{0}^{\frac{\pi}{2}}
= \frac{1}{4} \left[ \cos 2\theta \right]_0^{\frac{\pi}{2}}
= \frac{1}{4} [\cos \pi - \cos 0] = \frac{1}{4} [ -1 - 1 ] = -\frac{1}{2}
\]

---

#### Compute \(C_1 = \int_{0}^{\frac{\pi}{2}} \theta\, \cos 4\theta\, d\theta\):

Similarly, let \(u = \theta, dv = \cos 4\theta d\theta\), \(du = d\theta, v = \frac{1}{4} \sin 4\theta\):

\[
C_1 = \left[ \theta \cdot \frac{1}{4} \sin 4\theta \right]_0^{\frac{\pi}{2}} - \int_{0}^{\frac{\pi}{2}} \frac{1}{4} \sin 4\theta\, d\theta
\]
\[
= \frac{1}{4} \left[ \frac{\pi}{2} \sin(2\pi) - 0 \cdot \sin 0 \right] - \frac{1}{4} \int_{0}^{\frac{\pi}{2}} \sin 4\theta d\theta
\]
\[
\sin(2\pi) = 0
\]
\[
\int \sin 4\theta\, d\theta = -\frac{1}{4} \cos 4\theta
\]
So,
\[
C_1 = 0 - \frac{1}{4} \left[ -\frac{1}{4} \cos 4\theta \right]_0^{\frac{\pi}{2}}
= \frac{1}{16} [\cos 4\theta ]_0^{\frac{\pi}{2}}
\]
\[
4\theta, \theta = 0: \cos 0 = 1; \theta = \frac{\pi}{2}: \cos 2\pi = 1
\]
Thus,
\[
C_1 = \frac{1}{16} (1 - 1) = 0
\]

---

#### Compute \(B_2 = \int_{0}^{\frac{\pi}{2}} \theta^2\, \cos 2\theta\, d\theta\):

By parts; let \(u = \theta^2, dv = \cos 2\theta d\theta\), \(du = 2\theta d\theta, v = \frac{1}{2} \sin 2\theta\):

\[
B_2 = \left. \theta^2 \cdot \frac{1}{2} \sin 2\theta \right|_0^{\frac{\pi}{2}} - \int_{0}^{\frac{\pi}{2}} \frac{1}{2} \sin 2\theta \cdot 2\theta d\theta
\]
\[
= \left. \frac{1}{2} \theta^2 \sin 2\theta \right|_0^{\frac{\pi}{2}} - \int_{0}^{\frac{\pi}{2}} \theta \sin 2\theta d\theta
\]
Now from previous, when \(\theta = 0\) or \(\pi/2\), \(\sin 2\theta = 0\): \( \sin 0 = 0, \sin \pi = 0 \),
the first term is 0.

So,
\[
B_2 = - \int_{0}^{\frac{\pi}{2}} \theta \sin 2\theta d\theta
\]

Let’s compute \(I = \int_{0}^{\frac{\pi}{2}} \theta \sin 2\theta d\theta\):

Integration by parts:
Let \(u = \theta, dv = \sin 2\theta\, d\theta\), \(du = d\theta, v = -\frac{1}{2} \cos 2\theta\):

\[
I = \left. -\frac{1}{2} \theta \cos 2\theta \right|_{0}^{\frac{\pi}{2}} + \frac{1}{2} \int_{0}^{\frac{\pi}{2}} \cos 2\theta d\theta
\]
\[
\int \cos 2\theta\, d\theta = \frac{1}{2} \sin 2\theta
\]
So,

\[
I = -\frac{1}{2} \left[ \frac{\pi}{2} \cos \pi - 0 \cdot \cos 0 \right] + \frac{1}{2} \left[ \frac{1}{2} \sin 2\theta \right]_0^{\frac{\pi}{2}}
\]

\[
\cos \pi = -1, \sin 2\theta|_{\theta=0} = 0, \sin 2\theta|_{\theta=\frac{\pi}{2}} = 0
\]
So,

\[
I = -\frac{1}{2} \left[ \frac{\pi}{2} \times (-1) \right] + 0 = \frac{\pi}{4}
\]

Therefore,
\[
B_2 = -I = -\frac{\pi}{4}
\]

---

#### Compute \(C_2 = \int_{0}^{\frac{\pi}{2}} \theta^2 \cos 4\theta\, d\theta\):

Again, by parts:

Let \(u = \theta^2, dv = \cos 4\theta d\theta\) \\
\(du = 2\theta d\theta, v = \frac{1}{4} \sin 4\theta\):

\[
C_2 = \left. \theta^2 \cdot \frac{1}{4} \sin 4\theta \right|_0^{\frac{\pi}{2}} - \int_{0}^{\frac{\pi}{2}} \frac{1}{4} \sin 4\theta \cdot 2\theta d\theta \\
= \frac{1}{4} \left[ \theta^2 \sin 4\theta \right]_0^{\frac{\pi}{2}} - \frac{1}{2} \int_{0}^{\frac{\pi}{2}} \theta \sin 4\theta\, d\theta
\]

Now, \(\theta = 0\): \(\sin 0 = 0\), \(\theta = \frac{\pi}{2}\): \(\sin 2\pi = 0\), so the first term zero.

Let’s compute:
\[
I' = \int_{0}^{\frac{\pi}{2}} \theta \sin 4\theta\, d\theta
\]

Integration by parts:
Let \(u = \theta, dv = \sin 4\theta\, d\theta\), \(du = d\theta, v = -\frac{1}{4} \cos 4\theta\):

\[
I' = \left. -\frac{1}{4} \theta \cos 4\theta \right|_{0}^{\frac{\pi}{2}} + \frac{1}{4} \int_{0}^{\frac{\pi}{2}} \cos 4\theta d\theta
\]
Also,

\[
\int \cos 4\theta d\theta = \frac{1}{4} \sin 4\theta
\]
So,
\[
I' = -\frac{1}{4} \left[ \frac{\pi}{2} \cos 2\pi - 0 \cdot \cos 0 \right] + \frac{1}{4} \left[ \frac{1}{4} \sin 4\theta \right]_0^{\frac{\pi}{2}}
\]
\[
\cos 2\pi = 1; \sin 4\theta|_{\theta=0} = 0; \sin 4\theta|_{\theta=\frac{\pi}{2}} = \sin 2\pi = 0
\]
Hence,

\[
I' = -\frac{1}{4} \cdot \frac{\pi}{2} (1) + 0 = -\frac{\pi}{8}
\]

Therefore,
\[
C_2 = -\frac{1}{2} I' = -\frac{1}{2} \left(-\frac{\pi}{8}\right) = \frac{\pi}{16}
\]

---

### Step 8: Assemble all results

Now,
\[
A_1 = \frac{\pi^2}{8} \qquad A_2 = \frac{\pi^3}{24}
\]
\[
B_1 = -\frac{1}{2} \qquad B_2 = -\frac{\pi}{4}
\]
\[
C_1 = 0\qquad\;\;\;\;\;\;\;\;\; C_2 = \frac{\pi}{16}
\]

Plug into:

\[
J_1 = \frac{3}{8} A_1 - \frac{1}{2} B_1 + \frac{1}{8} C_1
= \frac{3}{8} \cdot \frac{\pi^2}{8} - \frac{1}{2} \cdot \left(-\frac{1}{2}\right) + 0
= \frac{3\pi^2}{64} + \frac{1}{4}
\]

\[
J_2 = \frac{3}{8} A_2 - \frac{1}{2} B_2 + \frac{1}{8} C_2
= \frac{3}{8} \cdot \frac{\pi^3}{24} - \frac{1}{2} \cdot \left(-\frac{\pi}{4}\right) + \frac{1}{8} \cdot \frac{\pi}{16}
\]
Compute each term:
- \(\frac{3}{8} \cdot \frac{\pi^3}{24} = \frac{3 \pi^3}{192} = \frac{\pi^3}{64}\)
- \(-\frac{1}{2} \cdot \left(-\frac{\pi}{4}\right) = \frac{\pi}{8}\)
- \(\frac{1}{8} \cdot \frac{\pi}{16} = \frac{\pi}{128}\)

Thus,

\[
J_2 = \frac{\pi^3}{64} + \frac{\pi}{8} + \frac{\pi}{128}
= \frac{\pi^3}{64} + \frac{17\pi}{128}
\]

---

Now,

\[
I = \frac{3}{4} J_2 - \frac{\pi}{4} J_1
\]

Calculate individually:

- \(\frac{3}{4} J_2 = \frac{3}{4} \left(\frac{\pi^3}{64} + \frac{17\pi}{128}\right) = \frac{3\pi^3}{256} + \frac{51\pi}{512}\)
- \(\frac{\pi}{4} J_1 = \frac{\pi}{4} \left( \frac{3\pi^2}{64} + \frac{1}{4} \right) = \frac{3\pi^3}{256} + \frac{\pi}{16}\)

Therefore,

\[
I = \left(\frac{3\pi^3}{256} + \frac{51\pi}{512}\right) - \left( \frac{3\pi^3}{256} + \frac{\pi}{16} \right ) = \frac{51\pi}{512} - \frac{\pi}{16}
\]
\[
= \pi \left( \frac{51}{512} - \frac{32}{512} \right ) = \pi \left( \frac{19}{512} \right )
\]

---

### Step 9: Final exact and numerical answers

Thus, the exact value is:

\[
I = \frac{19\pi}{512}
\]

Numerical value:

\[
I \approx \frac{19 \times 3.14159265358979323846}{512} \approx \frac{59.689260418206071}{512} \approx 0.1166126196
\]

(Actual computation: \(19 \times \pi = 59.690260418206066\), \(59.690260418206066/512 = 0.11660164222228253\))

To 10 decimal places: \(0.1166016422\)

---

### Step 10: JSON output

```json
{"answer": "\\frac{19\\pi}{512}", "numerical_answer": "0.1166016422"}
```