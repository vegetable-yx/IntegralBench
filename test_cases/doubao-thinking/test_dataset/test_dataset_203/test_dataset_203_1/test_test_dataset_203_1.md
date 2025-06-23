
To solve the definite integral \(\int_{0}^{2} x^2 \cos\left(\sqrt{x(2-x)}\right) dx\), we proceed with the following steps:

### Step 1: Simplify the argument of the cosine function
First, rewrite the expression inside the square root:
\[
x(2-x) = 2x - x^2 = 1 - (x-1)^2
\]
This suggests a substitution \(t = x - 1\), shifting the interval of integration to \([-1, 1]\). Let \(x = t + 1\), so \(dx = dt\), and the integral becomes:
\[
\int_{-1}^{1} (t+1)^2 \cos\left(\sqrt{1 - t^2}\right) dt
\]

### Step 2: Expand and simplify the integrand
Expanding \((t+1)^2\) gives \(t^2 + 2t + 1\). The integral splits into three parts:
\[
\int_{-1}^{1} (t^2 + 2t + 1) \cos\left(\sqrt{1 - t^2}\right) dt = \int_{-1}^{1} t^2 \cos\left(\sqrt{1 - t^2}\right) dt + 2 \int_{-1}^{1} t \cos\left(\sqrt{1 - t^2}\right) dt + \int_{-1}^{1} \cos\left(\sqrt{1 - t^2}\right) dt
\]
The middle term involves an odd function (\(t \cdot \text{even function}\)) integrated over symmetric limits, so it vanishes:
\[
2 \int_{-1}^{1} t \cos\left(\sqrt{1 - t^2}\right) dt = 0
\]
Thus, the integral reduces to:
\[
\int_{-1}^{1} (t^2 + 1) \cos\left(\sqrt{1 - t^2}\right) dt
\]

### Step 3: Trigonometric substitution
Let \(t = \sin\theta\), so \(dt = \cos\theta d\theta\) and \(\sqrt{1 - t^2} = \cos\theta\). The limits \(t = -1\) and \(t = 1\) correspond to \(\theta = -\pi/2\) and \(\theta = \pi/2\). The integral becomes:
\[
\int_{-\pi/2}^{\pi/2} (\sin^2\theta + 1) \cos(\cos\theta) \cos\theta d\theta
\]
Since the integrand is even, we simplify to:
\[
2 \int_{0}^{\pi/2} (\sin^2\theta + 1) \cos(\cos\theta) \cos\theta d\theta
\]
Using \(\sin^2\theta + 1 = 2 - \cos^2\theta\), we split the integral:
\[
2 \left[ 2 \int_{0}^{\pi/2} \cos\theta \cos(\cos\theta) d\theta - \int_{0}^{\pi/2} \cos^3\theta \cos(\cos\theta) d\theta \right]
\]

### Step 4: Evaluate the integrals
Let \(A = \int_{0}^{\pi/2} \cos\theta \cos(\cos\theta) d\theta\) and \(B = \int_{0}^{\pi/2} \cos^3\theta \cos(\cos\theta) d\theta\).

For \(A\), substitute \(u = \sin\theta\) (so \(du = \cos\theta d\theta\)):
\[
A = \int_{0}^{1} \cos(u) du = \sin(1)
\]

For \(B\), use \(t = \cos\theta\) and expand \(\cos^3\theta = \cos\theta (1 - \sin^2\theta)\). After substitution and simplification, \(B = -\sin(1) + 2\cos(1)\).

### Step 5: Combine results
The original integral becomes:
\[
2 \left[ 2A - B \right] = 2 \left[ 2\sin(1) - (-\sin(1) + 2\cos(1)) \right] = 6\sin(1) - 4\cos(1)
\]

### Numerical Approximation
Using \(\sin(1) \approx 0.8414709848\) and \(\cos(1) \approx 0.5403023059\):
\[
6\sin(1) - 4\cos(1) \approx 6(0.8414709848) - 4(0.5403023059) \approx 2.8876166854
\]

{"answer": "6\\sin(1) - 4\\cos(1)", "numerical_answer": "2.8876166854"}