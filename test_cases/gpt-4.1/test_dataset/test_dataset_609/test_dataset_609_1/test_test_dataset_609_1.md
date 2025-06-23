Let's proceed step by step.

1. **Analyze the function:**  
We are to compute:
\[
I = \int_0^1 \left\lfloor\cos\left(\frac{\pi}{x}\right)\right\rfloor \, dx
\]
for \( x \in (0,1] \).

2. **Examine the range of \(\cos\left(\frac{\pi}{x}\right)\):**

- As \( x \to 0^+ \), \( \frac{\pi}{x} \to +\infty \), so \( \cos\left(\frac{\pi}{x}\right) \) oscillates between -1 and 1 infinitely many times.
- As \( x = 1 \), \( \cos(\pi/1) = \cos(\pi) = -1 \).

But since the argument \( \frac{\pi}{x} \) runs from \(+\infty\) down to \(\pi\) as \(x\) goes from 0 up to 1, let's see at which points \(\cos(\pi/x)\) steps across integer values whose floor changes.

The floor function for cosine can only take values -1 and 0 for \(x \in (0,1]\):

- \(\cos(\pi/x) < 0\)  ⇒ floor is -1
- \(0 \leq \cos(\pi/x) \leq 1\)  ⇒ floor is 0

But \(\cos(\pi/x)\) only hits or exceeds 0 at discrete values.

Let us compute where \(\cos(\pi/x) = 0\):
\[
\cos\left(\frac{\pi}{x}\right) = 0 \implies \frac{\pi}{x} = \frac{\pi}{2} + k\pi \implies x = \frac{2}{1+2k}
\]
But for \(x \in (0,1],\) \(k\) must be positive integer (since \( x < 1 \implies 1+2k > 2 \implies k \ge 1\)).

Let \( \theta = \frac{\pi}{x} \).

- For \(\cos(\theta) < 0\), \(\theta \in (\pi/2 + 2\pi n, 3\pi/2 + 2\pi n)\), \(n = 0,1,2,\ldots\)

That is, for
\[
\frac{\pi}{x} \in (\pi/2 + 2\pi n, 3\pi/2 + 2\pi n) \implies
x \in \left(\frac{1}{2n + 3}, \frac{1}{2n + 1}\right)
\]
because
\[
\frac{\pi}{x} = \pi/2 + 2\pi n \implies x = \frac{2}{1+4n},
\]
but to get endpoints in terms of \(n\), let's solve \( \frac{\pi}{x} = \pi/2 + 2\pi n \implies x = \frac{2}{1+4n} \) and \( \frac{\pi}{x} = 3\pi/2 + 2\pi n \implies x = \frac{2}{3+4n} \).

But it's easier to use:

\[
\cos\left(\frac{\pi}{x}\right) < 0 \quad \text{when} \quad \frac{\pi}{x} \in (\pi/2 + k\pi, 3\pi/2 + k\pi)
\]
for integer \(k \geq 0\).

Thus,
\[
\frac{\pi}{x} \in \left(\frac{\pi}{2} + k\pi, \frac{3\pi}{2} + k\pi \right)
\]
\[
\implies x \in \left( \frac{1}{\frac{1}{2} + k}, \frac{1}{\frac{3}{2} + k} \right)
\]

But let's be precise by inverting the endpoints:
For each integer \( k \ge 0 \),
\[
\frac{\pi}{x} = \frac{\pi}{2} + k\pi \implies x_{k,1} = \frac{2}{1 + 2k}
\]
\[
\frac{\pi}{x} = \frac{3\pi}{2} + k\pi \implies x_{k,2} = \frac{2}{3 + 2k}
\]
So the intervals where \( \cos(\pi/x) < 0 \) and thus the floor is -1 are:
\[
x \in \left( \frac{2}{1 + 2k}, \frac{2}{3 + 2k} \right)
\]
for \( k = 0, 1, 2, \ldots \), as long as \( \frac{2}{1 + 2k} > 0 \), i.e., for \( k \) such that \( 1 + 2k > 0 \). Since we are in \( x \in (0,1] \), only those intervals entirely within (0,1].

- For \(k=0\): \( (2, 2/3) \), but 2 is not in (0,1], but \(2/3\) is.
- For \(k=1\): \( (2/3, 2/5) \)
- For \(k=2\): \( (2/5, 2/7) \), etc.

So, for each \(k\),
\[
\text{Interval: } x \in \left( \frac{2}{2k+1}, \frac{2}{2k+3} \right)
\]
We want all such intervals that fall inside (0,1]; that is, for \(2/(2k+1) < 1 \implies 2 < 2k+1 \implies k > 0.5\), so \(k \ge 1\). For \(k=1\), \(2/(2 \cdot 1 + 1) = 2/3 < 1\), for \(k=0\), \(2/1 = 2 > 1\).

Therefore, the intervals where \( \left\lfloor \cos(\pi/x) \right\rfloor = -1 \) inside (0,1] are
\[
\left( \frac{2}{2k+1}, \frac{2}{2k+3} \right)
\]
for \(k = 1, 2, 3, \ldots\), with both endpoints less than or equal to 1.

We also note that outside these intervals, the floor is zero.

3. **Express the integral as a sum:**

Since the function is -1 on these intervals and 0 elsewhere (almost everywhere), the integral reduces to minus the total length of these intervals:
\[
I = \sum_{k=1}^{N} \int_{\frac{2}{2k+1}}^{\frac{2}{2k+3}} (-1) dx
\]
where \( N \) is the highest \(k\) for which \( \frac{2}{2k+1} > 0 \) and \( \frac{2}{2k+3} \ge 0 \) and both are ≤ 1.

But since as \(k\) increases, both endpoints approach zero, so the sum is theoretically infinite, but for each \(k\), the interval is within (0,1].

So:
\[
I = -\sum_{k=1}^{\infty} \left( \frac{2}{2k+3} - \frac{2}{2k+1} \right)
\]
\[
= -2 \sum_{k=1}^{\infty} \left( \frac{1}{2k+3} - \frac{1}{2k+1} \right)
\]
\[
= -2 \sum_{k=1}^{\infty} \left( \frac{1}{2k+3} - \frac{1}{2k+1} \right)
\]
\[
= -2 \lim_{N\to\infty} \sum_{k=1}^{N} \left( \frac{1}{2k+3} - \frac{1}{2k+1} \right)
\]

Note:
\[
\frac{1}{2k+3} - \frac{1}{2k+1} = \frac{(2k+1)-(2k+3)}{(2k+3)(2k+1)} = \frac{-2}{(2k+3)(2k+1)}
\]
Thus,
\[
I = -2 \sum_{k=1}^{\infty} \left( \frac{-2}{(2k+3)(2k+1)} \right) = 4 \sum_{k=1}^{\infty} \frac{1}{(2k+3)(2k+1)}
\]

Let us simplify \( \frac{1}{(2k+3)(2k+1)} \):
\[
\frac{1}{(2k+3)(2k+1)} = \frac{A}{2k+1} + \frac{B}{2k+3}
\]
Solve:
\[
1 = A(2k+3) + B(2k+1)
\]
Let \(2k+1 = x\), so \(2k+3 = x+2\):
\[
1 = A(x+2) + Bx \implies 1 = (A+B)x + 2A
\]
Matching coefficients:
- For \(x\): \(A+B = 0\) ⇒ \(B = -A\)
- Constant: \(2A = 1\) ⇒ \(A = \frac{1}{2}\), \(B = -\frac{1}{2}\)

Thus,
\[
\frac{1}{(2k+3)(2k+1)} = \frac{1}{2} \left( \frac{1}{2k+1} - \frac{1}{2k+3} \right)
\]

Therefore:
\[
I = 4 \sum_{k=1}^{\infty} \frac{1}{2} \left( \frac{1}{2k+1} - \frac{1}{2k+3} \right)
= 2 \sum_{k=1}^{\infty} \left( \frac{1}{2k+1} - \frac{1}{2k+3} \right)
\]

This sum telescopes! Let's write out the first few terms:

- For \(k=1\): \(1/3 - 1/5\)
- For \(k=2\): \(1/5 - 1/7\)
- For \(k=3\): \(1/7 - 1/9\)
- And so on.

So the sum is:
\[
2 \left( \frac{1}{3} - \frac{1}{5} + \frac{1}{5} - \frac{1}{7} + \frac{1}{7} - \frac{1}{9} + \ldots \right)
= 2 \left( \frac{1}{3} - \frac{1}{\infty} \right) = 2 \cdot \frac{1}{3}
= \frac{2}{3}
\]
But let's check the limits:

The partial sum up to \(N\) is:
\[
S_N = \sum_{k=1}^N \left( \frac{1}{2k+1} - \frac{1}{2k+3} \right) = \frac{1}{3} - \frac{1}{2N+3}
\]
So in the limit \(N \to \infty\):
\[
S_\infty = \frac{1}{3}
\]
so
\[
I = 2 \cdot \frac{1}{3} = \frac{2}{3}
\]

4. **Check for missed values at endpoints:**

Check \(x = 1\): \(\cos(\pi/1) = \cos(\pi) = -1\), so the integrand at \(x=1\) is -1.
At the lower limit as \(x \to 0+\), \(\cos(\pi/x)\) oscillates between -1 and 1 infinitely, but the set where the floor jumps is Lebesgue measure zero.

The integrand is -1 on a set of measure \(\frac{2}{3}\), and zero elsewhere.

Therefore, the exact value is \(\boxed{\frac{2}{3}}\).

5. **Numerical value:**  
\[
\boxed{\frac{2}{3} = 0.6666666667}
\]

6. **Final answer in required JSON format:**

```json
{"answer": "\\frac{2}{3}", "numerical_answer": "0.6666666667"}
```