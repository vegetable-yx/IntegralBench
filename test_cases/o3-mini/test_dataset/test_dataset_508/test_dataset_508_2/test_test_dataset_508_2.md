We start with the integral

  I = ∫₀^(441) (π sin(π√x) / √x) dx.

Step 1. Substitute u = √x. Then x = u² and dx = 2u du. The limits change as follows: when x = 0, u = 0; when x = 441, u = √441 = 21. Thus the integral becomes

  I = ∫₀^(21) [π sin(πu) / u] · (2u du)
    = ∫₀^(21) [2π sin(πu)] du.

Step 2. Factor out the constant and integrate:

  I = 2π ∫₀^(21) sin(πu) du.

Recall that ∫ sin(πu) du = –(1/π) cos(πu) + C. Applying the limits:

  ∫₀^(21) sin(πu) du = –(1/π) [cos(π·21) – cos(π·0)]
                 = –(1/π)[cos(21π) – 1].

Now multiply by 2π:

  I = 2π · ( –(1/π)[cos(21π) – 1] )
    = –2 [cos(21π) – 1]
    = –2cos(21π) + 2.

Step 3. Use the fact that cos(21π) = (–1)²¹ = –1 (since 21 is odd):

  I = –2(–1) + 2 = 2 + 2 = 4.

Thus the exact value of the integral is 4.

Step 4. The numerical approximation (to 10 decimal places) is 4.0000000000.

{"answer": "4", "numerical_answer": "4.0000000000"}