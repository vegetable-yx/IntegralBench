To compute the definite integral \(\int_0^{2\pi}\left|1+2\sin x\right|dx\), we follow these steps:

### Step 1: Identify the intervals where \(1 + 2\sin x\) is non-negative and negative
The expression \(1 + 2\sin x\) changes sign depending on the value of \(\sin x\). We solve for \(x\) where \(1 + 2\sin x = 0\):
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
We split the integral as follows:
\[
\int_0^{2\pi}\left|1+2\sin x\right|dx = \int_0^{7\pi/6}(1+2\sin x)dx - \int_{7\pi/6}^{11\pi/6}(1+2\sin x)dx + \int_{11\pi/6}^{2\pi}(1+2\sin x)dx
\]

#### Integral 1: \(\int_0^{7\pi/6}(1+2\sin x)dx\)
\[
\int(1+2\sin x)dx = x - 2\cos x + C
\]
Evaluating from \(0\) to \(\frac{7\pi}{6}\):
\[
\left[\frac{7\pi}{6} - 2\cos\left(\frac{7\pi}{6}\right)\right] - \left[0 - 2\cos(0)\right] = \frac{7\pi}{6} - 2\left(-\frac{\sqrt{3}}{2}\right) + 2 = \frac{7\pi}{6} + \sqrt{3} + 2
\]

#### Integral 2: \(\int_{7\pi/6}^{11\pi/6}(1+2\sin x)dx\)
Evaluating the antiderivative from \(\frac{7\pi}{6}\) to \(\frac{11\pi}{6}\):
\[
\left[\frac{11\pi}{6} - 2\cos\left(\frac{11\pi}{6}\right)\right] - \left[\frac{7\pi}{6} - 2\cos\left(\frac{7\pi}{6}\right)\right] = \frac{11\pi}{6} - 2\left(\frac{\sqrt{3}}{2}\right) - \frac{7\pi}{6} + 2\left(-\frac{\sqrt{3}}{2}\right) = \frac{4\pi}{6} - \sqrt{3} - \sqrt{3} = \frac{2\pi}{3} - 2\sqrt{3}
\]
Since this integral is subtracted, we have:
\[
-\left(\frac{2\pi}{3} - 2\sqrt{3}\right) = -\frac{2\pi}{3} + 2\sqrt{3}
\]

#### Integral 3: \(\int_{11\pi/6}^{2\pi}(1+2\sin x)dx\)
Evaluating the antiderivative from \(\frac{11\pi}{6}\) to \(2\pi\):
\[
\left[2\pi - 2\cos(2\pi)\right] - \left[\frac{11\pi}{6} - 2\cos\left(\frac{11\pi}{6}\right)\right] = 2\pi - 2(1) - \frac{11\pi}{6} + 2\left(\frac{\sqrt{3}}{2}\right) = \frac{\pi}{6} - 2 + \sqrt{3}
\]

### Step 3: Combine the results
Adding all three parts together:
\[
\left(\frac{7\pi}{6} + \sqrt{3} + 2\right) + \left(-\frac{2\pi}{3} + 2\sqrt{3}\right) + \left(\frac{\pi}{6} - 2 + \sqrt{3}\right)
\]
Simplify the terms:
\[
\frac{7\pi}{6} - \frac{4\pi}{6} + \frac{\pi}{6} + \sqrt{3} + 2\sqrt{3} + \sqrt{3} + 2 - 2 = \frac{4\pi}{6} + 4\sqrt{3} = \frac{2\pi}{3} + 4\sqrt{3}
\]

### Step 4: Numerical approximation
\[
\frac{2\pi}{3} + 4\sqrt{3} \approx 2.0943951024 + 6.9282032303 = 9.0225983327
\]

### Final Answer
\[
\boxed{
{"answer": "\\frac{2\\pi}{3} + 4\\sqrt{3}", "numerical_answer": "9.0225983327"}
}
\]