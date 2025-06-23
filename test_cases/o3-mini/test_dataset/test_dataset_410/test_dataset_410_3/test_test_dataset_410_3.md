We wish to evaluate

  I = ∫₀^(∞) e^(–x²) cos(2x) dx.

Step 1. Recognize that the integrand e^(–x²) cos(2x) is an even function. Hence, the integral from 0 to ∞ is half the integral from –∞ to ∞:

  I = ½ ∫₋∞^(∞) e^(–x²) cos(2x) dx.

Step 2. Recall that the well-known formula for the Fourier cosine transform of the Gaussian is

  ∫₋∞^(∞) e^(–x²) e^(i2x) dx = √π e^(–(2)²/4) = √π e^(–1).

Since the cosine is the real part of the complex exponential and the integrand is even, we have

  ∫₋∞^(∞) e^(–x²) cos(2x) dx = √π e^(–1).

Step 3. Therefore, substituting back we find

  I = ½ √π e^(–1).

Step 4. The exact answer is thus

  I = (√π/2) e^(–1).

Step 5. To find a numerical approximation, first note:
  √π ≈ 1.7724538509  and  e^(–1) ≈ 0.3678794412.
Then,
  I ≈ (1.7724538509/2) × 0.3678794412 ≈ 0.8862269255 × 0.3678794412 ≈ 0.3260246644.

Final Answer in JSON format:
{"answer": "\\frac{\\sqrt{\\pi}}{2}e^{-1}", "numerical_answer": "0.3260246644"}