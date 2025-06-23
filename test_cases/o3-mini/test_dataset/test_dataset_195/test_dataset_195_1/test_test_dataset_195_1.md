We wish to evaluate

  I = ∫₀¹ (arcsin x)(arccos x) dx.

Step 1. Express arcsin and arccos in a convenient form

Recall that for x ∈ [0, 1] one has
  arccos x = π/2 – arcsin x.
Thus,
  I = ∫₀¹ (arcsin x)[π/2 – arcsin x] dx
    = (π/2) ∫₀¹ arcsin x dx – ∫₀¹ (arcsin x)² dx.

Let us denote
  I₁ = ∫₀¹ arcsin x dx  and  I₂ = ∫₀¹ (arcsin x)² dx.

Step 2. Compute I₁ = ∫₀¹ arcsin x dx

Make the substitution:
  u = arcsin x → x = sin u, dx = cos u du.
When x = 0, u = 0 and when x = 1, u = π/2.
Thus,
  I₁ = ∫₀^(π/2) u cos u du.

Apply integration by parts:
 Let w = u  → dw = du,
   dv = cos u du → v = sin u.
Then,
  I₁ = [u sin u]₀^(π/2) – ∫₀^(π/2) sin u du.
Evaluate:
 [u sin u]₀^(π/2) = (π/2)·sin(π/2) – 0 = π/2.
 ∫₀^(π/2) sin u du = [–cos u]₀^(π/2) = (–cos(π/2)) – (–cos 0) = 0 + 1 = 1.
Thus,
  I₁ = (π/2) – 1.

Step 3. Compute I₂ = ∫₀¹ (arcsin x)² dx

Substitute again u = arcsin x (so that x = sin u and dx = cos u du). Then,
  I₂ = ∫₀^(π/2) u² cos u du.
Apply integration by parts:
 Let w = u²  → dw = 2u du,
   dv = cos u du → v = sin u.
Thus,
  I₂ = [u² sin u]₀^(π/2) – ∫₀^(π/2) 2u sin u du.
The boundary term is:
 [u² sin u]₀^(π/2) = (π/2)²·1 – 0 = π²/4.
Now, compute J = ∫₀^(π/2) 2u sin u du.
Again, use integration by parts:
 Let p = u  → dp = du,
   dq = sin u du → q = –cos u.
Then,
 J = 2{[u (–cos u)]₀^(π/2) – ∫₀^(π/2) (–cos u) du}
   = 2{–u cos u |₀^(π/2) + ∫₀^(π/2) cos u du}.
Evaluate:
 At u = π/2: –(π/2) cos(π/2) = 0, at u = 0: 0.
 ∫₀^(π/2) cos u du = sin u |₀^(π/2) = 1 – 0 = 1.
Thus,
 J = 2(0 + 1) = 2.
So, I₂ becomes:
  I₂ = (π²/4) – 2.

Step 4. Combine your results to obtain I

Recall that
  I = (π/2) I₁ – I₂.
Substitute I₁ and I₂:
  I = (π/2)[(π/2) – 1] – [(π²/4) – 2]
    = (π²/4 – π/2) – (π²/4 – 2)
    = (π²/4 – π/2 – π²/4 + 2)
    = 2 – (π/2).
Thus, the exact answer can be written as
  I = 2 – π/2 = (4 – π)/2.

Step 5. Numerical approximation

Calculate a numerical value:
  π/2 ≈ 1.5707963268,
so
  I = 2 – 1.5707963268 ≈ 0.4292036732.

Final Answer in JSON format:

{"answer": "2 - \\frac{\\pi}{2}", "numerical_answer": "0.4292036732"}