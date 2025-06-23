Let's denote the integral as \( I \):
\[
I = \int_{0}^{1} \arcsin(x) \arccos(x) \, dx
\]

**Step 1: Use a substitution to relate \(\arcsin(x)\) and \(\arccos(x)\)**

Recall that:
\[
\arccos(x) = \frac{\pi}{2} - \arcsin(x)
\]
Therefore,
\[
I = \int_0^1 \arcsin(x) \left(\frac{\pi}{2} - \arcsin(x)\right) dx \\
= \frac{\pi}{2} \int_0^1 \arcsin(x) dx - \int_0^1 \arcsin(x)^2 dx
\]
Let:
\[
A = \int_0^1 \arcsin(x) dx, \quad B = \int_0^1 \arcsin(x)^2 dx
\]
Therefore,
\[
I = \frac{\pi}{2} A - B
\]

**Step 2: Compute \( A = \int_0^1 \arcsin(x) dx \)**

Use integration by parts:

Let \( u = \arcsin(x) \), \( dv = dx \).
Then \( du = \frac{1}{\sqrt{1-x^2}} dx \), \( v = x \).

So:
\[
A = u v \Big|_0^1 - \int_0^1 v du = x \arcsin(x) \Big|_0^1 - \int_0^1 x \frac{1}{\sqrt{1-x^2}} dx
\]

Evaluate \( x \arcsin(x) \Big|_0^1 = (1 \cdot \arcsin(1)) - (0 \cdot \arcsin(0)) = \frac{\pi}{2} \)

Now,
\[
\int_0^1 \frac{x}{\sqrt{1-x^2}} dx
\]
Let \( t = 1 - x^2 \), \( dt = -2x dx \implies -\frac{dt}{2} = x dx \),

So when \( x = 0 \): \( t = 1 \), \( x = 1 \): \( t = 0 \).

Thus:
\[
\int_0^1 \frac{x}{\sqrt{1-x^2}} dx = \int_{x=0}^{x=1} \frac{x}{\sqrt{1-x^2}} dx = \int_{t=1}^{0} \frac{1}{\sqrt{t}} \left( -\frac{dt}{2} \right )
= \frac{1}{2} \int_{0}^{1} t^{-1/2} dt = \frac{1}{2} \left[ 2 t^{1/2} \right]_{0}^{1} = \left [ t^{1/2} \right]_{0}^{1} = 1 - 0 = 1
\]

So,
\[
A = \frac{\pi}{2} - 1
\]

**Step 3: Compute \( B = \int_0^1 \arcsin(x)^2 dx \)**
Let’s use the identity:
\[
B = \int_0^1 \arcsin(x)^2 dx
\]

Let’s apply integration by parts:

Let \( u = \arcsin(x)^2 \), \( dv = dx \).
Then \( du = 2 \arcsin(x) \frac{1}{\sqrt{1-x^2}} dx \), \( v = x \).

So:
\[
B = u v \Big|_0^1 - \int_0^1 v du = x \arcsin(x)^2 \Big|_0^1 - \int_0^1 2 x \arcsin(x) \frac{1}{\sqrt{1-x^2}} dx
\]

At \( x = 1 \): \( \arcsin(1) = \frac{\pi}{2} \), so
\( x \arcsin(x)^2|_{x=1} = 1 \left(\frac{\pi}{2}\right)^2 = \frac{\pi^2}{4} \)
At \( x = 0 \): \( 0 \).

So,
\[
B = \frac{\pi^2}{4} - 2 \int_0^1 x \arcsin(x) \frac{1}{\sqrt{1-x^2}} dx
\]

Let’s compute:
\[
C = \int_0^1 x \arcsin(x) \frac{1}{\sqrt{1-x^2}} dx
\]

Let’s use substitution \( x = \sin \theta \), \( dx = \cos \theta d\theta \), when \( x=0, \theta=0 \), \( x=1, \theta=\frac{\pi}{2} \).

Then,
\[
x = \sin \theta,\quad \arcsin(x) = \theta,\quad \sqrt{1-x^2} = \cos \theta
\]
So,
\[
C = \int_{\theta=0}^{\frac{\pi}{2}} \sin \theta \cdot \theta \cdot \frac{1}{\cos \theta} \cdot \cos \theta d\theta = \int_{0}^{\frac{\pi}{2}} \theta \sin \theta d\theta
\]

So now, it reduces to:
\[
C = \int_0^{\frac{\pi}{2}} \theta \sin \theta d\theta
\]
This is a standard integral.

Use integration by parts:
Let \( u = \theta \), \( dv = \sin \theta d\theta \), \( du = d\theta \), \( v = -\cos \theta \).
So:
\[
C = -\theta \cos \theta \Big|_0^{\frac{\pi}{2}} + \int_0^{\frac{\pi}{2}} \cos \theta d\theta = -\theta \cos \theta \Big|_0^{\frac{\pi}{2}} + \sin \theta \Big|_0^{\frac{\pi}{2}}
\]

Evaluate:
At \( \theta = \frac{\pi}{2} \):

\( -\theta \cos \theta = -\frac{\pi}{2} \cdot 0 = 0 \), \( \sin \frac{\pi}{2} = 1 \)
At \( \theta = 0 \):

\( -0 \cdot 1 = 0 \), \( \sin 0 = 0 \)

So,
\[
C = (0 - 0) + (1 - 0) = 1
\]

So,
\[
B = \frac{\pi^2}{4} - 2C = \frac{\pi^2}{4} - 2 \cdot 1 = \frac{\pi^2}{4} - 2
\]

**Step 4: Substitute values of \( A \) and \( B \) into the main answer**

Recall:
\[
I = \frac{\pi}{2} A - B = \frac{\pi}{2} \left( \frac{\pi}{2} - 1 \right ) - \left( \frac{\pi^2}{4} - 2 \right )
\]

Expand:
\[
\frac{\pi}{2} \left( \frac{\pi}{2} - 1 \right ) = \frac{\pi^2}{4} - \frac{\pi}{2}
\]
So,
\[
I = \left( \frac{\pi^2}{4} - \frac{\pi}{2} \right ) - \left( \frac{\pi^2}{4} - 2 \right ) = \frac{\pi^2}{4} - \frac{\pi}{2} - \frac{\pi^2}{4} + 2 = - \frac{\pi}{2} + 2
\]
So,
\[
\boxed{I = 2 - \frac{\pi}{2}}
\]

**Step 5: Numerical value**

\(\pi \approx 3.1415926536\), so

\[
I \approx 2 - \frac{3.1415926536}{2} = 2 - 1.5707963268 = 0.4292036732
\]

**Step 6: JSON output**

```json
{"answer": "2 - \\frac{\\pi}{2}", "numerical_answer": "0.4292036732"}
```