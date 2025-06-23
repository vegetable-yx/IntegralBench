<think>
Okay, let's tackle this integral step by step. The integral given is ∫₀² x^(-1/2) [1 + 1.0√(x(2.0 - x))]^(-3/2) dx. Hmm, first, I need to see if there's a substitution that can simplify this expression. The presence of √(x(2 - x)) suggests maybe a trigonometric substitution or something that can exploit the symmetry of the expression under the square root.

Let me consider the variable substitution. The term inside the square root is x(2 - x), which resembles the form of a quadratic. Let's complete the square for x(2 - x). Expanding that, it's 2x - x², which can be rewritten as -(x² - 2x) = -(x² - 2x +1 -1) = -(x -1)^2 +1. So, x(2 - x) = 1 - (x -1)^2. That looks like a standard form for a trigonometric substitution. Maybe substituting x -1 = sinθ or something similar. Let's try that.

Let me set t = x -1. Then, x = t +1, and when x=0, t=-1; x=2, t=1. But the integral becomes from t=-1 to t=1. The expression under the square root becomes 1 - t². So √(x(2 -x)) = √(1 - t²). Then, dx = dt. But also, x^(-1/2) is (t +1)^(-1/2). Hmm, not sure if that's better. Let's write the integral in terms of t:

∫ from t=-1 to t=1 (t +1)^(-1/2) [1 + √(1 - t²)]^(-3/2) dt.

Hmm, maybe another substitution. Alternatively, perhaps a substitution that can simplify the denominator. Let's see. The denominator is [1 + √(1 - t²)]^(3/2). Maybe set u = √(1 - t²) +1. But not sure. Alternatively, maybe use a substitution that can make the denominator simpler. Let's think about trigonometric substitution for the term √(1 - t²). Let me set t = sinθ. Then, √(1 - t²) = cosθ, and dt = cosθ dθ. Then, when t=-1, θ=-π/2; t=1, θ=π/2. So the integral becomes:

∫ from θ=-π/2 to θ=π/2 (sinθ +1)^(-1/2) [1 + cosθ]^(-3/2) * cosθ dθ.

Hmm, combining terms. Let's see. The denominator [1 + cosθ]^(3/2) can be simplified using the identity 1 + cosθ = 2cos²(θ/2). So [1 + cosθ]^(3/2) = (2)^(3/2) cos³(θ/2). Similarly, the numerator (sinθ +1)^(-1/2). Let's see, sinθ +1 = 1 + sinθ. There's an identity for 1 + sinθ = 2 sin²(θ/2 + π/4) or maybe using 1 + sinθ = (sin(θ/2) + cos(θ/2))². Let me check:

1 + sinθ = sin²(θ/2) + cos²(θ/2) + 2 sin(θ/2)cos(θ/2) = (sin(θ/2) + cos(θ/2))². Yes, that's correct. So √(1 + sinθ) = sin(θ/2) + cos(θ/2). Therefore, (1 + sinθ)^(-1/2) = 1/(sin(θ/2) + cos(θ/2)).

Putting this back into the integral:

∫ [1/(sin(θ/2) + cos(θ/2))] * [1/(2^(3/2) cos³(θ/2))] * cosθ dθ, integrated from -π/2 to π/2.

Simplify the terms:

First, 2^(3/2) is 2*sqrt(2). So denominator term is 2*sqrt(2) cos³(θ/2). Then, the numerator is cosθ. So combining:

1/(2*sqrt(2)) ∫ [cosθ / ( (sin(θ/2) + cos(θ/2)) * cos³(θ/2) ) ] dθ.

Let me simplify the expression inside the integral. Let's write cosθ in terms of θ/2. Remember that cosθ = 2cos²(θ/2) -1. Alternatively, cosθ = cos²(θ/2) - sin²(θ/2). Let's use that:

cosθ = cos²(θ/2) - sin²(θ/2) = (cos(θ/2) - sin(θ/2))(cos(θ/2) + sin(θ/2)).

So, substituting back into the integral:

1/(2*sqrt(2)) ∫ [ (cos(θ/2) - sin(θ/2))(cos(θ/2) + sin(θ/2)) / ( (sin(θ/2) + cos(θ/2)) * cos³(θ/2) ) ) ] dθ.

The (cos(θ/2) + sin(θ/2)) terms cancel out, leaving:

1/(2*sqrt(2)) ∫ [ (cos(θ/2) - sin(θ/2)) / cos³(θ/2) ] dθ.

Simplify numerator and denominator cos³(θ/2):

= 1/(2*sqrt(2)) ∫ [ (cos(θ/2) - sin(θ/2)) / cos³(θ/2) ] dθ

= 1/(2*sqrt(2)) ∫ [ 1/cos²(θ/2) - sin(θ/2)/cos³(θ/2) ] dθ

= 1/(2*sqrt(2)) [ ∫ sec²(θ/2) dθ - ∫ sin(θ/2) sec³(θ/2) dθ ]

Let's handle each integral separately.

First integral: ∫ sec²(θ/2) dθ. Let u = θ/2, du = dθ/2, so integral becomes 2 ∫ sec²u du = 2 tanu + C = 2 tan(θ/2) + C.

Second integral: ∫ sin(θ/2) sec³(θ/2) dθ. Let's rewrite sec³(θ/2) as 1/cos³(θ/2). So the integral becomes ∫ sin(θ/2)/cos³(θ/2) dθ. Let me set v = cos(θ/2), dv = - (1/2) sin(θ/2) dθ. Then, -2 dv = sin(θ/2) dθ. So the integral becomes ∫ (-2 dv)/v³ = -2 ∫ v^(-3) dv = -2 [ v^(-2)/(-2) ) ] + C = (1)/v² + C = 1/cos²(θ/2) + C = sec²(θ/2) + C.

Putting back into the expression:

1/(2*sqrt(2)) [ 2 tan(θ/2) - sec²(θ/2) ] evaluated from θ = -π/2 to θ = π/2.

Compute the antiderivative at the limits:

First, evaluate at θ = π/2:

2 tan(π/4) - sec²(π/4) = 2*(1) - (sqrt(2))² = 2 - 2 = 0.

Evaluate at θ = -π/2:

2 tan(-π/4) - sec²(-π/4) = 2*(-1) - (sqrt(2))² = -2 - 2 = -4.

Subtracting the lower limit from the upper limit:

0 - (-4) = 4.

Multiply by the constant factor 1/(2*sqrt(2)):

(1/(2*sqrt(2))) * 4 = 4/(2*sqrt(2)) = 2/sqrt(2) = sqrt(2).

So the exact value of the integral is sqrt(2). 

Wait, let me check that again. The antiderivative evaluated at π/2 gives 0, and at -π/2 gives -4. So the difference is 0 - (-4) = 4. Then 4/(2*sqrt(2)) = 2/sqrt(2) = sqrt(2). Yes, correct. So the exact answer is sqrt(2). The numerical approximation is approximately 1.4142135624. Rounded to 10 decimal places, that's 1.4142135624.

But let me verify the steps again to make sure I didn't make a mistake. Let's check the substitution steps again. Starting from the substitution t = x -1, leading to the integral in terms of t. Then substituting t = sinθ. Then expressing everything in terms of θ. Then simplifying the trigonometric expressions. Then integrating. The key steps seem correct. The cancellation of (cos + sin) terms, splitting into two integrals, integrating each part. The first integral gives 2 tan(θ/2), the second gives -sec²(θ/2). Evaluating from -π/2 to π/2. At π/2, θ/2 is π/4, tan(π/4)=1, sec²(π/4))=2. So 2*1 - 2 = 0. At -π/2, θ/2 is -π/4, tan(-π/4)=-1, sec²(-π/4)=2. So 2*(-1) -2 = -4. The difference is 0 - (-4) =4. Multiply by 1/(2√2) gives 4/(2√2)=√2. Yes, that's correct. So the exact answer is √2, approximately 1.4142135624.
</think>

{"answer": "\\sqrt{2}", "numerical_answer": "1.4142135624"}