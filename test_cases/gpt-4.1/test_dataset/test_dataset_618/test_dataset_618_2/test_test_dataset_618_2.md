Let's define the function to integrate:
\[
I = \int_{0}^{1} \left( \frac{1}{x} - \left\lfloor \frac{1}{x} \right\rfloor \right) dx
\]

### Step 1: Partition the Interval

Notice that \(\left\lfloor \frac{1}{x} \right\rfloor\) is constant on each interval \(x \in \left(\frac{1}{n+1}, \frac{1}{n}\right]\) for \(n \geq 1\):

- When \(x \in \left(\frac{1}{n+1}, \frac{1}{n}\right]\) we have \(n < \frac{1}{x} \leq n+1\), so \(\left\lfloor \frac{1}{x} \right\rfloor = n\).
- At \(x=1\), \(\frac{1}{x}=1\), \(\lfloor 1 \rfloor =1\).
- As \(x \to 0^+\), \(\frac{1}{x} \to \infty\).

So, partition:
\[
I = \sum_{n=1}^{\infty} \int_{\frac{1}{n+1}}^{\frac{1}{n}} \left( \frac{1}{x} - n \right) dx
\]

### Step 2: Compute Each Integral

Compute each term:
\[
\int_{\frac{1}{n+1}}^{\frac{1}{n}} \left( \frac{1}{x} - n \right) dx
= \int_{\frac{1}{n+1}}^{\frac{1}{n}} \frac{1}{x} dx - n \int_{\frac{1}{n+1}}^{\frac{1}{n}} dx
\]
\[
= \left[ \ln x \right]_{\frac{1}{n+1}}^{\frac{1}{n}} - n \left[ x \right]_{\frac{1}{n+1}}^{\frac{1}{n}}
\]
\[
= \left(\ln \frac{1}{n} - \ln \frac{1}{n+1}\right) - n \left(\frac{1}{n} - \frac{1}{n+1}\right)
\]
\[
= \ln \frac{n+1}{n} - n \left(\frac{1}{n} - \frac{1}{n+1}\right)
\]
Calculate the second term:
\[
n \left( \frac{1}{n} - \frac{1}{n+1} \right) = 1 - \frac{n}{n+1} = \frac{1}{n+1}
\]
Thus,
\[
\int_{\frac{1}{n+1}}^{\frac{1}{n}} \left( \frac{1}{x} - n \right) dx
= \ln \frac{n+1}{n} - \frac{1}{n+1}
\]

### Step 3: Sum Over All Intervals

Thus,
\[
I = \sum_{n=1}^{\infty} \left( \ln \frac{n+1}{n} - \frac{1}{n+1} \right )
= \sum_{n=1}^{\infty} \ln \frac{n+1}{n} - \sum_{n=1}^{\infty} \frac{1}{n+1}
\]

The first sum telescopes:
\[
\sum_{n=1}^{N} \ln \frac{n+1}{n} = \ln (N+1) - \ln 1 = \ln (N+1)
\]

The second sum:
\[
\sum_{n=1}^{N} \frac{1}{n+1} = \sum_{k=2}^{N+1} \frac{1}{k} = H_{N+1} - 1
\]
where \(H_n\) is the \(n\)-th Harmonic number.

So,
\[
I_N = \ln (N+1) - (H_{N+1} - 1)
\]

Take the limit as \(N \to \infty\):

Recall that
\[
H_n = \ln n + \gamma + \frac{1}{2n} - \dots
\]
So,
\[
I = \lim_{N \to \infty} \left( \ln (N+1) - (H_{N+1} - 1) \right)
= 1 - \gamma
\]

### Step 4: Numerical Value

Euler-Mascheroni constant \(\gamma \approx 0.5772156649\).

Thus,
\[
I \approx 1 - 0.5772156649 = 0.4227843351
\]

### Final Answer

```json
{"answer": "1-\\gamma", "numerical_answer": "0.4227843351"}
```