Let's compute the definite integral:
\[
I= \int_0^1\left(\frac{x^2}{2-x^2}+\sqrt{\frac{2x}{x+1}}\right)\:dx
\]

We'll handle each term separately.

---

### 1. Integral of \(\frac{x^2}{2-x^2}\) from 0 to 1

First, we rewrite the integrand:
\[
\frac{x^2}{2-x^2} = \frac{2-x^2 - 2}{2-x^2} = 1 - \frac{2}{2-x^2}
\]
so
\[
\int_0^1 \frac{x^2}{2-x^2} dx = \int_0^1 1 dx - 2 \int_0^1 \frac{1}{2-x^2} dx
\]
The first integral is straightforward:
\[
\int_0^1 1\,dx = 1
\]

Now, compute \(\int_0^1 \frac{1}{2-x^2} dx\):

Let’s factor the denominator:
\[
2-x^2 = (\sqrt{2}-x)(\sqrt{2}+x)
\]

Let's use partial fractions:
\[
\frac{1}{2-x^2} = \frac{1}{(\sqrt{2}-x)(\sqrt{2}+x)}
\]

Write as:
\[
\frac{1}{2-x^2} = \frac{A}{\sqrt{2}-x} + \frac{B}{\sqrt{2}+x}
\]
Multiplying both sides by \(2-x^2\):
\[
1 = A(\sqrt{2}+x)+B(\sqrt{2}-x)
\]
Plug \(x = \sqrt{2}\):
\[
1 = A(2 \sqrt{2}), \implies A = \frac{1}{2\sqrt{2}}
\]
Plug \(x = -\sqrt{2}\):
\[
1 = B(2\sqrt{2}) \implies B = \frac{1}{2\sqrt{2}}
\]
So,
\[
\frac{1}{2-x^2} = \frac{1}{2\sqrt{2}}\left[\frac{1}{\sqrt{2}-x}+\frac{1}{\sqrt{2}+x}\right]
\]

Thus,
\[
\int_0^1 \frac{1}{2-x^2} dx = \frac{1}{2\sqrt{2}} \int_0^1 \left(\frac{1}{\sqrt{2}-x}+\frac{1}{\sqrt{2}+x}\right) dx
\]

Integrate term by term:
\[
\int_0^1 \frac{1}{\sqrt{2}-x} dx = -\ln | \sqrt{2} - x | \Big|_0^1 = -\ln (\sqrt{2} - 1) + \ln \sqrt{2}
\]
\[
\int_0^1 \frac{1}{\sqrt{2}+x} dx = \ln | \sqrt{2} + x | \Big|_0^1 = \ln (\sqrt{2} + 1) - \ln \sqrt{2}
\]

Therefore,
\[
\int_0^1 \frac{1}{2-x^2} dx = \frac{1}{2\sqrt{2}}\left( -\ln (\sqrt{2} - 1) + \ln (\sqrt{2}) + \ln (\sqrt{2} + 1) - \ln (\sqrt{2}) \right) 
\]
\[
= \frac{1}{2\sqrt{2}}\left( -\ln (\sqrt{2} - 1) + \ln (\sqrt{2} + 1) \right )
\]
\[
= \frac{1}{2\sqrt{2}} \ln \left( \frac{\sqrt{2}+1}{\sqrt{2}-1} \right )
\]

Recall that the original term to integrate was:
\[
\int_0^1 \frac{x^2}{2-x^2} dx = 1 - 2 \int_0^1 \frac{1}{2-x^2} dx
\]
\[
= 1 - 2 \times \frac{1}{2\sqrt{2}} \ln \left( \frac{\sqrt{2}+1}{\sqrt{2}-1} \right )
\]
\[
= 1 - \frac{1}{\sqrt{2}} \ln \left( \frac{\sqrt{2}+1}{\sqrt{2}-1} \right )
\]

---

### 2. Integral of \(\sqrt{\frac{2x}{x+1}}\) from 0 to 1

Let’s set \(I_2 = \int_0^1 \sqrt{\frac{2x}{x+1}} dx\).

Let’s make the substitution \(x = t^2\), with \(dx = 2t dt\), and as \(x\) goes from 0 to 1, \(t\) goes from 0 to 1.

Plug in:
\[
\sqrt{\frac{2x}{x+1}} = \sqrt{\frac{2t^2}{t^2+1}} = t \sqrt{\frac{2}{t^2 + 1}}
\]

Now, \(dx = 2t dt\):

\[
I_2 = \int_0^1 t \sqrt{\frac{2}{t^2 + 1}} \cdot 2t dt = 2 \int_0^1 t^2 \sqrt{\frac{2}{t^2 + 1}} dt
\]

Now,
\[
2 \int_0^1 t^2 \sqrt{\frac{2}{t^2 + 1}} dt = 2 \sqrt{2} \int_0^1 \frac{t^2}{\sqrt{t^2 + 1}} dt
\]

Let’s handle the integral:
\[
\int_0^1 \frac{t^2}{\sqrt{t^2+1}} dt
\]
Recall that:
\[
\int \frac{x^2}{\sqrt{x^2+1}} dx = \int \left( \sqrt{x^2+1} - \frac{1}{\sqrt{x^2+1}} \right ) dx
\]
Because:
\[
\frac{x^2}{\sqrt{x^2+1}} = \sqrt{x^2+1} - \frac{1}{\sqrt{x^2+1}}
\]

So,
\[
\int_0^1 \frac{t^2}{\sqrt{t^2+1}} dt = \int_0^1 \sqrt{t^2+1} dt - \int_0^1 \frac{1}{\sqrt{t^2+1}} dt
\]

Let's compute both:

**A.** \(\displaystyle \int_0^1 \sqrt{t^2+1} dt\):

We can use:
\[
\int \sqrt{t^2+1}\, dt = \frac12 t \sqrt{t^2+1} + \frac12 \sinh^{-1}(t)
\]

**B.** \(\displaystyle \int_0^1 \frac{1}{\sqrt{t^2+1}} dt\):

We can use:
\[
\int \frac{1}{\sqrt{t^2+1}} dt = \sinh^{-1}(t)
\]

Compute over limits 0 to 1:

- For \(t=0\): \(\sqrt{0+1}=1\), \(0 \cdot 1 = 0\), \(\sinh^{-1}(0) = 0\).
- For \(t=1\): \(\sqrt{1+1} = \sqrt{2}\), \(1 \cdot \sqrt{2} = \sqrt{2}\), \(\sinh^{-1}(1) = \ln(1 + \sqrt{2})\).

Now,
\[
\int_0^1 \sqrt{t^2+1} dt = \left[ \frac12 t \sqrt{t^2+1} + \frac12 \sinh^{-1}(t) \right]_0^1
\]
At \(t=1\):
\[
\frac12 \cdot 1 \cdot \sqrt{2} + \frac12 \ln(1 + \sqrt{2}) = \frac{\sqrt{2}}{2} + \frac12 \ln(1 + \sqrt{2})
\]
At \(t=0\), both terms are 0.

So,
\[
\int_0^1 \sqrt{t^2+1} dt = \frac{\sqrt{2}}{2} + \frac12 \ln(1 + \sqrt{2})
\]

Now,
\[
\int_0^1 \frac{1}{\sqrt{t^2+1}} dt = \sinh^{-1}(1) - \sinh^{-1}(0) = \ln(1+\sqrt{2}) - 0 = \ln(1+\sqrt{2})
\]

Therefore,
\[
\int_0^1 \frac{t^2}{\sqrt{t^2+1}} dt = \left(\frac{\sqrt{2}}{2} + \frac12 \ln(1+\sqrt{2})\right) - \ln(1+\sqrt{2}) = \frac{\sqrt{2}}{2} - \frac12 \ln(1+\sqrt{2})
\]

Plug back into \(I_2\):
\[
I_2 = 2\sqrt{2} \left( \frac{\sqrt{2}}{2} - \frac12 \ln(1 + \sqrt{2}) \right )
\]
\[
= \sqrt{2}^2 - \sqrt{2} \ln(1+\sqrt{2})
\]
\[
= 2 - \sqrt{2} \ln (1+\sqrt{2})
\]

---

### 3. Combine the results

Add both parts:

\[
I = \left[1 - \frac{1}{\sqrt{2}} \ln \left( \frac{\sqrt{2}+1}{\sqrt{2}-1} \right)\right] + \left[2 - \sqrt{2} \ln(1+\sqrt{2})\right]
\]

\[
I = 3 - \sqrt{2} \ln (1+\sqrt{2}) - \frac{1}{\sqrt{2}} \ln\left(\frac{\sqrt{2}+1}{\sqrt{2}-1}\right)
\]

---

### 4. Simplify the logarithmic terms

Let’s try to see if a further simplification is possible.

Notice that \(\frac{\sqrt{2}+1}{\sqrt{2}-1}\) can be rationalized:

\[
\frac{\sqrt{2}+1}{\sqrt{2}-1} = \frac{(\sqrt{2}+1)(\sqrt{2}+1)}{(\sqrt{2}-1)(\sqrt{2}+1)} = \frac{(\sqrt{2}+1)^2}{2-1} = (\sqrt{2}+1)^2
\]
so
\[
\ln \left( \frac{\sqrt{2}+1}{\sqrt{2}-1}\right ) = \ln \left( (\sqrt{2}+1)^2 \right ) = 2 \ln (\sqrt{2}+1)
\]

So the answer becomes:
\[
I = 3 - \sqrt{2} \ln(1+\sqrt{2}) - \frac{1}{\sqrt{2}}\cdot 2 \ln(\sqrt{2}+1) 
\]
\[
= 3 - \sqrt{2} \ln(1+\sqrt{2}) - \frac{2}{\sqrt{2}} \ln(\sqrt{2}+1)
\]
\[
= 3 - \sqrt{2} \ln(1+\sqrt{2}) - \sqrt{2} \ln(\sqrt{2}+1)
\]
\[
= 3 - \sqrt{2} \left[ \ln(1+\sqrt{2}) + \ln(\sqrt{2}+1) \right ]
\]
\[
= 3 - \sqrt{2} \cdot \ln \left( (1+\sqrt{2})^2 \right )
\]
\[
= 3 - 2\sqrt{2} \ln(1+\sqrt{2})
\]

---

### 5. Numerical Value (rounded to 10 decimal places)

Let’s calculate \(1 + \sqrt{2}\):
\[
\sqrt{2} \approx 1.4142135623730951
\]
\[
1+\sqrt{2} \approx 2.4142135623730951
\]
\[
\ln(1+\sqrt{2}) \approx \ln(2.4142135623730951) \approx 0.881373587019543
\]

Now,
\[
I \approx 3 - 2\sqrt{2} \times 0.881373587019543
\]
\[
2\sqrt{2} \approx 2 \times 1.4142135623730951 \approx 2.8284271247461903
\]
\[
2.8284271247461903 \times 0.881373587019543 \approx 2.492295255531683
\]
\[
I \approx 3 - 2.492295255531683 = 0.507704744468317
\]

Rounded to 10 decimal places: **0.5077047445**

---

### Final JSON Output

```json
{"answer": "3 - 2\\sqrt{2}\\ln(1+\\sqrt{2})", "numerical_answer": "0.5077047445"}
```