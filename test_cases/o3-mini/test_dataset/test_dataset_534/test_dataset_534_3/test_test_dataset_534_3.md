We start by writing the integral in a standard Gaussian form. The given integral is

  I = ∫₋∞^∞ exp[ -(x - 2024)²/4 ] dx.

Step 1: Make a substitution to center the variable.
Let u = x - 2024. Then, du = dx and the limits remain u → -∞ to u → ∞. The integral becomes

  I = ∫₋∞^∞ exp(-u²/4) du.

Step 2: Recognize the standard Gaussian integral.
The standard Gaussian integral is given by

  ∫₋∞^∞ exp(-u²/(2σ²)) du = √(2πσ²).

To match our integrand with the standard form, write
  exp(-u²/4) = exp(-u²/(2·2)).
Thus, σ² = 2 and σ = √2.

Step 3: Substitute σ into the standard Gaussian result.
Thus, the integral becomes
  I = √(2π(2)) = √(4π) = 2√π.

Step 4: Provide a numerical approximation.
Numerically, π ≈ 3.1415926536 so that
  2√π ≈ 2 × 1.7724538509 = 3.5449077018.

The final answer in JSON format is:
{"answer": "2\\sqrt{\\pi}", "numerical_answer": "3.5449077018"}