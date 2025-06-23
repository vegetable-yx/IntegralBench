Let's compute the definite integral:
\[
\int_1^2 \left(2^{x-1} + \log_2(2x)\right)\,dx
\]

### Step 1: Integrate term by term

#### First term: \(\int_1^2 2^{x-1}\,dx\)

Let \(u = x-1\), \(du = dx\).

\[
\int 2^{x-1}dx = \int 2^u du = \frac{2^u}{\ln 2} = \frac{2^{x-1}}{\ln 2}
\]

Thus,
\[
\int_1^2 2^{x-1}\,dx = \left[\frac{2^{x-1}}{\ln 2}\right]_1^2 = \frac{2^{2-1} - 2^{1-1}}{\ln 2} = \frac{2^1 - 2^0}{\ln 2} = \frac{2-1}{\ln 2} = \frac{1}{\ln 2}
\]

#### Second term: \(\int_1^2 \log_2(2x)\,dx\)

Recall that \(\log_2(2x) = \log_2 2 + \log_2 x = 1 + \log_2 x\).

So,
\[
\int_1^2 \log_2(2x)\,dx = \int_1^2 1\,dx + \int_1^2 \log_2 x\,dx = (2-1) + \int_1^2 \log_2 x\,dx = 1 + \int_1^2 \log_2 x\,dx
\]

Let's focus on \(\int \log_2 x\,dx\):

\[
\log_2 x = \frac{\ln x}{\ln 2}
\]
\[
\int \log_2 x\,dx = \frac{1}{\ln 2}\int \ln x\,dx
\]
\[
\int \ln x\,dx = x \ln x - x
\]
So,
\[
\int \log_2 x\,dx = \frac{1}{\ln 2}(x \ln x - x)
\]

Therefore,
\[
\int_1^2 \log_2 x\,dx = \frac{1}{\ln 2}\left[x \ln x - x\right]_1^2
= \frac{1}{\ln 2}\left[(2 \ln 2 - 2) - (1 \ln 1 - 1)\right]
= \frac{1}{\ln 2}\left[(2 \ln 2 - 2) - (0 - 1)\right]
= \frac{1}{\ln 2}(2\ln 2 - 2 + 1)
= \frac{1}{\ln 2}(2\ln 2 - 1)
\]

So, the integral for the second term is:
\[
1 + \frac{1}{\ln 2}(2\ln 2 - 1)
\]

### Step 2: Combine results

Add the results together:
\[
\frac{1}{\ln 2} + 1 + \frac{1}{\ln 2}(2\ln 2 - 1)
\]

Combine like terms:
\[
\frac{1}{\ln 2} + \left( \frac{2\ln 2 - 1}{\ln 2} \right) + 1 
= \frac{1 + 2\ln 2 - 1}{\ln 2} + 1
= \frac{2\ln 2}{\ln 2} + 1 
= 2 + 1 = 3
\]

### Step 3: Numerical value

Thus, the exact answer is **3**.

Rounded to 10 decimal places:
\[
3.0000000000
\]

### Step 4: JSON Output

```json
{"answer": "3", "numerical_answer": "3.0000000000"}
```