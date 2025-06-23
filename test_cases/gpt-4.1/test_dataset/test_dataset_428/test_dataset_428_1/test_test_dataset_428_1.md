Given:
\[
I = \int_0^3 (x^2 + 1) \, d\lfloor x\rfloor
\]

Let's follow the steps:

### Step 1: Understanding the Differential

\(d\lfloor x\rfloor\) is the Stieltjes measure, which "jumps" at integer points. For \(0 \leq x < 3\), the points where \(\lfloor x\rfloor\) jumps are at \(x = 1, 2, 3\).

The measure \(d\lfloor x\rfloor\) places a unit mass at each integer \(k\) inside \((0,3]\). But at 0, \(\lfloor x\rfloor\) doesn't jump: it is constant to the right of 0, \(\lfloor 0\rfloor = 0\), and before that not defined in our domain.

For a function \(f(x)\),
\[
\int_a^b f(x) \, d\lfloor x\rfloor = \sum_{a < n \leq b} f(n)
\]

### Step 2: Setting up the sum

From \(a=0\) to \(b=3\), the integer values within the interval \((0, 3]\) are 1, 2, and 3.

So,
\[
I = f(1) + f(2) + f(3) \\
= (1^2 + 1) + (2^2 + 1) + (3^2 + 1) \\
= (1 + 1) + (4 + 1) + (9 + 1) \\
= 2 + 5 + 10 = 17
\]

### Step 3: Numerical approximation

\[
I \approx 17.0000000000
\]

### Final Answer

```json
{"answer": "17", "numerical_answer": "17.0000000000"}
```