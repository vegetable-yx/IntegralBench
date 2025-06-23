We start with the integral

  I = ∫₁^(∞) (log x)/(x²) dx.

Step 1. Use integration by parts:
  Let u = log x → du = (1/x) dx,
  and dv = (1/x²) dx → v = ∫ (1/x²) dx = -1/x.
Thus, integration by parts gives:
  I = [u v]₁^(∞) - ∫₁^(∞) v du
   = [(log x)(-1/x)]₁^(∞) - ∫₁^(∞)(-1/x)(1/x) dx.

Step 2. Evaluate the boundary term:
  At x → ∞, note that log x grows unboundedly but 1/x tends to 0, so (log x)/x → 0. Thus, the term at ∞ is 0.
  At x = 1, log 1 = 0, so the term is 0.
Therefore, [u v]₁^(∞) = 0 - 0 = 0.

Step 3. The remaining integral becomes:
  I = 0 - ( -∫₁^(∞) (1/x²) dx) = ∫₁^(∞) (1/x²) dx.
Now compute ∫₁^(∞) (1/x²) dx:
  ∫₁^(∞) (1/x²) dx = lim₍b→∞₎ [ -1/x ]₁^b = ( -0 ) - ( -1 ) = 1.

Thus, the exact answer is 1.

Step 4. Numerical Approximation:
  The numerical value is 1.0000000000 when rounded to 10 decimal places.

The final answer in the required JSON format is:
{"answer": "1", "numerical_answer": "1.0000000000"}