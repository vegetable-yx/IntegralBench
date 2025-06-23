We start with the integral

  I = ∫₀^(441) [π sin(π√x) / √x] dx.

Step 1. Make the substitution:
  Let u = √x ⇒ x = u² and dx = 2u du.
When x = 0, u = 0; when x = 441, u = 21.

Substitute these into the integral:
  I = ∫₀^(21) [π sin(πu) / u] × (2u du)
    = 2π ∫₀^(21) sin(πu) du.

Step 2. Make a further substitution:
  Let v = πu ⇒ dv = π du ⇒ du = dv/π.
When u = 0, v = 0; when u = 21, v = 21π.

Then the integral becomes:
  I = 2π ∫₀^(21π) sin(v) (dv/π)
    = 2 ∫₀^(21π) sin(v) dv.

Step 3. Compute the integral in v:
  ∫ sin(v) dv = –cos(v) + C.
Thus,
  I = 2 [ –cos(v) ] from v = 0 to v = 21π
    = 2 [ –cos(21π) + cos(0) ]
    = 2 [cos(0) – cos(21π)].

Recall that cos(0) = 1 and cos(21π) = (–1)^(21) = –1 (since 21 is odd), so:
  I = 2 [1 – (–1)]
    = 2 (1 + 1)
    = 4.

Step 4. Final answers:
The exact value of the integral is 4 and the numerical approximation is 4.0000000000.

{"answer": "$4$", "numerical_answer": "4.0000000000"}