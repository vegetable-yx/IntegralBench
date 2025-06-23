Let's denote the integral as:
\[
I = \int_0^1 \left( \frac{1}{x} - \left\lfloor \frac{1}{x} \right\rfloor \right) dx
\]

**Step 1: Analyze the integrand**

Notice that for \( x \in (0, 1) \), \( \frac{1}{x} \in [1, \infty) \), and \( \left\lfloor \frac{1}{x} \right\rfloor \) is an integer that changes value whenever \( \frac{1}{x} \) is an integer, i.e., at \( x = \frac{1}{n} \) for integer \( n \geq 1 \).

So, for \( x \in \left( \frac{1}{n+1}, \frac{1}{n} \right] \), \( \frac{1}{x} \in [n, n+1) \implies \left\lfloor \frac{1}{x} \right\rfloor = n \).

Thus, the interval decomposes as:
\[
(0,1) = \bigcup_{n=1}^{\infty} \left( \frac{1}{n+1}, \frac{1}{n} \right]
\]

The original integral becomes:
\[
I = \sum_{n=1}^{\infty} \int_{\frac{1}{n+1}}^{\frac{1}{n}} \left( \frac{1}{x} - n \right) dx
\]

**Step 2: Compute the integral on each subinterval**

Compute for each \( n \geq 1 \):
\[
I_n = \int_{\frac{1}{n+1}}^{\frac{1}{n}} \left( \frac{1}{x} - n \right) dx
\]

Break into two parts:
\[
I_n = \int_{\frac{1}{n+1}}^{\frac{1}{n}} \frac{1}{x} dx - n \int_{\frac{1}{n+1}}^{\frac{1}{n}} dx
\]

Compute each term:
\[
\int_{\frac{1}{n+1}}^{\frac{1}{n}} \frac{1}{x} dx = \ln\left(\frac{1}{n}\right) - \ln\left(\frac{1}{n+1}\right) = \ln\left(\frac{n+1}{n}\right)
\]
\[
\int_{\frac{1}{n+1}}^{\frac{1}{n}} dx = \frac{1}{n} - \frac{1}{n+1} = \frac{1}{n(n+1)}
\]

Putting together:
\[
I_n = \ln\left(\frac{n+1}{n}\right) - n \cdot \frac{1}{n(n+1)} = \ln\left(\frac{n+1}{n}\right) - \frac{1}{n+1}
\]

**Step 3: Sum over all \( n \)**
\[
I = \sum_{n=1}^{\infty} \left[ \ln\left(\frac{n+1}{n}\right) - \frac{1}{n+1} \right]
\]

The sum splits into:
\[
I = \sum_{n=1}^{\infty} \ln\left(\frac{n+1}{n}\right) - \sum_{n=1}^{\infty} \frac{1}{n+1}
\]

The first term telescopes:
\[
\sum_{n=1}^{N} \ln\left(\frac{n+1}{n}\right) = \ln\left(\frac{N+1}{1}\right) = \ln(N+1)
\]
Take the limit as \( N \to \infty \):

The second term is:
\[
\sum_{n=1}^{N} \frac{1}{n+1} = \sum_{k=2}^{N+1} \frac{1}{k} = H_{N+1} - 1
\]
where \( H_n \) is the \( n \)-th harmonic number.

Therefore,
\[
I_N = \ln(N+1) - (H_{N+1} - 1)
\]

Take the limit as \( N \to \infty \):

Recall \( H_{N+1} = \ln(N+1) + \gamma + \frac{1}{2(N+1)} - \frac{1}{12(N+1)^2} + \ldots \) where \( \gamma \) is Euler's constant.

Thus,
\[
I_N \sim \ln(N+1) - (\ln(N+1) + \gamma) + 1 = 1 - \gamma
\]
As \( N \to \infty \), smaller order terms go to zero.

**Step 4: Final answers**

**Exact value:**
\[
I = 1 - \gamma
\]
where \( \gamma \) is Euler–Mascheroni constant.

**Numerical value:**

\( \gamma \approx 0.5772156649 \)

So,
\[
I \approx 1 - 0.5772156649 = 0.4227843351
\]

**JSON output:**
```json
{"answer": "1 - \\gamma", "numerical_answer": "0.4227843351"}
```