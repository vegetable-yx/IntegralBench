First, we split the given integral into two parts:
 I = ∫₀¹ (x²/(2 – x²) + √(2x/(x+1))) dx = I₁ + I₂.

Step 1. Evaluate I₁:

I₁ = ∫₀¹ x²/(2 – x²) dx.

Notice that
 x²/(2 – x²) = [2 – (2 – x²)]/(2 – x²) = 2/(2 – x²) – 1.
Thus,
 I₁ = 2∫₀¹ 1/(2 – x²) dx − ∫₀¹ 1 dx = 2J − 1,
where
 J = ∫₀¹ 1/(2 – x²) dx.

Using the substitution x = √2 sinθ (so that dx = √2 cosθ dθ and when x = 0, θ = 0; when x = 1, sinθ = 1/√2, i.e. θ = π/4), observe that

 2 – x² = 2 − 2 sin²θ = 2 cos²θ.
Then
 J = ∫₀^(π/4) 1/(2 cos²θ) · (√2 cosθ dθ)
     = (√2/2) ∫₀^(π/4) 1/cosθ dθ
     = (√2/2) ∫₀^(π/4) secθ dθ.
Recall that ∫ secθ dθ = ln|secθ + tanθ| + C, hence
 J = (√2/2) [ln|secθ + tanθ|]₀^(π/4)
     = (√2/2) [ln((sec(π/4) + tan(π/4))/(sec0 + tan0))]
     = (√2/2) ln((√2 + 1)/1)
     = (√2/2) ln(1+√2).
Thus,
 I₁ = 2J − 1 = √2 ln(1+√2) − 1.

Step 2. Evaluate I₂:

I₂ = ∫₀¹ √(2x/(x+1)) dx.
Write the integrand as:
 √(2x/(x+1)) = (√2 √x)/√(x+1).

We make the substitution:
 t = √(x+1) → x = t² − 1 , dx = 2t dt.
When x = 0, t = 1; when x = 1, t = √2.

Now, in terms of t the integrand becomes:
 √(2x) = √[2(t²−1)] = √2 √(t²−1) and √(x+1) = t.
Thus,
 I₂ = ∫₁^(√2) [ (√2 √(t²−1))/t ] · (2t dt)
    = 2√2 ∫₁^(√2) √(t²−1) dt.

A standard integral gives:
 ∫ √(t²−1) dt = (t/2)√(t²−1) − (1/2) ln|t+√(t²−1)| + C.
So, if we define:
 F(t) = (t/2)√(t²−1) − (1/2) ln|t+√(t²−1)|,
then
 I₂ = 2√2 [F(√2) − F(1)].

At t = 1: 
 √(1²−1) = 0, so F(1) = (1/2 · 0) − (1/2) ln(1) = 0.
At t = √2:
 √( (√2)²−1) = √(2−1) = 1, so
 F(√2) = (√2/2)·1 − (1/2) ln(√2+1) = (√2/2) − (1/2) ln(1+√2).

Thus,
 I₂ = 2√2 [(√2/2) − (1/2) ln(1+√2)]
    = 2√2·(√2/2) − 2√2·(1/2) ln(1+√2)
    = 2 − √2 ln(1+√2).

Step 3. Combine I₁ and I₂:

I = I₁ + I₂ = (√2 ln(1+√2) − 1) + (2 − √2 ln(1+√2)) = 1.

Thus, the exact value of the integral is 1.

Step 4. Numerical approximation:
 1.0000000000 (to 10 decimal places).

The final answer in the required JSON format is:
{"answer": "$1$", "numerical_answer": "1.0000000000"}