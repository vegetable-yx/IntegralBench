Let's proceed step by step:

Given:
\[
I = \int_1^2 \left(2^{x-1} + \log_2(2x)\right)\,dx
\]

### Step 1: Split the Integral

\[
I = \int_1^2 2^{x-1}\,dx + \int_1^2 \log_2(2x)\,dx
\]

---

### Step 2: Compute Each Integral

#### a) \( \int_1^2 2^{x-1} dx \)

Let’s use substitution: \( u = x-1 \Rightarrow du = dx \).
When \( x = 1,\, u = 0 \); when \( x = 2,\, u = 1 \).

\[
\int_1^2 2^{x-1} dx = \int_0^1 2^u du = \frac{2^u}{\ln 2} \Big|_{u = 0}^{u = 1} = \frac{2^1 - 2^0}{\ln 2} = \frac{2 - 1}{\ln 2} = \frac{1}{\ln 2}
\]

---

#### b) \( \int_1^2 \log_2(2x) dx \)

Recall: \( \log_2(2x) = \log_2 2 + \log_2 x = 1 + \log_2 x \).

So,
\[
\int_1^2 \log_2(2x) dx = \int_1^2 1\,dx + \int_1^2 \log_2 x\,dx = (2 - 1) + \int_1^2 \log_2 x\,dx = 1 + \int_1^2 \log_2 x\,dx
\]

Recall:
\[
\log_2 x = \frac{\ln x}{\ln 2}
\]

So,
\[
\int_1^2 \log_2 x\,dx = \frac{1}{\ln 2} \int_1^2 \ln x\,dx
\]

We know:
\[
\int \ln x\,dx = x \ln x - x + C
\]
So,
\[
\int_1^2 \ln x\,dx = [2 \ln 2 - 2] - [1 \ln 1 - 1] = (2 \ln 2 - 2) - (0 - 1) = 2 \ln 2 - 1
\]
So,
\[
\int_1^2 \log_2 x\,dx = \frac{2 \ln 2 - 1}{\ln 2}
\]

Therefore,
\[
\int_1^2 \log_2(2x)\,dx = 1 + \frac{2 \ln 2 - 1}{\ln 2} = 1 + 2 - \frac{1}{\ln 2} = 3 - \frac{1}{\ln 2}
\]

---

### Step 3: Add the Two Results

From above,
\[
I = \frac{1}{\ln 2} + \left(3 - \frac{1}{\ln 2}\right) = 3
\]

---

### Step 4: Numerical Approximation

\[
3 \text{ (rounded to 10 decimal places is } 3.0000000000\text{)}
\]

---

### Step 5: Final JSON Output

```json
{"answer": "3", "numerical_answer": "3.0000000000"}
```