# Evaluating $\int_0^4\{x\}^4\mathrm{~dx}$

In this integral, $\{x\}$ represents the fractional part of $x$, which is defined as $\{x\} = x - \lfloor x \rfloor$, where $\lfloor x \rfloor$ is the greatest integer less than or equal to $x$.

## Step 1: Rewrite the integral over individual unit intervals

Since the fractional part of $x$ repeats in unit intervals, I'll split the integral from $0$ to $4$ into four separate integrals, each spanning a unit interval:

$$\int_0^4\{x\}^4\mathrm{~dx} = \int_0^1\{x\}^4\mathrm{~dx} + \int_1^2\{x\}^4\mathrm{~dx} + \int_2^3\{x\}^4\mathrm{~dx} + \int_3^4\{x\}^4\mathrm{~dx}$$

## Step 2: Evaluate the fractional part in each interval

For $x \in [0,1]$: $\{x\} = x$
For $x \in [1,2]$: $\{x\} = x-1$
For $x \in [2,3]$: $\{x\} = x-2$
For $x \in [3,4]$: $\{x\} = x-3$

## Step 3: Rewrite the integral

$$\int_0^4\{x\}^4\mathrm{~dx} = \int_0^1 x^4 \mathrm{~dx} + \int_1^2 (x-1)^4 \mathrm{~dx} + \int_2^3 (x-2)^4 \mathrm{~dx} + \int_3^4 (x-3)^4 \mathrm{~dx}$$

Each of these integrals has the same structure. Let's evaluate the general form:

$$\int_0^1 x^4 \mathrm{~dx} = \left. \frac{x^5}{5} \right|_0^1 = \frac{1}{5}$$

Since each of the other integrals involves a substitution of the form $u = x-n$ where $n$ is a constant, they will all evaluate to the same result:

$$\int_1^2 (x-1)^4 \mathrm{~dx} = \int_0^1 u^4 \mathrm{~du} = \frac{1}{5}$$
$$\int_2^3 (x-2)^4 \mathrm{~dx} = \int_0^1 u^4 \mathrm{~du} = \frac{1}{5}$$
$$\int_3^4 (x-3)^4 \mathrm{~dx} = \int_0^1 u^4 \mathrm{~du} = \frac{1}{5}$$

## Step 4: Compute the final result

$$\int_0^4\{x\}^4\mathrm{~dx} = \frac{1}{5} + \frac{1}{5} + \frac{1}{5} + \frac{1}{5} = \frac{4}{5} = 0.8$$

Therefore, the exact answer is $\frac{4}{5}$ and the numerical approximation (to 10 decimal places) is $0.8000000000$.

{"answer": "\\frac{4}{5}", "numerical_answer": "0.8000000000"}