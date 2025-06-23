Let's solve the integral:
\[
I = \int_0^\pi \cos(x)\cos(3x)\cos(5x)dx
\]

**Step 1: Expand the product of cosines**

We can use the product-to-sum formulas:
\[
\cos(A)\cos(B) = \frac{1}{2}[\cos(A+B) + \cos(A-B)]
\]

Let’s first combine two of them, say, \(\cos(3x)\cos(5x)\):
\[
\cos(3x)\cos(5x) = \frac{1}{2} [\cos(3x + 5x) + \cos(3x - 5x)]
= \frac{1}{2} [\cos(8x) + \cos(-2x)]
= \frac{1}{2} [\cos(8x) + \cos(2x)]
\]

Now multiply by \(\cos(x)\):
\[
I = \int_0^\pi \cos(x) \cdot \frac{1}{2} [\cos(8x) + \cos(2x)] dx
= \frac{1}{2} \int_0^\pi \cos(x)\cos(8x)dx + \frac{1}{2} \int_0^\pi \cos(x)\cos(2x)dx
\]

Let’s expand each term using the product-to-sum again:
\[
\cos(x)\cos(8x) = \frac{1}{2} [\cos(x+8x) + \cos(x-8x)] = \frac{1}{2} [\cos(9x) + \cos(-7x)] = \frac{1}{2} [\cos(9x) + \cos(7x)]
\]
\[
\cos(x)\cos(2x) = \frac{1}{2} [\cos(x+2x) + \cos(x-2x)] = \frac{1}{2} [\cos(3x) + \cos(-x)] = \frac{1}{2} [\cos(3x) + \cos(x)]
\]

So, our integral becomes:
\[
I = \frac{1}{2}\left( \int_0^\pi \frac{1}{2}[\cos(9x) + \cos(7x)] dx + \int_0^\pi \frac{1}{2}[\cos(3x) + \cos(x)] dx \right)
\]
\[
= \frac{1}{4} \int_0^\pi \cos(9x)dx + \frac{1}{4} \int_0^\pi \cos(7x)dx + \frac{1}{4} \int_0^\pi \cos(3x)dx + \frac{1}{4} \int_0^\pi \cos(x)dx
\]

**Step 2: Integrate each term**

\[
\int_0^\pi \cos(ax)dx = \left[\frac{1}{a}\sin(ax)\right]_0^\pi = \frac{1}{a}(\sin(a\pi) - \sin(0)) = 0 \text{ for integer } a
\]
because \(\sin(a\pi) = 0\), \(\sin(0) = 0\).

So:

- \(\int_0^\pi \cos(9x)dx = 0\)
- \(\int_0^\pi \cos(7x)dx = 0\)
- \(\int_0^\pi \cos(3x)dx = 0\)
- \(\int_0^\pi \cos(x)dx = 0\)

But let's double-check \(\int_0^\pi \cos(x)dx\):

\[
\int_0^\pi \cos(x)dx = \sin(x)\Big|_0^\pi = \sin(\pi) - \sin(0) = 0-0=0
\]

Similarly, the others, since the sine of integer multiples of \(\pi\) is zero.

**Step 3: Therefore,**
\[
I = 0
\]

**Step 4: Numerical Approximation**
\[
0.0000000000
\]

---

{"answer": "0", "numerical_answer": "0.0000000000"}