# Evaluating $\int_{-4}^4e^{|x|}\cdot\{x\}\mathsf{dx}$

In this integral, $\{x\}$ represents the fractional part of $x$, defined as $\{x\} = x - \lfloor x \rfloor$.

## Step 1: Rewriting the integral

First, I'll split the integral at $x=0$ since $|x|$ has different expressions on either side:

$$\int_{-4}^4e^{|x|}\cdot\{x\}\mathsf{dx} = \int_{-4}^0e^{-x}\cdot\{x\}\mathsf{dx} + \int_{0}^4e^{x}\cdot\{x\}\mathsf{dx}$$

## Step 2: Evaluating $\int_{-4}^0e^{-x}\cdot\{x\}\mathsf{dx}$

For negative numbers $x$, the fractional part is $\{x\} = x - \lfloor x \rfloor$. When $-4 \leq x < 0$:
- For $-4 \leq x < -3$: $\{x\} = x+4$
- For $-3 \leq x < -2$: $\{x\} = x+3$
- For $-2 \leq x < -1$: $\{x\} = x+2$
- For $-1 \leq x < 0$: $\{x\} = x+1$

So I need to split this integral into four parts:

$$\int_{-4}^0e^{-x}\cdot\{x\}\mathsf{dx} = \int_{-4}^{-3}e^{-x}\cdot(x+4)\mathsf{dx} + \int_{-3}^{-2}e^{-x}\cdot(x+3)\mathsf{dx} + \int_{-2}^{-1}e^{-x}\cdot(x+2)\mathsf{dx} + \int_{-1}^{0}e^{-x}\cdot(x+1)\mathsf{dx}$$

For each interval, I'll compute $\int e^{-x}(x+k)dx = -e^{-x}(x+k) - e^{-x}$:

For $[-4,-3]$:
$$\int_{-4}^{-3}e^{-x}\cdot(x+4)\mathsf{dx} = [-e^{-x}(x+4) - e^{-x}]_{-4}^{-3} = -e^3((-3)+4) - e^3 + e^4((-4)+4) + e^4 = -e^3 - e^3 + e^4 = -2e^3 + e^4$$

For $[-3,-2]$:
$$\int_{-3}^{-2}e^{-x}\cdot(x+3)\mathsf{dx} = [-e^{-x}(x+3) - e^{-x}]_{-3}^{-2} = -e^2((-2)+3) - e^2 + e^3((-3)+3) + e^3 = -e^2 - e^2 + e^3 = -2e^2 + e^3$$

For $[-2,-1]$:
$$\int_{-2}^{-1}e^{-x}\cdot(x+2)\mathsf{dx} = [-e^{-x}(x+2) - e^{-x}]_{-2}^{-1} = -e^1((-1)+2) - e^1 + e^2((-2)+2) + e^2 = -e^1 - e^1 + e^2 = -2e + e^2$$

For $[-1,0]$:
$$\int_{-1}^{0}e^{-x}\cdot(x+1)\mathsf{dx} = [-e^{-x}(x+1) - e^{-x}]_{-1}^{0} = -e^0((0)+1) - e^0 + e^1((-1)+1) + e^1 = -1 - 1 + e = -2 + e$$

Adding these results:
$$\int_{-4}^0e^{-x}\cdot\{x\}\mathsf{dx} = (-2e^3 + e^4) + (-2e^2 + e^3) + (-2e + e^2) + (-2 + e) = -2 - 2e - 2e^2 - 2e^3 + e + e^2 + e^3 + e^4 = -2 - e - e^2 - e^3 + e^4$$

## Step 3: Evaluating $\int_{0}^4e^{x}\cdot\{x\}\mathsf{dx}$

For $0 \leq x \leq 4$, the fractional part is:
- For $0 \leq x < 1$: $\{x\} = x$
- For $1 \leq x < 2$: $\{x\} = x-1$
- For $2 \leq x < 3$: $\{x\} = x-2$
- For $3 \leq x < 4$: $\{x\} = x-3$

So I split this integral into four parts:

$$\int_{0}^4e^{x}\cdot\{x\}\mathsf{dx} = \int_{0}^{1}e^{x}\cdot x\mathsf{dx} + \int_{1}^{2}e^{x}\cdot(x-1)\mathsf{dx} + \int_{2}^{3}e^{x}\cdot(x-2)\mathsf{dx} + \int_{3}^{4}e^{x}\cdot(x-3)\mathsf{dx}$$

For each interval, I compute $\int e^x(x-k)dx = e^x(x-k) - e^x$:

For $[0,1]$:
$$\int_{0}^{1}e^{x}\cdot x\mathsf{dx} = [e^x \cdot x - e^x]_{0}^{1} = e^1 \cdot 1 - e^1 - e^0 \cdot 0 + e^0 = e - e + 1 = 1$$

For $[1,2]$:
$$\int_{1}^{2}e^{x}\cdot(x-1)\mathsf{dx} = [e^x(x-1) - e^x]_{1}^{2} = e^2(2-1) - e^2 - e^1(1-1) + e^1 = e^2 - e^2 + e = e$$

For $[2,3]$:
$$\int_{2}^{3}e^{x}\cdot(x-2)\mathsf{dx} = [e^x(x-2) - e^x]_{2}^{3} = e^3(3-2) - e^3 - e^2(2-2) + e^2 = e^3 - e^3 + e^2 = e^2$$

For $[3,4]$:
$$\int_{3}^{4}e^{x}\cdot(x-3)\mathsf{dx} = [e^x(x-3) - e^x]_{3}^{4} = e^4(4-3) - e^4 - e^3(3-3) + e^3 = e^4 - e^4 + e^3 = e^3$$

Adding these results:
$$\int_{0}^4e^{x}\cdot\{x\}\mathsf{dx} = 1 + e + e^2 + e^3$$

## Step 4: Computing the final result

$$\int_{-4}^4e^{|x|}\cdot\{x\}\mathsf{dx} = \int_{-4}^0e^{-x}\cdot\{x\}\mathsf{dx} + \int_{0}^4e^{x}\cdot\{x\}\mathsf{dx}$$

$$= (-2 - e - e^2 - e^3 + e^4) + (1 + e + e^2 + e^3) = -2 + 1 + e^4 = -1 + e^4$$

Therefore, the exact value of the integral is $-1 + e^4$.

Calculating the numerical value:
$e^4 \approx 54.59815003$
$-1 + e^4 \approx 53.59815003$

Rounded to 10 decimal places: $53.5981500332$

{"answer": "-1 + e^4", "numerical_answer": "53.5981500332"}