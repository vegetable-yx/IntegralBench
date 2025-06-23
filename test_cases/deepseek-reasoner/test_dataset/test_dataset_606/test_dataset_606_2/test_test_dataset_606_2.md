<think>
Okay, let's tackle this integral step by step. The problem is to compute the definite integral from 0 to 1 of [arcsin(x²) + arcsin(√x)] divided by sqrt(1 - x²) dx. Hmm, that looks a bit complicated, but maybe I can break it down.

First, let me write the integral properly:

∫₀¹ [sin⁻¹(x²) + sin⁻¹(√x)] / √(1 - x²) dx

I notice that the denominator is sqrt(1 - x²), which is the derivative of arcsin(x). That might be useful. Also, the numerator has two inverse sine functions. Maybe splitting the integral into two parts would help. Let me try that.

So, split the integral into two separate integrals:

I = ∫₀¹ [sin⁻¹(x²)/√(1 - x²)] dx + ∫₀¹ [sin⁻¹(√x)/√(1 - x²)] dx

Let me call the first integral I₁ and the second one I₂. So, I = I₁ + I₂.

Starting with I₁: ∫₀¹ sin⁻¹(x²)/√(1 - x²) dx

Hmm, integrating arcsin(x²) over this denominator. Maybe substitution? Let's think. If I let u = sin⁻¹(x²), then du/dx = (1/√(1 - x⁴)) * 2x. But that doesn't seem to help directly because the denominator here is sqrt(1 - x²), not sqrt(1 - x⁴). Maybe another substitution.

Alternatively, perhaps integration by parts. Let me recall that integration by parts formula: ∫u dv = uv - ∫v du.

Let me set u = sin⁻¹(x²), then du = [2x / sqrt(1 - x⁴)] dx. Then dv = dx / sqrt(1 - x²), so v = sin⁻¹(x). Hmm, so then:

I₁ = u*v from 0 to 1 - ∫₀¹ v du

So, that would be [sin⁻¹(x²) * sin⁻¹(x)] from 0 to 1 minus ∫₀¹ sin⁻¹(x) * [2x / sqrt(1 - x⁴)] dx

But this seems more complicated. The new integral might not be easier. Maybe this approach isn't the best. Let me think again.

Alternatively, maybe substitution for I₁. Let me set t = x². Then when x=0, t=0; x=1, t=1. Then dt = 2x dx, so dx = dt/(2√t). Then the integral becomes:

∫₀¹ sin⁻¹(t) / sqrt(1 - t) * (dt)/(2√t)

Hmm, that's ∫₀¹ [sin⁻¹(t) / (2√t sqrt(1 - t))] dt

Not sure if that helps. Maybe another substitution here. Let me think. Alternatively, maybe express sin⁻¹(t) as an integral. Wait, sin⁻¹(t) is the integral from 0 to t of 1/sqrt(1 - u²) du. But substituting that into the integral might lead to a double integral. Maybe switching the order of integration? Let's see.

Alternatively, perhaps a substitution for the entire expression. Let me think about the denominator sqrt(1 - x²). If I set x = sinθ, then sqrt(1 - x²) becomes cosθ, and dx = cosθ dθ. Let's try that for I₁.

So, for I₁, substitute x = sinθ, so θ ranges from 0 to π/2. Then:

I₁ = ∫₀^{π/2} [sin⁻¹(sin²θ) / cosθ] * cosθ dθ

The cosθ cancels out, so I₁ = ∫₀^{π/2} sin⁻¹(sin²θ) dθ

Hmm, sin²θ is between 0 and 1, so sin⁻¹(sin²θ) is valid. But sin²θ is less than or equal to sinθ for θ in [0, π/2], right? Because sinθ is between 0 and 1 here, and squaring it makes it smaller. So sin²θ ≤ sinθ, so sin⁻¹(sin²θ) would be less than θ. Not sure if that helps.

Alternatively, maybe express sin²θ as 1 - cos²θ, but that might not help. Wait, sin²θ = (1 - cos2θ)/2. Hmm, not sure. Alternatively, maybe use a power series expansion for arcsin. But that might get complicated.

Alternatively, perhaps consider substitution in I₁. Let me set u = sinθ, but I already did that. Maybe another substitution. Let me think. Alternatively, maybe integrating I₂ first, which might be easier.

Looking at I₂: ∫₀¹ [sin⁻¹(√x) / sqrt(1 - x²)] dx

Again, maybe substitution. Let me set t = √x, so x = t², dx = 2t dt. Then when x=0, t=0; x=1, t=1. So:

I₂ = ∫₀¹ [sin⁻¹(t) / sqrt(1 - t⁴)] * 2t dt

Hmm, sqrt(1 - t⁴) in the denominator. That seems complicated. Maybe another substitution here. Let me think. Alternatively, maybe integrating by parts here as well.

Let me try substitution for I₂. Let me set u = t², but not sure. Alternatively, if I set u = t², then du = 2t dt, which is part of the integral. Wait, the integral is 2t dt times sin⁻¹(t)/sqrt(1 - t⁴). Hmm, maybe not.

Alternatively, set u = t², so that sqrt(1 - t⁴) becomes sqrt(1 - u²). Then, but then the integral becomes:

∫₀¹ [sin⁻¹(√u) / sqrt(1 - u²)] * du

Wait, but that's similar to the original I₂. Hmm, maybe not helpful.

Alternatively, perhaps substitution for I₂. Let me set y = sin⁻¹(√x). Wait, not sure. Let me think again.

Wait, maybe there's a relationship between the two integrals I₁ and I₂. Let me check the original integral. The original integrand is [sin⁻¹(x²) + sin⁻¹(√x)] / sqrt(1 - x²). Maybe there's a substitution that relates x² and √x. For example, if I set x = t² in one integral and x = sqrt(t) in another? Not sure.

Wait, let's consider substitution in the original integral. Let me try substituting x = sinθ. Then, dx = cosθ dθ, and sqrt(1 - x²) = cosθ. Then the integral becomes:

∫₀^{π/2} [sin⁻¹(sin²θ) + sin⁻¹(sinθ)] / cosθ * cosθ dθ

Which simplifies to:

∫₀^{π/2} [sin⁻¹(sin²θ) + θ] dθ

Because sin⁻¹(sinθ) = θ for θ in [-π/2, π/2], which it is here since θ is from 0 to π/2.

So the integral becomes:

∫₀^{π/2} sin⁻¹(sin²θ) dθ + ∫₀^{π/2} θ dθ

The second integral is straightforward: [θ²/2] from 0 to π/2, which is (π²/8). So I = (π²/8) + ∫₀^{π/2} sin⁻¹(sin²θ) dθ

Now, need to compute the first integral: ∫₀^{π/2} sin⁻¹(sin²θ) dθ

Hmm, how to handle this. Let me consider substitution. Let me set φ = sin²θ. Then, θ = sin⁻¹(√φ). But maybe that's not helpful. Alternatively, express sin²θ in terms of cos2θ. Wait, sin²θ = (1 - cos2θ)/2. So sin⁻¹(sin²θ) = sin⁻¹[(1 - cos2θ)/2]

Hmm, not sure. Alternatively, maybe use a trigonometric identity. Let me think. Let me denote y = sinθ. Then, sin²θ = y², and sin⁻¹(y²) is the angle whose sine is y². Let me denote that angle as α, so sinα = y². Then, α = sin⁻¹(y²). But how does that relate to θ?

Alternatively, maybe use integration by parts here. Let me set u = sin⁻¹(sin²θ), dv = dθ. Then du = [ (2 sinθ cosθ) / sqrt(1 - sin⁴θ) ] dθ, and v = θ.

Wait, let's compute du. If u = sin⁻¹(sin²θ), then du/dθ = [1 / sqrt(1 - sin⁴θ)] * d/dθ (sin²θ) = [1 / sqrt(1 - sin⁴θ)] * 2 sinθ cosθ dθ

So, du = [2 sinθ cosθ / sqrt(1 - sin⁴θ)] dθ

Then, integration by parts gives:

uv|₀^{π/2} - ∫₀^{π/2} v du

But uv evaluated at π/2: sin⁻¹(sin²(π/2)) * π/2. sin(π/2) = 1, so sin²(π/2) = 1, so sin⁻¹(1) = π/2. So uv at π/2 is (π/2)*(π/2) = π²/4. At 0, sin²0 = 0, so sin⁻¹(0) = 0, so uv at 0 is 0. So the first term is π²/4.

Then, the integral becomes:

π²/4 - ∫₀^{π/2} θ * [2 sinθ cosθ / sqrt(1 - sin⁴θ)] dθ

Hmm, this seems complicated, but maybe we can simplify the integrand. Let's look at the denominator: sqrt(1 - sin⁴θ) = sqrt( (1 - sin²θ)(1 + sin²θ) ) = sqrt( cos²θ (1 + sin²θ) ) = cosθ sqrt(1 + sin²θ)

So, the integrand becomes:

θ * [2 sinθ cosθ / (cosθ sqrt(1 + sin²θ))] = θ * [2 sinθ / sqrt(1 + sin²θ)]

So, the integral simplifies to:

π²/4 - 2 ∫₀^{π/2} [θ sinθ / sqrt(1 + sin²θ)] dθ

Hmm, this still looks difficult. Maybe another substitution here. Let me set t = sinθ. Then, when θ=0, t=0; θ=π/2, t=1. Then, dt = cosθ dθ. But we have θ in terms of t. Hmm, not sure. Alternatively, maybe set u = 1 + sin²θ. Then du = 2 sinθ cosθ dθ. But not sure.

Alternatively, perhaps express sinθ / sqrt(1 + sin²θ) as something. Let me note that:

sinθ / sqrt(1 + sin²θ) = [sinθ / sqrt(1 + sin²θ)] = [sinθ / sqrt(1 + sin²θ)]

Hmm, maybe set t = sinθ, then dt = cosθ dθ. But we have θ in terms of t. Let's see:

Let t = sinθ, so θ = sin⁻¹(t), and cosθ dθ = dt. Then, sqrt(1 + sin²θ) = sqrt(1 + t²). So the integral becomes:

2 ∫₀¹ [sin⁻¹(t) * t / sqrt(1 + t²)] * [dt / cosθ]

Wait, but cosθ = sqrt(1 - t²). So, substituting, we have:

2 ∫₀¹ [sin⁻¹(t) * t / sqrt(1 + t²)] * [dt / sqrt(1 - t²)]

So, combining the denominators:

2 ∫₀¹ [t sin⁻¹(t) / (sqrt(1 + t²) sqrt(1 - t²))] dt

Simplify the denominator: sqrt( (1 + t²)(1 - t²) ) = sqrt(1 - t⁴)

So, the integral becomes:

2 ∫₀¹ [t sin⁻¹(t) / sqrt(1 - t⁴)] dt

Hmm, this seems similar to the original I₁. Wait, but I₁ was ∫₀¹ sin⁻¹(x²)/sqrt(1 - x²) dx. Not sure if there's a connection here. Maybe not. This seems like a different integral.

Alternatively, maybe there's a substitution here. Let me set u = t². Then, t = sqrt(u), dt = (1/(2√u)) du. Then, the integral becomes:

2 ∫₀¹ [sqrt(u) sin⁻¹(sqrt(u)) / sqrt(1 - u²)] * (1/(2√u)) du

Simplify: 2 * (1/2) ∫₀¹ [sin⁻¹(sqrt(u)) / sqrt(1 - u²)] du = ∫₀¹ [sin⁻¹(√u) / sqrt(1 - u²)] du

But that's exactly the original I₂! Wait, so this integral here is equal to I₂. So, going back:

We had:

I = (π²/8) + ∫₀^{π/2} sin⁻¹(sin²θ) dθ

Then, after integration by parts, we found that:

∫₀^{π/2} sin⁻¹(sin²θ) dθ = π²/4 - 2 ∫₀^{π/2} [θ sinθ / sqrt(1 + sin²θ)] dθ

But then, through substitution, we found that:

2 ∫₀^{π/2} [θ sinθ / sqrt(1 + sin²θ)] dθ = I₂

Therefore, ∫₀^{π/2} sin⁻¹(sin²θ) dθ = π²/4 - I₂

So, substituting back into I:

I = (π²/8) + (π²/4 - I₂) = (π²/8 + π²/4) - I₂ = (3π²/8) - I₂

But wait, the original integral I is equal to I₁ + I₂. But here, we expressed I in terms of I₂. Let me check:

Wait, original I = I₁ + I₂. Then, after substitution, we found that I = (π²/8) + ∫₀^{π/2} sin⁻¹(sin²θ) dθ. Then, ∫₀^{π/2} sin⁻¹(sin²θ) dθ = π²/4 - I₂. Therefore, I = π²/8 + π²/4 - I₂ = 3π²/8 - I₂. But since I = I₁ + I₂, then:

I₁ + I₂ = 3π²/8 - I₂ ⇒ I₁ + 2I₂ = 3π²/8

Hmm, but this seems like an equation involving I₁ and I₂. But we need another equation to solve for I₁ and I₂. Wait, but maybe we can find another relation between I₁ and I₂.

Alternatively, perhaps there's a symmetry between I₁ and I₂. Let me check the original integrals:

I₁ = ∫₀¹ sin⁻¹(x²)/sqrt(1 - x²) dx

I₂ = ∫₀¹ sin⁻¹(√x)/sqrt(1 - x²) dx

Let me try substituting x = √t in I₂. So, set t = x², so x = sqrt(t), dx = (1/(2√t)) dt. Then, when x=0, t=0; x=1, t=1. So:

I₂ = ∫₀¹ [sin⁻¹(√(sqrt(t)) ) / sqrt(1 - t)] * (1/(2√t)) dt

Simplify: sin⁻¹(t^{1/4}) / sqrt(1 - t) * (1/(2√t)) dt

Wait, that seems more complicated. Alternatively, maybe another substitution. Let me set u = x² in I₁. Then, x = sqrt(u), dx = (1/(2√u)) du. Then:

I₁ = ∫₀¹ [sin⁻¹(u) / sqrt(1 - u)] * (1/(2√u)) du

Hmm, so I₁ = (1/2) ∫₀¹ [sin⁻¹(u) / (sqrt(u) sqrt(1 - u))] du

Similarly, I₂ is ∫₀¹ [sin⁻¹(√x)/sqrt(1 - x²)] dx. Let me set v = √x, so x = v², dx = 2v dv. Then:

I₂ = ∫₀¹ [sin⁻¹(v) / sqrt(1 - v⁴)] * 2v dv

Hmm, not sure if that helps. But maybe there's a relationship between I₁ and I₂ through substitution.

Alternatively, let's consider swapping variables. Suppose in I₁, we set t = x², so x = sqrt(t). Then, I₁ becomes:

∫₀¹ [sin⁻¹(t) / sqrt(1 - t)] * (1/(2√t)) dt

Similarly, I₂ is:

∫₀¹ [sin⁻¹(√x)/sqrt(1 - x²)] dx

If we set in I₂, x = sqrt(u), then dx = (1/(2√u)) du, and:

I₂ = ∫₀¹ [sin⁻¹(u^{1/2}) / sqrt(1 - u)] * (1/(2√u)) du

Which is similar to I₁. So, I₁ and I₂ are similar but with different exponents. Not sure if that helps.

Alternatively, maybe consider adding I₁ and I₂. But I think we need another approach.

Wait, going back to the previous result where I = 3π²/8 - I₂, and since I = I₁ + I₂, then:

I₁ + I₂ = 3π²/8 - I₂ ⇒ I₁ + 2I₂ = 3π²/8

But we need another equation to solve for I₁ and I₂. Alternatively, maybe we can find another relation between I₁ and I₂.

Alternatively, let's consider the original substitution where x = sinθ for the entire integral. Then, I = ∫₀^{π/2} [sin⁻¹(sin²θ) + θ] dθ

But we can also write this as:

I = ∫₀^{π/2} sin⁻¹(sin²θ) dθ + ∫₀^{π/2} θ dθ

We already know that the second integral is π²/8. So, if we can compute the first integral, we can get I. But we found that the first integral is π²/4 - I₂. So:

I = (π²/4 - I₂) + π²/8 = 3π²/8 - I₂

But since I = I₁ + I₂, then:

I₁ + I₂ = 3π²/8 - I₂ ⇒ I₁ + 2I₂ = 3π²/8

But we need another equation. Maybe we can find another relation by considering substitution in I₁.

Alternatively, let's consider integrating I₁ by substitution. Let me set t = x². Then, as before, I₁ becomes:

(1/2) ∫₀¹ [sin⁻¹(t) / (sqrt(t) sqrt(1 - t))] dt

Let me consider substitution here. Let me set u = sqrt(t). Then, t = u², dt = 2u du. Then:

I₁ = (1/2) ∫₀¹ [sin⁻¹(u²) / (u sqrt(1 - u²))] * 2u du = ∫₀¹ [sin⁻¹(u²) / sqrt(1 - u²)] du

Wait, that's the same as the original I₁. Not helpful.

Alternatively, maybe integrate I₁ by parts. Let me set u = sin⁻¹(t), dv = [1 / (sqrt(t) sqrt(1 - t))] dt

Then, du = [1 / sqrt(1 - t²)] dt, and v = ?

But integrating dv = [1 / (sqrt(t) sqrt(1 - t))] dt. Let me compute v:

v = ∫ [1 / (sqrt(t) sqrt(1 - t))] dt

Let me set w = sin²φ, so t = sin²φ, dt = 2 sinφ cosφ dφ. Then:

v = ∫ [1 / (sinφ * cosφ)] * 2 sinφ cosφ dφ = ∫ 2 dφ = 2φ + C = 2 sin⁻¹(√t) + C

So, v = 2 sin⁻¹(√t)

Therefore, integrating by parts:

I₁ = (1/2)[u*v from 0 to1 - ∫₀¹ v du]

= (1/2)[ sin⁻¹(t) * 2 sin⁻¹(√t) |₀¹ - ∫₀¹ 2 sin⁻¹(√t) * [1 / sqrt(1 - t²)] dt ]

At t=1: sin⁻¹(1) = π/2, sin⁻¹(√1) = π/2, so term is (π/2)*(π/2) = π²/4. At t=0: sin⁻¹(0) = 0, sin⁻¹(0) =0, so first term is π²/4.

Then, the integral becomes:

(1/2)[π²/4 - 2 ∫₀¹ [sin⁻¹(√t) / sqrt(1 - t²)] dt ]

But the integral ∫₀¹ [sin⁻¹(√t) / sqrt(1 - t²)] dt is exactly I₂. So:

I₁ = (1/2)[π²/4 - 2 I₂] = (π²/8) - I₂

So, now we have:

I₁ = π²/8 - I₂

But earlier, we had:

I₁ + 2I₂ = 3π²/8

Substituting I₁ from this equation into that:

(π²/8 - I₂) + 2I₂ = 3π²/8

Simplify:

π²/8 + I₂ = 3π²/8 ⇒ I₂ = 3π²/8 - π²/8 = 2π²/8 = π²/4

Then, substituting back into I₁ = π²/8 - I₂:

I₁ = π²/8 - π²/4 = -π²/8

Wait, that can't be right. How can I₁ be negative? The integrand of I₁ is [sin⁻¹(x²)] / sqrt(1 - x²), which is non-negative over [0,1], so the integral should be positive. So, getting a negative result here suggests a mistake in the calculation.

Wait, let's check the integration by parts steps for I₁. Let me go back.

We set u = sin⁻¹(t), dv = [1 / (sqrt(t) sqrt(1 - t))] dt

Then, du = [1 / sqrt(1 - t²)] dt, and v = 2 sin⁻¹(√t)

So, integrating by parts:

I₁ = (1/2)[u*v |₀¹ - ∫₀¹ v du]

At t=1: u = π/2, v = 2*(π/2) = π. So u*v = (π/2)*π = π²/2. At t=0: u=0, v=0. So the first term is π²/2.

Then, the integral becomes:

(1/2)[π²/2 - ∫₀¹ 2 sin⁻¹(√t) * [1 / sqrt(1 - t²)] dt ]

= (1/2)(π²/2 - 2 I₂)

= π²/4 - I₂

Ah, here's the mistake. Earlier, I had a (1/2) factor outside, but when calculating the first term, I think I made a mistake. Let me redo this step.

Original I₁ after substitution t = x² was:

I₁ = (1/2) ∫₀¹ [sin⁻¹(t) / (sqrt(t) sqrt(1 - t))] dt

Then, integrating by parts with u = sin⁻¹(t), dv = [1 / (sqrt(t) sqrt(1 - t))] dt

Then, as computed, v = 2 sin⁻¹(√t)

So, integrating by parts:

I₁ = (1/2)[u*v |₀¹ - ∫₀¹ v du]

At t=1: u = π/2, v = 2*(π/2) = π. So u*v = (π/2)*π = π²/2.

At t=0: u=0, v=0. So the first term is π²/2.

Then, the integral part is:

- ∫₀¹ v du = - ∫₀¹ 2 sin⁻¹(√t) * [1 / sqrt(1 - t²)] dt

So, I₁ = (1/2)[π²/2 - 2 ∫₀¹ [sin⁻¹(√t)/sqrt(1 - t²)] dt ]

But ∫₀¹ [sin⁻¹(√t)/sqrt(1 - t²)] dt is I₂. Therefore:

I₁ = (1/2)(π²/2 - 2 I₂) = π²/4 - I₂

So, correct. Then, I₁ = π²/4 - I₂

But we also had from the previous equation:

I = 3π²/8 - I₂

But I = I₁ + I₂ = (π²/4 - I₂) + I₂ = π²/4

Wait, that contradicts the previous result. Wait, no. Let me check.

Wait, earlier, after substitution x = sinθ, we had:

I = ∫₀^{π/2} [sin⁻¹(sin²θ) + θ] dθ = ∫₀^{π/2} sin⁻¹(sin²θ) dθ + π²/8

Then, after integrating by parts, we found that ∫₀^{π/2} sin⁻¹(sin²θ) dθ = π²/4 - I₂

Therefore, I = (π²/4 - I₂) + π²/8 = 3π²/8 - I₂

But also, I = I₁ + I₂

But we also found that I₁ = π²/4 - I₂

Therefore, substituting into I = I₁ + I₂:

I = (π²/4 - I₂) + I₂ = π²/4

But according to the other expression, I = 3π²/8 - I₂

So, setting these equal:

π²/4 = 3π²/8 - I₂ ⇒ I₂ = 3π²/8 - π²/4 = 3π²/8 - 2π²/8 = π²/8

Then, substituting back into I₁ = π²/4 - I₂:

I₁ = π²/4 - π²/8 = π²/8

So, I₁ = π²/8, I₂ = π²/8, and I = I₁ + I₂ = π²/8 + π²/8 = π²/4

Wait, so the integral I is π²/4. But let's verify this.

Wait, let's check the steps again. After substitution x = sinθ, I becomes ∫₀^{π/2} [sin⁻¹(sin²θ) + θ] dθ

. Then, integrating by parts for the first part, we found that ∫₀^{π/2} sin⁻¹(sin²θ) dθ = π²/4 - I₂

. Then, I = (π²/4 - I₂) + π²/8 = 3π²/8 - I₂

. But also, I = I₁ + I₂ = (π²/4 - I₂) + I₂ = π²/4

. Therefore, 3π²/8 - I₂ = π²/4 ⇒ I₂ = 3π²/8 - π²/4 = π²/8

. Then, I₁ = π²/4 - π²/8 = π²/8

. So, I = π²/8 + π²/8 = π²/4

So, the final result is π²/4. That seems plausible. Let me check with a numerical approximation.

π²/4 is approximately (9.8696)/4 ≈ 2.4674.

Let me compute the integral numerically to check. Let's approximate the integral numerically.

The integral is ∫₀¹ [arcsin(x²) + arcsin(√x)] / sqrt(1 - x²) dx

We can approximate this using numerical integration. Let's use a calculator or approximate it step by step.

Alternatively, since we have the analytical result as π²/4 ≈ 2.467401100272339654708622749.

Rounded to 10 decimal places, that's approximately 2.4674011003.

But let's verify with a numerical approximation. Let's compute the integral numerically.

But since I don't have a calculator here, but given that the steps led us to π²/4, and the steps seem correct after correcting the integration by parts, I think the analytical answer is π²/4.

Therefore, the exact answer is π²/4, and the numerical approximation is approximately 2.4674011003.
</think>

{"answer": "\\frac{\\pi^2}{4}", "numerical_answer": "2.4674011003"}