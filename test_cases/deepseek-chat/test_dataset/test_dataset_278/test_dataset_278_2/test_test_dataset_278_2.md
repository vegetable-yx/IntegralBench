To solve the definite integral 

\[
\int\limits_0^2 x^{1/2}(2-x)^{-1/2}\cosh\left(\sqrt{x(2-x)}\right)dx,
\]

we will follow these steps:

### Step 1: Simplify the Integrand
First, observe the integrand:

\[
x^{1/2}(2-x)^{-1/2}\cosh\left(\sqrt{x(2-x)}\right).
\]

Let’s make a substitution to simplify the expression. Let:

\[
u = \sqrt{x(2-x)}.
\]

However, this substitution might not directly simplify the integral. Instead, consider the substitution:

\[
x = 2\sin^2\theta, \quad dx = 4\sin\theta\cos\theta d\theta.
\]

The limits change as follows:
- When \( x = 0 \), \( \theta = 0 \).
- When \( x = 2 \), \( \theta = \frac{\pi}{2} \).

Now, express the integrand in terms of \( \theta \):

\[
x^{1/2} = (2\sin^2\theta)^{1/2} = \sqrt{2}\sin\theta,
\]
\[
(2-x)^{-1/2} = (2 - 2\sin^2\theta)^{-1/2} = (2\cos^2\theta)^{-1/2} = \frac{1}{\sqrt{2}\cos\theta},
\]
\[
\sqrt{x(2-x)} = \sqrt{2\sin^2\theta \cdot 2\cos^2\theta} = 2\sin\theta\cos\theta.
\]

Thus, the integrand becomes:

\[
\sqrt{2}\sin\theta \cdot \frac{1}{\sqrt{2}\cos\theta} \cdot \cosh(2\sin\theta\cos\theta) = \frac{\sin\theta}{\cos\theta} \cosh(2\sin\theta\cos\theta).
\]

The integral now is:

\[
\int_0^{\pi/2} \frac{\sin\theta}{\cos\theta} \cosh(2\sin\theta\cos\theta) \cdot 4\sin\theta\cos\theta d\theta = 4 \int_0^{\pi/2} \sin^2\theta \cosh(2\sin\theta\cos\theta) d\theta.
\]

### Step 2: Further Simplification
Notice that \( 2\sin\theta\cos\theta = \sin(2\theta) \). Thus, the integral becomes:

\[
4 \int_0^{\pi/2} \sin^2\theta \cosh(\sin(2\theta)) d\theta.
\]

This integral does not have a straightforward antiderivative in terms of elementary functions. However, we can consider symmetry or another substitution. 

Let’s try \( \phi = 2\theta \), \( d\phi = 2d\theta \), and the limits become \( 0 \) to \( \pi \):

\[
4 \int_0^{\pi} \sin^2\left(\frac{\phi}{2}\right) \cosh(\sin\phi) \cdot \frac{d\phi}{2} = 2 \int_0^{\pi} \sin^2\left(\frac{\phi}{2}\right) \cosh(\sin\phi) d\phi.
\]

Using the identity \( \sin^2\left(\frac{\phi}{2}\right) = \frac{1 - \cos\phi}{2} \), we get:

\[
2 \int_0^{\pi} \frac{1 - \cos\phi}{2} \cosh(\sin\phi) d\phi = \int_0^{\pi} (1 - \cos\phi) \cosh(\sin\phi) d\phi.
\]

### Step 3: Split the Integral
Split the integral into two parts:

\[
\int_0^{\pi} \cosh(\sin\phi) d\phi - \int_0^{\pi} \cos\phi \cosh(\sin\phi) d\phi.
\]

The first integral is known:

\[
\int_0^{\pi} \cosh(\sin\phi) d\phi = \pi I_0(1),
\]

where \( I_0 \) is the modified Bessel function of the first kind.

The second integral can be computed as follows. Let \( v = \sin\phi \), \( dv = \cos\phi d\phi \):

\[
\int_0^{\pi} \cos\phi \cosh(\sin\phi) d\phi = \int_0^0 \cosh(v) dv = 0,
\]

because the limits of integration are the same. Thus, the second integral vanishes.

### Step 4: Final Answer
The integral simplifies to:

\[
\pi I_0(1).
\]

The modified Bessel function \( I_0(1) \) has a known value, and its numerical approximation is:

\[
I_0(1) \approx 1.266065877752.
\]

Thus, the numerical approximation of the integral is:

\[
\pi \cdot 1.266065877752 \approx 3.9774632605.
\]

### Final Answer
```json
{"answer": "\\pi I_0(1)", "numerical_answer": "3.9774632605"}
```