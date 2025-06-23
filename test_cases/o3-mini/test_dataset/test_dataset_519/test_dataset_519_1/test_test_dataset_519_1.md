We start with the integral
  I = ∫₀^(π/2) (cos(x))/(2 - cos²(x)) dx.
Step 1. Use the substitution u = sin(x), so that du = cos(x) dx.
Step 2. Rewrite cos²(x) in terms of u:
  cos²(x) = 1 - sin²(x) = 1 - u².
Then the denominator becomes:
  2 - cos²(x) = 2 - (1 - u²) = 1 + u².
Step 3. Change the limits of integration:
  When x = 0, u = sin(0) = 0;
  When x = π/2, u = sin(π/2) = 1.
Step 4. The integral simplifies to:
  I = ∫₀¹ du/(1 + u²).
Step 5. Recognize that ∫ du/(1+u²) is the standard integral whose antiderivative is arctan(u).
Thus, we have:
  I = arctan(u)|₀¹ = arctan(1) − arctan(0) = (π/4) - 0 = π/4.
Step 6. Numerical approximation:
  π/4 ≈ 0.7853981634.

{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}