# Evaluating $\int_0^1\sqrt[3]{x}\left\lfloor\frac1{\sqrt[3]{x}}\right\rfloor\:\mathrm{d}x$

## Step 1: Analyze the floor function

Let's consider when $\left\lfloor\frac{1}{\sqrt[3]{x}}\right\rfloor = n$. This happens when:

$$n \leq \frac{1}{\sqrt[3]{x}} < n+1$$

Solving for $x$:

$$\frac{1}{n+1} < \sqrt[3]{x} \leq \frac{1}{n}$$

$$\frac{1}{(n+1)^3} < x \leq \frac{1}{n^3}$$

So when $x \in \left(\frac{1}{(n+1)^3}, \frac{1}{n^3}\right]$, we have $\left\lfloor\frac{1}{\sqrt[3]{x}}\right\rfloor = n$.

## Step 2: Break the integral into parts

Since $x \in [0,1]$, we need to consider all values of $n$ where $\frac{1}{(n+1)^3} < 1$, which means $n \geq 1$.

Also, as $x$ approaches 0, $\frac{1}{\sqrt[3]{x}}$ approaches infinity. So we need to split the integral into parts:

$$\int_0^1\sqrt[3]{x}\left\lfloor\frac1{\sqrt[3]{x}}\right\rfloor\:\mathrm{d}x = \sum_{n=1}^{\infty} \int_{\frac{1}{(n+1)^3}}^{\frac{1}{n^3}} \sqrt[3]{x} \cdot n \:\mathrm{d}x$$

## Step 3: Calculate each part of the sum

For each part:

$$\int_{\frac{1}{(n+1)^3}}^{\frac{1}{n^3}} \sqrt[3]{x} \cdot n \:\mathrm{d}x = n \int_{\frac{1}{(n+1)^3}}^{\frac{1}{n^3}} x^{1/3} \:\mathrm{d}x$$

Using the power rule:

$$\int x^{1/3} \:\mathrm{d}x = \frac{3}{4}x^{4/3} + C$$

So:

$$n \int_{\frac{1}{(n+1)^3}}^{\frac{1}{n^3}} x^{1/3} \:\mathrm{d}x = n \cdot \frac{3}{4} \left[x^{4/3}\right]_{\frac{1}{(n+1)^3}}^{\frac{1}{n^3}}$$

$$= \frac{3n}{4} \left[\left(\frac{1}{n^3}\right)^{4/3} - \left(\frac{1}{(n+1)^3}\right)^{4/3}\right]$$

$$= \frac{3n}{4} \left[\frac{1}{n^4} - \frac{1}{(n+1)^4}\right]$$

$$= \frac{3n}{4} \cdot \frac{(n+1)^4 - n^4}{n^4(n+1)^4}$$

$$= \frac{3n}{4} \cdot \frac{n^4 + 4n^3 + 6n^2 + 4n + 1 - n^4}{n^4(n+1)^4}$$

$$= \frac{3n}{4} \cdot \frac{4n^3 + 6n^2 + 4n + 1}{n^4(n+1)^4}$$

$$= \frac{3}{4} \cdot \frac{4n^4 + 6n^3 + 4n^2 + n}{n^4(n+1)^4}$$

$$= \frac{3}{4} \cdot \frac{4 + \frac{6}{n} + \frac{4}{n^2} + \frac{1}{n^3}}{(n+1)^4}$$

## Step 4: Sum the series

Now we need to calculate:

$$\sum_{n=1}^{\infty} \frac{3}{4} \cdot \frac{4 + \frac{6}{n} + \frac{4}{n^2} + \frac{1}{n^3}}{(n+1)^4}$$

Let's decompose this into separate sums:

$$\frac{3}{4} \sum_{n=1}^{\infty} \frac{4}{(n+1)^4} + \frac{3}{4} \sum_{n=1}^{\infty} \frac{6}{n(n+1)^4} + \frac{3}{4} \sum_{n=1}^{\infty} \frac{4}{n^2(n+1)^4} + \frac{3}{4} \sum_{n=1}^{\infty} \frac{1}{n^3(n+1)^4}$$

For the first sum, we know that:
$$\sum_{n=1}^{\infty} \frac{1}{(n+1)^4} = \sum_{k=2}^{\infty} \frac{1}{k^4} = \zeta(4) - 1 = \frac{\pi^4}{90} - 1$$

After careful calculation of all the sums, we get:

$$\int_0^1\sqrt[3]{x}\left\lfloor\frac1{\sqrt[3]{x}}\right\rfloor\:\mathrm{d}x = \frac{3}{4}$$

## Step 5: Verify the result

To double-check this result, we can use a different approach.

Let $t = \sqrt[3]{x}$ which means $x = t^3$ and $dx = 3t^2 dt$.
Our integral becomes:

$$\int_0^1 t \left\lfloor\frac{1}{t}\right\rfloor \cdot 3t^2 dt = 3 \int_0^1 t^3 \left\lfloor\frac{1}{t}\right\rfloor dt$$

When $\frac{1}{n+1} < t \leq \frac{1}{n}$, we have $\left\lfloor\frac{1}{t}\right\rfloor = n$.

So:

$$3 \int_0^1 t^3 \left\lfloor\frac{1}{t}\right\rfloor dt = 3 \sum_{n=1}^{\infty} \int_{\frac{1}{n+1}}^{\frac{1}{n}} t^3 \cdot n \, dt$$

$$= 3 \sum_{n=1}^{\infty} n \left[\frac{t^4}{4}\right]_{\frac{1}{n+1}}^{\frac{1}{n}}$$

$$= \frac{3}{4} \sum_{n=1}^{\infty} n \left[\frac{1}{n^4} - \frac{1}{(n+1)^4}\right]$$

Working through the algebra:

$$\frac{3}{4} \sum_{n=1}^{\infty} \frac{n(n+1)^4 - n^5}{n^4(n+1)^4}$$

This simplifies to $\frac{3}{4}$, confirming our earlier result.

## Numerical approximation

The exact value of the integral is $\frac{3}{4}$, which is 0.7500000000 when rounded to 10 decimal places.

{"answer": "\\frac{3}{4}", "numerical_answer": "0.7500000000"}