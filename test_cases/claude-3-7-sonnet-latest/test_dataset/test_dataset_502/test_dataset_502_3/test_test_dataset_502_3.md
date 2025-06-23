# Evaluating $\large\int_{64}^{729}\frac{x^{1/2}}{x^{1/2}-x^{1/3}}dx$

## Step 1: Simplify the integrand

Let's start by factoring out $x^{1/3}$ from the denominator:

$$\frac{x^{1/2}}{x^{1/2}-x^{1/3}} = \frac{x^{1/2}}{x^{1/3}(x^{1/6}-1)} = \frac{x^{1/6}}{x^{1/6}-1}$$

## Step 2: Substitute $u = x^{1/6}$

Let $u = x^{1/6}$, which means $x = u^6$ and $dx = 6u^5 du$

The new limits become:
- Lower limit: $u = (64)^{1/6} = 2$
- Upper limit: $u = (729)^{1/6} = 3$

Substituting into our integral:

$$\int_{64}^{729}\frac{x^{1/2}}{x^{1/2}-x^{1/3}}dx = \int_{2}^{3}\frac{u}{u-1} \cdot 6u^5 du = 6\int_{2}^{3}\frac{u^6}{u-1}du$$

## Step 3: Apply polynomial division

We can write:
$$\frac{u^6}{u-1} = u^5 + u^4 + u^3 + u^2 + u + 1 + \frac{1}{u-1}$$

This gives us:
$$6\int_{2}^{3}\frac{u^6}{u-1}du = 6\int_{2}^{3}(u^5 + u^4 + u^3 + u^2 + u + 1 + \frac{1}{u-1})du$$

## Step 4: Integrate each term

$$6\int_{2}^{3}(u^5 + u^4 + u^3 + u^2 + u + 1 + \frac{1}{u-1})du$$

$$= 6\left[\frac{u^6}{6} + \frac{u^5}{5} + \frac{u^4}{4} + \frac{u^3}{3} + \frac{u^2}{2} + u + \ln|u-1|\right]_{2}^{3}$$

## Step 5: Evaluate at the limits

$$= 6\left[\frac{3^6}{6} + \frac{3^5}{5} + \frac{3^4}{4} + \frac{3^3}{3} + \frac{3^2}{2} + 3 + \ln|3-1| - \left(\frac{2^6}{6} + \frac{2^5}{5} + \frac{2^4}{4} + \frac{2^3}{3} + \frac{2^2}{2} + 2 + \ln|2-1|\right)\right]$$

$$= 6\left[\frac{729}{6} + \frac{243}{5} + \frac{81}{4} + \frac{27}{3} + \frac{9}{2} + 3 + \ln(2) - \left(\frac{64}{6} + \frac{32}{5} + \frac{16}{4} + \frac{8}{3} + \frac{4}{2} + 2 + \ln(1)\right)\right]$$

Note that $\ln(1) = 0$

$$= 6\left[\frac{729}{6} + \frac{243}{5} + \frac{81}{4} + \frac{27}{3} + \frac{9}{2} + 3 + \ln(2) - \frac{64}{6} - \frac{32}{5} - \frac{16}{4} - \frac{8}{3} - \frac{4}{2} - 2\right]$$

## Step 6: Simplify

Let's calculate each term:
$$6 \cdot \frac{729}{6} = 729$$
$$6 \cdot \frac{243}{5} = \frac{1458}{5}$$
$$6 \cdot \frac{81}{4} = \frac{486}{4} = 121.5$$
$$6 \cdot \frac{27}{3} = 54$$
$$6 \cdot \frac{9}{2} = 27$$
$$6 \cdot 3 = 18$$
$$6 \cdot \ln(2) = 6\ln(2)$$
$$-6 \cdot \frac{64}{6} = -64$$
$$-6 \cdot \frac{32}{5} = -\frac{192}{5}$$
$$-6 \cdot \frac{16}{4} = -24$$
$$-6 \cdot \frac{8}{3} = -16$$
$$-6 \cdot \frac{4}{2} = -12$$
$$-6 \cdot 2 = -12$$

Adding these terms:
$$729 + \frac{1458}{5} + 121.5 + 54 + 27 + 18 + 6\ln(2) - 64 - \frac{192}{5} - 24 - 16 - 12 - 12$$

$$= 729 + \frac{1458-192}{5} + 121.5 + 54 + 27 + 18 - 64 - 24 - 16 - 12 - 12 + 6\ln(2)$$

$$= 729 + \frac{1266}{5} + 121.5 + 54 + 27 + 18 - 64 - 24 - 16 - 12 - 12 + 6\ln(2)$$

$$= 729 + 253.2 + 121.5 + 54 + 27 + 18 - 64 - 24 - 16 - 12 - 12 + 6\ln(2)$$

$$= 821.7 + 6\ln(2)$$

The exact result is:
$$\int_{64}^{729}\frac{x^{1/2}}{x^{1/2}-x^{1/3}}dx = 821.7 + 6\ln(2)$$

## Step 7: Numerical approximation

Computing $6\ln(2) \approx 6 \times 0.6931471806 \approx 4.1588830836$

Therefore:
$$821.7 + 6\ln(2) \approx 821.7 + 4.1588830836 \approx 825.8588830836$$

Rounded to 10 decimal places: $825.8588830836$

{"answer": "821.7 + 6\\ln(2)", "numerical_answer": "825.8588830836"}