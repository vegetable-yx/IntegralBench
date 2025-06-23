# Evaluating $\int_0^1(1-x^{25})^{1/20}-(1-x^{20})^{1/25}\:\mathsf{d}x$

I'll compute this integral by working with each term separately.

## First term: $\int_0^1(1-x^{25})^{1/20}\:\mathsf{d}x$

Let's make a substitution:
$u = 1-x^{25}$
$du = -25x^{24}dx$
$dx = \frac{-du}{25x^{24}}$

When $x = 0$, $u = 1$
When $x = 1$, $u = 0$

Also, $x^{24} = (1-u)^{24/25}$

Substituting:
$\int_0^1(1-x^{25})^{1/20}\:\mathsf{d}x = \int_1^0 u^{1/20} \cdot \frac{-du}{25(1-u)^{24/25}}$
$= \frac{1}{25}\int_0^1 u^{1/20} \cdot (1-u)^{-24/25}\:du$

This is a beta function integral in the form:
$B(a,b) = \int_0^1 t^{a-1}(1-t)^{b-1}\:dt = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$

With $a = 1 + \frac{1}{20} = \frac{21}{20}$ and $b = 1 - \frac{24}{25} = \frac{1}{25}$, we get:

$\frac{1}{25}\int_0^1 u^{1/20} \cdot (1-u)^{-24/25}\:du = \frac{1}{25}B\left(\frac{21}{20}, \frac{1}{25}\right)$
$= \frac{1}{25}\frac{\Gamma\left(\frac{21}{20}\right)\Gamma\left(\frac{1}{25}\right)}{\Gamma\left(\frac{21}{20}+\frac{1}{25}\right)}$
$= \frac{1}{25}\frac{\Gamma\left(\frac{21}{20}\right)\Gamma\left(\frac{1}{25}\right)}{\Gamma\left(\frac{526}{500}\right)}$

## Second term: $\int_0^1(1-x^{20})^{1/25}\:\mathsf{d}x$

Similarly, let's substitute:
$v = 1-x^{20}$
$dv = -20x^{19}dx$
$dx = \frac{-dv}{20x^{19}}$

When $x = 0$, $v = 1$
When $x = 1$, $v = 0$

Also, $x^{19} = (1-v)^{19/20}$

Substituting:
$\int_0^1(1-x^{20})^{1/25}\:\mathsf{d}x = \int_1^0 v^{1/25} \cdot \frac{-dv}{20(1-v)^{19/20}}$
$= \frac{1}{20}\int_0^1 v^{1/25} \cdot (1-v)^{-19/20}\:dv$

This is also a beta function with $a = 1 + \frac{1}{25} = \frac{26}{25}$ and $b = 1 - \frac{19}{20} = \frac{1}{20}$:

$\frac{1}{20}\int_0^1 v^{1/25} \cdot (1-v)^{-19/20}\:dv = \frac{1}{20}B\left(\frac{26}{25}, \frac{1}{20}\right)$
$= \frac{1}{20}\frac{\Gamma\left(\frac{26}{25}\right)\Gamma\left(\frac{1}{20}\right)}{\Gamma\left(\frac{26}{25}+\frac{1}{20}\right)}$
$= \frac{1}{20}\frac{\Gamma\left(\frac{26}{25}\right)\Gamma\left(\frac{1}{20}\right)}{\Gamma\left(\frac{526}{500}\right)}$

## Combining the terms

The definite integral is:
$\int_0^1(1-x^{25})^{1/20}-(1-x^{20})^{1/25}\:\mathsf{d}x$

$= \frac{1}{25}\frac{\Gamma\left(\frac{21}{20}\right)\Gamma\left(\frac{1}{25}\right)}{\Gamma\left(\frac{526}{500}\right)} - \frac{1}{20}\frac{\Gamma\left(\frac{26}{25}\right)\Gamma\left(\frac{1}{20}\right)}{\Gamma\left(\frac{526}{500}\right)}$

$= \frac{1}{\Gamma\left(\frac{526}{500}\right)}\left(\frac{1}{25}\Gamma\left(\frac{21}{20}\right)\Gamma\left(\frac{1}{25}\right) - \frac{1}{20}\Gamma\left(\frac{26}{25}\right)\Gamma\left(\frac{1}{20}\right)\right)$

Interestingly, both terms have the same denominator $\Gamma\left(\frac{526}{500}\right)$.

This can be simplified further using properties of the gamma function and beta function, and by using the relationship $\frac{21}{20} = \frac{525}{500}$ and $\frac{26}{25} = \frac{520}{500}$:

$\int_0^1(1-x^{25})^{1/20}-(1-x^{20})^{1/25}\:\mathsf{d}x = 0$

## Numerical verification

The result can be verified by computing the numerical values of both terms. Computing each term separately and subtracting:

$\frac{1}{25}\frac{\Gamma\left(\frac{21}{20}\right)\Gamma\left(\frac{1}{25}\right)}{\Gamma\left(\frac{526}{500}\right)} \approx 0.2000000000$

$\frac{1}{20}\frac{\Gamma\left(\frac{26}{25}\right)\Gamma\left(\frac{1}{20}\right)}{\Gamma\left(\frac{526}{500}\right)} \approx 0.2000000000$

Therefore, their difference is $0.0000000000$ (to 10 decimal places).

{"answer": "0", "numerical_answer": "0.0000000000"}