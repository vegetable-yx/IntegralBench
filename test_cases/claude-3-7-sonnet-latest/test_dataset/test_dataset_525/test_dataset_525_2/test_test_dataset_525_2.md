# Evaluating $\int_{1/\sqrt{2}}^1\frac{\arcsin(x)}{x^3}\:dx$

## Step 1: Set up a substitution

Let's use $u = \arcsin(x)$ to simplify this integral.

When $u = \arcsin(x)$, we have:
- $x = \sin(u)$
- $dx = \cos(u) \, du$

Also, the bounds change:
- When $x = 1/\sqrt{2}$, $u = \arcsin(1/\sqrt{2}) = \pi/4$
- When $x = 1$, $u = \arcsin(1) = \pi/2$

## Step 2: Rewrite the integral with the substitution

$\int_{1/\sqrt{2}}^1\frac{\arcsin(x)}{x^3}\:dx = \int_{\pi/4}^{\pi/2}\frac{u}{\sin^3(u)}\cos(u)\:du = \int_{\pi/4}^{\pi/2}\frac{u\cos(u)}{\sin^3(u)}\:du$

## Step 3: Use the identity $\cos(u) = \frac{d}{du}(\sin(u))$

Let's set $v = \sin(u)$, so $dv = \cos(u) \, du$.

This gives us:
$\int_{\pi/4}^{\pi/2}\frac{u\cos(u)}{\sin^3(u)}\:du = \int_{\pi/4}^{\pi/2}\frac{u}{v^3}\:dv$

## Step 4: Use integration by parts

Let's try a different approach. Let's integrate by parts directly.

Let's set:
- $f(x) = \arcsin(x)$
- $g'(x) = \frac{1}{x^3}$

Then:
- $f'(x) = \frac{1}{\sqrt{1-x^2}}$
- $g(x) = -\frac{1}{2x^2}$

Using the integration by parts formula $\int f(x)g'(x)dx = f(x)g(x) - \int f'(x)g(x)dx$:

$$\int\frac{\arcsin(x)}{x^3}\:dx = -\frac{\arcsin(x)}{2x^2} - \int -\frac{1}{2x^2} \cdot \frac{1}{\sqrt{1-x^2}}\:dx$$

$$= -\frac{\arcsin(x)}{2x^2} + \frac{1}{2}\int \frac{1}{x^2\sqrt{1-x^2}}\:dx$$

## Step 5: Evaluate the remaining integral

Let's substitute $t = 1-x^2$, which gives $dt = -2x\,dx$ or $dx = -\frac{dt}{2x}$:

$$\frac{1}{2}\int \frac{1}{x^2\sqrt{1-x^2}}\:dx = \frac{1}{2}\int \frac{1}{x^2\sqrt{t}} \cdot \left(-\frac{dt}{2x}\right)$$

$$= -\frac{1}{4}\int \frac{1}{x^3\sqrt{t}}\:dt$$

But $x^2 = 1-t$, so $x^3 = x \cdot x^2 = x(1-t)$

Since we need $\frac{1}{x^3}$, this gets complicated.

Let's try a different substitution. Let's use $x = \sin(u)$ as initially planned:

$$\int\frac{\arcsin(x)}{x^3}\:dx = \int\frac{u}{\sin^3(u)}\cos(u)\:du$$

We can use the identity $\csc(u) = \frac{1}{\sin(u)}$:

$$\int\frac{u}{\sin^3(u)}\cos(u)\:du = \int u\csc^3(u)\cos(u)\:du$$

This can be written as:

$$\int u\csc^3(u)\cos(u)\:du = \int u\csc^2(u)\csc(u)\cos(u)\:du = \int u\csc^2(u)\cot(u)\csc(u)\:du$$

But $\cot(u)\csc(u) = \frac{\cos(u)}{\sin^2(u)}$, so:

$$\int u\csc^2(u)\cot(u)\csc(u)\:du = \int u\csc^2(u)\frac{\cos(u)}{\sin^2(u)}\:du = \int \frac{u\cos(u)}{\sin^4(u)}\:du$$

## Step 6: Let's restart with a more direct approach

Let's use integration by parts with:
- $f(x) = \arcsin(x)$
- $g'(x) = \frac{1}{x^3}$

So:
- $f'(x) = \frac{1}{\sqrt{1-x^2}}$
- $g(x) = -\frac{1}{2x^2}$

$$\int\frac{\arcsin(x)}{x^3}\:dx = \arcsin(x) \cdot \left(-\frac{1}{2x^2}\right) - \int \frac{1}{\sqrt{1-x^2}} \cdot \left(-\frac{1}{2x^2}\right)\:dx$$

$$= -\frac{\arcsin(x)}{2x^2} + \frac{1}{2}\int \frac{1}{x^2\sqrt{1-x^2}}\:dx$$

For the remaining integral, let's use the substitution $x = \frac{1}{\sqrt{1+t^2}}$:
- This gives $dx = -\frac{t}{(1+t^2)^{3/2}}\:dt$
- When $x = \frac{1}{\sqrt{1+t^2}}$, we have $1-x^2 = 1-\frac{1}{1+t^2} = \frac{t^2}{1+t^2}$
- And $\sqrt{1-x^2} = \frac{t}{\sqrt{1+t^2}}$
- Also, $x^2 = \frac{1}{1+t^2}$

Substituting:

$$\frac{1}{2}\int \frac{1}{x^2\sqrt{1-x^2}}\:dx = \frac{1}{2}\int \frac{1}{\frac{1}{1+t^2} \cdot \frac{t}{\sqrt{1+t^2}}} \cdot \left(-\frac{t}{(1+t^2)^{3/2}}\right)\:dt$$

$$= -\frac{1}{2}\int \frac{(1+t^2) \cdot \sqrt{1+t^2}}{t \cdot t} \cdot \frac{t}{(1+t^2)^{3/2}}\:dt$$

$$= -\frac{1}{2}\int \frac{1}{t}\:dt = -\frac{1}{2}\ln|t| + C$$

Now, to express in terms of $x$: when $x = \frac{1}{\sqrt{1+t^2}}$, we have $t^2 = \frac{1-x^2}{x^2}$, so $t = \frac{\sqrt{1-x^2}}{x}$

Therefore:

$$-\frac{1}{2}\ln|t| + C = -\frac{1}{2}\ln\left|\frac{\sqrt{1-x^2}}{x}\right| + C = -\frac{1}{2}\ln\frac{\sqrt{1-x^2}}{|x|} + C$$

Since our domain is $(0,1]$, we have $|x| = x$:

$$-\frac{1}{2}\ln\frac{\sqrt{1-x^2}}{x} + C = -\frac{1}{2}\ln\frac{\sqrt{1-x^2}}{x} + C$$

So the full integral is:

$$\int\frac{\arcsin(x)}{x^3}\:dx = -\frac{\arcsin(x)}{2x^2} - \frac{1}{2}\ln\frac{\sqrt{1-x^2}}{x} + C$$

## Step 7: Apply the bounds

Evaluating at the upper bound $x = 1$:
- $\arcsin(1) = \frac{\pi}{2}$
- $\sqrt{1-1^2} = 0$, so $\ln\frac{\sqrt{1-x^2}}{x}$ is undefined at $x = 1$

Let's take the limit as $x \rightarrow 1$:
$\lim_{x \rightarrow 1} -\frac{\arcsin(x)}{2x^2} - \frac{1}{2}\ln\frac{\sqrt{1-x^2}}{x}$

For $\ln\frac{\sqrt{1-x^2}}{x}$, as $x \rightarrow 1$, $\sqrt{1-x^2} \rightarrow 0$, so $\ln\frac{\sqrt{1-x^2}}{x} \rightarrow -\infty$

This suggests the integral might diverge. Let's reconsider our approach.

## Alternative approach:

Let's use the substitution $u = \arcsin(x)$, which gives $x = \sin(u)$ and $dx = \cos(u) \, du$.

The integral becomes:
$$\int\frac{\arcsin(x)}{x^3}\:dx = \int\frac{u}{\sin^3(u)}\cos(u)\:du$$

Now let's try a different approach using integration by parts:
Let $v = u$ and $dw = \frac{\cos(u)}{\sin^3(u)}\:du$

Then $dv = du$ and we need to find $w$ by integrating $\frac{\cos(u)}{\sin^3(u)}$:
$$w = \int\frac{\cos(u)}{\sin^3(u)}\:du$$

Using the substitution $t = \sin(u)$, we get $dt = \cos(u)\:du$:
$$w = \int\frac{1}{t^3}\:dt = -\frac{1}{2t^2} + C$$

So $w = -\frac{1}{2\sin^2(u)} + C$

Now applying integration by parts:
$$\int u \cdot \frac{\cos(u)}{\sin^3(u)}\:du = u \cdot \left(-\frac{1}{2\sin^2(u)}\right) - \int 1 \cdot \left(-\frac{1}{2\sin^2(u)}\right)\:du$$

$$= -\frac{u}{2\sin^2(u)} + \frac{1}{2}\int\csc^2(u)\:du$$

$$= -\frac{u}{2\sin^2(u)} + \frac{1}{2}\cot(u) + C$$

Substituting back $u = \arcsin(x)$ and $\sin(u) = x$:
$$\int\frac{\arcsin(x)}{x^3}\:dx = -\frac{\arcsin(x)}{2x^2} + \frac{1}{2}\cot(\arcsin(x)) + C$$

Since $\cot(\arc