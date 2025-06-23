To solve the definite integral \(\int\limits_{0}^{1}\frac{x}{\sqrt{1+x}}\:\mathbf{K}\left(\sqrt{\frac{x}{1+x}}\right)\mathbf{K}\left(\sqrt{1-x}\right)dx\), we need to carefully analyze the integrand and use known properties of the complete elliptic integral of the first kind, \(\mathbf{K}(k)\).

### Step 1: Analytical Computation

The integrand involves the complete elliptic integral of the first kind, \(\mathbf{K}(k)\), which is defined as:
\[
\mathbf{K}(k) = \int_0^{\frac{\pi}{2}} \frac{d\theta}{\sqrt{1 - k^2 \sin^2 \theta}}
\]

Given the complexity of the integrand, we will use a known result involving the product of two complete elliptic integrals. Specifically, we use the following identity:
\[
\mathbf{K}(k) \mathbf{K}(\sqrt{1 - k^2}) = \frac{\pi^2}{4}
\]

However, our integrand involves \(\mathbf{K}\left(\sqrt{\frac{x}{1+x}}\right)\) and \(\mathbf{K}\left(\sqrt{1-x}\right)\). We need to transform these arguments to match the form of the identity.

Let \(k = \sqrt{\frac{x}{1+x}}\). Then:
\[
\sqrt{1 - k^2} = \sqrt{1 - \frac{x}{1+x}} = \sqrt{\frac{1}{1+x}} = \frac{1}{\sqrt{1+x}}
\]

Thus, we have:
\[
\mathbf{K}\left(\sqrt{\frac{x}{1+x}}\right) \mathbf{K}\left(\sqrt{1 - \frac{x}{1+x}}\right) = \mathbf{K}\left(\sqrt{\frac{x}{1+x}}\right) \mathbf{K}\left(\frac{1}{\sqrt{1+x}}\right)
\]

Using the identity:
\[
\mathbf{K}\left(\sqrt{\frac{x}{1+x}}\right) \mathbf{K}\left(\frac{1}{\sqrt{1+x}}\right) = \frac{\pi^2}{4}
\]

Now, the integral simplifies to:
\[
\int_0^1 \frac{x}{\sqrt{1+x}} \cdot \frac{\pi^2}{4} \, dx
\]

Factor out the constant \(\frac{\pi^2}{4}\):
\[
\frac{\pi^2}{4} \int_0^1 \frac{x}{\sqrt{1+x}} \, dx
\]

### Step 2: Evaluate the Integral

To evaluate \(\int_0^1 \frac{x}{\sqrt{1+x}} \, dx\), we use the substitution \(u = 1 + x\), hence \(du = dx\) and \(x = u - 1\). The limits change from \(x = 0\) to \(u = 1\) and from \(x = 1\) to \(u = 2\).

The integral becomes:
\[
\int_1^2 \frac{u - 1}{\sqrt{u}} \, du = \int_1^2 \left( u^{1/2} - u^{-1/2} \right) \, du
\]

Integrate term by term:
\[
\int_1^2 u^{1/2} \, du - \int_1^2 u^{-1/2} \, du
\]

\[
= \left[ \frac{2}{3} u^{3/2} \right]_1^2 - \left[ 2 u^{1/2} \right]_1^2
\]

Evaluate at the limits:
\[
= \left( \frac{2}{3} \cdot 2^{3/2} - \frac{2}{3} \cdot 1^{3/2} \right) - \left( 2 \cdot 2^{1/2} - 2 \cdot 1^{1/2} \right)
\]

\[
= \left( \frac{2}{3} \cdot 2\sqrt{2} - \frac{2}{3} \right) - \left( 2\sqrt{2} - 2 \right)
\]

\[
= \left( \frac{4\sqrt{2}}{3} - \frac{2}{3} \right) - \left( 2\sqrt{2} - 2 \right)
\]

\[
= \frac{4\sqrt{2}}{3} - \frac{2}{3} - 2\sqrt{2} + 2
\]

Combine like terms:
\[
= \left( \frac{4\sqrt{2}}{3} - 2\sqrt{2} \right) + \left( 2 - \frac{2}{3} \right)
\]

\[
= \left( \frac{4\sqrt{2} - 6\sqrt{2}}{3} \right) + \left( \frac{6 - 2}{3} \right)
\]

\[
= \left( \frac{-2\sqrt{2}}{3} \right) + \left( \frac{4}{3} \right)
\]

\[
= \frac{4 - 2\sqrt{2}}{3}
\]

### Step 3: Numerical Approximation

The exact answer is:
\[
\frac{\pi^2}{4} \cdot \frac{4 - 2\sqrt{2}}{3}
\]

Simplify:
\[
= \frac{\pi^2 (4 - 2\sqrt{2})}{12}
\]

\[
= \frac{\pi^2 (2 - \sqrt{2})}{6}
\]

Numerical approximation:
\[
\pi^2 \approx 9.869604401
\]

\[
2 - \sqrt{2} \approx 0.585786438
\]

\[
\frac{9.869604401 \cdot 0.585786438}{6} \approx 0.968946146
\]

### Step 4: Final Answer in JSON Format

\[
\boxed{
\begin{aligned}
\text{"answer": "}\frac{\pi^2 (2 - \sqrt{2})}{6}\text{"}, \\
\text{"numerical_answer": "0.968946146"}
\end{aligned}
}
\]