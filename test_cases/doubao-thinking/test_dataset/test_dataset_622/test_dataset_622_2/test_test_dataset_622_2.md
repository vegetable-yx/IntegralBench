
To solve the definite integral \(\int_0^{\frac{\pi}{2}}\frac{\cos^2x(1+\cos x)}{(1+\cos x+\sin x)^2}\mathrm{d}x\), we proceed as follows:


### Step 1: Substitution with Weierstrass Substitution
We use the Weierstrass substitution \(t = \tan\left(\frac{x}{2}\right)\), which transforms trigonometric functions into rational functions. For \(x \in [0, \frac{\pi}{2}]\), \(t \in [0, 1]\). The substitutions are:
\[
\sin x = \frac{2t}{1+t^2}, \quad \cos x = \frac{1-t^2}{1+t^2}, \quad \mathrm{d}x = \frac{2\mathrm{d}t}{1+t^2}.
\]

### Step 2: Simplify the Integrand
First, compute the denominator \(1 + \cos x + \sin x\):
\[
1 + \cos x + \sin x = 1 + \frac{1-t^2}{1+t^2} + \frac{2t}{1+t^2} = \frac{2(1+t)}{1+t^2}.
\]
The numerator \(\cos^2x(1+\cos x)\) becomes:
\[
\cos^2x(1+\cos x) = \left(\frac{1-t^2}{1+t^2}\right)^2 \left(1 + \frac{1-t^2}{1+t^2}\right) = \frac{2(1-t^2)^2}{(1+t^2)^3}.
\]
Thus, the integrand simplifies to:
\[
\frac{\cos^2x(1+\cos x)}{(1+\cos x+\sin x)^2} \cdot \mathrm{d}x = \frac{\frac{2(1-t^2)^2}{(1+t^2)^3}}{\left(\frac{2(1+t)}{1+t^2}\right)^2} \cdot \frac{2\mathrm{d}t}{1+t^2} = \frac{(1-t)^2}{(1+t^2)^2}\mathrm{d}t.
\]


### Step 3: Evaluate the Simplified Integral
The integral reduces to:
\[
\int_0^1 \frac{(1-t)^2}{(1+t^2)^2}\mathrm{d}t.
\]
Expand the numerator \((1-t)^2 = 1 - 2t + t^2\), so:
\[
\frac{(1-t)^2}{(1+t^2)^2} = \frac{1 + t^2 - 2t}{(1+t^2)^2} = \frac{1}{1+t^2} - \frac{2t}{(1+t^2)^2}.
\]
Integrate term-by-term:
- The first term: \(\int_0^1 \frac{1}{1+t^2}\mathrm{d}t = \left[\arctan t\right]_0^1 = \frac{\pi}{4}\).
- The second term: \(\int_0^1 \frac{2t}{(1+t^2)^2}\mathrm{d}t = \left[-\frac{1}{1+t^2}\right]_0^1 = \left(-\frac{1}{2}\right) - (-1) = \frac{1}{2}\).


### Step 4: Combine Results
Thus, the integral evaluates to:
\[
\int_0^{\frac{\pi}{2}}\frac{\cos^2x(1+\cos x)}{(1+\cos x+\sin x)^2}\mathrm{d}x = \frac{\pi}{4} - \frac{1}{2}.
\]


### Numerical Approximation
The numerical value of \(\frac{\pi}{4} - \frac{1}{2}\) is approximately \(0.2853981634\) (rounded to 10 decimal places).


{"answer": "\\frac{\\pi}{4} - \\frac{1}{2}", "numerical_answer": "0.2853981634"}