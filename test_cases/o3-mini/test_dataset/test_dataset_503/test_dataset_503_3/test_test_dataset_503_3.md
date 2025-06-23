We start with the integral

  I = ∫₀^π cos(x) cos(3x) cos(5x) dx.

Step 1. Multiply two cosine factors using the product‐to‐sum identity:
  cos(3x) cos(5x) = ½ [cos(3x + 5x) + cos(3x − 5x)]
               = ½ [cos(8x) + cos(−2x)]
Since cos(−2x) = cos(2x), we have
  cos(3x) cos(5x) = ½ [cos(8x) + cos(2x)].

Step 2. Multiply with cos(x):
  cos(x) cos(3x) cos(5x) = cos(x) · ½ [cos(8x) + cos(2x)]
        = ½ [cos(x) cos(8x) + cos(x) cos(2x)].

Step 3. Apply the product‐to‐sum identity again:
  For cos(x) cos(8x):
    cos(x) cos(8x) = ½ [cos(x + 8x) + cos(x − 8x)]
               = ½ [cos(9x) + cos(7x)].
  For cos(x) cos(2x):
    cos(x) cos(2x) = ½ [cos(x + 2x) + cos(x − 2x)]
               = ½ [cos(3x) + cos(x)].

Thus,
  cos(x) cos(3x) cos(5x) = ½ {½ [cos(9x) + cos(7x)] + ½ [cos(3x) + cos(x)]}
               = ¼ [cos(9x) + cos(7x) + cos(3x) + cos(x)].

Step 4. Substitute this back into the integral:
  I = ∫₀^π cos(x) cos(3x) cos(5x) dx
    = ¼ ∫₀^π [cos(9x) + cos(7x) + cos(3x) + cos(x)] dx.

Step 5. Integrate each term individually:
  For any integer k ≠ 0,
    ∫₀^π cos(kx) dx = [sin(kx)/k]₀^π = (sin(kπ)/k) − (sin 0/k) = 0,
since sin(nπ) = 0.

So each term ∫₀^π cos(9x) dx, ∫₀^π cos(7x) dx, ∫₀^π cos(3x) dx, and ∫₀^π cos(x) dx equals 0.

Thus, I = ¼ (0 + 0 + 0 + 0) = 0.

Step 6. Numerical approximation:
  Since the exact answer is 0, the numerical approximation is 0.0000000000.

Final JSON output:
{"answer": "$0$", "numerical_answer": "0.0000000000"}