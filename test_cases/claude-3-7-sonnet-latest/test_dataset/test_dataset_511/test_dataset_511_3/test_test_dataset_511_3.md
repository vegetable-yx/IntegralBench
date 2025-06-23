# Evaluating $\int_0^8\frac{\cos\sqrt{x}}{\sqrt{x}}dx$

## Step 1: Make a substitution to simplify the integral

Let $u = \sqrt{x}$, then $x = u^2$ and $dx = 2u \, du$.

Also, when $x = 0$, $u = 0$; and when $x = 8$, $u = 2\sqrt{2}$.

Substituting into the integral:
$$\int_0^8\frac{\cos\sqrt{x}}{\sqrt{x}}dx = \int_0^{2\sqrt{2}}\frac{\cos u}{u} \cdot 2u \, du = 2\int_0^{2\sqrt{2}} \cos u \, du$$

## Step 2: Evaluate the resulting integral

We know that $\int \cos u \, du = \sin u + C$, so:
$$2\int_0^{2\sqrt{2}} \cos u \, du = 2[\sin u]_0^{2\sqrt{2}} = 2(\sin(2\sqrt{2}) - \sin(0))$$

Since $\sin(0) = 0$, we have:
$$2\int_0^{2\sqrt{2}} \cos u \, du = 2\sin(2\sqrt{2})$$

## Step 3: Express the final answer

The exact answer is $2\sin(2\sqrt{2})$.

## Step 4: Calculate the numerical approximation

$2\sin(2\sqrt{2}) \approx 2 \times 0.9926671908 \approx 1.9853343815$

Therefore:

{"answer": "2\\sin(2\\sqrt{2})", "numerical_answer": "1.9853343815"}