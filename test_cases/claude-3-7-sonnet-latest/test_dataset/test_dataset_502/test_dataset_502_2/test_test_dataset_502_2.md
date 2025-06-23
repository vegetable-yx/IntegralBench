# Calculating $\large\int_{64}^{729}\frac{x^{1/2}}{x^{1/2}-x^{1/3}}dx$

## Step 1: Simplify the integrand

I'll start by simplifying the expression inside the integral:

$$\frac{x^{1/2}}{x^{1/2}-x^{1/3}}$$

Let me try a substitution to make this more manageable. Let's set $u = x^{1/6}$, which means:
- $x = u^6$
- $dx = 6u^5 du$
- When $x = 64 = 2^6$, $u = 2$
- When $x = 729 = 3^6$, $u = 3$

With this substitution:
- $x^{1/2} = (u^6)^{1/2} = u^3$
- $x^{1/3} = (u^6)^{1/3} = u^2$

Now the integrand becomes:
$$\frac{u^3}{u^3-u^2} \cdot 6u^5 du = \frac{6u^8}{u^2(u-1)} du = \frac{6u^6}{u-1} du$$

## Step 2: Apply partial fractions decomposition

Let's decompose $\frac{6u^6}{u-1}$ into simpler terms.

$$\frac{6u^6}{u-1} = 6u^5 + 6u^4 + 6u^3 + 6u^2 + 6u + \frac{6}{u-1}$$

To verify this, I'll multiply both sides by $(u-1)$:
$$6u^6 = (u-1)(6u^5 + 6u^4 + 6u^3 + 6u^2 + 6u) + 6$$
$$6u^6 = 6u^6 - 6u^5 + 6u^5 - 6u^4 + 6u^4 - 6u^3 + 6u^3 - 6u^2 + 6u^2 - 6u + 6$$
$$6u^6 = 6u^6 + 6$$

This confirms our decomposition is correct.

## Step 3: Integrate each term

$$\int\frac{6u^6}{u-1}du = \int(6u^5 + 6u^4 + 6u^3 + 6u^2 + 6u + \frac{6}{u-1})du$$

Integrating term by term:
$$\int 6u^5 du = u^6$$
$$\int 6u^4 du = \frac{6u^5}{5}$$
$$\int 6u^3 du = \frac{6u^4}{4} = \frac{3u^4}{2}$$
$$\int 6u^2 du = 2u^3$$
$$\int 6u du = 3u^2$$
$$\int \frac{6}{u-1} du = 6\ln|u-1|$$

Combining all terms:
$$\int\frac{6u^6}{u-1}du = u^6 + \frac{6u^5}{5} + \frac{3u^4}{2} + 2u^3 + 3u^2 + 6\ln|u-1| + C$$

## Step 4: Apply the bounds

Now I'll evaluate this expression at the bounds $u = 3$ and $u = 2$:

For $u = 3$:
$$3^6 + \frac{6(3^5)}{5} + \frac{3(3^4)}{2} + 2(3^3) + 3(3^2) + 6\ln|3-1|$$
$$= 729 + \frac{6(243)}{5} + \frac{3(81)}{2} + 2(27) + 3(9) + 6\ln(2)$$
$$= 729 + \frac{1458}{5} + \frac{243}{2} + 54 + 27 + 6\ln(2)$$
$$= 729 + 291.6 + 121.5 + 54 + 27 + 6\ln(2)$$
$$= 1223.1 + 6\ln(2)$$

For $u = 2$:
$$2^6 + \frac{6(2^5)}{5} + \frac{3(2^4)}{2} + 2(2^3) + 3(2^2) + 6\ln|2-1|$$
$$= 64 + \frac{6(32)}{5} + \frac{3(16)}{2} + 2(8) + 3(4) + 6\ln(1)$$
$$= 64 + \frac{192}{5} + \frac{48}{2} + 16 + 12 + 0$$
$$= 64 + 38.4 + 24 + 16 + 12$$
$$= 154.4$$

The definite integral is:
$$(1223.1 + 6\ln(2)) - 154.4 = 1068.7 + 6\ln(2)$$

## Step 5: Express in exact form

The exact answer is:
$$1068.7 + 6\ln(2) = \frac{10687}{10} + 6\ln(2)$$

## Step 6: Calculate numerical approximation

$$6\ln(2) \approx 6 \times 0.6931471806 \approx 4.1588830836$$

Therefore:
$$\frac{10687}{10} + 6\ln(2) \approx 1068.7 + 4.1588830836 \approx 1072.8588830836$$

Rounded to 10 decimal places: 1072.8588830836

{"answer": "\\frac{10687}{10} + 6\\ln(2)", "numerical_answer": "1072.8588830836"}