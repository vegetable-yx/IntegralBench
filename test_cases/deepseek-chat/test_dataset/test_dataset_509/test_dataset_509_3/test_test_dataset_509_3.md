To compute the definite integral \(\int_0^{2\pi}\left|1+2\sin x\right|dx\), we follow these steps:

### Step 1: Identify the intervals where \(1 + 2\sin x\) is non-negative and negative
The expression \(1 + 2\sin x\) changes sign depending on the value of \(\sin x\). We solve for when \(1 + 2\sin x = 0\):
\[
1 + 2\sin x = 0 \implies \sin x = -\frac{1}{2}
\]
The solutions in \([0, 2\pi]\) are:
\[
x = \frac{7\pi}{6}, \frac{11\pi}{6}
\]
Thus, the integral splits into three intervals:
1. \([0, \frac{7\pi}{6}]\): \(1 + 2\sin x \geq 0\)
2. \([\frac{7\pi}{6}, \frac{11\pi}{6}]\): \(1 + 2\sin x \leq 0\)
3. \([\frac{11\pi}{6}, 2\pi]\): \(1 + 2\sin x \geq 0\)

### Step 2: Compute the integral over each interval
1. **Interval \([0, \frac{7\pi}{6}]\)**:
\[
\int_0^{\frac{7\pi}{6}} (1 + 2\sin x) dx = \left[x - 2\cos x\right]_0^{\frac{7\pi}{6}} = \left(\frac{7\pi}{6} - 2\cos\left(\frac{7\pi}{6}\right)\right) - (0 - 2\cos 0) = \frac{7\pi}{6} + \sqrt{3} + 2
\]

2. **Interval \([\frac{7\pi}{6}, \frac{11\pi}{6}]\)**:
\[
\int_{\frac{7\pi}{6}}^{\frac{11\pi}{6}} -(1 + 2\sin x) dx = -\left[x - 2\cos x\right]_{\frac{7\pi}{6}}^{\frac{11\pi}{6}} = -\left(\frac{11\pi}{6} - 2\cos\left(\frac{11\pi}{6}\right) - \left(\frac{7\pi}{6} - 2\cos\left(\frac{7\pi}{6}\right)\right)\right) = \frac{4\pi}{3} - 2\sqrt{3}
\]

3. **Interval \([\frac{11\pi}{6}, 2\pi]\)**:
\[
\int_{\frac{11\pi}{6}}^{2\pi} (1 + 2\sin x) dx = \left[x - 2\cos x\right]_{\frac{11\pi}{6}}^{2\pi} = \left(2\pi - 2\cos(2\pi)\right) - \left(\frac{11\pi}{6} - 2\cos\left(\frac{11\pi}{6}\right)\right) = \frac{\pi}{6} + \sqrt{3} - 2
\]

### Step 3: Sum the integrals over all intervals
\[
\int_0^{2\pi}\left|1+2\sin x\right|dx = \left(\frac{7\pi}{6} + \sqrt{3} + 2\right) + \left(\frac{4\pi}{3} - 2\sqrt{3}\right) + \left(\frac{\pi}{6} + \sqrt{3} - 2\right)
\]
Simplify the expression:
\[
= \frac{7\pi}{6} + \frac{4\pi}{3} + \frac{\pi}{6} + \sqrt{3} - 2\sqrt{3} + \sqrt{3} + 2 - 2 = \left(\frac{7\pi}{6} + \frac{8\pi}{6} + \frac{\pi}{6}\right) + 0 + 0 = \frac{16\pi}{6} = \frac{8\pi}{3}
\]

### Step 4: Numerical approximation
The exact answer is \(\frac{8\pi}{3}\). Numerically:
\[
\frac{8\pi}{3} \approx 8.3775804096
\]

### Final Answer
```json
{"answer": "\\frac{8\\pi}{3}", "numerical_answer": "8.3775804096"}
```