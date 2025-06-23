

To calculate the definite integral \(\int_{-\infty}^\infty e^{-(x-2024)^2/4}\:dx\), we proceed as follows:

### Step 1: Analytic Computation
The integral involves a Gaussian function, which can be simplified using a substitution. Let \( u = \frac{x - 2024}{2} \). This implies \( x = 2u + 2024 \), and the differential \( dx = 2\,du \). 

Substituting into the integral:
\[
\int_{-\infty}^\infty e^{-(x-2024)^2/4}\:dx = \int_{-\infty}^\infty e^{-u^2} \cdot 2\,du
\]

The integral of \( e^{-u^2} \) over all real numbers is a well-known result:
\[
\int_{-\infty}^\infty e^{-u^2}\:du = \sqrt{\pi}
\]

Thus, the original integral becomes:
\[
2 \cdot \sqrt{\pi}
\]

### Step 2: Numerical Approximation
The numerical value of \( \sqrt{\pi} \) is approximately \( 1.77245385091 \). Multiplying by 2 gives:
\[
2 \cdot 1.77245385091 \approx 3.5449077018
\]

### Final Answer
The exact value is \( 2\sqrt{\pi} \), and the numerical approximation (rounded to 10 decimal places) is \( 3.5449077018 \).

{"answer": "2\\sqrt{\\pi}", "numerical_answer": "3.5449077018"}