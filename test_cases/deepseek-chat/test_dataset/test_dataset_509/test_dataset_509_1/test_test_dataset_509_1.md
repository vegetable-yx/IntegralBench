To compute the definite integral \(\int_0^{2\pi}\left|1+2\sin x\right|dx\), we follow these steps:

### Step 1: Identify the intervals where \(1 + 2\sin x\) is non-negative
The expression \(1 + 2\sin x\) changes sign depending on the value of \(\sin x\). We solve for \(x\) where \(1 + 2\sin x = 0\):
\[
1 + 2\sin x = 0 \implies \sin x = -\frac{1}{2}
\]
The solutions in \([0, 2\pi]\) are:
\[
x = \frac{7\pi}{6}, \frac{11\pi}{6}
\]
Thus, \(1 + 2\sin x \geq 0\) on the intervals \([0, \frac{7\pi}{6}]\) and \([\frac{11\pi}{6}, 2\pi]\), and \(1 + 2\sin x < 0\) on \((\frac{7\pi}{6}, \frac{11\pi}{6})\).

### Step 2: Split the integral into the relevant intervals
\[
\int_0^{2\pi}\left|1+2\sin x\right|dx = \int_0^{\frac{7\pi}{6}} (1 + 2\sin x) \, dx + \int_{\frac{7\pi}{6}}^{\frac{11\pi}{6}} -(1 + 2\sin x) \, dx + \int_{\frac{11\pi}{6}}^{2\pi} (1 + 2\sin x) \, dx
\]

### Step 3: Compute each integral separately
1. **First integral**:
\[
\int_0^{\frac{7\pi}{6}} (1 + 2\sin x) \, dx = \left[x - 2\cos x\right]_0^{\frac{7\pi}{6}} = \left(\frac{7\pi}{6} - 2\cos\left(\frac{7\pi}{6}\right)\right) - (0 - 2\cos 0) = \frac{7\pi}{6} - 2\left(-\frac{\sqrt{3}}{2}\right) + 2 = \frac{7\pi}{6} + \sqrt{3} + 2
\]

2. **Second integral**:
\[
\int_{\frac{7\pi}{6}}^{\frac{11\pi}{6}} -(1 + 2\sin x) \, dx = -\left[x - 2\cos x\right]_{\frac{7\pi}{6}}^{\frac{11\pi}{6}} = -\left(\frac{11\pi}{6} - 2\cos\left(\frac{11\pi}{6}\right) - \left(\frac{7\pi}{6} - 2\cos\left(\frac{7\pi}{6}\right)\right)\right) = -\left(\frac{11\pi}{6} - 2\left(\frac{\sqrt{3}}{2}\right) - \frac{7\pi}{6} + 2\left(-\frac{\sqrt{3}}{2}\right)\right) = -\left(\frac{4\pi}{6} - \sqrt{3} + \sqrt{3}\right) = -\frac{2\pi}{3}
\]

3. **Third integral**:
\[
\int_{\frac{11\pi}{6}}^{2\pi} (1 + 2\sin x) \, dx = \left[x - 2\cos x\right]_{\frac{11\pi}{6}}^{2\pi} = \left(2\pi - 2\cos(2\pi)\right) - \left(\frac{11\pi}{6} - 2\cos\left(\frac{11\pi}{6}\right)\right) = 2\pi - 2 - \frac{11\pi}{6} + 2\left(\frac{\sqrt{3}}{2}\right) = \frac{\pi}{6} - 2 + \sqrt{3}
\]

### Step 4: Combine the results
\[
\int_0^{2\pi}\left|1+2\sin x\right|dx = \left(\frac{7\pi}{6} + \sqrt{3} + 2\right) + \left(-\frac{2\pi}{3}\right) + \left(\frac{\pi}{6} - 2 + \sqrt{3}\right) = \frac{7\pi}{6} - \frac{4\pi}{6} + \frac{\pi}{6} + 2\sqrt{3} = \frac{4\pi}{6} + 2\sqrt{3} = \frac{2\pi}{3} + 2\sqrt{3}
\]

### Step 5: Numerical approximation
\[
\frac{2\pi}{3} + 2\sqrt{3} \approx 2.0943951024 + 3.4641016151 = 5.5584967175
\]

### Final Answer
```json
{"answer": "\\frac{2\\pi}{3} + 2\\sqrt{3}", "numerical_answer": "5.5584967175"}
```