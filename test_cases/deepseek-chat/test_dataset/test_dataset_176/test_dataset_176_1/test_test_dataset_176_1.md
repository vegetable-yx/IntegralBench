To solve the definite integral 

\[
\int\limits_0^{2.0} x^{1/2} (2.0 - x)^{-1/2} \arcsin^2\left(0.5 \sqrt{x(2.0 - x)}\right) dx,
\]

we will follow the steps below:

### Step 1: Simplify the Integrand
First, observe the argument of the \(\arcsin\) function:

\[
0.5 \sqrt{x(2.0 - x)} = \sin \theta.
\]

Let’s make a substitution to simplify the integral. Let:

\[
x = 2 \sin^2 \phi, \quad dx = 4 \sin \phi \cos \phi \, d\phi.
\]

The limits of integration change as follows:
- When \(x = 0\), \(\phi = 0\).
- When \(x = 2.0\), \(\phi = \frac{\pi}{2}\).

Now, express the integrand in terms of \(\phi\):

\[
\sqrt{x} = \sqrt{2} \sin \phi, \quad \sqrt{2.0 - x} = \sqrt{2} \cos \phi.
\]

The argument of \(\arcsin\) becomes:

\[
0.5 \sqrt{x(2.0 - x)} = 0.5 \sqrt{4 \sin^2 \phi \cos^2 \phi} = \sin \phi \cos \phi.
\]

Thus, the \(\arcsin\) term is:

\[
\arcsin(\sin \phi \cos \phi) = \arcsin\left(\frac{1}{2} \sin 2\phi\right).
\]

The integrand transforms as:

\[
x^{1/2} (2.0 - x)^{-1/2} \arcsin^2\left(0.5 \sqrt{x(2.0 - x)}\right) dx = \sqrt{2} \sin \phi \cdot \frac{1}{\sqrt{2} \cos \phi} \cdot \arcsin^2(\sin \phi \cos \phi) \cdot 4 \sin \phi \cos \phi \, d\phi.
\]

Simplifying:

\[
= 4 \sin^2 \phi \, \arcsin^2(\sin \phi \cos \phi) \, d\phi.
\]

### Step 2: Simplify the \(\arcsin\) Term
Notice that:

\[
\arcsin(\sin \phi \cos \phi) = \arcsin\left(\frac{1}{2} \sin 2\phi\right).
\]

For \(\phi \in [0, \frac{\pi}{2}]\), \(\frac{1}{2} \sin 2\phi \in [0, \frac{1}{2}]\), and \(\arcsin\left(\frac{1}{2} \sin 2\phi\right) = \phi\) (since \(\sin \phi \cos \phi = \frac{1}{2} \sin 2\phi\) and \(\arcsin(\sin \theta) = \theta\) for \(\theta \in [-\frac{\pi}{2}, \frac{\pi}{2}]\)).

Thus, the integrand simplifies further to:

\[
4 \sin^2 \phi \cdot \phi^2 \, d\phi.
\]

### Step 3: Compute the Integral
Now, the integral becomes:

\[
\int_0^{\pi/2} 4 \phi^2 \sin^2 \phi \, d\phi.
\]

We can use the identity \(\sin^2 \phi = \frac{1 - \cos 2\phi}{2}\):

\[
= 4 \int_0^{\pi/2} \phi^2 \left(\frac{1 - \cos 2\phi}{2}\right) d\phi = 2 \int_0^{\pi/2} \phi^2 (1 - \cos 2\phi) d\phi.
\]

Split the integral:

\[
= 2 \left( \int_0^{\pi/2} \phi^2 \, d\phi - \int_0^{\pi/2} \phi^2 \cos 2\phi \, d\phi \right).
\]

#### First Integral:
\[
\int_0^{\pi/2} \phi^2 \, d\phi = \left. \frac{\phi^3}{3} \right|_0^{\pi/2} = \frac{\pi^3}{24}.
\]

#### Second Integral:
Use integration by parts for \(\int \phi^2 \cos 2\phi \, d\phi\):

Let \(u = \phi^2\), \(dv = \cos 2\phi \, d\phi\), then \(du = 2\phi \, d\phi\), \(v = \frac{1}{2} \sin 2\phi\).

\[
\int \phi^2 \cos 2\phi \, d\phi = \frac{\phi^2}{2} \sin 2\phi - \int \phi \sin 2\phi \, d\phi.
\]

For the remaining integral, let \(u = \phi\), \(dv = \sin 2\phi \, d\phi\), then \(du = d\phi\), \(v = -\frac{1}{2} \cos 2\phi\):

\[
\int \phi \sin 2\phi \, d\phi = -\frac{\phi}{2} \cos 2\phi + \frac{1}{2} \int \cos 2\phi \, d\phi = -\frac{\phi}{2} \cos 2\phi + \frac{1}{4} \sin 2\phi.
\]

Thus:

\[
\int \phi^2 \cos 2\phi \, d\phi = \frac{\phi^2}{2} \sin 2\phi + \frac{\phi}{2} \cos 2\phi - \frac{1}{4} \sin 2\phi.
\]

Evaluate from \(0\) to \(\pi/2\):

\[
\left. \left( \frac{\phi^2}{2} \sin 2\phi + \frac{\phi}{2} \cos 2\phi - \frac{1}{4} \sin 2\phi \right) \right|_0^{\pi/2} = \frac{\pi^2}{8} \cdot 0 + \frac{\pi}{4} \cdot (-1) - \frac{1}{4} \cdot 0 - (0 + 0 - 0) = -\frac{\pi}{4}.
\]

#### Combine Results:
\[
2 \left( \frac{\pi^3}{24} - \left(-\frac{\pi}{4}\right) \right) = 2 \left( \frac{\pi^3}{24} + \frac{\pi}{4} \right) = \frac{\pi^3}{12} + \frac{\pi}{2}.
\]

### Step 4: Numerical Approximation
Compute the numerical value:

\[
\frac{\pi^3}{12} + \frac{\pi}{2} \approx 2.9348022005 + 1.5707963268 = 4.5055985273.
\]

### Final Answer
The exact answer is:

\[
\frac{\pi^3}{12} + \frac{\pi}{2}.
\]

The numerical approximation is \(4.5055985273\).

```json
{"answer": "\\frac{\\pi^3}{12} + \\frac{\\pi}{2}", "numerical_answer": "4.5055985273"}
```