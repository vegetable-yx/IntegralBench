Let's solve the definite integral:
\[
I = \int_{1/\sqrt{2}}^1 \frac{\arcsin(x)}{x^3} \, dx
\]

**Step 1: Compute the indefinite integral analytically**

Let’s use integration by parts.

Let:
- \( u = \arcsin(x) \implies du = \frac{1}{\sqrt{1 - x^2}} dx \)
- \( dv = x^{-3} dx \implies v = \int x^{-3} dx = \frac{x^{-2}}{-2} = -\frac{1}{2x^2} \)

Applying integration by parts:
\[
\int \arcsin(x) x^{-3} dx = u v - \int v du
= \arcsin(x) \left(-\frac{1}{2x^2}\right) - \int \left(-\frac{1}{2x^2}\right) \cdot \frac{1}{\sqrt{1 - x^2}} dx
\]
\[
= -\frac{\arcsin(x)}{2 x^2} + \frac{1}{2} \int \frac{dx}{x^2 \sqrt{1-x^2}}
\]

So,
\[
I = \int_{1/\sqrt{2}}^1 \frac{\arcsin(x)}{x^3} dx = \left[ -\frac{\arcsin(x)}{2x^2} + \frac{1}{2} \int \frac{dx}{x^2 \sqrt{1 - x^2}} \right]_{x=1/\sqrt{2}}^{x=1}
\]

Now compute the remaining integral:
\[
J = \int \frac{dx}{x^2 \sqrt{1 - x^2}}
\]

Let’s use the substitution \( x = \sin \theta \implies dx = \cos \theta d\theta \), \( \sqrt{1-x^2} = \sqrt{1-\sin^2\theta} = \cos\theta \), \( x^2 = \sin^2\theta \):

\[
J = \int \frac{dx}{x^2 \sqrt{1-x^2}}
= \int \frac{\cos\theta d\theta}{\sin^2\theta \cos\theta}
= \int \frac{d\theta}{\sin^2\theta}
= \int \csc^2\theta \, d\theta
= -\cot\theta + C
\]

Recall that \( x = \sin\theta \implies \theta = \arcsin(x) \), and \( \cot\theta = \frac{\cos\theta}{\sin\theta} = \frac{\sqrt{1-x^2}}{x} \):

So
\[
J = -\cot(\arcsin x) = -\frac{ \sqrt{1 - x^2} }{ x }
\]

Plug back in:
\[
I = \left[ -\frac{\arcsin x}{2 x^2} + \frac{1}{2} \left( -\frac{ \sqrt{1 - x^2 } }{ x } \right) \right]_{x=1/\sqrt{2}}^{x=1}
\]
\[
= \left[ -\frac{\arcsin x}{2 x^2} - \frac{ \sqrt{1 - x^2 } }{ 2 x } \right]_{x=1/\sqrt{2}}^{x=1}
\]

**Step 2: Apply the limits**

First at \( x=1 \):

- \( \arcsin(1) = \frac{\pi}{2} \)
- \( x^2 = 1 \)
- \( \sqrt{1-x^2} = \sqrt{0} = 0 \)

At \( x=1/\sqrt{2} \):

- \( \arcsin(1/\sqrt{2}) = \arcsin(\sqrt{2}/2) = \frac{\pi}{4} \)
- \( x^2 = (1/\sqrt{2})^2 = 1/2 \)
- \( \sqrt{1 - x^2 } = \sqrt{1-1/2} = \sqrt{1/2} = 1/\sqrt{2} \)

Now calculate each piece:

At \(x=1\):
\[
-\frac{ \arcsin(1) }{ 2 \cdot 1^2 } - \frac{ 0 }{ 2 \cdot 1 } = -\frac{ \pi }{ 4 }
\]

At \(x=1/\sqrt{2}\):
\[
-\frac{ \arcsin(1/\sqrt{2}) }{ 2 (1/2) } - \frac{ (1/\sqrt{2}) }{ 2 \cdot (1/\sqrt{2}) }
= -\frac{ (\pi/4) }{ 1 } - \frac{ 1 }{ 2 }
= -\frac{\pi}{4} - \frac{1}{2}
\]

So, the difference is:

\[
I = \left(-\frac{\pi}{4}\right) - \left(-\frac{\pi}{4} - \frac{1}{2}\right) = \boxed{ \frac{1}{2} }
\]

**Step 3: Numerical approximation**

Clearly \(\frac{1}{2} = 0.5\) exactly.

Expanded to 10 decimal places: \(0.5000000000\).

**Step 4: Final answer in JSON format**

```json
{"answer": "\\frac{1}{2}", "numerical_answer": "0.5000000000"}
```