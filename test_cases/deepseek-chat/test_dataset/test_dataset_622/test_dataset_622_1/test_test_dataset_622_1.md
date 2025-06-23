To compute the definite integral 

\[
\int_0^{\frac{\pi}{2}} \frac{\cos^2 x (1 + \cos x)}{(1 + \cos x + \sin x)^2} \, dx,
\]

we follow these steps:

### Step 1: Simplify the Integrand
First, observe the denominator \(1 + \cos x + \sin x\). We can rewrite it using the identity \(1 + \cos x + \sin x = 2\cos^2\left(\frac{x}{2}\right) + 2\sin\left(\frac{x}{2}\right)\cos\left(\frac{x}{2}\right) = 2\cos\left(\frac{x}{2}\right)\left(\cos\left(\frac{x}{2}\right) + \sin\left(\frac{x}{2}\right)\right)\).

However, a more useful substitution is to let:

\[
t = \tan\left(\frac{x}{2}\right).
\]

Then, we have the standard substitutions:
\[
\sin x = \frac{2t}{1 + t^2}, \quad \cos x = \frac{1 - t^2}{1 + t^2}, \quad dx = \frac{2}{1 + t^2} dt.
\]

The limits change as follows:
- When \(x = 0\), \(t = 0\).
- When \(x = \frac{\pi}{2}\), \(t = 1\).

### Step 2: Substitute and Simplify
Substitute \(t = \tan\left(\frac{x}{2}\right)\) into the integral:

\[
\int_0^{\frac{\pi}{2}} \frac{\cos^2 x (1 + \cos x)}{(1 + \cos x + \sin x)^2} dx = \int_0^1 \frac{\left(\frac{1 - t^2}{1 + t^2}\right)^2 \left(1 + \frac{1 - t^2}{1 + t^2}\right)}{\left(1 + \frac{1 - t^2}{1 + t^2} + \frac{2t}{1 + t^2}\right)^2} \cdot \frac{2}{1 + t^2} dt.
\]

Simplify the integrand:

Numerator:
\[
\cos^2 x (1 + \cos x) = \left(\frac{1 - t^2}{1 + t^2}\right)^2 \left(1 + \frac{1 - t^2}{1 + t^2}\right) = \left(\frac{1 - t^2}{1 + t^2}\right)^2 \left(\frac{2}{1 + t^2}\right) = \frac{2(1 - t^2)^2}{(1 + t^2)^3}.
\]

Denominator:
\[
(1 + \cos x + \sin x)^2 = \left(1 + \frac{1 - t^2}{1 + t^2} + \frac{2t}{1 + t^2}\right)^2 = \left(\frac{2 + 2t}{1 + t^2}\right)^2 = \frac{4(1 + t)^2}{(1 + t^2)^2}.
\]

Thus, the integrand becomes:
\[
\frac{\frac{2(1 - t^2)^2}{(1 + t^2)^3}}{\frac{4(1 + t)^2}{(1 + t^2)^2}} \cdot \frac{2}{1 + t^2} = \frac{2(1 - t^2)^2}{4(1 + t)^2(1 + t^2)} \cdot \frac{2}{1 + t^2} = \frac{(1 - t^2)^2}{(1 + t)^2(1 + t^2)} \cdot \frac{1}{1 + t^2} = \frac{(1 - t)^2}{(1 + t^2)^2}.
\]

So the integral simplifies to:
\[
\int_0^1 \frac{(1 - t)^2}{(1 + t^2)^2} dt.
\]

### Step 3: Expand and Separate
Expand the numerator:
\[
(1 - t)^2 = 1 - 2t + t^2.
\]

Thus:
\[
\int_0^1 \frac{1 - 2t + t^2}{(1 + t^2)^2} dt = \int_0^1 \frac{1 + t^2}{(1 + t^2)^2} dt - 2 \int_0^1 \frac{t}{(1 + t^2)^2} dt = \int_0^1 \frac{1}{1 + t^2} dt - 2 \int_0^1 \frac{t}{(1 + t^2)^2} dt.
\]

The first integral is straightforward:
\[
\int \frac{1}{1 + t^2} dt = \arctan t.
\]

For the second integral, let \(u = 1 + t^2\), \(du = 2t dt\):
\[
\int \frac{t}{(1 + t^2)^2} dt = \frac{1}{2} \int \frac{1}{u^2} du = -\frac{1}{2u} = -\frac{1}{2(1 + t^2)}.
\]

### Step 4: Evaluate the Integrals
Now evaluate from 0 to 1:
\[
\left. \arctan t \right|_0^1 - 2 \left( -\frac{1}{2(1 + t^2)} \right)_0^1 = \left(\frac{\pi}{4} - 0\right) - 2 \left(-\frac{1}{4} + \frac{1}{2}\right) = \frac{\pi}{4} - 2 \left(\frac{1}{4}\right) = \frac{\pi}{4} - \frac{1}{2}.
\]

### Step 5: Numerical Approximation
The exact answer is \(\frac{\pi}{4} - \frac{1}{2}\). Numerically:
\[
\frac{\pi}{4} \approx 0.7853981634, \quad \frac{\pi}{4} - \frac{1}{2} \approx 0.2853981634.
\]

### Final Answer
```json
{"answer": "\\frac{\\pi}{4} - \\frac{1}{2}", "numerical_answer": "0.2853981634"}
```