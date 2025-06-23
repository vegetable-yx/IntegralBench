To solve the definite integral \(\int_{\pi/6}^{\pi/3}\frac{\sin(x)+\cos(x)}{\sqrt{\sin(2x)}}\,dx\), we will follow the steps outlined.

### Step 1: Simplify the integrand

First, recall the double-angle identity for sine:
\[
\sin(2x) = 2\sin(x)\cos(x)
\]
Thus, the integrand can be rewritten as:
\[
\frac{\sin(x) + \cos(x)}{\sqrt{2\sin(x)\cos(x)}}
\]

### Step 2: Substitute \(u = \sin(x) + \cos(x)\)

Let \(u = \sin(x) + \cos(x)\). Then, we need to find \(du\):
\[
du = (\cos(x) - \sin(x))\,dx
\]

However, this substitution does not directly simplify the integral. Instead, we can use a trigonometric identity to simplify the integrand further.

### Step 3: Use trigonometric identities

Notice that:
\[
\sin(x) + \cos(x) = \sqrt{2}\sin\left(x + \frac{\pi}{4}\right)
\]
and
\[
\sin(2x) = 2\sin(x)\cos(x) = \sin^2\left(x + \frac{\pi}{4}\right) - \cos^2\left(x + \frac{\pi}{4}\right)
\]

However, this approach also seems complicated. Let's try another method.

### Step 4: Use a different substitution

Let \(t = \sin(x) - \cos(x)\). Then:
\[
dt = (\cos(x) + \sin(x))\,dx
\]

Notice that:
\[
\sin(2x) = 1 - (\sin(x) - \cos(x))^2 = 1 - t^2
\]

Thus, the integral becomes:
\[
\int \frac{dt}{\sqrt{1 - t^2}}
\]

This is a standard integral:
\[
\int \frac{dt}{\sqrt{1 - t^2}} = \arcsin(t) + C
\]

### Step 5: Evaluate the definite integral

Now, we need to evaluate the integral from \(\pi/6\) to \(\pi/3\). First, find the limits in terms of \(t\):
\[
t = \sin(x) - \cos(x)
\]

At \(x = \pi/6\):
\[
t = \sin\left(\frac{\pi}{6}\right) - \cos\left(\frac{\pi}{6}\right) = \frac{1}{2} - \frac{\sqrt{3}}{2} = \frac{1 - \sqrt{3}}{2}
\]

At \(x = \pi/3\):
\[
t = \sin\left(\frac{\pi}{3}\right) - \cos\left(\frac{\pi}{3}\right) = \frac{\sqrt{3}}{2} - \frac{1}{2} = \frac{\sqrt{3} - 1}{2}
\]

Thus, the integral becomes:
\[
\arcsin\left(\frac{\sqrt{3} - 1}{2}\right) - \arcsin\left(\frac{1 - \sqrt{3}}{2}\right)
\]

### Step 6: Numerical approximation

Using a calculator, we find:
\[
\arcsin\left(\frac{\sqrt{3} - 1}{2}\right) \approx 0.37469902
\]
\[
\arcsin\left(\frac{1 - \sqrt{3}}{2}\right) \approx -0.37469902
\]

Thus, the numerical approximation of the integral is:
\[
0.37469902 - (-0.37469902) = 0.74939804
\]

### Final Answer

\[
\boxed{
\begin{aligned}
\text{"answer": "arcsin\left(\frac{\sqrt{3} - 1}{2}\right) - arcsin\left(\frac{1 - \sqrt{3}}{2}\right)",} \\
\text{"numerical_answer": "0.74939804"}
\end{aligned}
}
\]