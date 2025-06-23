To solve the definite integral \(\int_{-\pi/2}^{\pi/2} \cos(20x) \sin(25x) \, dx\), we can use the product-to-sum identities for trigonometric functions. Specifically, we use the identity:

\[
\cos(A) \sin(B) = \frac{1}{2} [\sin(A + B) - \sin(A - B)]
\]

Let \(A = 20x\) and \(B = 25x\). Applying the identity, we get:

\[
\cos(20x) \sin(25x) = \frac{1}{2} [\sin(45x) - \sin(-5x)]
\]

Since \(\sin(-5x) = -\sin(5x)\), we can rewrite the expression as:

\[
\cos(20x) \sin(25x) = \frac{1}{2} [\sin(45x) + \sin(5x)]
\]

Now, we can split the integral into two separate integrals:

\[
\int_{-\pi/2}^{\pi/2} \cos(20x) \sin(25x) \, dx = \frac{1}{2} \int_{-\pi/2}^{\pi/2} \sin(45x) \, dx + \frac{1}{2} \int_{-\pi/2}^{\pi/2} \sin(5x) \, dx
\]

We will evaluate each integral separately.

### Integral of \(\sin(45x)\):

\[
\int \sin(45x) \, dx = -\frac{1}{45} \cos(45x) + C
\]

Evaluating from \(-\pi/2\) to \(\pi/2\):

\[
\left[ -\frac{1}{45} \cos(45x) \right]_{-\pi/2}^{\pi/2} = -\frac{1}{45} \left( \cos\left(\frac{45\pi}{2}\right) - \cos\left(-\frac{45\pi}{2}\right) \right)
\]

Since \(\cos\) is an even function, \(\cos(-\theta) = \cos(\theta)\):

\[
-\frac{1}{45} \left( \cos\left(\frac{45\pi}{2}\right) - \cos\left(\frac{45\pi}{2}\right) \right) = -\frac{1}{45} \cdot 0 = 0
\]

### Integral of \(\sin(5x)\):

\[
\int \sin(5x) \, dx = -\frac{1}{5} \cos(5x) + C
\]

Evaluating from \(-\pi/2\) to \(\pi/2\):

\[
\left[ -\frac{1}{5} \cos(5x) \right]_{-\pi/2}^{\pi/2} = -\frac{1}{5} \left( \cos\left(\frac{5\pi}{2}\right) - \cos\left(-\frac{5\pi}{2}\right) \right)
\]

Since \(\cos\) is an even function, \(\cos(-\theta) = \cos(\theta)\):

\[
-\frac{1}{5} \left( \cos\left(\frac{5\pi}{2}\right) - \cos\left(\frac{5\pi}{2}\right) \right) = -\frac{1}{5} \cdot 0 = 0
\]

### Combining the Results:

\[
\int_{-\pi/2}^{\pi/2} \cos(20x) \sin(25x) \, dx = \frac{1}{2} \cdot 0 + \frac{1}{2} \cdot 0 = 0
\]

### Numerical Approximation:

The numerical approximation of the result is \(0.0000000000\).

### Final Answer:

\[
\boxed{
\begin{aligned}
\text{"answer": "0",} \\
\text{"numerical_answer": "0.0000000000"}
\end{aligned}
}
\]