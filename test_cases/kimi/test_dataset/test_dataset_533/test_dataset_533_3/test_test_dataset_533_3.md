To solve the definite integral \(\int_{-1}^1 (5x^3 - 3x)^2 \, dx\), we will follow the steps outlined:

### Step 1: Expand the integrand
First, we expand the integrand \((5x^3 - 3x)^2\):

\[
(5x^3 - 3x)^2 = (5x^3 - 3x)(5x^3 - 3x) = 25x^6 - 30x^4 + 9x^2
\]

### Step 2: Integrate term by term
Next, we integrate each term of the expanded polynomial from \(-1\) to \(1\):

\[
\int_{-1}^1 (25x^6 - 30x^4 + 9x^2) \, dx
\]

We can split this into three separate integrals:

\[
\int_{-1}^1 25x^6 \, dx - \int_{-1}^1 30x^4 \, dx + \int_{-1}^1 9x^2 \, dx
\]

### Step 3: Evaluate each integral
We evaluate each integral separately:

1. \(\int_{-1}^1 25x^6 \, dx\):

\[
25 \int_{-1}^1 x^6 \, dx = 25 \left[ \frac{x^7}{7} \right]_{-1}^1 = 25 \left( \frac{1^7}{7} - \frac{(-1)^7}{7} \right) = 25 \left( \frac{1}{7} - \left( -\frac{1}{7} \right) \right) = 25 \left( \frac{2}{7} \right) = \frac{50}{7}
\]

2. \(\int_{-1}^1 30x^4 \, dx\):

\[
30 \int_{-1}^1 x^4 \, dx = 30 \left[ \frac{x^5}{5} \right]_{-1}^1 = 30 \left( \frac{1^5}{5} - \frac{(-1)^5}{5} \right) = 30 \left( \frac{1}{5} - \left( -\frac{1}{5} \right) \right) = 30 \left( \frac{2}{5} \right) = 12
\]

3. \(\int_{-1}^1 9x^2 \, dx\):

\[
9 \int_{-1}^1 x^2 \, dx = 9 \left[ \frac{x^3}{3} \right]_{-1}^1 = 9 \left( \frac{1^3}{3} - \frac{(-1)^3}{3} \right) = 9 \left( \frac{1}{3} - \left( -\frac{1}{3} \right) \right) = 9 \left( \frac{2}{3} \right) = 6
\]

### Step 4: Combine the results
Now, we combine the results of the integrals:

\[
\frac{50}{7} - 12 + 6 = \frac{50}{7} - 6 = \frac{50}{7} - \frac{42}{7} = \frac{8}{7}
\]

### Step 5: Numerical approximation
The numerical approximation of \(\frac{8}{7}\) rounded to 10 decimal places is:

\[
\frac{8}{7} \approx 1.1428571429
\]

### Final Answer
\[
\boxed{
\begin{aligned}
\text{"answer": "}\frac{8}{7}\text{"}, \\
\text{"numerical_answer": "1.1428571429"}
\end{aligned}
}
\]