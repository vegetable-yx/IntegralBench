
To solve the definite integral \(\int_0^1 \frac{\arcsin(x^2) + \arcsin(\sqrt{x})}{\sqrt{1-x^2}} \, dx\), we proceed as follows:


### Step 1: Split the integral and use substitution
Let \( I = I_1 + I_2 \), where:
\[
I_1 = \int_0^1 \frac{\arcsin(x^2)}{\sqrt{1-x^2}} \, dx, \quad I_2 = \int_0^1 \frac{\arcsin(\sqrt{x})}{\sqrt{1-x^2}} \, dx.
\]


### Step 2: Integration by parts for \(I_1\) and \(I_2\)
For \(I_1\), let \( u = \arcsin(x^2) \) and \( dv = \frac{dx}{\sqrt{1-x^2}} \). Then \( du = \frac{2x}{\sqrt{1-x^4}} \, dx \) and \( v = \arcsin(x) \). Integration by parts gives:
\[
I_1 = \left. \arcsin(x^2) \arcsin(x) \right|_0^1 - \int_0^1 \arcsin(x) \cdot \frac{2x}{\sqrt{1-x^4}} \, dx.
\]
Evaluating the boundary term: \( \arcsin(1^2) \arcsin(1) - \arcsin(0^2) \arcsin(0) = \frac{\pi}{2} \cdot \frac{\pi}{2} - 0 = \frac{\pi^2}{4} \). Thus:
\[
I_1 = \frac{\pi^2}{4} - K, \quad \text{where } K = \int_0^1 \arcsin(x) \cdot \frac{2x}{\sqrt{1-x^4}} \, dx.
\]

For \(I_2\), let \( u = \arcsin(\sqrt{x}) \) and \( dv = \frac{dx}{\sqrt{1-x^2}} \). Then \( du = \frac{1}{2\sqrt{x} \sqrt{1-x}} \, dx \) and \( v = \arcsin(x) \). Integration by parts gives:
\[
I_2 = \left. \arcsin(\sqrt{x}) \arcsin(x) \right|_0^1 - \int_0^1 \arcsin(x) \cdot \frac{1}{2\sqrt{x} \sqrt{1-x}} \, dx.
\]
Evaluating the boundary term: \( \arcsin(\sqrt{1}) \arcsin(1) - \arcsin(\sqrt{0}) \arcsin(0) = \frac{\pi}{2} \cdot \frac{\pi}{2} - 0 = \frac{\pi^2}{4} \). Thus:
\[
I_2 = \frac{\pi^2}{4} - L, \quad \text{where } L = \int_0^1 \arcsin(x) \cdot \frac{1}{2\sqrt{x} \sqrt{1-x}} \, dx.
\]


### Step 3: Relate \(K\) and \(L\) to \(I_1\) and \(I_2\)
- For \(K\), substitute \( t = x^2 \) (so \( x = \sqrt{t} \), \( dx = \frac{1}{2\sqrt{t}} dt \)). Then:
  \[
  K = \int_0^1 \arcsin(\sqrt{t}) \cdot \frac{2\sqrt{t}}{\sqrt{1-t^2}} \cdot \frac{1}{2\sqrt{t}} dt = \int_0^1 \frac{\arcsin(\sqrt{t})}{\sqrt{1-t^2}} dt = I_2.
  \]

- For \(L\), substitute \( t = \sqrt{x} \) (so \( x = t^2 \), \( dx = 2t dt \)). Then:
  \[
  L = \int_0^1 \arcsin(t^2) \cdot \frac{1}{2t \sqrt{1-t^2}} \cdot 2t dt = \int_0^1 \frac{\arcsin(t^2)}{\sqrt{1-t^2}} dt = I_1.
  \]


### Step 4: Solve for \(I\)
Adding \(I_1\) and \(I_2\):
\[
I = I_1 + I_2 = \left( \frac{\pi^2}{4} - K \right) + \left( \frac{\pi^2}{4} - L \right) = \frac{\pi^2}{2} - (K + L).
\]
But \( K = I_2 \) and \( L = I_1 \), so \( K + L = I_1 + I_2 = I \). Thus:
\[
I = \frac{\pi^2}{2} - I \implies 2I = \frac{\pi^2}{2} \implies I = \frac{\pi^2}{4}.
\]


### Numerical Approximation
The exact value is \( \frac{\pi^2}{4} \approx 2.4674011003 \) (rounded to 10 decimal places).


{"answer": "\\frac{\\pi^2}{4}", "numerical_answer": "2.4674011003"}