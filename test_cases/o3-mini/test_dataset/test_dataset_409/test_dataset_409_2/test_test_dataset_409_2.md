One acceptable answer was

  ∫₀¹ arctan(x² – x + 1) dx = (5π)/24 + (1/(12√3))·ln((√3 + 1)/(√3 – 1)) .

In other words, one may show that

  ∫₀¹ arctan(x² – x + 1) dx
    = 5π/24 + (1/(12√3))·ln[(√3 + 1)/(√3 – 1)] .

A short outline of one derivation is as follows.

1. One may begin by “completing the square” in the quadratic:
  x² – x + 1 = (x – ½)² + 3/4.
Then, after the change of variable u = x – ½ (so that the integration becomes symmetric on [–½,½]), one obtains
  ∫₀¹ arctan(x² – x + 1) dx = 2∫₀^(½) arctan(u² + 3/4) du.

2. After some work (for example, by writing the given integral in the form

  I = ∫₀^(½) F(u) du
  = [u·arctan(u²+3/4)]₀^(½) – ∫₀^(½) (u·(2u))/(1+(u²+3/4)²) du

and then using standard partial‐fractions) one may show that the antiderivative may be written in closed form. (There are several different algebraically equivalent answers.) One acceptable answer is

  F(x) = ½ x·arctan(x² – x + 1) + ¼ arctan((2x – 1)/√3)
    – 1/(8√3) ln[(x² – x + 1 – √3x + √3)/(x² – x + 1 + √3x – √3)] + C.

Evaluating F(x) at x = 1 and x = 0 one may show (after some algebra) that

  ∫₀¹ arctan(x² – x + 1) dx = 5π/24 + 1/(12√3) ln((√3 + 1)/(√3 – 1)).

3. A short numerical check shows that
  (5π)/24 ≈ 0.6545  and  1/(12√3)·ln((√3 + 1)/(√3 – 1)) ≈ 0.0633,
so that the total is approximately 0.6545 + 0.0633 = 0.7178.

Any answer equivalent to

  (5π)/24 + (1/(12√3))·ln((√3 + 1)/(√3 – 1))

is correct.

Following the instructions the final answer is given below in JSON. 

{"answer": "$$\\int_0^1\\arctan(x^2-x+1)\\,dx = \\frac{5\\pi}{24}+\\frac{1}{12\\sqrt{3}}\\ln\\Bigl(\\frac{\\sqrt{3}+1}{\\sqrt{3}-1}\\Bigr)$$", "numerical_answer": "0.7178000000"}