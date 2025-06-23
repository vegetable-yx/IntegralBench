Let's proceed step by step:

**Step 1: Substitute.**

Let \( u = x^6 + x \). Then

\[
\frac{du}{dx} = 6x^5 + 1 \implies du = (6x^5 + 1)dx
\]

But our integrand has just \((x^6 + x)^4\), not enough to directly substitute, so let's look for a substitution or try standard methods.

Alternatively, expand the integrand:

\[
\int_{-1}^0 5(x^6 + x)^4\, dx
\]

Let us expand \((x^6 + x)^4\) using the binomial theorem:

\[
(x^6 + x)^4 = \sum_{k=0}^4 \binom{4}{k} (x^6)^{4 - k} x^k = \sum_{k=0}^4 \binom{4}{k} x^{6(4-k)} x^k = \sum_{k=0}^4 \binom{4}{k} x^{6(4-k) + k}
\]
But \(x^{6(4-k) + k} = x^{24 - 5k}\).

But that's incorrect; it should be:

\[
(x^6 + x)^4 = \sum_{k=0}^4 \binom{4}{k} (x^6)^{k} (x)^{4 - k} = \sum_{k=0}^4 \binom{4}{k} x^{6k} x^{4 - k} = \sum_{k=0}^4 \binom{4}{k} x^{6k + 4 - k} = \sum_{k=0}^4 \binom{4}{k} x^{4 + 5k}
\]

So, the integrand is:

\[
5(x^6 + x)^4 = 5 \sum_{k=0}^4 \binom{4}{k} x^{4 + 5k}
\]

So,

\[
\int_{-1}^0 5(x^6 + x)^4 dx = 5 \sum_{k=0}^4 \binom{4}{k} \int_{-1}^0 x^{4 + 5k} dx
\]

The integral:

\[
\int x^{n} dx = \frac{x^{n+1}}{n+1}
\]

From \(a\) to \(b\):

\[
\int_{a}^b x^n dx = \left[ \frac{x^{n+1}}{n+1} \right]_a^b = \frac{b^{n+1} - a^{n+1}}{n+1}
\]

So,

\[
\int_{-1}^0 x^{4+5k} dx = \frac{0^{5+5k} - (-1)^{5+5k}}{5+5k} = \frac{ -(-1)^{5 + 5k} }{5 + 5k } = \frac{(-1)^{6 + 5k}}{5 + 5k }
\]

But \(0^{n} = 0\) for \(n>0\).

Now, \(4 + 5k \geq 4\) for \(k \geq 0\), so always positive exponent.

So,

\[
\int_{-1}^0 x^{4 + 5k} dx = \frac{ -(-1)^{5 + 5k} }{5 + 5k }
\]

Now, \(5 + 5k = 5(1 + k)\), so:

\[
\int_{-1}^0 x^{4 + 5k} dx = -\frac{1}{5(1 + k)} (-1)^{5 + 5k}
\]

Also, \( (-1)^{5 + 5k} = (-1)^5 \cdot (-1)^{5k} = -1 \cdot (-1)^{k} \) (since \(5k\) is odd when \(k\) is odd, even otherwise)

But for each \(k\), \( (-1)^{5k} = (-1)^{k} \):

- If \(k\) is even, \(5k\) is even, so \( (-1)^{5k}=1 \)
- If \(k\) is odd, \(5k\) is odd, so \( (-1)^{5k}=-1 \)

Therefore,

\[
(-1)^{5 + 5k} = -1 \cdot (-1)^k = -(-1)^k
\]

Thus, the integral:

\[
\int_{-1}^0 x^{4 + 5k} dx = -\frac{1}{5(1 + k)} \cdot \left[ -(-1)^{k} \right] = \frac{(-1)^{k}}{5(1 + k)}
\]

Therefore, putting it together:

\[
\int_{-1}^0 5(x^6 + x)^4 dx = 5 \sum_{k=0}^4 \binom{4}{k} \cdot \frac{(-1)^k}{5(1 + k)} = \sum_{k=0}^4 \binom{4}{k} \frac{(-1)^k}{1 + k}
\]

**Step 2: Evaluate the sum**

Let's write it out:

\[
S = \sum_{k=0}^4 \binom{4}{k} \frac{(-1)^k}{1 + k}
\]

Evaluate for each \(k\):

- \(k = 0\): \(\binom{4}{0} = 1,\, (-1)^0 = 1,\, 1+k = 1\)  
  \(= 1 \cdot \frac{1}{1} = 1\)

- \(k = 1\): \(\binom{4}{1} = 4,\, (-1)^1 = -1,\, 1+k=2\)  
  \(= 4 \cdot \frac{-1}{2} = -2\)

- \(k = 2\): \(\binom{4}{2} = 6,\, (-1)^2=1,\, 1+k=3\)  
  \(= 6 \cdot \frac{1}{3} = 2\)

- \(k = 3\): \(\binom{4}{3} = 4,\, (-1)^3 = -1,\, 1+k=4\)  
  \(= 4 \cdot \frac{-1}{4} = -1\)

- \(k = 4\): \(\binom{4}{4} = 1,\, (-1)^4 = 1,\, 1+k=5\)  
  \(= 1 \cdot \frac{1}{5} = 0.2\)

Sum:

\[
S = 1 - 2 + 2 - 1 + 0.2 = (1 + 2 + 0.2) + (-2 - 1) = (3.2) + (-3) = 0.2
\]

**Step 3: Final exact answer**

Thus, the exact value is:

\[
\boxed{0.2}
\]

Or, in fraction, \(\frac{1}{5}\).

**Numerical value:** \(0.2\) to ten decimal places is \(0.2000000000\).

**Step 4: Output JSON**

```json
{"answer": "\\frac{1}{5}", "numerical_answer": "0.2000000000"}
```