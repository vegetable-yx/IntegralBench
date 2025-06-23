To compute the definite integral 

\[
I = \int\limits_{0}^{\pi/2} \frac{\sin^{2n}x}{\sin^{2n}x + \cos^{2n}x} \, dx,
\]

we can use a clever substitution to simplify the integral. Here are the steps:

### Step 1: Use the substitution \( x = \frac{\pi}{2} - t \)
Let \( x = \frac{\pi}{2} - t \). Then \( dx = -dt \), and the limits change as follows:
- When \( x = 0 \), \( t = \frac{\pi}{2} \).
- When \( x = \frac{\pi}{2} \), \( t = 0 \).

The integral becomes:

\[
I = \int_{\pi/2}^{0} \frac{\sin^{2n}\left(\frac{\pi}{2} - t\right)}{\sin^{2n}\left(\frac{\pi}{2} - t\right) + \cos^{2n}\left(\frac{\pi}{2} - t\right)} (-dt) = \int_{0}^{\pi/2} \frac{\cos^{2n}t}{\cos^{2n}t + \sin^{2n}t} \, dt.
\]

Notice that the integrand is now \( \frac{\cos^{2n}x}{\sin^{2n}x + \cos^{2n}x} \). 

### Step 2: Add the original and transformed integrals
Let \( I \) be the original integral. Then:

\[
I = \int_{0}^{\pi/2} \frac{\sin^{2n}x}{\sin^{2n}x + \cos^{2n}x} \, dx,
\]

and from the substitution, we have:

\[
I = \int_{0}^{\pi/2} \frac{\cos^{2n}x}{\sin^{2n}x + \cos^{2n}x} \, dx.
\]

Adding these two expressions for \( I \):

\[
2I = \int_{0}^{\pi/2} \frac{\sin^{2n}x + \cos^{2n}x}{\sin^{2n}x + \cos^{2n}x} \, dx = \int_{0}^{\pi/2} 1 \, dx = \frac{\pi}{2}.
\]

Thus:

\[
I = \frac{\pi}{4}.
\]

### Step 3: Numerical approximation
The exact value is \( \frac{\pi}{4} \), and its numerical approximation to 10 decimal places is:

\[
\frac{\pi}{4} \approx 0.7853981634.
\]

### Final Answer
```json
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}
```