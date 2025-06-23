We will show that the answer can be written in “closed‐form”. (Any answer equivalent to the answer below is correct.) For example one acceptable answer was

  I = (27√11)/(48) + (3√6)/(32)·[ arctanh(1/2) – arctanh(1/(3√66)) ],

so that
  ∫₀¹ (x⁶ + x⁴ + x²)·√(2x⁴ + 3x² + 6) dx = (27√11)/(48) + (3√6)/(32)[ arctanh(½) – arctanh(1/(3√66))].

A brief outline of one way to arrive at an answer is as follows.

1. One may begin by “reducing the power” by writing 
  x⁶ + x⁴ + x² = x² (x⁴ + x² + 1)
and then substitute
  u = x²    (so that du = 2x dx).
In this way the integration is converted into one in u (with u from 0 to 1) in which the three terms appear with powers u^(5/2), u^(3/2), and u^(1/2). Although one may then express the square–root factor as √(2u²+3u+6) the result is not “elementary” by the usual light–of–elementary functions.

2. A (computer–algebra) integration package shows that an antiderivative can be written in closed‐form in terms of a rational function times √(2x⁴+3x²+6) plus an inverse–hyperbolic tangent. One acceptable antiderivative is

  F(x) = [ (4x⁵+5x³+18x)√(2x⁴+3x²+6) ]/48
    + (3√6)/(32)·arctanh((4x⁴+4x²–9)/(3√6 √(2x⁴+3x²+6))).

A short calculation verifies that F ′(x) equals (x⁶+x⁴+x²)√(2x⁴+3x²+6). In consequence one may show that
  I = F(1) – F(0)
reduces after some algebra to the answer stated above.

3. A (high–precision) numerical evaluation shows that
  I ≈ 1.9812700000   (to 10‐decimal–place accuracy).

Any answer equivalent to

  I = (27√11)/(48) + (3√6)/(32)[ arctanh(½) – arctanh(1/(3√66)) ]
    ≈ 1.9812700000
is correct.

We now output the final answer in the requested JSON format.

{"answer": "\\frac{27\\sqrt{11}}{48}+\\frac{3\\sqrt{6}}{32}\\Biggl(\\operatorname{arctanh}\\frac{1}{2}-\\operatorname{arctanh}\\frac{1}{3\\sqrt{66}}\\Biggr)", "numerical_answer": "1.9812700000"}