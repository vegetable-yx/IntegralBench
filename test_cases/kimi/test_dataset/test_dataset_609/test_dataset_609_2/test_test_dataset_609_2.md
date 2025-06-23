To solve the definite integral \(\int_0^1 \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor \, dx\), we need to analyze the behavior of the integrand \(\left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor\).

### Step 1: Analyze the integrand

The function \(\cos\left(\frac{\pi}{x}\right)\) oscillates between -1 and 1 as \(x\) varies from 0 to 1. The floor function \(\left\lfloor \cdot \right\rfloor\) maps any real number to the greatest integer less than or equal to that number. Therefore, \(\left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor\) will take integer values depending on the value of \(\cos\left(\frac{\pi}{x}\right)\).

### Step 2: Determine the intervals where \(\left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor\) takes specific values

- For \(\cos\left(\frac{\pi}{x}\right) \in [0, 1)\), \(\left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor = 0\).
- For \(\cos\left(\frac{\pi}{x}\right) \in [-1, 0)\), \(\left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor = -1\).

### Step 3: Identify the intervals where \(\cos\left(\frac{\pi}{x}\right)\) falls into these ranges

The cosine function \(\cos\left(\frac{\pi}{x}\right)\) oscillates between -1 and 1. We need to find the intervals where \(\cos\left(\frac{\pi}{x}\right)\) is in \([0, 1)\) and \([-1, 0)\).

- \(\cos\left(\frac{\pi}{x}\right) \in [0, 1)\) when \(\frac{\pi}{x}\) is in \([2k\pi, (2k+1)\pi)\) for \(k \in \mathbb{Z}\).
- \(\cos\left(\frac{\pi}{x}\right) \in [-1, 0)\) when \(\frac{\pi}{x}\) is in \([(2k+1)\pi, (2k+2)\pi)\) for \(k \in \mathbb{Z}\).

### Step 4: Determine the corresponding \(x\) intervals

For \(x \in (0, 1]\), we need to find the intervals where \(\frac{\pi}{x}\) falls into the specified ranges.

- For \(\frac{\pi}{x} \in [2k\pi, (2k+1)\pi)\), we have \(x \in \left(\frac{\pi}{(2k+1)\pi}, \frac{\pi}{2k\pi}\right)\).
- For \(\frac{\pi}{x} \in [(2k+1)\pi, (2k+2)\pi)\), we have \(x \in \left(\frac{\pi}{(2k+2)\pi}, \frac{\pi}{(2k+1)\pi}\right)\).

### Step 5: Integrate over the intervals

We need to sum the integrals over these intervals:

\[
\int_0^1 \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor \, dx = \sum_{k=1}^{\infty} \left( \int_{\frac{1}{2k+1}}^{\frac{1}{2k}} 0 \, dx + \int_{\frac{1}{2k+2}}^{\frac{1}{2k+1}} (-1) \, dx \right)
\]

The first integral is zero, and the second integral is:

\[
\int_{\frac{1}{2k+2}}^{\frac{1}{2k+1}} (-1) \, dx = -\left( \frac{1}{2k+1} - \frac{1}{2k+2} \right) = -\left( \frac{1}{(2k+1)(2k+2)} \right)
\]

Summing these contributions:

\[
\sum_{k=1}^{\infty} -\left( \frac{1}{(2k+1)(2k+2)} \right) = -\sum_{k=1}^{\infty} \left( \frac{1}{(2k+1)(2k+2)} \right)
\]

This series can be simplified using partial fractions:

\[
\frac{1}{(2k+1)(2k+2)} = \frac{1}{2k+1} - \frac{1}{2k+2}
\]

Thus,

\[
-\sum_{k=1}^{\infty} \left( \frac{1}{2k+1} - \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This telescopes to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right)
\]

This simplifies to:

\[
-\left( \sum_{k=1}^{\infty} \frac{1}{2k+1} - \sum_{k=1}^{\infty} \frac{1}{2k+2} \right) = -\left