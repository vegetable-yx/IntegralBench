To solve the definite integral \(\int_1^2 (2^{x-1} + \log_2(2x)) \, dx\), we will break it down into two separate integrals and solve each one individually.

### Step 1: Split the Integral
\[
\int_1^2 (2^{x-1} + \log_2(2x)) \, dx = \int_1^2 2^{x-1} \, dx + \int_1^2 \log_2(2x) \, dx
\]

### Step 2: Solve the First Integral
\[
\int_1^2 2^{x-1} \, dx
\]

Let \(u = x - 1\). Then \(du = dx\) and when \(x = 1\), \(u = 0\); when \(x = 2\), \(u = 1\). The integral becomes:
\[
\int_0^1 2^u \, du
\]

The antiderivative of \(2^u\) is \(\frac{2^u}{\ln 2}\). Therefore:
\[
\int_0^1 2^u \, du = \left. \frac{2^u}{\ln 2} \right|_0^1 = \frac{2^1}{\ln 2} - \frac{2^0}{\ln 2} = \frac{2}{\ln 2} - \frac{1}{\ln 2} = \frac{1}{\ln 2}
\]

### Step 3: Solve the Second Integral
\[
\int_1^2 \log_2(2x) \, dx
\]

Recall that \(\log_2(2x) = \log_2 2 + \log_2 x = 1 + \log_2 x\). Thus, the integral becomes:
\[
\int_1^2 (1 + \log_2 x) \, dx = \int_1^2 1 \, dx + \int_1^2 \log_2 x \, dx
\]

The first part is straightforward:
\[
\int_1^2 1 \, dx = [x]_1^2 = 2 - 1 = 1
\]

For the second part, we use the change of base formula \(\log_2 x = \frac{\ln x}{\ln 2}\):
\[
\int_1^2 \log_2 x \, dx = \int_1^2 \frac{\ln x}{\ln 2} \, dx = \frac{1}{\ln 2} \int_1^2 \ln x \, dx
\]

The antiderivative of \(\ln x\) is \(x \ln x - x\). Therefore:
\[
\int_1^2 \ln x \, dx = \left. (x \ln x - x) \right|_1^2 = (2 \ln 2 - 2) - (1 \ln 1 - 1) = 2 \ln 2 - 2 + 1 = 2 \ln 2 - 1
\]

Thus:
\[
\int_1^2 \log_2 x \, dx = \frac{1}{\ln 2} (2 \ln 2 - 1) = 2 - \frac{1}{\ln 2}
\]

Combining both parts:
\[
\int_1^2 (1 + \log_2 x) \, dx = 1 + \left(2 - \frac{1}{\ln 2}\right) = 3 - \frac{1}{\ln 2}
\]

### Step 4: Combine the Results
\[
\int_1^2 (2^{x-1} + \log_2(2x)) \, dx = \frac{1}{\ln 2} + \left(3 - \frac{1}{\ln 2}\right) = 3
\]

### Step 5: Numerical Approximation
The exact answer is \(3\), which is already a numerical value.

### Final Answer in JSON Format
\[
\boxed{
\begin{aligned}
&\text{"answer": "3",} \\
&\text{"numerical_answer": "3.0000000000"}
\end{aligned}
}
\]