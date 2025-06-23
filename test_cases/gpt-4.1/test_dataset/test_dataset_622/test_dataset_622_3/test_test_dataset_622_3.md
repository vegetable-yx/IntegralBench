Let's compute:

\[
I = \int_0^{\frac{\pi}{2}} \frac{\cos^2 x (1 + \cos x)}{(1 + \cos x + \sin x)^2} \, dx
\]

**Step 1: Simplifying the Denominator**

First, let’s write the denominator:

\[
1 + \cos x + \sin x
\]

Set \( \sin x + \cos x = \sqrt{2}\sin(x + \frac{\pi}{4}) \), so

\[
1 + \sin x + \cos x = 1 + \sqrt{2}\sin(x + \frac{\pi}{4})
\]

**Step 2: Substitution**

Let’s try substituting \( x \to \frac{\pi}{2} - x \):

- \( \sin x \to \cos x \)
- \( \cos x \to \sin x \)
- \( dx \to -dx \)

Setting \( t = \frac{\pi}{2} - x \), as \( x: 0 \to \frac{\pi}{2} \), \( t: \frac{\pi}{2} \to 0 \).
So:

\[
I = \int_0^{\frac{\pi}{2}} \frac{\cos^2 x (1+\cos x)}{(1+\cos x+\sin x)^2}dx
= \int_0^{\frac{\pi}{2}} \frac{\sin^2 x (1+\sin x)}{(1+\sin x+\cos x)^2}dx
\]

Therefore, the integral is invariant under \( x \to \frac{\pi}{2} - x \). Let's use symmetry.

Let \( I_1 \) be the original integrand,
and \( I_2 \) be its mirrored partner:

\[
I = \frac{1}{2} \int_0^{\frac{\pi}{2}} \left[
\frac{\cos^2 x (1+\cos x)}{(1+\cos x+\sin x)^2}
+ \frac{\sin^2 x (1+\sin x)}{(1+\sin x+\cos x)^2}
\right] dx
\]

Let’s add the terms in the numerator:

Write the full numerator:
\[
A = \cos^2 x (1+\cos x)(1+\sin x+\cos x)^2 + \sin^2 x (1+\sin x)(1+\cos x+\sin x)^2
\]
But we note \( (1+\cos x+\sin x)^2 = (1+\sin x+\cos x)^2 \), so in the denominator,
the terms are the same.

Alternatively, stick with the original integral and proceed with a substitution.

**Step 3: Substitute \( t = \tan \frac{x}{2} \)**

Let’s use the Weierstrass substitution:

Let \( t = \tan \frac{x}{2} \), so \( x = 2 \arctan t \), as \( x: 0 \to \frac{\pi}{2} \), \( t: 0 \to 1 \).

Recall:

\[
\sin x = \frac{2 t}{1 + t^2}
\]
\[
\cos x = \frac{1 - t^2}{1 + t^2}
\]
\[
dx = \frac{2}{1 + t^2} dt
\]

Now substitute:

First, compute the numerator:

\[
\cos^2 x (1+\cos x) = (\cos^2 x)(1 + \cos x)
= \left(\frac{1 - t^2}{1 + t^2}\right)^2 \left(1 + \frac{1 - t^2}{1 + t^2}\right)
\]

Calculate \( 1 + \cos x = \frac{2}{1 + t^2} \):

So,
\[
\cos^2 x (1+\cos x) = \left(\frac{(1 - t^2)^2}{(1 + t^2)^2}\right) \cdot \frac{2}{1 + t^2}
= \frac{2 (1 - t^2)^2}{(1 + t^2)^3}
\]

Now, denominator:

\[
1 + \cos x + \sin x = 1 + \frac{1 - t^2}{1 + t^2} + \frac{2t}{1 + t^2}
= \frac{1 + t^2 + 1 - t^2 + 2t}{1 + t^2}
= \frac{2 + 2t}{1 + t^2}
= \frac{2(1 + t)}{1 + t^2}
\]
So:

\[
(1 + \cos x + \sin x)^2 = \left( \frac{2(1 + t)}{1 + t^2} \right)^2
= \frac{4(1 + t)^2}{(1 + t^2)^2}
\]

And \( dx = \frac{2 dt}{1 + t^2} \).

Put it together:

\[
I = \int_{x=0}^{x=\frac{\pi}{2}} \frac{\cos^2 x (1+\cos x)}{(1+\cos x+\sin x)^2} dx
= \int_{t=0}^{t=1} \frac{2 (1 - t^2)^2}{(1 + t^2)^3} \cdot \frac{(1 + t^2)^2}{4 (1 + t)^2} \cdot \frac{2}{1 + t^2} dt
\]

Multiply numerators and denominators:

Numerator: \( 2 \cdot 2 \cdot (1 - t^2)^2 = 4(1 - t^2)^2 \)
Denominator: \( 4 (1 + t)^2 (1 + t^2)^2 (1 + t^2) \), but be careful, the \( (1 + t^2)^2 \) cancels.

Let's check step-by-step:

Start:

\[
\frac{\cos^2x (1+\cos x) dx}{
(1+\cos x+\sin x)^2
}
= \frac{2(1 - t^2)^2}{(1 + t^2)^3}
\cdot
\frac{(1 + t^2)^2}{4(1 + t)^2}
\cdot \frac{2 dt}{1 + t^2}
\]

Multiply:

Numerator: \(2 \times 2 = 4\) and \( (1-t^2)^2 \) and \( dt \)
Denominator: \( (1+t^2)^3 \times 4(1+t)^2 \times (1+t^2) \)
But \( (1 + t^2)^3 \) in numerator-denominator cancels one of the powers

So:

\[
\frac{4 (1 - t^2)^2}{4 (1 + t)^2 (1 + t^2)^2} dt
= \frac{(1 - t^2)^2}{(1 + t)^2 (1 + t^2)^2} dt
\]

Therefore,

\[
I = \int_0^1 \frac{(1 - t^2)^2}{(1 + t)^2 (1 + t^2)^2} dt
\]

Expand numerator:

\[
(1 - t^2)^2 = 1 - 2 t^2 + t^4
\]

So:

\[
I = \int_0^1 \frac{1 - 2 t^2 + t^4}{(1 + t)^2 (1 + t^2)^2} dt
= \int_0^1 \frac{1}{(1 + t)^2 (1 + t^2)^2} dt
- 2 \int_0^1 \frac{t^2}{(1 + t)^2 (1 + t^2)^2} dt
+ \int_0^1 \frac{t^4}{(1 + t)^2 (1 + t^2)^2} dt
\]

Alternatively, group these:

\[
I = \int_0^1 \frac{1 - 2 t^2 + t^4}{(1 + t)^2 (1 + t^2)^2} dt
\]

**Step 4: Partial Fraction Decomposition**

Let’s try to decompose the rational function.

Let’s write:

\[
\frac{1 - 2t^2 + t^4}{(1 + t)^2 (1 + t^2)^2}
\]

Let’s try to write:

\[
\frac{1 - 2 t^2 + t^4}{(1 + t)^2 (1 + t^2)^2}
= \frac{A}{1 + t} + \frac{B}{(1 + t)^2} + \frac{C t + D}{1 + t^2} + \frac{E t + F}{(1 + t^2)^2}
\]

Multiply both sides by \( (1 + t)^2 (1 + t^2)^2 \):

\[
1 - 2t^2 + t^4 = A (1 + t)(1 + t^2)^2
+ B (1 + t^2)^2
+ (C t + D)(1 + t)^2 (1 + t^2)
+ (E t + F)(1 + t)^2
\]

Let’s expand each term:

Calculate \( (1 + t^2)^2 = 1 + 2 t^2 + t^4 \)
and \( (1 + t)^2 = 1 + 2 t + t^2 \)

First, let’s try to make the denominator simpler by writing the integrand as

\[
\frac{(1 - t^2)^2}{(1 + t)^2 (1 + t^2)^2}
\]

Let’s observe that \( (1 - t^2) = (1 - t)(1 + t) \), so \( (1 - t^2)^2 = (1 - t)^2 (1 + t)^2 \), so

\[
\frac{(1 - t^2)^2}{(1 + t)^2 (1 + t^2)^2}
= \frac{(1 - t)^2}{(1 + t^2)^2}
\]

That’s a key simplification!

**Therefore:**

\[
I = \int_0^1 \frac{(1 - t)^2}{(1 + t^2)^2} dt
\]

Let’s expand numerator:

\[
(1 - t)^2 = 1 - 2 t + t^2,
\]
so:

\[
I = \int_0^1 \frac{1 - 2 t + t^2}{(1 + t^2)^2} dt
= \int_0^1 \frac{1}{(1 + t^2)^2} dt
- 2 \int_0^1 \frac{t}{(1 + t^2)^2} dt
+ \int_0^1 \frac{t^2}{(1 + t^2)^2} dt
\]

Let’s treat each integral.

---

### Compute Each Term

**(a) First Integral**

\[
I_1 = \int_0^1 \frac{1}{(1 + t^2)^2} dt
\]

Let’s recall:

\[
\int \frac{1}{(a^2 + x^2)^2} dx = \frac{x}{2 a^2 (a^2 + x^2)} + \frac{1}{2 a^3} \arctan \frac{x}{a} + C
\]

For \( a = 1 \):

\[
\int \frac{1}{(1 + x^2)^2} dx = \frac{x}{2 (1 + x^2)} + \frac{1}{2} \arctan x + C
\]

So,

\[
I_1 = \left[
\frac{t}{2 (1 + t^2)} + \frac{1}{2} \arctan t
\right]_0^1
= \left(\frac{1}{2 (1 + 1^2)} + \frac{1}{2} \arctan 1\right) - \left(0 + \frac{1}{2} \arctan 0\right)
\]
\[
= \frac{1}{4} + \frac{1}{2} \cdot \frac{\pi}{4}
\]

**(b) Second Integral**

\[
I_2 = \int_0^1 \frac{t}{(1 + t^2)^2} dt
\]

Let \( u = 1 + t^2, du = 2 t dt \), so \( t dt = \frac{du}{2} \),
when \( t = 0, u = 1 \), when \( t = 1, u = 2 \):

So,

\[
I_2 = \int_{t=0}^{t=1} \frac{t}{(1 + t^2)^2} dt
= \frac{1}{2} \int_{u=1}^{u=2} u^{-2} du
= \frac{1}{2} \left[-u^{-1}\right]_1^2
= \frac{1}{2} \left(-\frac{1}{2} + 1\right)
= \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}
\]

**(c) Third Integral**

\[
I_3 = \int_0^1 \frac{t^2}{(1 + t^2)^2} dt
\]

Observe:

\[
\frac{t^2}{(1+t^2)^2}
= \frac{1}{1 + t^2} - \frac{1}{(1 + t^2)^2}
\]

So,

\[
I_3 = \int_0^1 \frac{1}{1 + t^2} dt - \int_0^1 \frac{1}{(1 + t^2)^2} dt
= \left[\arctan t\right]_0^1 - I_1
\]
\[
= \arctan 1 - \arctan 0 - I_1 = \frac{\pi}{4} - I_1
\]

--- 

Now sum all the pieces:

\[
I = I_1 - 2 I_2 + I_3 = I_1 - 2 I_2 + I_3
\]

Substitute what we have:

\(
I_2 = \frac{1}{4}
\), \(
I_3 = \frac{\pi}{4} - I_1
\), \(I_1\) as above.

So:

\[
I = I_1 - 2 \cdot \frac{1}{4} + (\frac{\pi}{4} - I_1)
= I_1 - \frac{1}{2} + \frac{\pi}{4} - I_1 = \frac{\pi}{4} - \frac{1}{2}
\]

Therefore, the terms \( I_1 \) cancels out!

\[
\boxed{I = \frac{\pi}{4} - \frac{1}{2}}
\]

---

**Step 5: Numerical Approximation**

\[
I = \frac{\pi}{4} - \frac{1}{2} \approx 0.7853981634 - 0.5 = 0.2853981634
\]

So, rounded to 10 decimal places: 0.2853981634

---

**Step 6: JSON Output**

```json
{"answer": "\\frac{\\pi}{4} - \\frac{1}{2}", "numerical_answer": "0.2853981634"}
```