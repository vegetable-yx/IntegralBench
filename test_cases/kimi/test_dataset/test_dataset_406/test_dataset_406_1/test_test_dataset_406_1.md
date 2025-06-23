To solve the definite integral \(\int_{\pi/6}^{\pi/3}\frac{\sin(x)+\cos(x)}{\sqrt{\sin(2x)}}\,dx\), we will follow the steps outlined.

### Step 1: Analytical Solution

First, let's simplify the integrand. Recall that \(\sin(2x) = 2\sin(x)\cos(x)\). Thus, we can rewrite the integrand as follows:

\[
\frac{\sin(x) + \cos(x)}{\sqrt{\sin(2x)}} = \frac{\sin(x) + \cos(x)}{\sqrt{2\sin(x)\cos(x)}}
\]

Next, we can factor out \(\sqrt{2}\) from the denominator:

\[
\frac{\sin(x) + \cos(x)}{\sqrt{2\sin(x)\cos(x)}} = \frac{\sin(x) + \cos(x)}{\sqrt{2}\sqrt{\sin(x)\cos(x)}} = \frac{\sin(x) + \cos(x)}{\sqrt{2}\sqrt{\sin(x)\cos(x)}}
\]

Now, let's make a substitution to simplify the integral. Let \(u = \sin(x) - \cos(x)\). Then, \(du = (\cos(x) + \sin(x))dx\). Notice that \(\sin(x) + \cos(x)\) is the differential of \(u\), so we can rewrite the integral in terms of \(u\):

\[
\int \frac{\sin(x) + \cos(x)}{\sqrt{2\sin(x)\cos(x)}}\,dx = \int \frac{1}{\sqrt{2\sin(x)\cos(x)}} (\sin(x) + \cos(x))\,dx
\]

Since \(\sin(x) + \cos(x) = du\), we have:

\[
\int \frac{1}{\sqrt{2\sin(x)\cos(x)}} du
\]

Next, we need to express \(\sin(x)\cos(x)\) in terms of \(u\). Recall that:

\[
\sin(x)\cos(x) = \frac{1 - (\sin(x) - \cos(x))^2}{2} = \frac{1 - u^2}{2}
\]

Thus, the integral becomes:

\[
\int \frac{1}{\sqrt{2 \cdot \frac{1 - u^2}{2}}} du = \int \frac{1}{\sqrt{1 - u^2}} du
\]

This is a standard integral:

\[
\int \frac{1}{\sqrt{1 - u^2}} du = \arcsin(u) + C
\]

Now, we need to evaluate this from \(u = \sin(\pi/6) - \cos(\pi/6)\) to \(u = \sin(\pi/3) - \cos(\pi/3)\):

\[
u_1 = \sin(\pi/6) - \cos(\pi/6) = \frac{1}{2} - \frac{\sqrt{3}}{2} = \frac{1 - \sqrt{3}}{2}
\]

\[
u_2 = \sin(\pi/3) - \cos(\pi/3) = \frac{\sqrt{3}}{2} - \frac{1}{2} = \frac{\sqrt{3} - 1}{2}
\]

Thus, the definite integral is:

\[
\arcsin\left(\frac{\sqrt{3} - 1}{2}\right) - \arcsin\left(\frac{1 - \sqrt{3}}{2}\right)
\]

### Step 2: Numerical Approximation

Using a calculator or numerical integration tool, we can approximate the values of the arcsine functions:

\[
\arcsin\left(\frac{\sqrt{3} - 1}{2}\right) \approx 0.3746990267
\]

\[
\arcsin\left(\frac{1 - \sqrt{3}}{2}\right) \approx -0.3746990267
\]

Thus, the numerical approximation of the integral is:

\[
0.3746990267 - (-0.3746990267) = 0.7493980534
\]

### Step 3: Final Answer in JSON Format

\[
\boxed{
\begin{aligned}
\text{"answer": "arcsin\left(\frac{\sqrt{3} - 1}{2}\right) - arcsin\left(\frac{1 - \sqrt{3}}{2}\right)",} \\
\text{"numerical_answer": "0.7493980534"}
\end{aligned}
}
\]