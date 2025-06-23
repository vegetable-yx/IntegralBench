We wish to evaluate

  I = ∫₁∞ (log x)/(x²) dx.

Step 1. Use integration by parts:
  Let u = log x  ⟹ du = (1/x) dx,
  Let dv = 1/x² dx  ⟹ v = -1/x    (since ∫x^(–2)dx = -x^(–1)).

Then, by integration by parts:
  I = [u·v]₁∞ – ∫₁∞ v·du
   = [–(log x)/x]₁∞ – ∫₁∞ (–1/x)·(1/x) dx
   = [–(log x)/x]₁∞ + ∫₁∞ 1/x² dx.

Step 2. Evaluate the boundary term:
  lim (x→∞) [–(log x)/x] = 0  (since log x grows slower than x)
  At x = 1: –(log 1)/1 = 0  (because log 1 = 0)
Thus, the boundary term becomes 0 – 0 = 0.

Step 3. Evaluate the remaining integral:
  ∫₁∞ 1/x² dx = [–1/x]₁∞ = (0 – (–1)) = 1.

Thus, the original integral I = 1.

Step 4. Write the exact answer and numerical approximation:
 Exact answer: 1
 Numerical approximation (to 10 decimal places): 1.0000000000

{"answer": "1", "numerical_answer": "1.0000000000"}