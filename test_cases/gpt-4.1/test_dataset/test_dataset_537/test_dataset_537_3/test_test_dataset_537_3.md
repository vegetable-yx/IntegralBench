Let's solve the given integral step by step:

\[
I = \int_1^2 \left(2^{x-1} + \log_2(2x)\right)\,dx
\]

---

## 1. Split the Integral

\[
I = \int_1^2 2^{x-1} \, dx + \int_1^2 \log_2(2x)\, dx
\]

---

## 2. First Term: \(\int_1^2 2^{x-1} dx\)

Recall:
\[
2^{x-1} = \frac{2^x}{2}
\]
So,
\[
\int 2^{x-1} dx = \int \frac{2^x}{2} dx = \frac{1}{2} \int 2^x dx = \frac{1}{2} \cdot \frac{2^x}{\ln 2} = \frac{2^{x-1}}{\ln 2} + C
\]

So,
\[
\int_1^2 2^{x-1} dx = \left. \frac{2^{x-1}}{\ln 2} \right|_1^2 = \frac{2^{2-1}}{\ln 2} - \frac{2^{1-1}}{\ln 2} = \frac{2^1}{\ln 2} - \frac{2^0}{\ln 2} = \frac{2}{\ln 2} - \frac{1}{\ln 2} = \frac{1}{\ln 2}
\]

---

## 3. Second Term: \(\int_1^2 \log_2(2x) dx\)

First, recall:
\[
\log_2(2x) = \log_2 2 + \log_2 x = 1 + \log_2 x
\]
Thus:
\[
\int_1^2 \log_2(2x) dx = \int_1^2 (1 + \log_2 x) dx = \int_1^2 1 \, dx + \int_1^2 \log_2 x\, dx = (2-1) + \int_1^2 \log_2 x\, dx = 1 + \int_1^2 \log_2 x\, dx
\]

Now evaluate \(\int_1^2 \log_2 x\, dx\):

Recall:
\[
\log_2 x = \frac{\ln x}{\ln 2}
\]
So:
\[
\int_1^2 \log_2 x\, dx = \frac{1}{\ln 2}\int_1^2 \ln x\, dx
\]

We know:
\[
\int \ln x\, dx = x \ln x - x + C
\]

Therefore:
\[
\int_1^2 \ln x\, dx = \left[x\ln x - x\right]_1^2 = (2\ln 2 - 2) - (1\ln 1 - 1) = (2\ln 2 - 2) - (0 - 1) = 2\ln 2 - 1
\]

So,
\[
\int_1^2 \log_2 x\, dx = \frac{2\ln 2 - 1}{\ln 2}
\]

---

Hence:
\[
\int_1^2 \log_2(2x)\,dx = 1 + \frac{2\ln 2 - 1}{\ln 2}
\]

---

## 4. Combine Results

So,
\[
I = \underbrace{\frac{1}{\ln 2}}_{(1)} + \underbrace{\left[1 + \frac{2\ln 2 - 1}{\ln 2}\right]}_{(2)}
\]

Combine:
\[
I = \frac{1}{\ln 2} + 1 + \frac{2\ln 2 - 1}{\ln 2} = 1 + \frac{1 + 2\ln 2 - 1}{\ln 2} = 1 + \frac{2\ln 2}{\ln 2} = 1 + 2 = 3
\]

---

## 5. Numerical Approximation

\[
I = 3.0000000000
\]

---

## 6. JSON Output

```json
{"answer": "3", "numerical_answer": "3.0000000000"}
```