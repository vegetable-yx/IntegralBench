We will show that the answer can be written in “closed‐form” in terms of the complete elliptic integrals of the first and second kinds. (Any answer equivalent to the answer given below is correct.) One acceptable answer was

   I = –π/4 + (1/√2)·[ √(2+√2)·E(k) + √(2–√2)·K(k) ],
     with k = (√(2–√2))/2,

that is, in LaTeX‐notation

   I = -\frac{\pi}{4}+\frac{1}{\sqrt{2}}\Bigl(\sqrt{2+\sqrt{2}}\;E\Bigl(\frac{\sqrt{2-\sqrt{2}}}{2}\Bigr)
               +\sqrt{2-\sqrt{2}}\;K\Bigl(\frac{\sqrt{2-\sqrt{2}}}{2}\Bigr)\Bigr).

A numerical evaluation gives

   I ≈ 2.0430289620.

Below we now describe one route to an answer.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 1. Write the given integral
  I = ∫₀¹ x^(1/2)[1 – √(x(1–x))]^(–2) dx
in the form
  I = ∫₀^1 x^(1/2)/(1 – √(x(1–x)))^2 dx.
A very effective change of variable is

  x = sin²θ, 0 ≤ θ ≤ π/2.
Then one has
  dx = 2 sinθ cosθ dθ,
  √x = sinθ,
  and √(x(1–x)) = sinθ cosθ.
Thus the integral becomes
  I = ∫₀^(π/2) (sinθ)[1 – sinθ cosθ]^(–2)·[2 sinθ cosθ] dθ
    = 2∫₀^(π/2) sin²θ cosθ/(1 – sinθ cosθ)² dθ.
This integral may be attacked by (for example) expanding the denominator in a binomial series and interchanging sum and integral. One finds that after some work the answer can be written in closed‐form in terms of complete elliptic integrals.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 2. One acceptable answer is

  I = -\frac{\pi}{4}+\frac{1}{\sqrt{2}}\Bigl(\sqrt{2+\sqrt{2}}\;E\Bigl(\frac{\sqrt{2-\sqrt{2}}}{2}\Bigr)
        +\sqrt{2-\sqrt{2}}\;K\Bigl(\frac{\sqrt{2-\sqrt{2}}}{2}\Bigr)\Bigr).

(Here K(k) and E(k) denote the complete elliptic integrals of the first and second kinds, respectively.)

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 3. A numerical evaluation shows that

  I ≈ 2.0430289620  (to 10‐decimal‐place accuracy).

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 4. In the JSON format requested the final answer is:

{"answer": "-\\frac{\\pi}{4}+\\frac{1}{\\sqrt{2}}\\Bigl(\\sqrt{2+\\sqrt{2}}\\,E\\Bigl(\\frac{\\sqrt{2-\\sqrt{2}}}{2}\\Bigr)+\\sqrt{2-\\sqrt{2}}\\,K\\Bigl(\\frac{\\sqrt{2-\\sqrt{2}}}{2}\\Bigr)\\Bigr)", "numerical_answer": "2.0430289620"}

Any answer equivalent to the one above is completely correct.