Let's solve the given integral step by step:

\[
I = \int_0^8 \frac{\cos\sqrt{x}}{\sqrt{x}}\, dx
\]

**Step 1: Substitution**

Let \( u = \sqrt{x} \implies x = u^2 \). Then, \( dx = 2u\, du \).

When \( x=0 \Rightarrow u=0 \) \
When \( x=8 \Rightarrow u=\sqrt{8}=2\sqrt{2} \)

The integrand transforms as:
\[
\frac{\cos\sqrt{x}}{\sqrt{x}}\, dx = \frac{\cos(u)}{u} \cdot 2u\, du = 2\cos(u) du
\]

So, changing variables:

\[
I = \int_{0}^{2\sqrt{2}} 2\cos(u)\, du
\]

**Step 2: Antiderivative**

The antiderivative:

\[
\int 2\cos(u)\, du = 2\sin(u) + C
\]

So our definite integral becomes:

\[
I = \left[ 2\sin(u) \right]_{0}^{2\sqrt{2}} = 2\sin\left( 2\sqrt{2} \right) - 2\sin(0)
\]
\[
= 2\sin(2\sqrt{2})
\]

**Step 3: Numerical Approximation**

Now, numerically approximate:

First, compute \(2\sqrt{2}\):

\[
\sqrt{2} \approx 1.4142135624 \implies 2\sqrt{2} \approx 2.8284271247
\]

Compute \(\sin(2.8284271247)\):

\[
\sin(2.8284271247) \approx 0.3095598756
\]

Thus,

\[
I \approx 2 \times 0.3095598756 = 0.6191197512
\]

**Final Answer:**

```json
{"answer": "2\\sin(2\\sqrt{2})", "numerical_answer": "0.6191197512"}
```