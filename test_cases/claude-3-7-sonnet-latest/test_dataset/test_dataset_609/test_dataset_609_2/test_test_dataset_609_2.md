# Evaluating $\int_0^1\left\lfloor\cos\left(\frac{\pi}{x}\right)\right\rfloor\:\mathrm{d}x$

I'll compute this definite integral involving the floor function of $\cos(\pi/x)$.

## Step 1: Analyze the behavior of $\cos(\pi/x)$

First, I need to understand how $\cos(\pi/x)$ behaves for $x \in (0,1]$:

- When $x = 1$, $\cos(\pi/1) = \cos(\pi) = -1$
- As $x$ decreases toward 0, $\pi/x$ increases toward $\infty$
- Since $\cos(\theta)$ oscillates between -1 and 1, $\cos(\pi/x)$ will oscillate as $x$ approaches 0

Let's analyze the floor function $\lfloor\cos(\pi/x)\rfloor$:
- When $\cos(\pi/x) \in [-1,0)$, we have $\lfloor\cos(\pi/x)\rfloor = -1$
- When $\cos(\pi/x) \in [0,1)$, we have $\lfloor\cos(\pi/x)\rfloor = 0$

## Step 2: Find the intervals where $\lfloor\cos(\pi/x)\rfloor$ takes constant values

$\cos(\pi/x) = 0$ when $\pi/x = \pi/2 + n\pi$ for integer $n$
This means $x = \frac{1}{1/2 + n}$ for $n \geq 0$ (since $x \in (0,1]$)

The first few values are:
- $n=0$: $x = 2$, which is outside our integration range
- $n=1$: $x = 2/3$
- $n=2$: $x = 2/5$
- $n=3$: $x = 2/7$
And so on.

Similarly, $\cos(\pi/x) = -1$ when $\pi/x = \pi + n\pi$ for integer $n$
This means $x = \frac{1}{1 + n}$ for $n \geq 0$

The first few values are:
- $n=0$: $x = 1$
- $n=1$: $x = 1/2$
- $n=2$: $x = 1/3$
- $n=3$: $x = 1/4$
And so on.

## Step 3: Determine the pattern of the floor function

For $x \in (0,1]$, we can see that:
- $\lfloor\cos(\pi/x)\rfloor = -1$ when $x \in (\frac{1}{n+2}, \frac{1}{n+1}]$ for even $n \geq 0$
- $\lfloor\cos(\pi/x)\rfloor = 0$ when $x \in (\frac{1}{n+2}, \frac{1}{n+1}]$ for odd $n \geq 1$

Let's rewrite this more precisely:
- For $x \in (1/2, 1]$: $\lfloor\cos(\pi/x)\rfloor = -1$
- For $x \in (1/3, 1/2]$: $\lfloor\cos(\pi/x)\rfloor = 0$
- For $x \in (1/4, 1/3]$: $\lfloor\cos(\pi/x)\rfloor = -1$
- For $x \in (1/5, 1/4]$: $\lfloor\cos(\pi/x)\rfloor = 0$
And this pattern continues.

## Step 4: Calculate the integral

Now I can split the integral into the appropriate intervals:

$$\int_0^1\left\lfloor\cos\left(\frac{\pi}{x}\right)\right\rfloor\:\mathrm{d}x = \sum_{n=1}^{\infty}\int_{\frac{1}{n+1}}^{\frac{1}{n}}\left\lfloor\cos\left(\frac{\pi}{x}\right)\right\rfloor\:\mathrm{d}x$$

Using our pattern:
- For even $n$, the integral over $[\frac{1}{n+1}, \frac{1}{n}]$ equals $-1 \cdot (\frac{1}{n} - \frac{1}{n+1}) = -\frac{1}{n(n+1)}$
- For odd $n$, the integral over $[\frac{1}{n+1}, \frac{1}{n}]$ equals $0 \cdot (\frac{1}{n} - \frac{1}{n+1}) = 0$

Therefore:
$$\int_0^1\left\lfloor\cos\left(\frac{\pi}{x}\right)\right\rfloor\:\mathrm{d}x = \sum_{k=1}^{\infty}-\frac{1}{(2k)(2k+1)}$$

This simplifies to:
$$\int_0^1\left\lfloor\cos\left(\frac{\pi}{x}\right)\right\rfloor\:\mathrm{d}x = -\sum_{k=1}^{\infty}\frac{1}{2k(2k+1)}$$

We can rewrite this as:
$$-\sum_{k=1}^{\infty}\frac{1}{2k(2k+1)} = -\sum_{k=1}^{\infty}\frac{1}{2}\left(\frac{1}{k} - \frac{1}{k+1/2}\right)$$

This is a telescoping series. Let's work with:
$$S = -\frac{1}{2}\sum_{k=1}^{\infty}\left(\frac{1}{k} - \frac{1}{k+1/2}\right)$$

Using the properties of harmonic series and the digamma function, we can show that:
$$S = -\frac{1}{2}(2\ln(2) - 1)$$

Which simplifies to:
$$S = -\ln(2) + \frac{1}{2}$$

## Step 5: Numerical approximation

The exact value is $-\ln(2) + \frac{1}{2}$, which numerically is approximately:
$-0.6931471806 + 0.5 = -0.1931471806$

Therefore, the definite integral equals $-\ln(2) + \frac{1}{2} \approx -0.1931471806$

{"answer": "-\\ln(2) + \\frac{1}{2}", "numerical_answer": "-0.1931471806"}