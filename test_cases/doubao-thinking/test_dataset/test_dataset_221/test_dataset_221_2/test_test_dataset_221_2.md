

To solve the definite integral \(\int_{0}^{1} x^{-1/2}(1-x)^{-1/2} T_{4}\left(\sqrt{x(1-x)}\right) dx\), we follow these steps:

### Step 1: Recall the Chebyshev polynomial \(T_4(z)\)
The fourth Chebyshev polynomial of the first kind is \(T_4(z) = 8z^4 - 8z^2 + 1\).

### Step 2: Substitute \(z = \sqrt{x(1-x)}\) into \(T_4(z)\)
Substituting \(z = \sqrt{x(1-x)}\), we get:
\[
T_4\left(\sqrt{x(1-x)}\right) = 8\left(x(1-x)\right)^2 - 8\left(x(1-x)\right) + 1
\]

### Step 3: Expand the integrand
The integrand becomes:
\[
x^{-1/2}(1-x)^{-1/2} \left[8x^2(1-x)^2 - 8x(1-x) + 1\right]
\]
Simplifying each term:
- \(8x^2(1-x)^2 \cdot x^{-1/2}(1-x)^{-1/2} = 8x^{3/2}(1-x)^{3/2}\)
- \(-8x(1-x) \cdot x^{-1/2}(1-x)^{-1/2} = -8x^{1/2}(1-x)^{1/2}\)
- \(1 \cdot x^{-1/2}(1-x)^{-1/2} = \frac{1}{\sqrt{x(1-x)}}\)

### Step 4: Express the integral as a sum of Beta functions
The integral splits into three terms:
\[
I = 8 \int_{0}^{1} x^{3/2}(1-x)^{3/2} dx - 8 \int_{0}^{1} x^{1/2}(1-x)^{1/2} dx + \int_{0}^{1} \frac{1}{\sqrt{x(1-x)}} dx
\]
These integrals are Beta functions \(B(a,b) = \int_{0}^{1} t^{a-1}(1-t)^{b-1} dt = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}\), where \(\Gamma\) is the Gamma function.

### Step 5: Evaluate each Beta function
1. For \(8 \int_{0}^{1} x^{3/2}(1-x)^{3/2} dx\):  
   \(a = b = \frac{5}{2}\), so \(B\left(\frac{5}{2}, \frac{5}{2}\right) = \frac{\Gamma\left(\frac{5}{2}\right)^2}{\Gamma(5)}\).  
   \(\Gamma\left(\frac{5}{2}\right) = \frac{3\sqrt{\pi}}{4}\), \(\Gamma(5) = 24\).  
   Thus, \(B\left(\frac{5}{2}, \frac{5}{2}\right) = \frac{9\pi}{384} = \frac{3\pi}{128}\).  
   The first term: \(8 \cdot \frac{3\pi}{128} = \frac{3\pi}{16}\).

2. For \(-8 \int_{0}^{1} x^{1/2}(1-x)^{1/2} dx\):  
   \(a = b = \frac{3}{2}\), so \(B\left(\frac{3}{2}, \frac{3}{2}\right) = \frac{\Gamma\left(\frac{3}{2}\right)^2}{\Gamma(3)}\).  
   \(\Gamma\left(\frac{3}{2}\right) = \frac{\sqrt{\pi}}{2}\), \(\Gamma(3) = 2\).  
   Thus, \(B\left(\frac{3}{2}, \frac{3}{2}\right) = \frac{\pi}{8}\).  
   The second term: \(-8 \cdot \frac{\pi}{8} = -\pi\).

3. For \(\int_{0}^{1} \frac{1}{\sqrt{x(1-x)}} dx\):  
   \(a = b = \frac{1}{2}\), so \(B\left(\frac{1}{2}, \frac{1}{2}\right) = \frac{\Gamma\left(\frac{1}{2}\right)^2}{\Gamma(1)} = \pi\).  
   The third term: \(\pi\).

### Step 6: Combine the results
Adding the three terms:
\[
I = \frac{3\pi}{16} - \pi + \pi = \frac{3\pi}{16}
\]

### Numerical Approximation
The numerical value of \(\frac{3\pi}{16}\) is approximately \(0.5890486225\) (rounded to 10 decimal places).

{"answer": "\\frac{3\\pi}{16}", "numerical_answer": "0.5890486225"}