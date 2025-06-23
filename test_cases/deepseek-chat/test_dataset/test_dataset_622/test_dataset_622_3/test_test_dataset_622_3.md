To solve the definite integral 

\[
\int_0^{\frac{\pi}{2}} \frac{\cos^2 x (1 + \cos x)}{(1 + \cos x + \sin x)^2} \, dx,
\]

we will follow these steps:

### Step 1: Simplify the Integrand
First, observe the integrand:

\[
\frac{\cos^2 x (1 + \cos x)}{(1 + \cos x + \sin x)^2}.
\]

Let’s denote the denominator as \( D(x) = 1 + \cos x + \sin x \). We can rewrite the integrand as:

\[
\frac{\cos^2 x (1 + \cos x)}{D(x)^2}.
\]

### Step 2: Use a Substitution
Consider the substitution:

\[
t = \tan\left(\frac{x}{2}\right).
\]

This substitution is useful because it converts trigonometric functions into rational functions of \( t \). Recall the following identities:

\[
\sin x = \frac{2t}{1 + t^2}, \quad \cos x = \frac{1 - t^2}{1 + t^2}, \quad dx = \frac{2}{1 + t^2} dt.
\]

Under this substitution, the denominator \( D(x) \) becomes:

\[
D(x) = 1 + \frac{1 - t^2}{1 + t^2} + \frac{2t}{1 + t^2} = \frac{2 + 2t}{1 + t^2}.
\]

Similarly, the numerator \( \cos^2 x (1 + \cos x) \) becomes:

\[
\cos^2 x (1 + \cos x) = \left(\frac{1 - t^2}{1 + t^2}\right)^2 \left(1 + \frac{1 - t^2}{1 + t^2}\right) = \frac{(1 - t^2)^2}{(1 + t^2)^2} \cdot \frac{2}{1 + t^2} = \frac{2(1 - t^2)^2}{(1 + t^2)^3}.
\]

Thus, the integrand transforms to:

\[
\frac{\frac{2(1 - t^2)^2}{(1 + t^2)^3}}{\left(\frac{2 + 2t}{1 + t^2}\right)^2} = \frac{2(1 - t^2)^2 (1 + t^2)^2}{(1 + t^2)^3 (2 + 2t)^2} = \frac{2(1 - t^2)^2}{(1 + t^2)(2 + 2t)^2}.
\]

Simplifying further:

\[
\frac{2(1 - t^2)^2}{(1 + t^2) \cdot 4(1 + t)^2} = \frac{(1 - t^2)^2}{2(1 + t^2)(1 + t)^2}.
\]

Notice that \( 1 - t^2 = (1 - t)(1 + t) \), so:

\[
\frac{(1 - t)^2 (1 + t)^2}{2(1 + t^2)(1 + t)^2} = \frac{(1 - t)^2}{2(1 + t^2)}.
\]

Thus, the integral becomes:

\[
\int_{t=0}^{t=1} \frac{(1 - t)^2}{2(1 + t^2)} \cdot \frac{2}{1 + t^2} dt = \int_{0}^{1} \frac{(1 - t)^2}{(1 + t^2)^2} dt.
\]

### Step 3: Expand and Separate the Integral
Expand \( (1 - t)^2 \):

\[
(1 - t)^2 = 1 - 2t + t^2.
\]

So the integral becomes:

\[
\int_{0}^{1} \frac{1 - 2t + t^2}{(1 + t^2)^2} dt = \int_{0}^{1} \frac{1 + t^2}{(1 + t^2)^2} dt - 2 \int_{0}^{1} \frac{t}{(1 + t^2)^2} dt.
\]

Simplify each term:

\[
\int_{0}^{1} \frac{1 + t^2}{(1 + t^2)^2} dt = \int_{0}^{1} \frac{1}{1 + t^2} dt = \arctan t \Big|_{0}^{1} = \frac{\pi}{4}.
\]

For the second term:

\[
\int_{0}^{1} \frac{t}{(1 + t^2)^2} dt.
\]

Let \( u = 1 + t^2 \), \( du = 2t dt \):

\[
\int \frac{t}{u^2} \cdot \frac{du}{2} = \frac{1}{2} \int u^{-2} du = -\frac{1}{2u} + C.
\]

Evaluating from 0 to 1:

\[
-\frac{1}{2(1 + t^2)} \Big|_{0}^{1} = -\frac{1}{4} + \frac{1}{2} = \frac{1}{4}.
\]

Thus, the integral becomes:

\[
\frac{\pi}{4} - 2 \cdot \frac{1}{4} = \frac{\pi}{4} - \frac{1}{2}.
\]

### Step 4: Final Answer
The exact value of the integral is:

\[
\frac{\pi}{4} - \frac{1}{2}.
\]

A numerical approximation to 10 decimal places is:

\[
0.2853981634.
\]

### JSON Output
```json
{"answer": "\\frac{\\pi}{4} - \\frac{1}{2}", "numerical_answer": "0.2853981634"}
```