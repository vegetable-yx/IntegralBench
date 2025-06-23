We start with the integral

  I = ∫₀^(π/2) cos(x)/(2 – cos²(x)) dx.

Step 1. Use a substitution:
  Let u = sin(x) so that du = cos(x) dx.
  When x = 0, u = 0; and when x = π/2, u = 1.

Step 2. Rewrite the integral in terms of u:
  Since cos²(x) = 1 – sin²(x) = 1 – u², we have:
  2 – cos²(x) = 2 – (1 – u²) = 1 + u².
  Thus the integral becomes:
  I = ∫₀¹ du/(1 + u²).

Step 3. Evaluate the integral:
  ∫ du/(1 + u²) = arctan(u) + C.
  Hence, I = arctan(u)|₀¹ = arctan(1) – arctan(0) = π/4 – 0 = π/4.

Step 4. Provide numerical approximation:
  π/4 ≈ 0.7853981634 (rounded to 10 decimal places).

Final Answer in required JSON format:
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}