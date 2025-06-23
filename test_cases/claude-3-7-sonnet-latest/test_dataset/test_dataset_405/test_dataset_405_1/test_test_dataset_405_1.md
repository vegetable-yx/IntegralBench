# Evaluating $\int_{-4}^4e^{|x|}\cdot\{x\}\mathsf{dx}$

I'll compute this definite integral by analyzing the fractional part function $\{x\}$ and the absolute value in the exponent.

## Step 1: Understanding the integrand

The integrand contains:
- $e^{|x|}$ which is $e^{-x}$ when $x < 0$ and $e^x$ when $x \geq 0$
- $\{x\}$ which is the fractional part of $x$, defined as $\{x\} = x - \lfloor x \rfloor$

## Step 2: Splitting the integral

I'll split the integral at integer points where the fractional part function changes:

$$\int_{-4}^4e^{|x|}\cdot\{x\}\mathsf{dx} = \sum_{n=-4}^{3}\int_{n}^{n+1}e^{|x|}\cdot\{x\}\mathsf{dx}$$

Within each interval $[n, n+1]$, the fractional part $\{x\} = x - n$.

## Step 3: Evaluating each piece

Let's categorize based on the sign of $x$:

### For $x < 0$ (intervals from $-4$ to $0$):
In these intervals, $e^{|x|} = e^{-x}$ and $\{x\} = x - n$, so:

$$\int_{n}^{n+1}e^{-x}(x-n)\mathsf{dx} = \int_{n}^{n+1}(xe^{-x} - ne^{-x})\mathsf{dx}$$

For each interval $[n, n+1]$ where $n < 0$:
$$\int_{n}^{n+1}xe^{-x}\mathsf{dx} = \left[-(x+1)e^{-x}\right]_{n}^{n+1} = -(n+2)e^{-(n+1)} + (n+1)e^{-n}$$

$$\int_{n}^{n+1}ne^{-x}\mathsf{dx} = \left[-ne^{-x}\right]_{n}^{n+1} = -ne^{-(n+1)} + ne^{-n}$$

So for each interval $[n, n+1]$ where $n < 0$:
$$\int_{n}^{n+1}e^{-x}(x-n)\mathsf{dx} = -(n+2)e^{-(n+1)} + (n+1)e^{-n} + ne^{-(n+1)} - ne^{-n}$$
$$= -(n+2)e^{-(n+1)} + ne^{-(n+1)} + (n+1)e^{-n} - ne^{-n}$$
$$= -2e^{-(n+1)} + e^{-n}$$

### For $x \geq 0$ (intervals from $0$ to $4$):
In these intervals, $e^{|x|} = e^{x}$ and $\{x\} = x - n$, so:

$$\int_{n}^{n+1}e^{x}(x-n)\mathsf{dx} = \int_{n}^{n+1}(xe^{x} - ne^{x})\mathsf{dx}$$

For each interval $[n, n+1]$ where $n \geq 0$:
$$\int_{n}^{n+1}xe^{x}\mathsf{dx} = \left[xe^{x} - e^{x}\right]_{n}^{n+1} = (n+1)e^{n+1} - e^{n+1} - ne^{n} + e^{n}$$

$$\int_{n}^{n+1}ne^{x}\mathsf{dx} = \left[ne^{x}\right]_{n}^{n+1} = ne^{n+1} - ne^{n}$$

So for each interval $[n, n+1]$ where $n \geq 0$:
$$\int_{n}^{n+1}e^{x}(x-n)\mathsf{dx} = (n+1)e^{n+1} - e^{n+1} - ne^{n} + e^{n} - ne^{n+1} + ne^{n}$$
$$= (n+1)e^{n+1} - e^{n+1} - ne^{n+1} + e^{n}$$
$$= e^{n+1} + e^{n}$$

## Step 4: Summing the contributions

For the negative part ($-4 \leq n \leq -1$):
$$\sum_{n=-4}^{-1}\int_{n}^{n+1}e^{|x|}\cdot\{x\}\mathsf{dx} = \sum_{n=-4}^{-1}(-2e^{-(n+1)} + e^{-n})$$
$$= \sum_{n=-4}^{-1}(-2e^{-(n+1)}) + \sum_{n=-4}^{-1}(e^{-n})$$
$$= -2(e^{-(-3)} + e^{-(-2)} + e^{-(-1)} + e^{-(0)}) + (e^{-(-4)} + e^{-(-3)} + e^{-(-2)} + e^{-(-1)})$$
$$= -2(e^3 + e^2 + e^1 + e^0) + (e^4 + e^3 + e^2 + e^1)$$
$$= -2(e^3 + e^2 + e + 1) + (e^4 + e^3 + e^2 + e)$$
$$= e^4 - e^3 - e^2 - e - 2$$

For the positive part ($0 \leq n \leq 3$):
$$\sum_{n=0}^{3}\int_{n}^{n+1}e^{|x|}\cdot\{x\}\mathsf{dx} = \sum_{n=0}^{3}(e^{n+1} + e^{n})$$
$$= \sum_{n=0}^{3}e^{n+1} + \sum_{n=0}^{3}e^{n}$$
$$= (e^1 + e^2 + e^3 + e^4) + (e^0 + e^1 + e^2 + e^3)$$
$$= (e + e^2 + e^3 + e^4) + (1 + e + e^2 + e^3)$$
$$= 1 + 2e + 2e^2 + 2e^3 + e^4$$

## Step 5: Combining the results

$$\int_{-4}^4e^{|x|}\cdot\{x\}\mathsf{dx} = (e^4 - e^3 - e^2 - e - 2) + (1 + 2e + 2e^2 + 2e^3 + e^4)$$
$$= 2e^4 + e^3 + e^2 + e - 1$$

## Step 6: Numerical approximation

Computing the value with $e \approx 2.718281828459045$:
- $2e^4 \approx 2 \times 54.5981500331 \approx 109.1963000662$
- $e^3 \approx 20.0855369232$
- $e^2 \approx 7.3890560989$
- $e \approx 2.718281828459045$
- Final result $\approx 109.1963000662 + 20.0855369232 + 7.3890560989 + 2.718281828459045 - 1 \approx 138.3891749168$

Therefore, $\int_{-4}^4e^{|x|}\cdot\{x\}\mathsf{dx} = 2e^4 + e^3 + e^2 + e - 1 \approx 138.3891749168$

{"answer": "2e^4 + e^3 + e^2 + e - 1", "numerical_answer": "138.3891749168"}