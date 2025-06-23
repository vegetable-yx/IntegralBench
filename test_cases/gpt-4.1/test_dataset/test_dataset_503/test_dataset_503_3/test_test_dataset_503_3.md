Let's proceed step by step.

## Step 1: Write the Integral

\[
I = \int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx
\]

## Step 2: Expand the Integrand

We can use the product-to-sum identities for cosines:

First, combine two of the cosines using:
\[
\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]
\]

Let’s first combine \(\cos(x)\) and \(\cos(3x)\):

\[
\cos(x)\cos(3x) = \frac{1}{2}[\cos(x-3x) + \cos(x+3x)] = \frac{1}{2}[\cos(-2x) + \cos(4x)]
\]
But \(\cos(-2x) = \cos(2x)\), so this is \(\frac{1}{2}[\cos(2x) + \cos(4x)]\).

So the full integrand is:
\[
\cos(x)\cos(3x)\cos(5x) = \frac{1}{2}[\cos(2x) + \cos(4x)]\cos(5x)
\]

Now use product-to-sum again:

- \(\cos(2x) \cos(5x) = \frac{1}{2}[\cos(2x-5x) + \cos(2x+5x)] = \frac{1}{2}[\cos(-3x) + \cos(7x)] = \frac{1}{2}[\cos(3x) + \cos(7x)]\)
- \(\cos(4x) \cos(5x) = \frac{1}{2}[\cos(4x-5x) + \cos(4x+5x)] = \frac{1}{2}[\cos(-x) + \cos(9x)] = \frac{1}{2}[\cos(x) + \cos(9x)]\)

So adding these together:

\[
\cos(x)\cos(3x)\cos(5x) = \frac{1}{2}\left(\frac{1}{2}[\cos(3x) + \cos(7x)] + \frac{1}{2}[\cos(x) + \cos(9x)]\right)
\]
\[
= \frac{1}{4}[\cos(3x) + \cos(7x) + \cos(x) + \cos(9x)]
\]
\[
= \frac{1}{4} \left( \cos(x) + \cos(3x) + \cos(7x) + \cos(9x) \right)
\]

## Step 3: Substitute Into the Integral

\[
I = \int_0^\pi \cos(x)\cos(3x)\cos(5x) dx \\
= \frac{1}{4} \int_0^\pi [\cos(x) + \cos(3x) + \cos(7x) + \cos(9x)] dx
\]
\[
= \frac{1}{4}\left[\int_0^\pi \cos(x) dx + \int_0^\pi \cos(3x) dx + \int_0^\pi \cos(7x) dx + \int_0^\pi \cos(9x) dx\right]
\]

## Step 4: Integrate Each Term

We use:
\[
\int_0^\pi \cos(ax) dx = \left. \frac{\sin(ax)}{a} \right|_0^\pi = \frac{\sin(a\pi) - \sin(0)}{a} = 0
\]
since \(\sin(a\pi) = 0\) for integer \(a\).

Thus, all terms vanish:

\[
\int_0^\pi \cos(x) dx = 0\\
\int_0^\pi \cos(3x) dx = 0\\
\int_0^\pi \cos(7x) dx = 0\\
\int_0^\pi \cos(9x) dx = 0\\
\]

## Step 5: Collect the Result

So the whole integral is zero.

\[
I = \boxed{0}
\]

## Step 6: Numerical Approximation

Numerically, the value is also \(0.0000000000\).

---

```json
{"answer": "0", "numerical_answer": "0.0000000000"}
```