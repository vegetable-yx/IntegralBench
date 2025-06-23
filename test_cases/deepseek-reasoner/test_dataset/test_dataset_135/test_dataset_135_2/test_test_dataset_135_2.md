<think>
Okay, let's see. I need to compute the definite integral from 0 to 2 of x^(-1/2) times (2 - x)^(-1/2) times [1 - 0.5x(2 - x)] dx. Hmm, that looks a bit complicated, but maybe there's a substitution or a beta function involved here. Let me start by simplifying the integrand.

First, let's write the integral out again to make sure I have it right:

∫₀² x^(-1/2) (2 - x)^(-1/2) [1 - 0.5x(2 - x)] dx

Let me simplify the expression inside the brackets first. The term 0.5x(2 - x) can be expanded. Let's compute that:

0.5x(2 - x) = 0.5*(2x - x²) = x - 0.5x²

So, 1 - 0.5x(2 - x) = 1 - x + 0.5x². Wait, is that right? Let me check:

Wait, 0.5x(2 - x) is 0.5*2x - 0.5x² = x - 0.5x². So subtracting that from 1 gives 1 - x + 0.5x². Yes, that's correct.

So the integrand becomes x^(-1/2) (2 - x)^(-1/2) times (1 - x + 0.5x²). Hmm. Maybe I can split this into separate terms. Let's see:

x^(-1/2)(2 - x)^(-1/2) * 1 - x^(-1/2)(2 - x)^(-1/2) * x + 0.5x^(-1/2)(2 - x)^(-1/2) *x²

So, breaking the integral into three parts:

I = ∫₀² x^(-1/2)(2 - x)^(-1/2) dx - ∫₀² x^(1/2)(2 - x)^(-1/2) dx + 0.5 ∫₀² x^(3/2)(2 - x)^(-1/2) dx

Now, these integrals look like Beta functions or related to the Beta function. The Beta function is defined as B(a,b) = 2∫₀^(π/2) (sinθ)^(2a-1)(cosθ)^(2b-1) dθ, but also in terms of the Gamma function, B(a,b) = Γ(a)Γ(b)/Γ(a+b). Alternatively, the integral from 0 to 1 of t^{c-1}(1 - t)^{d - c -1} dt is related to Beta function as well. Wait, but here the limits are from 0 to 2, and the integrand has x and (2 - x). Maybe a substitution to make the interval from 0 to 1?

Let me try substitution. Let’s set t = x/2, so x = 2t, dx = 2dt. Then when x=0, t=0; x=2, t=1. Let's substitute:

First integral: ∫₀² x^(-1/2)(2 - x)^(-1/2) dx becomes ∫₀¹ (2t)^(-1/2)(2 - 2t)^(-1/2) * 2 dt

Simplify each term:

(2t)^(-1/2) = (2)^(-1/2) t^(-1/2)

(2 - 2t)^(-1/2) = (2(1 - t))^(-1/2) = 2^(-1/2)(1 - t)^(-1/2)

Multiply them together: 2^(-1/2) * 2^(-1/2) = 2^(-1), and t^(-1/2)(1 - t)^(-1/2). Then multiply by 2 dt:

So total factor is 2^(-1) * 2 = 1. So the first integral becomes ∫₀¹ t^(-1/2)(1 - t)^(-1/2) dt. That's the Beta function B(1/2, 1/2), which is Γ(1/2)Γ(1/2)/Γ(1) = π / 1 = π. So first integral is π.

Wait, but let me confirm. The Beta function B(a,b) is ∫₀¹ t^{a-1}(1 - t)^{b -1} dt. So here, a = 1/2, b = 1/2. So B(1/2,1/2) = π. So yes, first integral is π.

Now, the second integral: ∫₀² x^(1/2)(2 - x)^(-1/2) dx. Let's apply the same substitution t = x/2, x = 2t, dx = 2dt. Then x^(1/2) = (2t)^(1/2) = 2^(1/2) t^(1/2), and (2 - x)^(-1/2) = (2 - 2t)^(-1/2) = 2^(-1/2)(1 - t)^(-1/2). So multiplying these:

2^(1/2) t^(1/2) * 2^(-1/2) (1 - t)^(-1/2) = t^(1/2)(1 - t)^(-1/2). Then multiply by dx = 2dt:

So the integral becomes 2 ∫₀¹ t^(1/2)(1 - t)^(-1/2) dt. That's 2 * B(3/2, 1/2). Let's compute B(3/2,1/2) = Γ(3/2)Γ(1/2)/Γ(2). Γ(3/2) is (1/2)√π, Γ(1/2) is √π, Γ(2) is 1! = 1. So B(3/2,1/2) = (1/2 √π)(√π)/1 = (1/2) π. Therefore, the integral is 2 * (1/2) π = π. So the second integral is π.

Third integral: 0.5 ∫₀² x^(3/2)(2 - x)^(-1/2) dx. Again, substitution t = x/2, x = 2t, dx = 2dt. Then x^(3/2) = (2t)^(3/2) = 2^(3/2) t^(3/2), (2 - x)^(-1/2) = 2^(-1/2)(1 - t)^(-1/2). Multiply these:

2^(3/2) t^(3/2) * 2^(-1/2) (1 - t)^(-1/2) = 2^(1) t^(3/2)(1 - t)^(-1/2) = 2 t^(3/2)(1 - t)^(-1/2). Then multiply by dx = 2dt:

So the integral becomes 0.5 * 2 * 2 ∫₀¹ t^(3/2)(1 - t)^(-1/2) dt. Let's compute the constants: 0.5 * 2 * 2 = 2. So 2 ∫₀¹ t^(3/2)(1 - t)^(-1/2) dt. That's 2 * B(5/2, 1/2). Compute B(5/2,1/2) = Γ(5/2)Γ(1/2)/Γ(3). Γ(5/2) is (3/2)(1/2)√π = (3/4)√π. Γ(1/2) is √π. Γ(3) is 2! = 2. So B(5/2,1/2) = (3/4 √π)(√π)/2 = (3/4 * π)/2 = 3π/8. Therefore, the third integral is 2 * 3π/8 = 3π/4.

Putting it all together:

I = π - π + 0.5*(3π/4) ?

Wait, wait. Wait, the integral was split into three parts:

I = first integral - second integral + 0.5*third integral.

Wait, no. Wait, original split was:

I = ∫ [1 - x + 0.5x²] x^{-1/2}(2 - x)^{-1/2} dx = ∫ x^{-1/2}(2 - x)^{-1/2} dx - ∫ x^{1/2}(2 - x)^{-1/2} dx + 0.5 ∫ x^{3/2}(2 - x)^{-1/2} dx.

So, substituting the results:

First integral: π

Second integral: π

Third integral: 3π/4

So I = π - π + 0.5*(3π/4) = 0 + (3π/8) = 3π/8.

Wait, that seems too straightforward. Let me check again.

First integral: π

Second integral: π

Third integral: 3π/4

So the original expression is I = first - second + 0.5*third

So that's π - π + 0.5*(3π/4) = 0 + (3π/8) = 3π/8.

So the exact answer is 3π/8. Let me verify this again step by step.

First integral: yes, substitution gives B(1/2,1/2) = π.

Second integral: substitution gives 2*B(3/2,1/2) = 2*( (Γ(3/2)Γ(1/2))/Γ(2) ) = 2*( ( (1/2)√π * √π ) / 1 ) = 2*( (1/2)π ) = π. Correct.

Third integral: substitution gives 2*B(5/2,1/2) = 2*( (Γ(5/2)Γ(1/2))/Γ(3) ) = 2*( ( (3/2)(1/2)√π * √π ) / 2 ) = 2*( (3/4 π ) / 2 ) = 2*(3π/8) = 3π/4. Wait, but the third integral is 0.5 times the third integral. Wait, no. Wait, the original integral was 0.5 times the third integral. Let me check:

Original third integral: 0.5 ∫ x^{3/2}(2 - x)^{-1/2} dx. After substitution, we found that integral (without the 0.5) is 3π/4. So 0.5 times that is 3π/8.

So putting it all together:

I = π (first) - π (second) + 3π/8 (third) = 0 + 3π/8 = 3π/8.

Yes, that seems correct.

So the exact answer is 3π/8. Now, the numerical approximation. Let's approximate 3π/8. π is approximately 3.141592653589793. So 3π ≈ 9.42477796077, divided by 8 gives approximately 1.1780972450961724. Rounded to 10 decimal places: 1.1780972451.

Wait, let me compute it more precisely. Let's take π to more decimal places. π ≈ 3.1415926535897932384626433832795. So 3π = 9.4247779607693797153879301498385. Divided by 8: 9.4247779607693797153879301498385 / 8 = 1.1780972450961724644234912687298. So rounded to 10 decimal places: 1.1780972451.

Therefore, the exact answer is 3π/8, and the approximation is approximately 1.1780972451.

I think that's it. Let me just check if there's another way to confirm this result. Maybe using substitution or recognizing the integral as a Beta function from the start.

Alternatively, the original integrand is x^{-1/2}(2 - x)^{-1/2}[1 - 0.5x(2 - x)]. Let me see if there's a substitution that can simplify this. Let’s set t = x/2, but maybe not. Alternatively, let’s set u = x -1, but perhaps not. Alternatively, since the integral is from 0 to 2, and the integrand has x and 2 - x, which suggests symmetry around x=1. Let me check if the substitution x = 2 sin²θ or something like that.

Let’s try x = 2 sin²θ. Then dx = 4 sinθ cosθ dθ. When x=0, θ=0; x=2, θ=π/2.

Then x^{-1/2} = (2 sin²θ)^{-1/2} = (2)^{-1/2} (sinθ)^{-1}

(2 - x)^{-1/2} = (2 - 2 sin²θ)^{-1/2} = (2 cos²θ)^{-1/2} = (2)^{-1/2} (cosθ)^{-1}

So x^{-1/2}(2 - x)^{-1/2} dx becomes (2^{-1/2} sin^{-1}θ)(2^{-1/2} cos^{-1}θ) * 4 sinθ cosθ dθ = (2^{-1}) * 4 * (sinθ cosθ)^{-1} * sinθ cosθ dθ = (2^{-1} *4) dθ = 2 dθ.

So the integral becomes ∫0^{π/2} 2 [1 - 0.5x(2 - x)] dθ. Now, compute 0.5x(2 - x):

x = 2 sin²θ, so 0.5x(2 - x) = 0.5*2 sin²θ*(2 - 2 sin²θ) = sin²θ*(2 cos²θ) = 2 sin²θ cos²θ.

So 1 - 0.5x(2 - x) = 1 - 2 sin²θ cos²θ.

Therefore, the integral becomes ∫0^{π/2} 2 [1 - 2 sin²θ cos²θ] dθ = 2 ∫0^{π/2} [1 - 2 sin²θ cos²θ] dθ.

Let me compute this integral. First, split into two parts:

2 [ ∫0^{π/2} 1 dθ - 2 ∫0^{π/2} sin²θ cos²θ dθ ]

Compute the first integral: ∫0^{π/2} 1 dθ = π/2.

Second integral: ∫0^{π/2} sin²θ cos²θ dθ. Let's use power-reduction identities. Recall that sin²θ = (1 - cos2θ)/2, cos²θ = (1 + cos2θ)/2. So sin²θ cos²θ = [(1 - cos2θ)/2][(1 + cos2θ)/2] = (1 - cos²2θ)/4 = (sin²2θ)/4.

So ∫ sin²θ cos²θ dθ = 1/4 ∫ sin²2θ dθ. Let’s substitute φ = 2θ, dφ = 2 dθ, limits from 0 to π. Then integral becomes 1/4 * 1/2 ∫0^π sin²φ dφ = 1/8 ∫0^π sin²φ dφ. The integral of sin²φ over 0 to π is π/2. So this becomes 1/8 * π/2 = π/16.

Therefore, the second integral is π/16. So putting it all together:

2 [ π/2 - 2*(π/16) ] = 2 [ π/2 - π/8 ] = 2 [ (4π/8 - π/8) ] = 2*(3π/8) = 6π/8 = 3π/4. Wait, that contradicts the previous result. Wait, this can't be. Wait, what's happening here?

Wait, no. Wait, according to this substitution method, the integral is 3π/4, but earlier we had 3π/8. There's a discrepancy. That means I made a mistake somewhere.

Wait, let's check the substitution approach again. Let me go through it step by step.

Original integral: ∫₀² x^{-1/2}(2 - x)^{-1/2}[1 - 0.5x(2 - x)] dx.

Substitution x = 2 sin²θ, dx = 4 sinθ cosθ dθ. Then x^{-1/2} = (2 sin²θ)^{-1/2} = 2^{-1/2} sin^{-1}θ, (2 - x)^{-1/2} = (2 cos²θ)^{-1/2} = 2^{-1/2} cos^{-1}θ. So x^{-1/2}(2 - x)^{-1/2} dx = 2^{-1} * 4 sinθ cosθ dθ / (sinθ cosθ) ) = 2^{-1} *4 dθ = 2 dθ. Correct.

Then, the integrand becomes 2 [1 - 0.5x(2 - x)] dθ. Compute 0.5x(2 - x):

x = 2 sin²θ, so 0.5x(2 - x) = 0.5*2 sin²θ*(2 - 2 sin²θ) = sin²θ*(2 - 2 sin²θ) = 2 sin²θ - 2 sin⁴θ. Wait, no:

Wait, 0.5x(2 - x) = 0.5*(2 sin²θ)*(2 - 2 sin²θ) = 0.5*2 sin²θ*2(1 - sin²θ) = 2 sin²θ*(1 - sin²θ) = 2 sin²θ cos²θ. Yes, that's correct.

So 1 - 0.5x(2 - x) = 1 - 2 sin²θ cos²θ. Therefore, the integral becomes 2*(1 - 2 sin²θ cos²θ) dθ integrated from 0 to π/2.

So expanding, 2*∫(1 dθ) - 4*∫ sin²θ cos²θ dθ.

First integral: 2*(π/2) = π.

Second integral: 4*∫ sin²θ cos²θ dθ from 0 to π/2. As before, sin²θ cos²θ = (sin²2θ)/4. So ∫ sin²θ cos²θ dθ = 1/4 ∫ sin²2θ dθ. Let’s compute ∫0^{π/2} sin²2θ dθ. Let’s set φ = 2θ, so when θ=0, φ=0; θ=π/2, φ=π. Then dφ = 2 dθ, so dθ = dφ/2. The integral becomes ∫0^π sin²φ*(dφ/2) = (1/2) ∫0^π sin²φ dφ. The integral of sin²φ over 0 to π is π/2. So this becomes (1/2)*(π/2) = π/4. Therefore, ∫0^{π/2} sin²θ cos²θ dθ = 1/4 * π/4 = π/16.

Therefore, the second integral is 4*(π/16) = π/4.

So the total integral is π - π/4 = 3π/4. Wait, but this contradicts the previous result of 3π/8. So now I'm confused. Which one is correct?

Wait, this substitution method gives 3π/4, but the previous method of splitting into three integrals gave 3π/8. There's a mistake somewhere. Let me check the first method again.

First method:

Original integral split into three parts:

I = ∫ x^{-1/2}(2 - x)^{-1/2} dx - ∫ x^{1/2}(2 - x)^{-1/2} dx + 0.5 ∫ x^{3/2}(2 - x)^{-1/2} dx.

Computed first integral as π, second as π, third as 3π/4. Then I = π - π + 0.5*(3π/4) = 3π/8.

But substitution method gives 3π/4. So there's a discrepancy. Which one is correct?

Let me check the substitution method again. Let's compute the integral numerically to see which is correct.

Let me compute the integral numerically. The integrand is x^{-1/2}(2 - x)^{-1/2}[1 - 0.5x(2 - x)] from 0 to 2.

But integrating from 0 to 2, but at x=0 and x=2, the integrand has singularities. However, the integral is convergent because the exponents are -1/2, which are integrable.

Let me approximate the integral numerically. Let's use substitution x = 2 sin²θ, which transforms the integral to 2 ∫0^{π/2} [1 - 2 sin²θ cos²θ] dθ. Which we computed as 3π/4 ≈ 2.356194490192345.

But according to the first method, it's 3π/8 ≈ 1.1780972451. These are different by a factor of 2. So one of the methods is wrong.

Wait, but substitution method gives 3π/4, which is approximately 2.356, but the numerical approximation I did earlier was 1.178, which is half of that. So there's a mistake in one of the methods.

Let me check the substitution method again. Let's compute the integral numerically using substitution.

Wait, after substitution, the integral becomes 2 ∫0^{π/2} [1 - 2 sin²θ cos²θ] dθ. Let's compute this integral.

First, compute ∫0^{π/2} 1 dθ = π/2 ≈ 1.5708.

Then compute ∫0^{π/2} 2 sin²θ cos²θ dθ. Let's compute sin²θ cos²θ = (sin2θ)^2 /4. So ∫0^{π/2} (sin2θ)^2 /4 dθ. Let’s make substitution φ=2θ, dφ=2dθ, limits from 0 to π. Then integral becomes ∫0^π (sinφ)^2 /4 * dφ/2 = 1/8 ∫0^π sin²φ dφ. The integral of sin²φ from 0 to π is π/2. So this becomes 1/8 * π/2 = π/16 ≈ 0.19635.

Therefore, the integral becomes 2*(π/2 - 2*(π/16)) = 2*(π/2 - π/8) = 2*(3π/8) = 3π/4 ≈ 2.356194490192345.

But according to the first method, the answer is 3π/8 ≈ 1.1780972451. So which is correct?

Let me compute the integral numerically using numerical integration. Let's pick a numerical value. Let's use x=1. The integrand at x=1 is 1^{-1/2}*(2 -1)^{-1/2}*[1 -0.5*1*(2-1)] = 1*1*[1 -0.5*1*1] = 1*(0.5) = 0.5. So the integrand at x=1 is 0.5.

But the function x^{-1/2}(2 -x)^{-1/2} is symmetric around x=1. Let's check another point, say x=0.5. Then integrand is (0.5)^{-1/2}*(1.5)^{-1/2}*[1 -0.5*0.5*1.5] = sqrt(2) * sqrt(2/3) * [1 - 0.375] = sqrt(4/3) * 0.625 ≈ (1.1547) * 0.625 ≈ 0.7217.

Similarly, x=0.25: integrand is (0.25)^{-1/2}*(1.75)^{-1/2}*[1 -0.5*0.25*1.75] = 2 * (1.75)^{-1/2} * [1 - 0.21875] = 2*(approx 0.7559) * 0.78125 ≈ 2*0.7559*0.78125 ≈ 1.1837.

So the integrand is positive over the interval, and the integral should be around 1.178 or 2.356. Let's approximate numerically using a simple method. Let's use the substitution x = 2t, so t from 0 to 1. Then the integral becomes ∫₀¹ (2t)^{-1/2}(2 - 2t)^{-1/2}[1 -0.5*(2t)(2 - 2t)] *2 dt.

Simplify:

(2t)^{-1/2} = (2)^{-1/2} t^{-1/2}

(2 - 2t)^{-1/2} = (2(1 - t))^{-1/2} = 2^{-1/2}(1 - t)^{-1/2}

So together: 2^{-1} t^{-1/2}(1 - t)^{-1/2}

The bracket term: 1 -0.5*(2t)(2 - 2t) = 1 -0.5*(4t -4t²) = 1 -2t + 2t²

Multiply by 2 dt: 2*2^{-1} t^{-1/2}(1 - t)^{-1/2} [1 -2t + 2t²] dt = t^{-1/2}(1 - t)^{-1/2} [1 -2t + 2t²] dt.

So the integral becomes ∫₀¹ t^{-1/2}(1 - t)^{-1/2}(1 -2t + 2t²) dt.

This can be split into three integrals:

∫ t^{-1/2}(1 - t)^{-1/2} dt - 2 ∫ t^{1/2}(1 - t)^{-1/2} dt + 2 ∫ t^{3/2}(1 - t)^{-1/2} dt.

These are Beta functions:

First integral: B(1/2,1/2) = π

Second integral: 2*B(3/2,1/2) = 2*(Γ(3/2)Γ(1/2)/Γ(2)) = 2*( (1/2)√π * √π /1 ) = 2*(π/2) = π

Third integral: 2*B(5/2,1/2) = 2*(Γ(5/2)Γ(1/2))/Γ(3)) = 2*( (3/4)√π * √π /2 ) = 2*(3π/8) = 3π/4

So the integral becomes π - 2*(π) + 2*(3π/4) = π - 2π + 3π/2 = (1 -2 + 1.5)π = 0.5π ≈ 1.5708. Wait, this contradicts both previous results. Now I'm really confused.

Wait, this is the same integral as before, but after substitution, we have:

∫₀¹ t^{-1/2}(1 - t)^{-1/2}(1 -2t + 2t²) dt = π - 2π + 3π/2 = 0.5π. So this is π/2 ≈ 1.5708.

But this contradicts both previous results. What's going on here?

Wait, this is the same integral as the original, but after substitution, we have different expressions. Let me check the algebra again.

Original integral after substitution:

∫₀¹ t^{-1/2}(1 - t)^{-1/2}(1 -2t + 2t²) dt.

Split into three integrals:

I1 = ∫ t^{-1/2}(1 - t)^{-1/2} dt = B(1/2,1/2) = π

I2 = -2 t^{1/2}(1 - t)^{-1/2} dt = -2 B(3/2,1/2) = -2*(π/2) = -π

I3 = 2 ∫ t^{3/2}(1 - t)^{-1/2} dt = 2 B(5/2,1/2) = 2*(3π/8) = 3π/4

So total integral: π - π + 3π/4 = 3π/4 ≈ 2.356.

Wait, but this contradicts the previous calculation where after substitution, the integral became 3π/4. But according to this split, it's 3π/4. But earlier, when we split the original integrals, we had 3π/8. So where is the mistake?

Wait, the original integral after substitution was:

∫₀² x^{-1/2}(2 - x)^{-1/2}[1 -0.5x(2 -x)] dx = ∫₀¹ t^{-1/2}(1 - t)^{-1/2}(1 -2t + 2t²) dt.

But when we split this into three integrals:

I1 = ∫ t^{-1/2}(1 - t)^{-1/2} dt = π

I2 = -2 ∫ t^{1/2}(1 - t)^{-1/2} dt = -2 * B(3/2,1/2) = -2*(π/2) = -π

I3 = 2 ∫ t^{3/2}(1 - t)^{-1/2} dt = 2 * B(5/2,1/2) = 2*(3π/8) = 3π/4

So total integral: π - π + 3π/4 = 3π/4. So this suggests that the correct answer is 3π/4, which is approximately 2.356194490192345.

But earlier, when we split the original integral into three parts, we had:

I = π - π + 0.5*(3π/4) = 3π/8. So where is the mistake?

Ah! I think I made a mistake in the first method when splitting the original integral. Let me go back to the first method.

Original integral:

I = ∫₀² x^{-1/2}(2 - x)^{-1/2} [1 -0.5x(2 -x)] dx.

Expanding the bracket: 1 -0.5x(2 -x) = 1 -x +0.5x².

So I = ∫ x^{-1/2}(2 -x)^{-1/2} dx - ∫ x^{1/2}(2 -x)^{-1/2} dx + 0.5 ∫ x^{3/2}(2 -x)^{-1/2} dx.

First integral: π

Second integral: π

Third integral: 3π/4

So I = π - π + 0.5*(3π/4) = 0 + 3π/8 = 3π/8.

But according to substitution method, after substitution, the integral is 3π/4. So there's a contradiction. The mistake must be in the first method.

Wait, let's check the third integral again. The third integral is 0.5 ∫ x^{3/2}(2 -x)^{-1/2} dx. After substitution t = x/2, we found that this integral is 0.5 * 3π/4 = 3π/8. But according to the substitution method, the entire integral is 3π/4. So where is the error?

Wait, perhaps the mistake is in the substitution method. Let me check the substitution method again.

Original integral after substitution x = 2t:

I = ∫₀¹ t^{-1/2}(1 - t)^{-1/2}(1 -2t + 2t²) dt.

But expanding this, it's:

∫ t^{-1/2}(1 - t)^{-1/2} dt - 2 ∫ t^{1/2}(1 - t)^{-1/2} dt + 2 ∫ t^{3/2}(1 - t)^{-1/2} dt.

Which is I1 - 2I2 + 2I3.

But in the first method, the original split was:

I = I1 - I2 + 0.5 I3.

Wait, no. Wait, the original integrand after expansion is 1 -0.5x(2 -x) = 1 -x +0.5x². So when multiplied by x^{-1/2}(2 -x)^{-1/2}, the integral becomes:

∫ x^{-1/2}(2 -x)^{-1/2} dx - ∫ x^{1/2}(2 -x)^{-1/2} dx + 0.5 ∫ x^{3/2}(2 -x)^{-1/2} dx.

But in the substitution method, after substitution, the integrand becomes:

1 -2t + 2t², which corresponds to 1 -2*(x/2) + 2*(x/2)^2 = 1 -x + 0.5x². So that's correct.

But when we do the substitution, the integral becomes:

∫ t^{-1/2}(1 - t)^{-1/2}(1 -2t + 2t²) dt = I1 - 2I2 + 2I3.

But in the first method, the split was I1 - I2 + 0.5 I3. So there's a discrepancy in the coefficients of the integrals. The substitution method shows that the coefficients are 1, -2, +2, but the first method had coefficients 1, -1, +0.5. Therefore, the first method was incorrect in the coefficients.

Ah! Here's the mistake. When expanding 1 -0.5x(2 -x), we have 1 -x +0.5x². But when we split the integral, the coefficients are:

∫ [1 -x +0.5x²] x^{-1/2}(2 -x)^{-1/2} dx = ∫ x^{-1/2}(2 -x)^{-1/2} dx - ∫ x^{1/2}(2 -x)^{-1/2} dx + 0.5 ∫ x^{3/2}(2 -x)^{-1/2} dx.

But in the substitution method, after substitution, the integrand is 1 -2t + 2t², which corresponds to 1 -x +0.5x². So the coefficients of the integrals after substitution are 1, -2, +2. But in the first method, the coefficients are 1, -1, +0.5. Therefore, the first method incorrectly split the coefficients. The error is in the expansion of 0.5x(2 -x).

Wait, let's re-examine the expansion:

Original expression: 1 -0.5x(2 -x).

Compute 0.5x(2 -x):

0.5x*(2) -0.5x*x = x -0.5x².

So 1 -0.5x(2 -x) = 1 -x +0.5x². Correct.

So when we split the integral, it's:

∫ [1 -x +0.5x²] x^{-1/2}(2 -x)^{-1/2} dx = ∫ x^{-1/2}(2 -x)^{-1/2} dx - ∫ x^{1/2}(2 -x)^{-1/2} dx + 0.5 ∫ x^{3/2}(2 -x)^{-1/2} dx.

But in the substitution method, after substitution, the integrand becomes 1 -2t + 2t², which is 1 -2*(x/2) + 2*(x/2)^2 = 1 -x +0.5x². So the coefficients are correct.

But when we split the integral in the substitution method, we have:

I = I1 - 2I2 + 2I3.

But in the first method, it's I1 - I2 + 0.5I3. So there's a discrepancy. Therefore, the first method is wrong. The mistake must be in the first method's coefficients.

Wait, no. Let me check the substitution again. When we substitute x = 2t, then x = 2t, so x^{1/2} = sqrt(2t), and x^{3/2} = (2t)^{3/2} = 2^{3/2} t^{3/2}. But in the first method, when we split the integral, the coefficients are:

- ∫ x^{1/2}(2 -x)^{-1/2} dx. After substitution, this becomes - ∫ (2t)^{1/2} (2 -2t)^{-1/2} *2 dt = - ∫ 2^{1/2} t^{1/2} * 2^{-1/2}(1 -t)^{-1/2} *2 dt = - ∫ 2^{1/2 -1/2 +1} t^{1/2}(1 -t)^{-1/2} dt = - ∫ 2^{1} t^{1/2}(1 -t)^{-1/2} dt = -2 ∫ t^{1/2}(1 -t)^{-1/2} dt = -2 B(3/2,1/2) = -2*(π/2) = -π.

Similarly, the third integral in the first method is 0.5 ∫ x^{3/2}(2 -x)^{-1/2} dx. After substitution, this is 0.5 ∫ (2t)^{3/2}(2 -2t)^{-1/2} *2 dt = 0.5 * 2^{3/2} t^{3/2} * 2^{-1/2}(1 -t)^{-1/2} *2 dt = 0.5 * 2^{3/2 -1/2 +1} t^{3/2}(1 -t)^{-1/2} dt = 0.5 * 2^{2} ∫ t^{3/2}(1 -t)^{-1/2} dt = 0.5*4*B(5/2,1/2) = 2*(3π/8) = 3π/4.

So the first method's third integral is 3π/4. But according to the substitution method, the entire integral is I1 -2I2 +2I3 = π -2*(π/2) +2*(3π/8) = π -π + 3π/4 = 3π/4. So the first method's split is incorrect. The first method's split should have coefficients 1, -1, +0.5, but according to substitution, the coefficients are 1, -2, +2. Therefore, the first method's expansion is incorrect.

Wait, but the expansion of 1 -x +0.5x² is correct. So why the discrepancy?

Ah! Because when we split the integral, the coefficients are:

∫ [1 -x +0.5x²] x^{-1/2}(2 -x)^{-1/2} dx = ∫ x^{-1/2}(2 -x)^{-1/2} dx - ∫ x^{1/2}(2 -x)^{-1/2} dx + 0.5 ∫ x^{3/2}(2 -x)^{-1/2} dx.

But when we substitute x = 2t, the coefficients of the integrals change. For example, the term -x in the integrand becomes -2t, and 0.5x² becomes 0.5*(4t²) = 2t². So when we substitute, the integrand becomes 1 -2t +2t², which when integrated over t from 0 to1, gives the same as the original integral. But when we split the original integrals, the coefficients are different. So the mistake is that in the first method, the coefficients after substitution are not correctly accounted for.

Wait, no. The first method is correct in terms of the original variables. The substitution method is also correct. But the results are different. This suggests that there's a mistake in one of the methods.

But according to substitution method, the integral is 3π/4, and according to the first method, it's 3π/8. But when we compute the integral numerically, say, using numerical integration, which one is correct?

Let me compute the integral numerically using approximate methods. Let's approximate the integral using the trapezoidal rule with a few intervals.

The integral is from 0 to 2 of x^{-1/2}(2 -x)^{-1/2}[1 -0.5x(2 -x)] dx.

Let's make a substitution x = 2 sin²θ, which makes the integral 2 ∫0^{π/2} [1 - 2 sin²θ cos²θ] dθ. Let's compute this numerically.

Compute 2*(π/2 - 2*(π/16)) = 2*(π/2 - π/8) = 2*(3π/8) = 3π/4 ≈ 2.356194490192345.

Alternatively, compute the original integral numerically using a numerical approximation. Let's use x from 0 to 2, but avoid the singularities at 0 and 2 by integrating from ε to 2 - ε, with ε small.

Let's take ε = 0.0001. Then compute the integral from 0.0001 to 1.9999.

The integrand is x^{-1/2}(2 -x)^{-1/2}[1 -0.5x(2 -x)].

Let's approximate this using numerical integration. Let's use Simpson's rule with a few intervals. Let's divide the interval [0.0001, 1.9999] into n=1000 intervals. But this is time-consuming to do manually. Alternatively, use symmetry. Let's note that the integrand is symmetric around x=1. Let's make substitution x = 2 - y. Then the integral from 0 to 2 becomes the same as from 0 to 2, so we can integrate from 0 to1 and double it. But due to the singularities, it's better to use substitution.

Alternatively, use the substitution x = 2t², which makes dx = 4t dt. Then x=0 when t=0, x=2 when t=1. Then the integral becomes:

∫₀¹ (2t²)^{-1/2}(2 -2t²)^{-1/2}[1 -0.5*(2t²)(2 -2t²)] *4t dt.

Simplify:

(2t²)^{-1/2} = (2)^{-1/2} t^{-1}

(2 -2t²)^{-1/2} = (2(1 -t²))^{-1/2} = 2^{-1/2}(1 -t²)^{-1/2}

Multiply them: 2^{-1} t^{-1}(1 -t²)^{-1/2}

The bracket term: 1 -0.5*(2t²)(2 -2t²) = 1 -0.5*(4t² -4t^4) = 1 -2t² +2t^4

Multiply by 4t dt:

4t * 2^{-1} t^{-1}(1 -t²)^{-1/2} [1 -2t² +2t^4] dt = 2 (1 -t²)^{-1/2} [1 -2t² +2t^4] dt.

So the integral becomes 2 ∫₀¹ (1 -t²)^{-1/2}(1 -2t² +2t^4) dt.

This is easier to integrate numerically. Let's approximate this integral.

Let's expand the integrand:

(1 -t²)^{-1/2}(1 -2t² +2t^4) = (1 -2t² +2t^4)/sqrt(1 -t²).

Let's approximate this from t=0 to t=1.

Let's use substitution t = sinφ, so dt = cosφ dφ, and sqrt(1 -t²) = cosφ. The integral becomes:

2 ∫₀^{π/2} [1 -2 sin²φ +2 sin^4φ] / cosφ * cosφ dφ = 2 ∫₀^{π/2} [1 -2 sin²φ +2 sin^4φ] dφ.

Simplify the integrand:

1 -2 sin²φ +2 sin^4φ = 1 -2 sin²φ +2 sin^4φ.

Use power-reduction identities:

sin²φ = (1 - cos2φ)/2

sin^4φ = (3 -4 cos2φ + cos4φ)/8

So:

1 -2*(1 - cos2φ)/2 +2*(3 -4 cos2φ + cos4φ)/8

= 1 - (1 - cos2φ) + (3 -4 cos2φ + cos4φ)/4

= 1 -1 + cos2φ + (3/4 - cos2φ + (1/4)cos4φ)

= cos2φ + 3/4 - cos2φ + (1/4)cos4φ

= 3/4 + (1/4)cos4φ

So the integral becomes 2 ∫₀^{π/2} [3/4 + (1/4)cos4φ] dφ = 2*(3/4*(π/2) + (1/4)*(0)) = 2*(3π/8) = 3π/4.

Because ∫₀^{π/2} cos4φ dφ = [sin4φ/4] from 0 to π/2 = (sin2π - sin0)/4 = 0.

So the integral is 3π/4. Therefore, the correct answer is 3π/4 ≈ 2.356194490192345.

Therefore, the first method was incorrect coefficients. The mistake was in the first method's split of the integral. The correct answer is 3π/4.

But why did the first method give 3π/8? Because in the first method, when splitting the integral, the coefficients were incorrectly calculated. Specifically, when expanding 1 -0.5x(2 -x) =1 -x +0.5x², and then splitting the integral, the coefficients for each term are correct, but when converting to Beta functions, the substitution factors were not properly accounted for.

Wait, no. Let me re-examine the first method.

First method:

I = ∫ x^{-1/2}(2 -x)^{-1/2} dx - ∫ x^{1/2}(2 -x)^{-1/2} dx + 0.5 ∫ x^{3/2}(2 -x)^{-1/2} dx.

First integral: π

Second integral: π

Third integral: 3π/4

So I = π - π + 0.5*(3π/4) = 3π/8.

But according to substitution method, the correct answer is 3π/4. So the mistake must be in the first method's calculation of the third integral.

Wait, the third integral is 0.5 ∫ x^{3/2}(2 -x)^{-1/2} dx. After substitution x=2t, this becomes 0.5 ∫ (2t)^{3/2}(2 -2t)^{-1/2} *2 dt = 0.5 * 2^{3/2} *2^{ -1/2} *2 ∫ t^{3/2}(1 -t)^{-1/2} dt = 0.5 * 2^{3/2 -1/2 +1} ∫ t^{3/2}(1 -t)^{-1/2} dt.

Compute the exponents: 3/2 -1/2 =1, so 2^{1 +1} =2^2=4. So 0.5*4=2. So the third integral is 2*B(5/2,1/2) =2*(3π/8)=3π/4. Therefore, the third integral is 3π/4. So the first method's third integral is 0.5*3π/4=3π/8. But according to substitution method, the entire integral is 3π/4. Therefore, the first method's split must be incorrect.

But according to the expansion, the integral is I1 - I2 +0.5 I3. But according to substitution method, it's I1 -2I2 +2I3. Therefore, the expansion must be incorrect.

Wait, the expansion of 1 -0.5x(2 -x) is 1 -x +0.5x². Therefore, the integral is:

∫ [1 -x +0.5x²] x^{-1/2}(2 -x)^{-1/2} dx = ∫ x^{-1/2}(2 -x)^{-1/2} dx - ∫ x^{1/2}(2 -x)^{-1/2} dx +0.5 ∫ x^{3/2}(2 -x)^{-1/2} dx.

But according to substitution method, the same integral is:

∫ [1 -2t +2t²] t^{-1/2}(1 -t)^{-1/2} dt = ∫ t^{-1/2}(1 -t)^{-1/2} dt -2 ∫ t^{1/2}(1 -t)^{-1/2} dt +2 ∫ t^{3/2}(1 -t)^{-1/2} dt.

Which is I1 -2I2 +2I3.

But in the first method, the coefficients are I1 -I2 +0.5I3. Therefore, the first method is missing factors. The mistake is that when expanding 1 -x +0.5x², the coefficients are correct, but when substituting x=2t, the integrals I2 and I3 in the first method are not scaled correctly.

Wait, no. The integrals in the first method are in terms of x, while in substitution method, they are in terms of t. Therefore, the coefficients in the first method are correct, but the calculation of the integrals I2 and I3 in the first method must be wrong.

Wait, let's re-express the integrals in the first method:

First integral: ∫ x^{-1/2}(2 -x)^{-1/2} dx from 0 to2. This is π.

Second integral: ∫ x^{1/2}(2 -x)^{-1/2} dx from 0 to2. This was calculated as π.

Third integral: ∫ x^{3/2}(2 -x)^{-1/2} dx from 0 to2. This was calculated as 3π/4.

But according to substitution method, the entire integral is I1 -2I2 +2I3 = π -2π +2*(3π/4) = π -2π +3π/2 = (1 -2 +1.5)π = 0.5π. But this contradicts the substitution method's result of 3π/4.

Wait, this is even more confusing. There must be a fundamental mistake in the approach.

Alternatively, perhaps the original integral is indeed 3π/4, and the first method's mistake is in the calculation of the third integral.

Let me re-calculate the third integral in the first method.

Third integral: ∫₀² x^{3/2}(2 -x)^{-1/2} dx.

Let’s compute this using substitution x=2t, dx=2dt.

Then integral becomes ∫₀¹ (2t)^{3/2}(2 -2t)^{-1/2} *2 dt = 2^{3/2} *2^{ -1/2} *2 ∫ t^{3/2}(1 -t)^{-1/2} dt = 2^{3/2 -1/2 +1} ∫ t^{3/2}(1 -t)^{-1/2} dt = 2^{2} ∫ t^{3/2}(1 -t)^{-1/2} dt =4 B(5/2,1/2) =4*(3π/8)= 3π/2.

Wait, but earlier calculation said the third integral is 3π/4. So this is a mistake. Let me compute B(5/2,1/2):

B(5/2,1/2) = Γ(5/2)Γ(1/2)/Γ(3).

Γ(5/2) = (3/2)(1/2)√π = (3/4)√π.

Γ(1/2) = √π.

Γ(3) = 2! =2.

So B(5/2,1/2) = (3/4 √π)(√π)/2 = (3/4 *1)/2 = 3/8.

Therefore, B(5/2,1/2) =3π/8.

Therefore, the third integral is 4*(3π/8) = 3π/2.

But earlier, in the first method, the third integral was calculated as 3π/4. So this is a mistake. The correct value is 3π/2.

Therefore, the first method's third integral was incorrectly calculated as 3π/4 instead of 3π/2. Therefore, the first method's result was wrong.

So, correcting that:

I = π - π +0.5*(3π/2) =0 + 3π/4 =3π/4.

Ah! So the mistake was in the first method's calculation of the third integral. Originally, I thought the third integral was 3π/4, but it's actually 3π/2. Therefore, the correct answer is 3π/4.

So the correct exact answer is 3π/4, and the numerical approximation is approximately 2.356194490192345, which rounds to 2.3561944902 when rounded to 10 decimal places.

But wait, according to the substitution method, the integral is 3π/4 ≈ 2.356194490192345. But when I first thought the numerical approximation was 1.178, that was incorrect. The correct numerical value is approximately 2.3561944902.

Therefore, the correct answer is 3π/4, and the numerical approximation is approximately 2.3561944902.

But why did the initial substitution method give 3π/4, and the first method, after correcting the third integral, also gives 3π/4. So the correct answer is 3π/4.

Therefore, the initial mistake was in the first method's calculation of the third integral. The third integral is 3π/2, not 3π/4. Therefore, when multiplied by 0.5, it becomes 3π/4.

So the correct exact answer is 3π/4, and the numerical approximation is approximately 2.3561944902.

But wait, the user's original integral is ∫₀² x^{-1/2} (2-x)^{-1/2} [1-0.5x(2-x)] dx. After correcting the calculations, the correct answer is 3π/4.

But let me verify once more with the substitution x = 2 sin²θ. The integral becomes 2 ∫0^{π/2} [1 - 2 sin²θ cos²θ] dθ = 3π/4. This is confirmed by expanding the integrand and integrating term by term.

Therefore, the correct exact answer is 3π/4, and the numerical approximation is approximately 2.3561944902.
</think>

{"answer": "\\frac{3\\pi}{4}", "numerical_answer": "2.3561944902"}