We wish to evaluate

  I = ∫₋∞∞ e^(–2x² – 5x – 3) dx.

Step 1. Write the exponent in a form suitable for completing the square. Write

  –2x² – 5x – 3 = –2(x² + (5/2)x) – 3.

Step 2. Complete the square in x. Notice that

  x² + (5/2)x = (x + 5/4)² – (5/4)² = (x + 5/4)² – 25/16.

Thus, substituting back we have

  –2(x² + (5/2)x) – 3 = –2[(x + 5/4)² – 25/16] – 3
             = –2(x + 5/4)² + (2·25/16) – 3
             = –2(x + 5/4)² + (25/8) – 3.

Since 3 = 24/8, we combine the constants:

  (25/8) – 3 = (25/8) – (24/8) = 1/8.

Thus, the exponent becomes

  –2(x + 5/4)² + 1/8.

Step 3. Factor the constant term from the integral:

  I = ∫₋∞∞ e^(–2(x + 5/4)² + 1/8) dx 
     = e^(1/8) ∫₋∞∞ e^(–2(x + 5/4)²) dx.

Step 4. Change variables by letting u = x + 5/4, so that du = dx. The limits remain –∞ to ∞, and the integral becomes

  I = e^(1/8) ∫₋∞∞ e^(–2u²) du.

Step 5. Use the standard Gaussian integral

  ∫₋∞∞ e^(–a u²) du = √(π/a), for a > 0.

Here, a = 2 so that

  ∫₋∞∞ e^(–2u²) du = √(π/2).

Thus, the evaluated integral is

  I = e^(1/8) √(π/2).

Step 6. Write the exact answer and provide a numerical approximation. The exact answer is

  √(π/2) e^(1/8).

Now, we approximate:
  √(π/2) ≈ 1.2533141373     (using π ≈ 3.1415926536)
  e^(1/8) = e^(0.125) ≈ 1.1331484531.
Multiplying these we get
  I ≈ 1.2533141373 × 1.1331484531 ≈ 1.4201890000.

Thus, the final answers are:

Exact answer: √(π/2)e^(1/8)
Numerical answer (rounded to 10 decimal places): 1.4201890000

{"answer": "\\sqrt{\\frac{\\pi}{2}} e^{\\frac{1}{8}}", "numerical_answer": "1.4201890000"}