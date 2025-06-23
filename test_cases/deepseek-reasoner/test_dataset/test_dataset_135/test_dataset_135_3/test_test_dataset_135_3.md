<think>
Okay, let's see. I need to compute the definite integral from 0 to 2 of x^(-1/2) times (2 - x)^(-1/2) times [1 - 0.5x(2 - x)] dx. Hmm, that looks a bit complicated, but maybe there's a substitution or a beta function involved here. Let me start by simplifying the integrand.

First, let's write the integral out again to make sure I have it right:

∫₀² x^(-1/2) (2 - x)^(-1/2) [1 - 0.5x(2 - x)] dx

Let me simplify the expression inside the brackets first. The term 0.5x(2 - x) can be expanded. Let's compute that:

0.5x(2 - x) = 0.5*(2x - x²) = x - 0.5x²

So, 1 - 0.5x(2 - x) = 1 - x + 0.5x². Wait, is that right? Let me check:

Wait, 0.5x(2 - x) is 0.5*2x - 0.5x² = x - 0.5x². So subtracting that from 1 gives 1 - x + 0.5x². Yes, that's correct.

So the integrand becomes x^(-1/2) (2 - x)^(-1/2) times (1 - x + 0.5x²). Hmm. Maybe splitting this into separate terms would help. Let's split the product:

x^(-1/2)(2 - x)^(-1/2) * 1 - x^(-1/2)(2 - x)^(-1/2) * x + 0.5x^(-1/2)(2 - x)^(-1/2) * x²

So the integral becomes three separate integrals:

I = ∫₀² x^(-1/2)(2 - x)^(-1/2) dx
- ∫₀² x^(1/2)(2 - x)^(-1/2) dx
+ 0.5 ∫₀² x^(3/2)(2 - x)^(-1/2) dx

Now, these integrals look like Beta functions or related to the Beta function. The Beta function is defined as B(a,b) = 2∫₀}^{π/2} (sinθ)^{2a-1}(cosθ)^{2b-1} dθ, but also relates to the integral from 0 to 1 of t^{a-1}(1 - t)^{b-1} dt. Alternatively, integrals of the form ∫₀^c x^{n}(c - x)^m dx can be expressed using Beta functions with substitution.

Let me recall that the integral from 0 to c of x^{a}(c - x)^{b} dx = c^{a + b + 1} * B(a+1, b+1) = c^{a + b + 1} * Γ(a+1)Γ(b+1)/Γ(a + b + 2). But here, the limits are from 0 to 2, so c=2. Let's check each integral.

First integral: I1 = ∫₀² x^(-1/2)(2 - x)^(-1/2) dx

Let me make a substitution here. Let t = x/2, so x = 2t, dx = 2dt. Then when x=0, t=0; x=2, t=1. Then I1 becomes ∫₀¹ (2t)^(-1/2) (2 - 2t)^(-1/2) * 2 dt

Simplify each term:

(2t)^(-1/2) = 2^(-1/2) t^(-1/2)

(2 - 2t)^(-1/2) = (2(1 - t))^(-1/2) = 2^(-1/2) (1 - t)^(-1/2)

Multiply them together: 2^(-1/2) * 2^(-1/2) = 2^(-1), and t^(-1/2)(1 - t)^(-1/2). Then multiplied by 2 dt:

So I1 = 2 * 2^(-1) ∫₀¹ t^(-1/2)(1 - t)^(-1/2) dt = ∫₀¹ t^(-1/2)(1 - t)^(-1/2) dt

But the integral of t^{-1/2}(1 - t)^{-1/2} from 0 to 1 is the Beta function B(1/2, 1/2). And B(1/2,1/2) = Γ(1/2)Γ(1/2)/Γ(1) = π / 1 = π. So I1 = π.

Okay, that's the first integral. Now the second integral: I2 = ∫₀² x^(1/2)(2 - x)^(-1/2) dx

Again, let's use substitution t = x/2, so x=2t, dx=2dt. Then:

I2 = ∫₀¹ (2t)^(1/2) (2 - 2t)^(-1/2) * 2 dt

Simplify:

(2t)^(1/2) = 2^(1/2) t^(1/2)

(2 - 2t)^(-1/2) = 2^(-1/2)(1 - t)^(-1/2)

Multiply them: 2^(1/2) * 2^(-1/2) = 1, so t^(1/2)(1 - t)^(-1/2)

Multiply by 2 dt: 2 * t^(1/2)(1 - t)^(-1/2) dt

So I2 = 2 ∫₀¹ t^(1/2)(1 - t)^(-1/2) dt

This is 2 * B(3/2, 1/2). Because Beta function B(a,b) = ∫₀¹ t^{a-1}(1 - t)^{b-1} dt. So here, a-1 = 1/2 ⇒ a=3/2, and b-1 = -1/2 ⇒ b=1/2. So B(3/2, 1/2) = Γ(3/2)Γ(1/2)/Γ(2). Γ(3/2) = (1/2)√π, Γ(1/2) = √π, Γ(2) = 1! = 1. So B(3/2,1/2) = (1/2 √π)(√π) / 1 = (1/2) π. Therefore, I2 = 2 * (1/2) π = π.

Wait, that's interesting. So I2 = π. Hmm. Let me check that again.

Wait, Γ(3/2) is (1/2)Γ(1/2) = (1/2)√π. So yes, Γ(3/2)Γ(1/2) = (1/2)√π * √π = (1/2) π. Then Γ(3/2 + 1/2) = Γ(2) = 1. So B(3/2,1/2) = (1/2 π)/1 = π/2. Wait, no, wait. Wait, the Beta function is Γ(a)Γ(b)/Γ(a + b). Wait, no, the Beta function is B(a,b) = Γ(a)Γ(b)/Γ(a + b). So here, a=3/2, b=1/2. So Γ(3/2)Γ(1/2)/Γ(2). Γ(3/2) is (1/2)√π, Γ(1/2) is √π, Γ(2) is 1. So B(3/2,1/2) = (1/2 √π)(√π) / 1 = (1/2) π. Therefore, B(3/2,1/2) = π/2. Then I2 = 2 * (π/2) = π. Yes, that's correct. So I2 = π.

Third integral: I3 = 0.5 ∫₀² x^(3/2)(2 - x)^(-1/2) dx

Again, substitution t = x/2, x=2t, dx=2dt. Then:

I3 = 0.5 * ∫₀¹ (2t)^(3/2) (2 - 2t)^(-1/2) * 2 dt

Simplify:

(2t)^(3/2) = 2^(3/2) t^(3/2)

(2 - 2t)^(-1/2) = 2^(-1/2)(1 - t)^(-1/2)

Multiply them: 2^(3/2) * 2^(-1/2) = 2^(1) = 2. So 2 * t^(3/2)(1 - t)^(-1/2)

Multiply by 2 dt (from dx) and the 0.5 factor:

0.5 * 2 * 2 ∫₀¹ t^(3/2)(1 - t)^(-1/2) dt = 2 ∫₀¹ t^(3/2)(1 - t)^(-1/2) dt

So this is 2 * B(5/2, 1/2). Let's compute that.

B(5/2,1/2) = Γ(5/2)Γ(1/2)/Γ(3). Γ(5/2) is (3/2)(1/2)√π = (3/4)√π. Γ(1/2) is √π. Γ(3) is 2! = 2. So:

B(5/2,1/2) = (3/4 √π)(√π) / 2 = (3/4 π) / 2 = 3π/8. Therefore, I3 = 2 * (3π/8) = 3π/4.

Putting it all together, the original integral is I1 - I2 + 0.5 I3. Wait, no. Wait, the original integral is I = I1 - I2 + 0.5 I3. Wait, let's check:

Original integral was:

I = I1 - I2 + 0.5 I3

Wait, the original integrand was [1 - x + 0.5x²], so when we split the integrals, it's:

I = ∫ [1 term] - ∫ [x term] + 0.5 ∫ [x² term]

So yes, I1 is the first integral, I2 is the second, and I3 is the third. So:

I = I1 - I2 + 0.5 * I3

Wait, no. Wait, the third term is 0.5 times the integral of x² term. But in the original problem, the third term is 0.5x², so when we split, it's 0.5 times the integral of x² times x^(-1/2)(2 - x)^(-1/2). Wait, but in the split, the third integral is 0.5 ∫ x² * x^(-1/2)(2 - x)^(-1/2) dx = 0.5 ∫ x^(3/2)(2 - x)^(-1/2) dx. Which is exactly what I called I3. So the original integral is I1 - I2 + 0.5 I3. Wait, but in the problem statement, the integrand is [1 - 0.5x(2 - x)] which we expanded to 1 - x + 0.5x². So when we split the integral into three parts, the coefficients are 1, -1, and +0.5. So the integral is:

I = I1 - I2 + 0.5 I3

But according to our calculations:

I1 = π

I2 = π

I3 = 3π/4

So substituting:

Integral = π - π + 0.5*(3π/4) = 0 + (3π/8) = 3π/8

Wait, that's the result? Let me check again.

Wait, I3 was calculated as 0.5 times the integral of x² term. Wait, no, in the original split, the third term is 0.5 times the integral of x² term.

But when I computed I3, I considered the integral of x^(3/2)(2 - x)^(-1/2) dx, which is the x² term multiplied by x^(-1/2) (2 - x)^(-1/2). So x² * x^(-1/2) = x^(3/2). So yes, that's correct.

But when I computed I3, I found that 0.5 * ∫ x^(3/2)(2 - x)^(-1/2) dx = 0.5 * (3π/4). Wait, no. Wait, let's retrace:

Wait, in the third integral, the coefficient is 0.5, so the third term is 0.5 * I3, where I3 is the integral of x^(3/2)(2 - x)^(-1/2) dx. But when I computed I3, I substituted and found that the integral of x^(3/2)(2 - x)^(-1/2) dx from 0 to 2 is 3π/4. Wait, no. Wait, no, let's go back.

Wait, in the third integral, I3 was defined as 0.5 times the integral of x^(3/2)(2 - x)^(-1/2) dx. But when I did the substitution, I found that:

I3 (the third integral) = 0.5 * [2 * B(5/2,1/2)] = 0.5 * 2 * (3π/8) = 3π/8. Wait, no, let me check again.

Wait, the third integral is 0.5 ∫₀² x^(3/2)(2 - x)^(-1/2) dx. Then, after substitution, we had:

0.5 * 2 * 2 ∫₀¹ t^(3/2)(1 - t)^(-1/2) dt. Wait, no, let's redo the substitution step.

Original I3: 0.5 ∫₀² x^(3/2)(2 - x)^(-1/2) dx

Substitute x = 2t, dx = 2dt, limits 0 to 1.

So x^(3/2) = (2t)^(3/2) = 2^(3/2) t^(3/2)

(2 - x)^(-1/2) = (2 - 2t)^(-1/2) = (2(1 - t))^(-1/2) = 2^(-1/2)(1 - t)^(-1/2)

Multiply these: 2^(3/2) * 2^(-1/2) = 2^(1) = 2. So 2 * t^(3/2)(1 - t)^(-1/2)

Then multiply by dx = 2dt: 2 * t^(3/2)(1 - t)^(-1/2) * 2 dt = 4 t^(3/2)(1 - t)^(-1/2) dt

But the integral is 0.5 times that. So:

0.5 * 4 ∫₀¹ t^(3/2)(1 - t)^(-1/2) dt = 2 ∫₀¹ t^(3/2)(1 - t)^(-1/2) dt

Which is 2 * B(5/2, 1/2). Then B(5/2,1/2) = Γ(5/2)Γ(1/2)/Γ(3). Γ(5/2) is (3/2)(1/2)√π = (3/4)√π. Γ(1/2) is √π. Γ(3) is 2! = 2. So:

B(5/2,1/2) = (3/4 √π)(√π) / 2 = (3/4 * π) / 2 = 3π/8. Therefore, the integral I3 (the third term) is 2 * (3π/8) = 3π/4.

Wait, but the third term in the original integral is 0.5 times the integral of x² term. So the third term is 0.5 * I3, where I3 is the integral of x^(3/2)(2 - x)^(-1/2) dx. But according to the substitution, that integral is 3π/4. Therefore, the third term is 0.5 * 3π/4 = 3π/8.

Wait, no. Wait, in the substitution step, when we computed I3 (the third integral), we already included the 0.5 factor. Let me check:

Original third integral: 0.5 ∫₀² x^(3/2)(2 - x)^(-1/2) dx. After substitution, we found that this equals 3π/4. So yes, the third term is 3π/4. Therefore, putting it all together:

Integral = I1 - I2 + I3 = π - π + 3π/4 = 0 + 3π/4 = 3π/4. Wait, but that contradicts the previous calculation. Wait, no, no. Wait, the third term is 0.5 times the integral of x² term, which after substitution is 3π/4. So the third term is 0.5 * 3π/4 = 3π/8. Wait, no, no. Wait, the third integral is 0.5 times the integral of x^(3/2)(2 - x)^(-1/2) dx. But when we did the substitution, we found that the integral of x^(3/2)(2 - x)^(-1/2) dx is 3π/4. Therefore, 0.5 times that is 3π/8. So the third term is 3π/8.

But earlier, when we split the integral into three parts:

Integral = I1 - I2 + 0.5 I3, where I1 is π, I2 is π, and I3 is the integral of x^(3/2)(2 - x)^(-1/2) dx, which is 3π/4. Therefore, 0.5 * 3π/4 = 3π/8. So the total is π - π + 3π/8 = 3π/8.

Wait, so the final result is 3π/8. Let me confirm this again.

Yes, because:

I1 = π

I2 = π

Third term: 0.5 * I3 = 0.5 * (3π/4) = 3π/8

So Integral = π - π + 3π/8 = 3π/8.

So the exact answer is 3π/8. Then the numerical approximation would be 3 * π / 8. Let's compute that.

π is approximately 3.141592653589793. So 3π ≈ 9.42477796076938. Divided by 8: 9.42477796076938 / 8 ≈ 1.1780972450961725. Rounded to 10 decimal places, that's 1.1780972451.

Wait, but let me check with more precise calculation.

3 * π / 8? Wait, no, 3π/8. Wait, 3 divided by 8 is 0.375. 0.375 * π ≈ 0.375 * 3.141592653589793 = 1.1780972450961725. Yes, so approximately 1.1780972451.

But let me verify with a calculator. 3 * π = 9.42477796077, divided by 8: 9.42477796077 / 8 = 1.17809724509625. So yes, approximately 1.1780972451 when rounded to 10 decimal places.

So the exact answer is 3π/8, and the numerical approximation is approximately 1.1780972451.

But let me check if there's another way to compute the integral, maybe by recognizing a Beta function or a substitution that simplifies the entire integrand.

Alternatively, perhaps a substitution like x = 2 sin²θ. Let's try that.

Let x = 2 sin²θ, so when x=0, θ=0; x=2, θ=π/2. Then dx = 4 sinθ cosθ dθ.

Then x^(-1/2) = (2 sin²θ)^(-1/2) = (2)^(-1/2) (sinθ)^(-1)

(2 - x)^(-1/2) = (2 - 2 sin²θ)^(-1/2) = (2 cos²θ)^(-1/2) = (2)^(-1/2) (cosθ)^(-1)

So x^(-1/2)(2 - x)^(-1/2) = (2)^(-1) (sinθ cosθ)^(-1)

The term [1 - 0.5x(2 - x)] becomes 1 - 0.5*(2 sin²θ)(2 - 2 sin²θ) = 1 - 0.5*(2 sin²θ)(2 cos²θ) = 1 - 0.5*(4 sin²θ cos²θ) = 1 - 2 sin²θ cos²θ.

But 2 sinθ cosθ = sin(2θ), so sin²θ cos²θ = (sin2θ)^2 / 4. Therefore, 2 sin²θ cos²θ = (sin²2θ)/2. So:

1 - 2 sin²θ cos²θ = 1 - (sin²2θ)/2.

Putting it all together, the integral becomes:

∫₀^{π/2} [2^(-1) (sinθ cosθ)^(-1)] * [1 - (sin²2θ)/2] * 4 sinθ cosθ dθ

Simplify the terms:

2^(-1) * 4 = 2. The (sinθ cosθ)^(-1) multiplied by sinθ cosθ cancels out, leaving 1. So the integral simplifies to:

2 ∫₀^{π/2} [1 - (sin²2θ)/2] dθ

= 2 [ ∫₀^{π/2} 1 dθ - (1/2) ∫₀^{π/2} sin²2θ dθ ]

Compute each integral:

First integral: ∫₀^{π/2} 1 dθ = π/2

Second integral: ∫₀^{π/2} sin²2θ dθ. Let's use the identity sin²x = (1 - cos2x)/2. So:

∫ sin²2θ dθ = ∫ (1 - cos4θ)/2 dθ = (1/2)θ - (1/8) sin4θ evaluated from 0 to π/2.

At π/2: (1/2)(π/2) - (1/8) sin(2π) = π/4 - 0 = π/4

At 0: 0 - 0 = 0

So the integral is π/4.

Therefore, the second term is (1/2) * π/4 = π/8

Putting it all together:

2 [ π/2 - π/8 ] = 2 [ (4π/8 - π/8) ] = 2 [ 3π/8 ] = 6π/8 = 3π/4

Wait, wait, that's conflicting with the previous result. Wait, this substitution method gives 3π/4, but earlier we had 3π/8. There's a discrepancy here. That's a problem. Which one is correct?

Wait, this is a problem. Let me check where I went wrong.

Wait, in the substitution method, the integral becomes:

2 [ ∫₀^{π/2} 1 dθ - (1/2) ∫₀^{π/2} sin²2θ dθ ]

Which is 2 [ π/2 - (1/2)(π/4) ] = 2 [ π/2 - π/8 ] = 2 [ 3π/8 ] = 6π/8 = 3π/4.

But earlier, splitting into three integrals gave 3π/8. So there's a contradiction. Therefore, one of the methods is wrong.

Hmm. Let's check the substitution method again.

Original integral: ∫₀² x^{-1/2} (2 - x)^{-1/2} [1 - 0.5x(2 - x)] dx

Substitution x = 2 sin²θ, dx = 4 sinθ cosθ dθ

Then x^{-1/2} = (2 sin²θ)^{-1/2} = 2^{-1/2} sin^{-1}θ

(2 - x)^{-1/2} = (2 - 2 sin²θ)^{-1/2} = (2 cos²θ)^{-1/2} = 2^{-1/2} cos^{-1}θ

So x^{-1/2}(2 - x)^{-1/2} = 2^{-1} (sinθ cosθ)^{-1}

The term [1 - 0.5x(2 - x)] = 1 - 0.5*(2 sin²θ)(2 cos²θ) = 1 - 0.5*(4 sin²θ cos²θ) = 1 - 2 sin²θ cos²θ

Then the integrand becomes:

2^{-1} (sinθ cosθ)^{-1} * [1 - 2 sin²θ cos²θ] * 4 sinθ cosθ dθ

Simplify:

2^{-1} * 4 = 2. (sinθ cosθ)^{-1} * sinθ cosθ = 1. So the integrand is 2 * [1 - 2 sin²θ cos²θ] dθ

Wait, so the integral becomes 2 [1 - 2 sin²θ cos²θ] dθ from 0 to π/2.

Wait, that's different from what I had before. Wait, in the previous substitution step, I think I made a mistake in expanding [1 - 0.5x(2 - x)].

Wait, let's re-express [1 - 0.5x(2 - x)]:

x = 2 sin²θ, so 0.5x(2 - x) = 0.5 * 2 sin²θ * (2 - 2 sin²θ) = 0.5 * 2 sin²θ * 2 cos²θ = 0.5 * 4 sin²θ cos²θ = 2 sin²θ cos²θ. Therefore, 1 - 0.5x(2 - x) = 1 - 2 sin²θ cos²θ. So that part is correct.

So the integrand is 2 [1 - 2 sin²θ cos²θ] dθ. Therefore, the integral is 2 ∫₀^{π/2} [1 - 2 sin²θ cos²θ] dθ.

Now, let's compute this integral:

First, ∫₀^{π/2} 1 dθ = π/2

Second, ∫₀^{π/2} 2 sin²θ cos²θ dθ. Let's compute this.

Note that sin²θ cos²θ = (sinθ cosθ)^2 = (1/2 sin2θ)^2 = 1/4 sin²2θ. So 2 sin²θ cos²θ = 1/4 * 2 sin²2θ = 1/2 sin²2θ.

Therefore, the integral becomes:

2 [ π/2 - ∫₀^{π/2} (1/2 sin²2θ) dθ ] = 2 [ π/2 - (1/2) ∫₀^{π/2} sin²2θ dθ ]

Now, compute ∫₀^{π/2} sin²2θ dθ. Let's use substitution φ = 2θ, so when θ=0, φ=0; θ=π/2, φ=π. dφ = 2 dθ ⇒ dθ = dφ/2. So the integral becomes:

∫₀^{π} sin²φ * (dφ)/2 ) = (1/2) ∫₀^{π} sin²φ dφ

Using the identity sin²φ = (1 - cos2φ)/2:

= (1/2) ∫₀^{π} (1 - cos2φ)/2 dφ = (1/4) [ ∫₀^{π} 1 dφ - ∫₀^{π} cos2φ dφ ]

= (1/4) [ π - (1/2) sin2φ from 0 to π ]

But sin2φ at π is sin2π = 0, and at 0 is 0. So the second term is 0.

Thus, ∫₀^{π/2} sin²2θ dθ = (1/4) * π = π/4.

Therefore, the integral becomes:

2 [ π/2 - (1/2)(π/4) ] = 2 [ π/2 - π/8 ] = 2 [ 3π/8 ] = 6π/8 = 3π/4.

But this contradicts the previous result of 3π/8. So there's a mistake somewhere. But where?

Wait, the substitution method gave 3π/4, while the integral splitting method gave 3π/8. Which one is correct?

Let me check with a numerical approximation. Let's compute the integral numerically.

The integral is ∫₀² x^{-1/2} (2 - x)^{-1/2} [1 - 0.5x(2 - x)] dx.

Let me approximate this using numerical integration. Let's pick a few points or use symmetry.

Alternatively, since the substitution method gives 3π/4 ≈ 2.35619449019, while the integral splitting gives 3π/8 ≈ 1.1780972451. These are very different. So one of the methods must be wrong.

Wait, but in the substitution method, the integrand after substitution became 2 [1 - 2 sin²θ cos²θ] dθ. Let's compute that integral numerically.

Compute 2 * [ π/2 - (1/2)(π/4) ] = 2*(π/2 - π/8) = 2*(3π/8) = 3π/4 ≈ 2.356.

But if I compute the original integral numerically, say using a calculator or approximate method.

Let me try to compute the integral numerically. Let's approximate ∫₀² x^{-1/2} (2 - x)^{-1/2} [1 - 0.5x(2 - x)] dx.

First, note that x ranges from 0 to 2. The integrand at x=0: x^{-1/2} tends to infinity, but (2 - x)^{-1/2} is (2)^{-1/2}, so the integrand behaves like (sqrt(2))^{-1} * infinity * [1 - 0] → infinity. Similarly at x=2, similar behavior. So the integral is improper at both ends, but converges.

Let me use substitution x = 2t, so t from 0 to 1. Then dx = 2dt. The integral becomes:

∫₀¹ (2t)^{-1/2} (2 - 2t)^{-1/2} [1 - 0.5*(2t)(2 - 2t)] * 2 dt

Simplify:

(2t)^{-1/2} = 2^{-1/2} t^{-1/2}

(2 - 2t)^{-1/2} = 2^{-1/2} (1 - t)^{-1/2}

Multiply them: 2^{-1} t^{-1/2} (1 - t)^{-1/2}

The term [1 - 0.5*(2t)(2 - 2t)] = 1 - 0.5*(4t - 4t²) = 1 - 2t + 2t²

Multiply by 2 dt: 2^{-1} * 2 = 1. So the integral becomes:

∫₀¹ t^{-1/2} (1 - t)^{-1/2} [1 - 2t + 2t²] dt

This is the same as:

∫₀¹ t^{-1/2} (1 - t)^{-1/2} dt - 2 ∫₀¹ t^{1/2} (1 - t)^{-1/2} dt + 2 ∫₀¹ t^{3/2} (1 - t)^{-1/2} dt

Which is:

B(1/2,1/2) - 2 B(3/2,1/2) + 2 B(5/2,1/2)

We know B(1/2,1/2) = π

B(3/2,1/2) = π/2

B(5/2,1/2) = 3π/8

So substituting:

π - 2*(π/2) + 2*(3π/8) = π - π + 3π/4 = 0 + 3π/4 = 3π/4 ≈ 2.35619449019

But this contradicts the previous splitting into three integrals where we had 3π/8. Wait, but in this case, after substitution, the integral becomes 3π/4, which matches the substitution method. So where did I go wrong in the first approach?

Ah! I see now. In the first approach, when I split the integral into three parts, I think I made a mistake in the coefficients.

Wait, let's re-examine the original integral:

∫₀² x^{-1/2} (2 - x)^{-1/2} [1 - 0.5x(2 - x)] dx

Expand [1 - 0.5x(2 - x)] = 1 - x + 0.5x²

So the integrand is x^{-1/2} (2 - x)^{-1/2} (1 - x + 0.5x²)

Then, splitting into three terms:

Term1: x^{-1/2} (2 - x)^{-1/2} * 1

Term2: x^{-1/2} (2 - x)^{-1/2} * (-x)

Term3: x^{-1/2} (2 - x)^{-1/2} * 0.5x²

So the integral is:

∫ Term1 dx - ∫ Term2 dx + 0.5 ∫ Term3 dx

But Term2 is -x * x^{-1/2} (2 - x)^{-1/2} = -x^{1/2} (2 - x)^{-1/2}

Term3 is 0.5x² * x^{-1/2} (2 - x)^{-1/2} = 0.5 x^{3/2} (2 - x)^{-1/2}

So the integrals are:

I1 = ∫ x^{-1/2} (2 - x)^{-1/2} dx from 0 to 2 = π

I2 = ∫ x^{1/2} (2 - x)^{-1/2} dx from 0 to 2 = π

I3 = ∫ x^{3/2} (2 - x)^{-1/2} dx from 0 to 2 = 3π/4

Therefore, the original integral is:

I1 - I2 + 0.5 I3 = π - π + 0.5*(3π/4) = 0 + 3π/8 = 3π/8 ≈ 1.1780972451

But this contradicts the substitution method which gave 3π/4. So there's a mistake here. But where?

Wait, no. Wait, in the substitution method, after changing variables to t = x/2, the integral became:

∫₀¹ t^{-1/2} (1 - t)^{-1/2} [1 - 2t + 2t²] dt

Which is:

B(1/2,1/2) - 2 B(3/2,1/2) + 2 B(5/2,1/2) = π - 2*(π/2) + 2*(3π/8) = π - π + 3π/4 = 3π/4

But according to the first method, splitting into three integrals, the result is 3π/8. So which is correct?

Wait, but when we did the substitution x = 2t, the integral became:

∫₀¹ t^{-1/2} (1 - t)^{-1/2} [1 - 2t + 2t²] dt

Which is the same as:

∫₀¹ t^{-1/2} (1 - t)^{-1/2} dt - 2 ∫₀¹ t^{1/2} (1 - t)^{-1/2} dt + 2 ∫₀¹ t^{3/2} (1 - t)^{-1/2} dt

Which is:

B(1/2,1/2) - 2 B(3/2,1/2) + 2 B(5/2,1/2) = π - 2*(π/2) + 2*(3π/8) = π - π + 3π/4 = 3π/4

But according to the first method, when we split the original integral into three parts, we had:

I1 = ∫₀² x^{-1/2}(2 - x)^{-1/2} dx = π

I2 = ∫₀² x^{1/2}(2 - x)^{-1/2} dx = π

I3 = ∫₀² x^{3/2}(2 - x)^{-1/2} dx = 3π/4

Then the original integral is I1 - I2 + 0.5 I3 = π - π + 0.5*(3π/4) = 3π/8

But according to the substitution method, the integral is 3π/4. So there's a contradiction. Therefore, one of the methods is wrong.

But the substitution method seems more reliable because it's a single substitution leading to a result. Let's check the first method again.

Wait, in the first method, when we split the integral into three parts, the coefficients are:

1 * I1 - 1 * I2 + 0.5 * I3

But according to the substitution method, the integral is:

I1 - 2 I2 + 2 I3, where I1, I2, I3 are the Beta functions in terms of t. Wait, no. Wait, in the substitution method, after substitution, the integral became:

B(1/2,1/2) - 2 B(3/2,1/2) + 2 B(5/2,1/2)

Which is π - 2*(π/2) + 2*(3π/8) = 3π/4

But in the first method, the coefficients are 1, -1, 0.5. So there's a discrepancy in the coefficients. Therefore, the mistake must be in the first method.

Ah! I see now. When we expanded [1 - 0.5x(2 - x)] to 1 - x + 0.5x², that's correct. But when we split the integral into three parts, the coefficients are 1, -1, and 0.5. However, when we computed I3, which is the integral of x^{3/2}(2 - x)^{-1/2} dx, we found that to be 3π/4. But in the substitution method, the coefficient for the third term is +2, not +0.5. So where is the mistake?

Wait, no. The substitution method shows that the integral is:

∫₀² x^{-1/2}(2 - x)^{-1/2} [1 - 0.5x(2 - x)] dx = 3π/4

But according to the first method, splitting into three integrals gives 3π/8. Therefore, the first method must have an error.

Let me check the first method again.

Original integrand: x^{-1/2}(2 - x)^{-1/2} [1 - 0.5x(2 - x)] = x^{-1/2}(2 - x)^{-1/2} (1 - x + 0.5x²)

Split into three terms:

Term1: x^{-1/2}(2 - x)^{-1/2}

Term2: -x^{1/2}(2 - x)^{-1/2}

Term3: 0.5x^{3/2}(2 - x)^{-1/2}

Integrate each term from 0 to 2:

I1 = ∫ Term1 dx = π

I2 = ∫ Term2 dx = -π

I3 = ∫ Term3 dx = 0.5 * 3π/4 = 3π/8

Wait, no. Wait, Term3 is 0.5x^{3/2}(2 - x)^{-1/2}, so the integral of Term3 is 0.5 * ∫ x^{3/2}(2 - x)^{-1/2} dx. But in the first calculation, we found that ∫ x^{3/2}(2 - x)^{-1/2} dx from 0 to 2 is 3π/4. Therefore, the integral of Term3 is 0.5 * 3π/4 = 3π/8.

So the total integral is I1 + I2 + I3 = π - π + 3π/8 = 3π/8.

But according to the substitution method, the correct answer is 3π/4. Therefore, there's a mistake in the first method. But why?

Ah! I think I made a mistake in the substitution for the third integral. Let me recheck the third integral.

Third integral: ∫₀² x^{3/2}(2 - x)^{-1/2} dx

Substitution x = 2t, dx = 2dt. Then:

x^{3/2} = (2t)^{3/2} = 2^{3/2} t^{3/2}

(2 - x)^{-1/2} = (2 - 2t)^{-1/2} = 2^{-1/2}(1 - t)^{-1/2}

So the terms together: 2^{3/2} * 2^{-1/2} = 2^{1} = 2. So 2 * t^{3/2}(1 - t)^{-1/2}

Multiply by dx = 2dt: 2 * 2 * t^{3/2}(1 - t)^{-1/2} dt = 4 t^{3/2}(1 - t)^{-1/2} dt

Therefore, the integral becomes 4 ∫₀¹ t^{3/2}(1 - t)^{-1/2} dt = 4 B(5/2,1/2)

B(5/2,1/2) = Γ(5/2)Γ(1/2)/Γ(3) = (3/4 √π)(√π)/2 = 3π/8

So 4 * 3π/8 = 3π/2

Wait, the integral of x^{3/2}(2 - x)^{-1/2} dx from 0 to 2 is 3π/2. Therefore, the third term, which is 0.5 times this integral, is 0.5 * 3π/2 = 3π/4.

Therefore, the original integral is I1 - I2 + 0.5 I3 = π - π + 3π/4 = 3π/4.

Ah! So the mistake in the first method was in the calculation of I3. Earlier, I incorrectly calculated I3 as 3π/4, but in reality, the integral of x^{3/2}(2 - x)^{-1/2} dx is 3π/2, so 0.5 times that is 3π/4. Therefore, the correct result is 3π/4.

So where did I go wrong earlier? Let me check.

In the first calculation of I3, I think I made a mistake in the substitution step. Let me redo it.

Third integral: I3 = ∫₀² x^{3/2}(2 - x)^{-1/2} dx

Substitute x = 2t, dx = 2dt. Then:

I3 = ∫₀¹ (2t)^{3/2} (2 - 2t)^{-1/2} * 2 dt

= ∫₀¹ 2^{3/2} t^{3/2} * 2^{-1/2} (1 - t)^{-1/2} * 2 dt

= 2^{3/2} * 2^{-1/2} * 2 ∫₀¹ t^{3/2} (1 - t)^{-1/2} dt

= 2^{ (3/2 - 1/2 + 1) } ∫₀¹ t^{3/2} (1 - t)^{-1/2} dt

Wait, 2^{3/2} * 2^{-1/2} = 2^{1)} = 2. Then multiplied by 2 gives 4.

So I3 = 4 ∫₀¹ t^{3/2} (1 - t)^{-1/2} dt = 4 B(5/2,1/2)

B(5/2,1/2) = Γ(5/2)Γ(1/2)/Γ(3) = (3/2 * 1/2 * √π) * √π / 2! = (3/4 π) / 2 = 3π/8

Therefore, I3 = 4 * 3π/8 = 3π/2

Therefore, the third term in the original integral is 0.5 * I3 = 0.5 * 3π/2 = 3π/4

Therefore, the original integral is π - π + 3π/4 = 3π/4, which matches the substitution method.

So the mistake in the first approach was miscalculating I3. Initially, I thought I3 was 3π/4, but it's actually 3π/2, leading to 0.5 * 3π/2 = 3π/4.

Therefore, the correct exact answer is 3π/4, and the numerical approximation is approximately 2.3561944902.

But wait, this contradicts the previous numerical approximation. Wait, 3π/4 is approximately 3*3.141592653589793/4 ≈ 2.356194490192345. Rounded to 10 decimal places, that's 2.3561944902.

But earlier, when I thought the answer was 3π/8, the numerical value was ~1.178, but after correcting the mistake, it's 3π/4 ≈ 2.356.

So the correct answer is 3π/4.

Therefore, the initial mistake was in the calculation of I3. The correct value of the integral is 3π/4.

So the final answer is 3π/4, and the numerical approximation is approximately 2.3561944902.
</think>

{"answer": "\\frac{3\\pi}{4}", "numerical_answer": "2.3561944902"}