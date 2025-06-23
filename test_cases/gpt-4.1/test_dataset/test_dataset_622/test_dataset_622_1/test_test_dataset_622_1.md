Let's evaluate:

\[
I = \int_0^{\frac{\pi}{2}}\frac{\cos^2x(1+\cos x)}{(1+\cos x+\sin x)^2}\mathrm{d}x
\]

**Step 1: Simplify the denominator**

Let’s try the substitution:
\[
u = 1+\cos x+\sin x
\]

First, compute \( du \):

\[
\frac{du}{dx} = -\sin x + \cos x = \cos x - \sin x
\]
So,
\[
du = (\cos x - \sin x) dx
\]

Now, express everything in terms of \( u \).

Note the following:

- \(\cos x = C\), \(\sin x = S\)
- \(u = 1 + C + S\)

**Step 2: Express everything in terms of \( u \), \( C \) and \( S \) if possible**

Also, let's try another substitution, since the numerator contains \( \cos^2 x (1+\cos x) \) and the denominator contains \( 1+\cos x+\sin x \).

Alternatively, let’s use another substitution:
\[
t = \tan \frac{x}{2}
\]

Recall the Weierstrass substitution:

\[
\begin{align*}
\sin x &= \frac{2t}{1+t^2} \\
\cos x &= \frac{1-t^2}{1+t^2} \\
dx &= \frac{2}{1+t^2} dt
\end{align*}
\]

When \( x = 0 \), \( t = 0 \)
When \( x = \frac{\pi}{2} \), \( t = 1 \)

Now rewrite everything in terms of \( t \):

\[
\cos x = \frac{1-t^2}{1+t^2}, \quad \sin x = \frac{2t}{1+t^2}
\]

So,

\[
1+\cos x = 1 + \frac{1-t^2}{1+t^2} = \frac{1+t^2+1-t^2}{1+t^2} = \frac{2}{1+t^2}
\]

\[
1+\cos x+\sin x = \frac{2}{1+t^2} + \frac{2t}{1+t^2} = \frac{2+2t}{1+t^2} = \frac{2(1+t)}{1+t^2}
\]

So,

\[
(1+\cos x+\sin x)^2 = \frac{4 (1+t)^2}{(1+t^2)^2}
\]

Now, \(\cos^2 x = \left( \frac{1-t^2}{1+t^2} \right)^2 = \frac{(1-t^2)^2}{(1+t^2)^2}\)

And the numerator:

\[
\cos^2 x (1+\cos x) 
= \frac{(1-t^2)^2}{(1+t^2)^2} \cdot \left( \frac{2}{1+t^2} \right)
= \frac{2 (1-t^2)^2}{(1+t^2)^3}
\]

The integrand becomes:

\[
\frac{\cos^2 x (1+\cos x)}{\left( 1+\cos x + \sin x \right)^2 }
= \frac{2 (1-t^2)^2}{(1+t^2)^3} \div \frac{4 (1+t)^2}{(1+t^2)^2}
= \frac{2 (1-t^2)^2}{(1+t^2)^3} \cdot \frac{(1+t^2)^2}{4(1+t)^2}
= \frac{2 (1-t^2)^2}{4 (1+t)^2 (1+t^2)}
= \frac{(1-t^2)^2}{2 (1+t)^2 (1+t^2)}
\]

And \( dx = \frac{2}{1+t^2} dt \)

So the integral becomes:

\[
I = \int_{t=0}^{t=1} \frac{(1-t^2)^2}{2 (1+t)^2 (1+t^2)} \cdot \frac{2}{1+t^2} dt
= \int_{0}^1 \frac{(1-t^2)^2}{(1+t)^2 (1+t^2)^2} dt
\]

Now expand numerator:

\[
(1-t^2)^2 = 1 - 2t^2 + t^4
\]

So,

\[
I = \int_{0}^1 \frac{1-2t^2+t^4}{(1+t)^2 (1+t^2)^2} dt
\]

Let’s try to split/expand the integrand.

But first, notice that:

- \( (1+t)^2 = 1 + 2t + t^2 \)
- \( (1+t^2)^2 = 1 + 2t^2 + t^4 \)

But it's better to write as is.

**Step 3: Decompose the fraction**

Let’s try to express as a sum of simpler rational functions.

Let’s write

\[
\frac{1 - 2t^2 + t^4}{(1 + t)^2 (1 + t^2)^2}
\]

Let’s attempt partial fraction decomposition:

Assume:

\[
\frac{1 - 2t^2 + t^4}{(1 + t)^2 (1 + t^2)^2} 
= \frac{A}{1+t} + \frac{B}{(1+t)^2} + \frac{Ct+D}{1+t^2} + \frac{Et+F}{(1+t^2)^2}
\]

Let’s write the right-hand side with all denominators combined; equate coefficients.

Multiply both sides by \((1+t)^2 (1+t^2)^2\):

\[
1 - 2t^2 + t^4 = 
A(1+t)(1+t^2)^2 + 
B(1+t^2)^2 + 
(Ct+D)(1+t)^2(1+t^2) + 
(Et+F)(1+t)^2
\]

Let’s expand each term:

1. \( A(1+t)(1+t^2)^2 \):
- \( (1+t^2)^2 = 1 + 2t^2 + t^4 \)
- \( (1+t)(1 + 2t^2 + t^4 ) = (1)(1 + 2t^2 + t^4) + t(1 + 2t^2 + t^4) = 1 + 2t^2 + t^4 + t + 2t^3 + t^5 \)
- So, \( A(1 + t + 2t^2 + 2t^3 + t^4 + t^5) \)

2. \( B(1 + t^2)^2 = B(1 + 2t^2 + t^4 ) \)

3. \( (Ct + D)(1 + t)^2(1 + t^2) \)
- \( (1 + t)^2 = 1 + 2t + t^2 \)
- \( (1 + 2t + t^2)(1 + t^2 ) = 1(1 + t^2 ) + 2t(1 + t^2 ) + t^2(1 + t^2 ) = (1 + t^2 ) + (2t + 2 t^3) + (t^2 + t^4 ) = 1 + 2t + 2 t^2 + 2 t^3 + t^4 \)
- So, \( (Ct + D)(1 + 2t + 2 t^2 + 2 t^3 + t^4 ) \)
Let’s expand:
- \( Ct (1 + 2t + 2 t^2 + 2 t^3 + t^4 ) = C t \cdot 1 + C t \cdot 2 t + C t \cdot 2 t^2 + C t \cdot 2 t^3 + C t \cdot t^4 = C t + 2C t^2 + 2C t^3 + 2C t^4 + C t^5 \)
- \( D (1 + 2t + 2 t^2 + 2 t^3 + t^4 ) = D + 2D t + 2D t^2 + 2D t^3 + D t^4 \)
Sum:
- \( (Ct + D)(1 + 2t + 2 t^2 + 2 t^3 + t^4 ) = D + (C + 2D) t + (2C + 2D) t^2 + (2C + 2D ) t^3 + (2C+D ) t^4 + C t^5 \)

Let us just sum by degree:

- \( t^0: D \)
- \( t^1: C + 2D \)
- \( t^2: 2C + 2D \)
- \( t^3: 2C + 2D \)
- \( t^4: 2C + D \)
- \( t^5: C \)

Wait—that's a mistake. Let's expand more slowly:

First for \( Ct \):

- \( Ct (1) = C t \)
- \( Ct (2t) = 2C t^2 \)
- \( Ct (2t^2) = 2C t^3 \)
- \( Ct (2t^3) = 2C t^4 \)
- \( Ct (t^4) = C t^5 \)

Total: \( C t + 2C t^2 + 2C t^3 + 2C t^4 + C t^5 \)

For \( D \):

- \( D \cdot 1 = D \)
- \( D \cdot 2t = 2D t \)
- \( D \cdot 2t^2 = 2D t^2 \)
- \( D \cdot 2t^3 = 2D t^3 \)
- \( D \cdot t^4 = D t^4 \)

Total: \( D + 2D t + 2D t^2 + 2D t^3 + D t^4 \)

Sum all:

- \( t^0: D \)
- \( t^1: C t + 2D t = (C + 2D) t \)
- \( t^2: 2C t^2 + 2D t^2 = (2C + 2D) t^2 \)
- \( t^3: 2C t^3 + 2D t^3 = (2C + 2D) t^3 \)
- \( t^4: 2C t^4 + D t^4 = (2C + D) t^4 \)
- \( t^5: C t^5 \)

So,

- \( D \)
- \( (C + 2D) t \)
- \( (2C + 2D) t^2 \)
- \( (2C + 2D) t^3 \)
- \( (2C + D) t^4 \)
- \( C t^5 \)

4. \( (E t + F)(1 + t)^2 = (E t + F )( 1 + 2 t + t^2 )= E t (1 + 2t + t^2 ) + F (1 + 2t + t^2 ) = E t + 2E t^2 + E t^3 + F + 2F t + F t^2 \)
Sum:

- \( t^0: F \)
- \( t^1: E t + 2F t = (E + 2F) t \)
- \( t^2: 2E t^2 + F t^2 = (2E + F) t^2 \)
- \( t^3: E t^3 \)

Now, collect all terms for each power of \( t \) for the right side and equate to the left side.

Let’s write everything for each degree:

- \( t^0 \):
  - \( 1 = A \cdot 1 + B \cdot 1 + D + F  \)
- \( t^1 \):
  - \( 0 = A \cdot 1 + C + 2D + E + 2F  \)
- \( t^2 \):
  - \( -2 = 2A + 2B + 2C + 2D + 2E + F \)
- \( t^3 \):
  - \( 0 = 2A + 2C + 2D + E \)
- \( t^4 \):
  - \( 1 = A + B + 2C + D \)
- \( t^5 \):
  - \( 0 = A + C \)

Let’s be methodical and write the full expansions.

**First, expand the right-hand side:**

- \( A( 1 + t + 2 t^2 + 2 t^3 + t^4 + t^5 ) \)
  - \( t^0: A \)
  - \( t^1: A \)
  - \( t^2: 2A \)
  - \( t^3: 2A \)
  - \( t^4: A \)
  - \( t^5: A \)

- \( B (1 + 2 t^2 + t^4 ) \)
  - \( t^0: B \)
  - \( t^2: 2B \)
  - \( t^4: B \)

- \( Ct (1 + 2 t + 2 t^2 + 2 t^3 + t^4 ) \)
  - \( t^1: C \)
  - \( t^2: 2C \)
  - \( t^3: 2C \)
  - \( t^4: 2C \)
  - \( t^5: C \)

- \( D ( 1 + 2 t + 2 t^2 + 2 t^3 + t^4 ) \)
  - \( t^0: D \)
  - \( t^1: 2D \)
  - \( t^2: 2D \)
  - \( t^3: 2D \)
  - \( t^4: D \)

- \( E t (1 + 2 t + t^2 ) \)
  - \( t^1: E \)
  - \( t^2: 2E \)
  - \( t^3: E \)

- \( F (1 + 2 t + t^2 ) \)
  - \( t^0: F \)
  - \( t^1: 2F \)
  - \( t^2: F \)

Now add up coefficients by power:

- \( t^0 \): \( A + B + D + F \)
- \( t^1 \): \( A + C + 2D + E + 2F \)
- \( t^2 \): \( 2A + 2B + 2C + 2D + 2E + F \)
- \( t^3 \): \( 2A + 2C + 2D + E \)
- \( t^4 \): \( A + B + 2C + D \)
- \( t^5 \): \( A + C \)

Set equal to coefficients in \( 1 - 2 t^2 + t^4 \):

\( t^0: 1 \)
\( t^1: 0 \)
\( t^2: -2 \)
\( t^3: 0 \)
\( t^4: 1 \)
\( t^5: 0 \)

System:

\[
\begin{cases}
A + B + D + F = 1 \\
A + C + 2D + E + 2F = 0 \\
2A + 2B + 2C + 2D + 2E + F = -2 \\
2A + 2C + 2D + E = 0 \\
A + B + 2C + D = 1 \\
A + C = 0 \\
\end{cases}
\]

Let’s begin with \( A + C = 0 \Rightarrow C = -A \).

Now, try to find others.

- 1st equation: \( A + B + D + F = 1 \) (Eq 1)
- 2nd equation: \( A + C + 2D + E + 2F = 0 \) 
  - \( A + C = 0 \) (from Eq 6)
  - So \( 2D + E + 2F = 0 \) (Eq 2a)
- 3rd equation: \( 2A + 2B + 2C + 2D + 2E + F = -2 \)
- 4th: \( 2A + 2C + 2D + E = 0 \)
  - \( 2A + 2C = 0 \Rightarrow 2D + E = 0 \) (Eq 4a)
- 5th: \( A + B + 2C + D = 1 \)
  - \( A + B + 2C + D = 1 \)

Let’s express as much as possible in terms of \( A \):

- \( C = -A \)
- Eq 4a: \( 2D + E = 0 \implies E = -2D \)
- Eq 2a: \( 2D + E + 2F = 0 \). Substitute \( E = -2D \): \( 2D - 2D + 2F = 0 \implies 2F = 0 \implies F = 0 \)

So \( F = 0 \), \( E = -2D \).

Now, Eq 1: \( A + B + D + F = 1 \implies A + B + D = 1 \) (since \( F = 0 \)).

Eq 5: \( A + B + 2C + D = 1 \), insert \( C = -A \):
- \( A + B + 2(-A) + D = 1 \implies -A + B + D = 1 \)

Subtract Eq 1 and this equation:

- Eq 1: \( A + B + D = 1 \)
- Eq 5: \( -A + B + D = 1 \)

Subtract: \( (A + B + D) - (-A + B + D) = 1 - 1 \implies (A + A) = 0 \implies 2A = 0 \implies A = 0 \)

Therefore, \( C = -A = 0 \)

Now substitute:

- \( A = 0 \), \( C = 0 \)
- Eq 1: \( 0 + B + D = 1 \implies B + D = 1 \) (Eq I)
- \( F = 0 \)
- \( E = -2 D \)
- Eq 3: \( 2A + 2B + 2C + 2D + 2E + F = -2 \):

Plug all in,

- \( 2 \cdot 0 + 2 B + 2 \cdot 0 + 2D + 2E + 0 = -2 \)
- \( 2B + 2D + 2E = -2 \)
- \( E = -2D \implies 2E = -4D \)
- So,
- \( 2B + 2D -4D = -2 \implies 2B - 2D = -2 \implies B - D = -1 \) (Eq II)

Now, combine Eq I and Eq II:

- \( B + D = 1 \)
- \( B - D = -1 \)
So,
- Add: \( 2B = 0 \implies B = 0 \)
- \( D = 1 \)

So \( B = 0, D = 1 \), \( E = -2 \cdot 1 = -2 \), \( F = 0 \).

So, summarize:

- \( A = 0 \)
- \( B = 0 \)
- \( C = 0 \)
- \( D = 1 \)
- \( E = -2 \)
- \( F = 0 \)

Let’s check that these values recover the numerators for all terms.

So:
\[
\frac{1 - 2 t^2 + t^4}{(1+t)^2 (1+t^2)^2} = \frac{1}{1 + t^2} + \frac{ -2 t }{(1 + t^2)^2 }
\]

**Step 4: Write the decomposition**

The only nonzero coefficients are \( D \) and \( E \):

\[
\frac{1 - 2 t^2 + t^4}{(1+t)^2 (1+t^2)^2} = \frac{1}{1 + t^2} + \frac{ -2 t }{ (1 + t^2 )^2 }
\]

Therefore:

\[
I = \int_0^1 \frac{1}{1 + t^2} dt - 2 \int_0^1 \frac{ t }{ (1 + t^2 )^2 } dt
\]

**Step 5: Integrate each term**

First term:

\[
\int_0^1 \frac{1}{1 + t^2} dt = \arctan t \Big|_{t=0}^{t=1} = \arctan 1 - \arctan 0 = \frac{\pi}{4} - 0 = \frac{\pi}{4}
\]

Second term:

Let’s integrate \( \int \frac{ t }{ (1 + t^2 )^2 } dt \):

Let’s use substitution: \( u = 1 + t^2, du = 2 t dt \implies dt = du / (2 t) \):

So,

\[
\int \frac{ t }{ (1 + t^2 )^2 } dt = \int \frac{ t }{ u^2 } \cdot \frac{ du }{ 2 t } = \frac{1}{2} \int u^{-2} du = \frac{1}{2} \cdot \left(- u^{-1} \right) = -\frac{1}{2} \frac{1}{ 1 + t^2 }
\]

So,
\[
\int_0^1 \frac{ t }{ (1 + t^2 )^2 } dt = -\frac{1}{2} \left[ \frac{1}{1 + t^2 } \right]_{0}^{1} = -\frac{1}{2} \left( \frac{1}{2} - 1 \right) = -\frac{1}{2} \left( -\frac{1}{2} \right) = \frac{1}{4 }
\]

The factor in the original decomposition was minus 2 times this, so total contribution:
\[
-2 \cdot \frac{1}{4} = -\frac{1}{2}
\]

Therefore, the value of the integral is:
\[
I = \frac{\pi}{4} - \frac{1}{2}
\]

**Step 6: Numerical Approximation**

\[
\frac{\pi}{4} - \frac{1}{2} \approx \frac{3.141592653589793}{4} - \frac{1}{2} = 0.7853981633974483 - 0.5 = 0.2853981634
\]

Rounded to 10 decimal places: \( 0.2853981634 \)

**Final answer, formatted as requested:**

```json
{"answer": "\\frac{\\pi}{4} - \\frac{1}{2}", "numerical_answer": "0.2853981634"}
```