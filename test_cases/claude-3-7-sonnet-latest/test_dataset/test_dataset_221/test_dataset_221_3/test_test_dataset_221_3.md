# Evaluating $\int_{0}^{1}x^{-1/2}(1-x)^{-1/2}T_{4}\left(\sqrt{x(1-x)}\right)dx$

First, I need to recall that $T_4(x)$ is the 4th Chebyshev polynomial of the first kind.

The Chebyshev polynomial $T_4(x)$ is given by:
$T_4(x) = 8x^4 - 8x^2 + 1$

## Step 1: Substitute the Chebyshev polynomial
Let $u = \sqrt{x(1-x)}$, then:
$T_4(u) = T_4\left(\sqrt{x(1-x)}\right) = 8[x(1-x)]^2 - 8[x(1-x)] + 1$
$= 8x^2(1-x)^2 - 8x(1-x) + 1$
$= 8x^2(1-2x+x^2) - 8x(1-x) + 1$
$= 8x^2 - 16x^3 + 8x^4 - 8x + 8x^2 + 1$
$= 8x^4 - 16x^3 + 16x^2 - 8x + 1$

Now our integral becomes:
$\int_{0}^{1}x^{-1/2}(1-x)^{-1/2}(8x^4 - 16x^3 + 16x^2 - 8x + 1)dx$

## Step 2: Break down the integral
$\int_{0}^{1}x^{-1/2}(1-x)^{-1/2}(8x^4 - 16x^3 + 16x^2 - 8x + 1)dx$
$= 8\int_{0}^{1}x^{-1/2+4}(1-x)^{-1/2}dx - 16\int_{0}^{1}x^{-1/2+3}(1-x)^{-1/2}dx + 16\int_{0}^{1}x^{-1/2+2}(1-x)^{-1/2}dx - 8\int_{0}^{1}x^{-1/2+1}(1-x)^{-1/2}dx + \int_{0}^{1}x^{-1/2}(1-x)^{-1/2}dx$
$= 8\int_{0}^{1}x^{7/2}(1-x)^{-1/2}dx - 16\int_{0}^{1}x^{5/2}(1-x)^{-1/2}dx + 16\int_{0}^{1}x^{3/2}(1-x)^{-1/2}dx - 8\int_{0}^{1}x^{1/2}(1-x)^{-1/2}dx + \int_{0}^{1}x^{-1/2}(1-x)^{-1/2}dx$

## Step 3: Apply the Beta function
I'll use the Beta function formula:
$\int_{0}^{1}x^{\alpha-1}(1-x)^{\beta-1}dx = B(\alpha,\beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$

For each integral, I need to identify $\alpha$ and $\beta$:

1. $\int_{0}^{1}x^{7/2}(1-x)^{-1/2}dx = B(9/2,1/2) = \frac{\Gamma(9/2)\Gamma(1/2)}{\Gamma(5)}$

2. $\int_{0}^{1}x^{5/2}(1-x)^{-1/2}dx = B(7/2,1/2) = \frac{\Gamma(7/2)\Gamma(1/2)}{\Gamma(4)}$

3. $\int_{0}^{1}x^{3/2}(1-x)^{-1/2}dx = B(5/2,1/2) = \frac{\Gamma(5/2)\Gamma(1/2)}{\Gamma(3)}$

4. $\int_{0}^{1}x^{1/2}(1-x)^{-1/2}dx = B(3/2,1/2) = \frac{\Gamma(3/2)\Gamma(1/2)}{\Gamma(2)}$

5. $\int_{0}^{1}x^{-1/2}(1-x)^{-1/2}dx = B(1/2,1/2) = \frac{\Gamma(1/2)\Gamma(1/2)}{\Gamma(1)}$

Let's compute these values using the properties of the Gamma function:
- $\Gamma(1/2) = \sqrt{\pi}$
- $\Gamma(n+1) = n\Gamma(n)$
- $\Gamma(1) = 1$

Therefore:
- $\Gamma(3/2) = \frac{1}{2}\Gamma(1/2) = \frac{\sqrt{\pi}}{2}$
- $\Gamma(5/2) = \frac{3}{2}\Gamma(3/2) = \frac{3\sqrt{\pi}}{4}$
- $\Gamma(7/2) = \frac{5}{2}\Gamma(5/2) = \frac{15\sqrt{\pi}}{8}$
- $\Gamma(9/2) = \frac{7}{2}\Gamma(7/2) = \frac{105\sqrt{\pi}}{16}$

Now calculating each Beta function:

1. $B(9/2,1/2) = \frac{\Gamma(9/2)\Gamma(1/2)}{\Gamma(5)} = \frac{\frac{105\sqrt{\pi}}{16} \cdot \sqrt{\pi}}{24} = \frac{105\pi}{384}$

2. $B(7/2,1/2) = \frac{\Gamma(7/2)\Gamma(1/2)}{\Gamma(4)} = \frac{\frac{15\sqrt{\pi}}{8} \cdot \sqrt{\pi}}{6} = \frac{15\pi}{48}$

3. $B(5/2,1/2) = \frac{\Gamma(5/2)\Gamma(1/2)}{\Gamma(3)} = \frac{\frac{3\sqrt{\pi}}{4} \cdot \sqrt{\pi}}{2} = \frac{3\pi}{8}$

4. $B(3/2,1/2) = \frac{\Gamma(3/2)\Gamma(1/2)}{\Gamma(2)} = \frac{\frac{\sqrt{\pi}}{2} \cdot \sqrt{\pi}}{1} = \frac{\pi}{2}$

5. $B(1/2,1/2) = \frac{\Gamma(1/2)\Gamma(1/2)}{\Gamma(1)} = \frac{\sqrt{\pi} \cdot \sqrt{\pi}}{1} = \pi$

## Step 4: Combine all terms
Now let's substitute these values back:

$\int_{0}^{1}x^{-1/2}(1-x)^{-1/2}T_{4}\left(\sqrt{x(1-x)}\right)dx$
$= 8 \cdot \frac{105\pi}{384} - 16 \cdot \frac{15\pi}{48} + 16 \cdot \frac{3\pi}{8} - 8 \cdot \frac{\pi}{2} + \pi$
$= \frac{8 \cdot 105\pi}{384} - \frac{16 \cdot 15\pi}{48} + \frac{16 \cdot 3\pi}{8} - \frac{8\pi}{2} + \pi$
$= \frac{840\pi}{384} - \frac{240\pi}{48} + \frac{48\pi}{8} - 4\pi + \pi$
$= \frac{35\pi}{16} - 5\pi + 6\pi - 4\pi + \pi$
$= \frac{35\pi}{16} - 2\pi$
$= \frac{35\pi - 32\pi}{16}$
$= \frac{3\pi}{16}$

## Step 5: Numerical approximation
$\frac{3\pi}{16} \approx \frac{3 \times 3.14159265359}{16} \approx 0.5890486726$

Therefore, the value of the definite integral is $\frac{3\pi}{16} \approx 0.5890486726$.

{"answer": "\\frac{3\\pi}{16}", "numerical_answer": "0.5890486726"}