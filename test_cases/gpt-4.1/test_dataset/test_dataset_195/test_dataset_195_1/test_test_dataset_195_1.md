Let's solve the integral:
\[
I = \int_0^1 \arcsin(x)\arccos(x) \, dx
\]

**Step 1: Make substitutions using trigonometric identities.**

Recall that for \( x \in [0,1] \):
\[
\arcsin(x) + \arccos(x) = \frac{\pi}{2} \implies \arccos(x) = \frac{\pi}{2} - \arcsin(x)
\]
So,
\[
I = \int_0^1 \arcsin(x)\left(\frac{\pi}{2} - \arcsin(x)\right) dx
  = \frac{\pi}{2} \int_0^1 \arcsin(x) dx - \int_0^1 \arcsin^2(x) dx
\]
Let’s denote:
\[
A = \int_0^1 \arcsin(x) dx, \quad B = \int_0^1 \arcsin^2(x) dx
\]
Hence,
\[
I = \frac{\pi}{2}A - B
\]

---

**Step 2: Compute \(A\): \( \int_0^1 \arcsin(x) dx \)**

Let \( x = \sin \theta \implies dx = \cos \theta d\theta \), as \( x \) goes from 0 to 1, \( \theta \) goes from 0 to \( \frac{\pi}{2} \).

\[
A = \int_{x=0}^{x=1} \arcsin(x) dx = \int_{\theta=0}^{\theta=\frac{\pi}{2}} \theta \cos \theta d\theta
\]

Integrate by parts:
Let \( u = \theta \), \( dv = \cos \theta d\theta \)
\[
du = d\theta,\, v = \sin \theta
\]

So,
\[
\int \theta \cos \theta d\theta = \theta \sin \theta - \int \sin \theta d\theta
= \theta \sin \theta + \cos \theta + C
\]

Evaluate from \( 0 \) to \( \frac{\pi}{2} \):

At \( \theta = \frac{\pi}{2} \):
\[
\frac{\pi}{2} \cdot \sin \frac{\pi}{2} + \cos \frac{\pi}{2} = \frac{\pi}{2} (1) + 0 = \frac{\pi}{2}
\]

At \( \theta = 0 \):
\[
0 \cdot \sin 0 + \cos 0 = 0 + 1 = 1
\]

So,
\[
A = \left[\theta \sin \theta + \cos \theta\right]_0^{\frac{\pi}{2}} = \frac{\pi}{2} - 1
\]

---

**Step 3: Compute \(B\): \( \int_0^1 \arcsin^2(x) dx \)**

Again, use \( x = \sin \theta \), \( dx = \cos \theta d\theta \)
\[
B = \int_{x=0}^{x=1} \arcsin^2(x) dx = \int_{\theta=0}^{\theta=\frac{\pi}{2}} \theta^2 \cos \theta d\theta
\]

Integrate by parts:

Let \( u = \theta^2, dv = \cos \theta d\theta \implies du = 2\theta d\theta, v = \sin \theta \):

\[
\int \theta^2 \cos \theta d\theta = \theta^2 \sin \theta - \int 2\theta \sin \theta d\theta
\]

Now, compute \( \int 2\theta \sin \theta d\theta \):

Let \( w = \theta, dt = \sin \theta d\theta \implies dw = d\theta, t = -\cos \theta \):

\[
\int \theta \sin \theta d\theta = -\theta \cos \theta + \int \cos \theta d\theta = -\theta \cos \theta + \sin \theta
\]

Therefore,
\[
\int 2\theta \sin \theta d\theta = 2 (-\theta \cos \theta + \sin \theta)
\]
So,
\[
\int \theta^2 \cos \theta d\theta = \theta^2 \sin \theta - 2 (-\theta \cos \theta + \sin \theta)
= \theta^2 \sin \theta + 2\theta \cos \theta - 2\sin \theta
\]

Evaluate from \( 0 \) to \( \frac{\pi}{2} \):

At \( \theta = \frac{\pi}{2} \):

\[
\left(\frac{\pi}{2}\right)^2 \sin \frac{\pi}{2} + 2 \cdot \frac{\pi}{2} \cos \frac{\pi}{2} - 2 \sin \frac{\pi}{2}
= \frac{\pi^2}{4}(1) + 2\cdot \frac{\pi}{2} \cdot 0 - 2 \cdot 1
= \frac{\pi^2}{4} - 2
\]

At \( \theta = 0 \):

\[
0^2 \sin 0 + 2 \cdot 0 \cos 0 - 2 \sin 0 = 0 + 0 - 0 = 0
\]

Thus,
\[
B = (\frac{\pi^2}{4} - 2) - 0 = \frac{\pi^2}{4} - 2
\]

---

**Step 4: Combine results**

We have:
\[
I = \frac{\pi}{2}A - B = \frac{\pi}{2}\left(\frac{\pi}{2} - 1\right) - \left(\frac{\pi^2}{4} - 2\right)
\]

\[
I = \left(\frac{\pi^2}{4} - \frac{\pi}{2}\right) - \frac{\pi^2}{4} + 2
= -\frac{\pi}{2} + 2
\]

So the **exact answer** is:
\[
I = 2 - \frac{\pi}{2}
\]

---

**Step 5: Numerical approximation**

\[
2 - \frac{\pi}{2} \approx 2 - \frac{3.141592653589793}{2} \approx 2 - 1.5707963267948966 \approx 0.4292036732
\]

(Rounded to 10 decimal places.)

---

Final answer:
```json
{"answer": "2 - \\frac{\\pi}{2}", "numerical_answer": "0.4292036732"}
```