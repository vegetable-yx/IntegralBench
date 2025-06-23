Let's analyze and compute the integral:
\[
I = \int_{-1}^1\frac{\sin(\sqrt{x})}{\sinh(\sqrt{x})+\sin(\sqrt{x})}\,dx
\]

### Step 1: Symmetry analysis

Let us substitute \( x \mapsto -x \). We need to determine the parity of the integrand.

Let \( f(x) = \frac{\sin(\sqrt{x})}{\sinh(\sqrt{x})+\sin(\sqrt{x})} \).

**For negative arguments:**
- \(\sqrt{-x} = i \sqrt{x}\) for \( x \geq 0 \).
- \(\sin(i z) = i \sinh(z)\), \(\sinh(i z) = i \sin(z)\).

Let’s compute \( f(-x) \) for \( x \in [0,1] \):
\[
f(-x) = \frac{\sin(\sqrt{-x})}{\sinh(\sqrt{-x})+\sin(\sqrt{-x})}
\]
Let’s use \( y = \sqrt{x} \), so \( \sin(\sqrt{-x}) = \sin(i y) = i\sinh(y) \), \( \sinh(\sqrt{-x}) = \sinh(i y) = i\sin(y) \).

So,
\[
f(-x) = \frac{i\sinh(y)}{i\sin(y) + i\sinh(y)} = \frac{i\sinh(y)}{i(\sin(y) + \sinh(y))} = \frac{\sinh(y)}{\sin(y) + \sinh(y)}
\]
which is exactly the same as
\[
f(-x) = \frac{\sinh(\sqrt{x})}{\sin(\sqrt{x})+\sinh(\sqrt{x})}
\]
Thus, for real \( x \in [0,1] \),
\[
f(-x) = \frac{\sinh(\sqrt{x})}{\sin(\sqrt{x})+\sinh(\sqrt{x})}
\]

So, over the integral:
\[
I = \int_{-1}^1 f(x)\,dx = \int_{-1}^1 \frac{\sin(\sqrt{x})}{\sinh(\sqrt{x})+\sin(\sqrt{x})}\,dx
\]

Let’s split the integral:
\[
I = \int_0^1 f(x)\,dx + \int_{-1}^0 f(x)\,dx
\]
The second term can be rewritten (changing variable \( x \to -t \) with \( t \in [0,1] \)):
\[
\int_{-1}^0 f(x)\,dx = \int_1^0 f(-t)(-dt) = \int_0^1 f(-t)\,dt
\]
So,
\[
I = \int_0^1 f(x)\,dx + \int_0^1 f(-x)\,dx = \int_0^1 \left( f(x) + f(-x) \right)dx
\]
From above:
\[
f(x) = \frac{\sin(\sqrt{x})}{\sinh(\sqrt{x})+\sin(\sqrt{x})},\quad f(-x) = \frac{\sinh(\sqrt{x})}{\sin(\sqrt{x})+\sinh(\sqrt{x})}
\]
Therefore,
\[
f(x) + f(-x) = \frac{\sin(\sqrt{x}) + \sinh(\sqrt{x})}{\sin(\sqrt{x}) + \sinh(\sqrt{x})} = 1 \quad \text{for}~x > 0
\]

Thus,
\[
I = \int_{0}^{1} 1\,dx = 1
\]

### Step 2: Rewriting the full answer

Therefore, the value of the integral is exactly 1.

### Step 3: Numerical approximation

The numerical value to 10 decimal places is
\[
1.0000000000
\]

### Step 4: Output in JSON format:

```json
{"answer": "1", "numerical_answer": "1.0000000000"}
```