# Evaluating $\int_1^{2011}\frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}}\:dx$

## Step 1: Simplify the integrand

Let's start by rationalizing the denominator:

$$\frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}} \cdot \frac{\sqrt{2012-x}-\sqrt{x}}{\sqrt{2012-x}-\sqrt{x}} = \frac{\sqrt{x}(\sqrt{2012-x}-\sqrt{x})}{(\sqrt{2012-x})^2-(\sqrt{x})^2}$$

$$= \frac{\sqrt{x}(\sqrt{2012-x}-\sqrt{x})}{2012-x-x} = \frac{\sqrt{x}(\sqrt{2012-x}-\sqrt{x})}{2012-2x}$$

This gives us:

$$\frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}} = \frac{\sqrt{x}\sqrt{2012-x}}{2012-2x} - \frac{x}{2012-2x}$$

## Step 2: Evaluate the integral

Now we need to compute:

$$\int_1^{2011}\frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}}\:dx = \int_1^{2011}\left(\frac{\sqrt{x}\sqrt{2012-x}}{2012-2x} - \frac{x}{2012-2x}\right)dx$$

Let's substitute $u = 2012-x$, which gives $dx = -du$ and when $x = 1$, $u = 2011$; when $x = 2011$, $u = 1$. Also, $x = 2012-u$.

$$\int_1^{2011}\frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}}\:dx = \int_{2011}^{1}\left(\frac{\sqrt{2012-u}\sqrt{u}}{2012-2(2012-u)} - \frac{2012-u}{2012-2(2012-u)}\right)(-du)$$

$$= \int_{2011}^{1}\left(\frac{\sqrt{2012-u}\sqrt{u}}{2u-2012} - \frac{2012-u}{2u-2012}\right)(-du)$$

$$= \int_{2011}^{1}\left(\frac{\sqrt{(2012-u)u}}{2(u-1006)} - \frac{2012-u}{2(u-1006)}\right)(-du)$$

$$= \int_{1}^{2011}\left(\frac{\sqrt{(2012-u)u}}{2(u-1006)} - \frac{2012-u}{2(u-1006)}\right)du$$

By symmetry of the integral and the fact that we're integrating over the same bounds after substitution, we have:

$$\int_{1}^{2011}\frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}}\:dx = \int_{1}^{2011}\frac{\sqrt{2012-x}}{\sqrt{2012-x}+\sqrt{x}}\:dx$$

Now, let's note that:
$$\frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}} + \frac{\sqrt{2012-x}}{\sqrt{2012-x}+\sqrt{x}} = \frac{\sqrt{x}+\sqrt{2012-x}}{\sqrt{2012-x}+\sqrt{x}} = 1$$

Therefore:
$$\int_{1}^{2011}\frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}}\:dx + \int_{1}^{2011}\frac{\sqrt{2012-x}}{\sqrt{2012-x}+\sqrt{x}}\:dx = \int_{1}^{2011}1\:dx = 2011-1 = 2010$$

Since we established that these two integrals are equal, we have:
$$2 \cdot \int_{1}^{2011}\frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}}\:dx = 2010$$

Therefore:
$$\int_{1}^{2011}\frac{\sqrt{x}}{\sqrt{2012-x}+\sqrt{x}}\:dx = \frac{2010}{2} = 1005$$

## Step 3: Numerical approximation

The exact value is 1005, so the numerical approximation rounded to 10 decimal places is 1005.0000000000.

## Final Answer

{"answer": "1005", "numerical_answer": "1005.0000000000"}