<think>
Okay, so I need to compute the definite integral of arctan(x² - x + 1) from 0 to 1. Hmm, arctangent integrals can be tricky. Let me start by recalling some integration techniques. Maybe integration by parts? Since the integrand is arctan of a quadratic function, that might be a good approach.

Let me set u = arctan(x² - x + 1) and dv = dx. Then du would be the derivative of arctan, which is 1/(1 + (x² - x + 1)^2) times the derivative of the inside function. Wait, the derivative of x² - x + 1 is 2x - 1. So du = [ (2x - 1) ] / [1 + (x² - x + 1)^2] dx. And v would be x. So integration by parts gives uv - ∫v du. That would be x arctan(x² - x + 1) evaluated from 0 to 1 minus the integral from 0 to 1 of x*(2x - 1)/(1 + (x² - x + 1)^2) dx.

Hmm, let's compute the boundary terms first. At x=1: 1*arctan(1² -1 +1) = arctan(1) = π/4. At x=0: 0*arctan(0 -0 +1) = 0. So the first part is π/4 - 0 = π/4. Now the remaining integral is ∫₀¹ [x(2x -1)] / [1 + (x² - x +1)^2] dx. Let me denote this integral as I. So the original integral is π/4 - I.

Now I need to compute I. Let me look at the denominator: 1 + (x² - x +1)^2. Let me expand that. (x² - x +1)^2 = x^4 - 2x³ + 3x² - 2x +1. So denominator becomes x^4 - 2x³ + 3x² - 2x +2. Hmm, not sure if that helps. Maybe there's a substitution here. Let me see the numerator: x(2x -1) = 2x² -x. So the integrand is (2x² -x)/(x^4 - 2x³ + 3x² - 2x +2) dx.

Perhaps the denominator's derivative is related to the numerator? Let me check. Let’s compute the derivative of the denominator: d/dx [x^4 - 2x³ + 3x² - 2x +2] = 4x³ -6x² +6x -2. Hmm, not exactly the numerator. But maybe there's a linear combination or a substitution. Alternatively, maybe completing the square in the denominator.

Wait, the denominator is 1 + (x² -x +1)^2. Let me see if x² -x +1 can be rewritten. Completing the square: x² -x = x² -x + (1/4) - (1/4) = (x - 0.5)^2 - 1/4. So x² -x +1 = (x - 0.5)^2 + 3/4. So the denominator is 1 + [(x - 0.5)^2 + 3/4]^2. Not sure if that helps. Maybe a substitution t = x - 0.5? Let me try that. Let t = x - 1/2, so x = t + 1/2. Then the denominator becomes 1 + (t² + 3/4)^2. The numerator 2x² -x becomes 2(t + 1/2)^2 - (t + 1/2). Let me expand that:

2(t² + t + 1/4) - t - 1/2 = 2t² + 2t + 0.5 - t - 0.5 = 2t² + t. So the numerator is 2t² + t. The integral becomes ∫ [2t² + t] / [1 + (t² + 3/4)^2] dt, with the limits changing from x=0 to x=1, which is t=-1/2 to t=1/2.

So I = ∫_{-1/2}^{1/2} [2t² + t] / [1 + (t² + 3/4)^2] dt. Hmm, the integrand is a function of t. Let me check if the integrand is even or odd. The denominator is even in t because (t² + 3/4)^2 is even. The numerator is 2t² + t. The term 2t² is even, and t is odd. So the entire integrand is the sum of an even function (2t² / denominator) and an odd function (t / denominator). When integrating over symmetric limits (-a to a), the integral of the odd part is zero. Therefore, I = ∫_{-1/2}^{1/2} [2t² / denominator] dt + ∫_{-1/2}^{1/2} [t / denominator] dt. The second integral is zero. So I = 2 * ∫_{0}^{1/2} [2t² / denominator] dt. Wait, but the original integrand is even part plus odd part. So the integral from -1/2 to 1/2 is twice the integral from 0 to 1/2 of the even part. The even part is 2t² / denominator. So I = 2 * ∫_{0}^{1/2} [2t² / (1 + (t² + 3/4)^2)] dt. Hmm, simplifying that, I = 4 ∫_{0}^{1/2} [t² / (1 + (t² + 3/4)^2)] dt.

But this still looks complicated. Maybe another substitution. Let me set u = t² + 3/4. Then du/dt = 2t. Hmm, but the numerator here is t², which is (u - 3/4). Let me see. If u = t² + 3/4, then t² = u - 3/4. Then the integral becomes 1 + u². So the integrand becomes (u - 3/4) / (1 + u²) * (dt). But we have du = 2t dt, so t dt = du/2. However, the integrand here is t² / (1 + u²) dt. Since t² = u - 3/4, then the integrand is (u - 3/4)/(1 + u²) * dt. But dt in terms of du is dt = du/(2t). But t = sqrt(u - 3/4). Wait, this might complicate. Let me check:

Wait, u = t² + 3/4, so t = sqrt(u - 3/4). Then dt = (1/(2 sqrt(u - 3/4))) du. So substituting into the integral:

∫ [t² / (1 + u²)] dt = ∫ [ (u - 3/4) / (1 + u²) ] * [1/(2 sqrt(u - 3/4))] du = (1/2) ∫ [ sqrt(u - 3/4) / (1 + u²) ] du. Hmm, that seems more complicated. Maybe this substitution isn't helpful. Let me think of another approach.

Alternatively, perhaps partial fractions or trigonometric substitution. Let me look back at the denominator: 1 + (t² + 3/4)^2. Let me expand that: (t² + 3/4)^2 = t^4 + (3/2)t² + 9/16. So denominator is t^4 + (3/2)t² + 25/16. Hmm, not sure. Alternatively, maybe write denominator as (t^2 + a)^2 + b. Let me see:

(t² + 3/4)^2 + 1 = t^4 + (3/2)t² + 9/16 +1 = t^4 + (3/2)t² + 25/16. Maybe this can be written as a quadratic in t². Let me set y = t². Then denominator becomes y² + (3/2)y + 25/16. Let me check discriminant: (3/2)^2 - 4*1*(25/16) = 9/4 - 25/4 = -16/4 = -4. So it doesn't factor into real terms. Hmm, maybe not helpful.

Alternatively, perhaps integrating 2t² / [1 + (t² + 3/4)^2] from 0 to 1/2. Let me try substitution v = t. Wait, not helpful. Maybe integrating in terms of t. Let me try to split the numerator. Let me write 2t² as 2t² = A*(d/dt denominator) + B. But the derivative of denominator is 2(t² + 3/4)*(2t). Wait, denominator is 1 + (t² + 3/4)^2. So derivative is 2(t² + 3/4)*(2t) = 4t(t² + 3/4). So if I have 2t² = A*4t(t² + 3/4) + B. But this seems complicated. Maybe not the right approach.

Alternatively, perhaps express the integrand as a derivative of some function. Let me think. Let me consider the denominator is 1 + (t² + 3/4)^2. If I can relate the numerator to the derivative of the denominator. The derivative of denominator is 4t(t² + 3/4). The numerator is 2t². Hmm, not directly. But maybe split the numerator:

2t² = (1/2)(4t²) = (1/2)(4t² + 3 - 3) = (1/2)(4t² + 3) - 3/2. Wait, 4t² + 3? Not sure. Alternatively, 2t² = (1/2)(4t² + 3/2) - 3/4. Let me check:

(1/2)(4t² + 3/2) = 2t² + 3/4. So 2t² = (1/2)(4t² + 3/2) - 3/4. Hmm, maybe not helpful. Alternatively, perhaps split the fraction:

2t² / [1 + (t² + 3/4)^2] = A(t) * [ derivative of denominator ] + B(t). But I'm not sure. Alternatively, maybe use substitution z = t² + 3/4. Then dz/dt = 2t. But again, the numerator is 2t². Let me see:

Let z = t² + 3/4, so t² = z - 3/4. Then 2t² = 2z - 3/2. The integrand becomes (2z - 3/2) / (1 + z²) * dt. But dz = 2t dt, so dt = dz/(2t). But t = sqrt(z - 3/4). So dt = dz/(2 sqrt(z - 3/4)). Therefore, the integral becomes ∫ (2z - 3/2)/(1 + z²) * 1/(2 sqrt(z - 3/4)) dz. This seems complicated. Maybe not helpful.

Alternatively, perhaps consider integrating 2t² / (1 + (t² + 3/4)^2) dt. Let me try substitution u = t. Wait, not helpful. Maybe another substitution. Let me think of the denominator as 1 + (t² + 3/4)^2. Let me set u = t² + 3/4. Then denominator is 1 + u². The numerator 2t² = 2(u - 3/4). So the integrand becomes 2(u - 3/4)/(1 + u²) * dt. But du = 2t dt, so t dt = du/2. But we have dt = du/(2t) = du/(2 sqrt(u - 3/4)). So the integral becomes ∫ [2(u - 3/4)/(1 + u²)] * [du/(2 sqrt(u - 3/4))] = ∫ [sqrt(u - 3/4)]/(1 + u²) du. Hmm, this still looks complicated. Maybe another substitution. Let me set v = sqrt(u - 3/4). Then u = v² + 3/4, du = 2v dv. Then the integral becomes ∫ [v / (1 + (v² + 3/4)^2)] * 2v dv = 2 ∫ v² / (1 + (v² + 3/4)^2) dv. Hmm, this seems to lead back to a similar integral. Not helpful.

Alternatively, maybe try integrating numerically? But the problem says to compute the integral analytically first. Hmm. Maybe there's a trick I'm missing. Let me think again about the original integral.

Original integral after integration by parts: π/4 - I, where I = ∫₀¹ [x(2x -1)] / [1 + (x² -x +1)^2] dx. Let me try substitution y = x - 1/2. Wait, similar to before. Let me try substitution t = x - 1/2. Then x = t + 1/2, dx = dt. The limits from x=0 to x=1 become t=-1/2 to t=1/2. Then the denominator becomes 1 + ( (t + 1/2)^2 - (t + 1/2) +1 )^2. Let me compute the inside:

(t + 1/2)^2 - (t + 1/2) +1 = t² + t + 1/4 - t - 1/2 +1 = t² - 1/4 +1 = t² + 3/4. So denominator is 1 + (t² + 3/4)^2, same as before. The numerator x(2x -1) becomes (t + 1/2)(2(t + 1/2) -1) = (t + 1/2)(2t +1 -1) = (t + 1/2)(2t) = 2t(t + 1/2) = 2t² + t. So I = ∫_{-1/2}^{1/2} (2t² + t)/[1 + (t² + 3/4)^2] dt. As before, the integral of the odd function t over symmetric limits is zero, so I = ∫_{-1/2}^{1/2} 2t² / [1 + (t² + 3/4)^2] dt = 2 * ∫_{0}^{1/2} 2t² / [1 + (t² + 3/4)^2] dt. Wait, no. Wait, the integrand 2t² is even, so integrating from -a to a is 2 times from 0 to a. So I = 2 * ∫_{0}^{1/2} [2t² / denominator] dt. So I = 4 ∫_{0}^{1/2} t² / [1 + (t² + 3/4)^2] dt. Hmm. Let me try substitution u = t. Not helpful. Maybe substitution u = tanθ? Let me see. Let me set t² + 3/4 = tanθ. Then denominator becomes 1 + tan²θ = sec²θ. Then dt? Let me compute. t² = tanθ - 3/4. Differentiating both sides: 2t dt = sec²θ dθ. So dt = sec²θ dθ / (2t). But t = sqrt(tanθ - 3/4). Hmm, this seems complicated. Maybe not the way to go.

Alternatively, perhaps use substitution u = t. Wait, not helpful. Let me think again. Maybe there's a symmetry or a trick. Let me consider the original integral again. The integrand is arctan(x² -x +1). Let me check if x² -x +1 can be rewritten. x² -x +1 = (x - 0.5)^2 + 3/4. So arctan((x - 0.5)^2 + 3/4). Not sure. Maybe use substitution y = 1 - x. Let me try substitution x = 1 - t. Then when x=0, t=1; x=1, t=0. The integral becomes ∫₁⁰ arctan((1 - t)^2 - (1 - t) +1) (-dt) = ∫₀¹ arctan((1 - 2t + t²) -1 + t +1) dt. Simplify inside: (1 -2t + t²) -1 + t +1 = t² - t +1. So the integral becomes ∫₀¹ arctan(t² - t +1) dt. Which is the same as the original integral. So the integral is symmetric around x=0.5. So maybe this symmetry can help. But I don't see how immediately.

Alternatively, perhaps adding the original integral and the transformed integral. Let me denote the original integral as J = ∫₀¹ arctan(x² -x +1) dx. Then after substitution x = 1 - t, J = ∫₀¹ arctan(t² - t +1) dt. So J = J, which doesn't help. But maybe adding J and J, but that's trivial. Hmm.

Alternatively, maybe consider J = ∫₀¹ arctan(x² -x +1) dx. Let me consider the integral of arctan(x² -x +1) + arctan(...something...). Maybe there's a complementary angle identity. For example, arctan(a) + arctan(b) = something if ab =1. Let me check if x² -x +1 and another function multiply to 1. Let me see. Suppose we have x² -x +1 and (something) such that (x² -x +1)(something) =1. Let me solve for something: something = 1/(x² -x +1). But not sure if that helps. Alternatively, maybe there's a relation between arctan(x² -x +1) and arctan of another expression. Let me compute tan(arctan(x² -x +1) + arctan(...)). Maybe if I can find an expression that sums to a constant. For example, if arctan(a) + arctan(b) = π/4 or something. Let me try to see.

Let me compute tan(arctan(x² -x +1) + arctan(y)). Let me set this equal to something. The tangent of sum is [ (x² -x +1) + y ] / [1 - (x² -x +1)y]. Suppose I want this to be a constant. For example, if I can find y such that this expression is 1, which would imply that the sum is π/4. Let me set [ (x² -x +1) + y ] / [1 - (x² -x +1)y ] =1. Then (x² -x +1) + y = 1 - (x² -x +1)y. Rearranging: (x² -x +1) + y + (x² -x +1)y -1 =0. Let me factor: (x² -x +1)(1 + y) + y -1 =0. Hmm, not sure. Let me solve for y:

From (x² -x +1) + y = 1 - (x² -x +1)y,

Bring all terms to left:

(x² -x +1) + y -1 + (x² -x +1)y =0

Factor y:

(x² -x +1 -1) + y(1 + x² -x +1) =0

Simplify:

(x² -x) + y(x² -x +2) =0

Solve for y:

y = - (x² -x)/(x² -x +2)

So if we set y = - (x² -x)/(x² -x +2), then arctan(x² -x +1) + arctan(y) = arctan(1) = π/4. Wait, is that correct? Let me check with specific x. Let me take x=0. Then x² -x +1 =1, y = - (0 -0)/(0 -0 +2)=0. So arctan(1) + arctan(0) = π/4 +0=π/4. Correct. Another test: x=1. x² -x +1=1-1+1=1, y= - (1 -1)/(1 -1 +2)=0. Same as before. Hmm, interesting. Let me try x=0.5. x² -x +1=0.25 -0.5 +1=0.75. y= - (0.25 -0.5)/(0.25 -0.5 +2)= - (-0.25)/(1.75)=0.25/1.75=1/7. So arctan(0.75) + arctan(1/7). Let me compute tan(arctan(0.75) + arctan(1/7)):

(0.75 + 1/7)/(1 - 0.75*(1/7)) = ( (21/28 + 4/28) ) / (1 - 3/28) = (25/28)/(25/28) =1. So yes, the sum is π/4. Therefore, arctan(x² -x +1) + arctan( - (x² -x)/(x² -x +2) ) = π/4. Wait, but the second arctan has a negative argument. So arctan(-y) = -arctan(y). So the identity becomes arctan(x² -x +1) - arctan( (x² -x)/(x² -x +2) ) = π/4. Therefore, arctan(x² -x +1) = π/4 + arctan( (x² -x)/(x² -x +2) ). 

This is a useful identity! Therefore, the original integral J can be written as ∫₀¹ [π/4 + arctan( (x² -x)/(x² -x +2) ) ] dx = π/4 *1 + ∫₀¹ arctan( (x² -x)/(x² -x +2) ) dx. So J = π/4 + ∫₀¹ arctan( (x² -x)/(x² -x +2) ) dx.

Now, let me denote K = ∫₀¹ arctan( (x² -x)/(x² -x +2) ) dx. So J = π/4 + K. But then, if I can relate K back to J somehow. Let me see. Let me look at the argument of arctan in K: (x² -x)/(x² -x +2). Let me denote this as (x² -x)/(x² -x +2) = [ (x² -x +2) -2 ] / (x² -x +2) = 1 - 2/(x² -x +2). Hmm, not sure. Alternatively, maybe substitution. Let me set t = 1 -x. Then when x=0, t=1; x=1, t=0. Then K becomes ∫₁⁰ arctan( ( (1 -t)^2 - (1 -t) ) / ( (1 -t)^2 - (1 -t) +2 ) ) (-dt) = ∫₀¹ arctan( ( (1 - 2t + t² -1 +t ) / (1 - 2t + t² -1 +t +2 ) ) dt. Simplify numerator: 1 -2t + t² -1 +t = t² -t. Denominator: 1 -2t + t² -1 +t +2 = t² -t +2. So K = ∫₀¹ arctan( (t² -t)/ (t² -t +2) ) dt. Which is the same as K = ∫₀¹ arctan( (x² -x)/(x² -x +2) ) dx. So K is the same as the original integral but with the argument of arctan being (x² -x)/(x² -x +2). But how does this help?

Wait, earlier we had J = π/4 + K. If I can express K in terms of J, maybe we can solve for J. Let me see. Let me compute K. Let me consider the argument of arctan in K: (x² -x)/(x² -x +2). Let me denote this as A/B, where A = x² -x and B = x² -x +2. So A/B = (B -2)/B = 1 - 2/B. So arctan(A/B) = arctan(1 - 2/B). Not sure. Alternatively, maybe use the identity we had before. Let me see if there's a similar identity for K. Let me compute tan(arctan(A/B) + arctan(something)) to get a constant. Let me try:

Let’s suppose arctan(A/B) + arctan(y) = something. Let me try to find y such that tan(sum) is a constant. Let me set tan(sum) = [ (A/B) + y ] / [1 - (A/B)y ] = C. Let me choose C=1 to get sum=π/4. So:

(A/B + y)/(1 - (A/B)y) =1 → A/B + y =1 - (A/B)y → A/B + y + (A/B)y -1 =0 → y(1 + A/B) =1 - A/B → y = (1 - A/B)/(1 + A/B) = (B - A)/(B + A). 

So if we set y = (B - A)/(B + A), then arctan(A/B) + arctan(y) = π/4. Let me check with specific x. Let x=0: A=0-0=0, B=0-0+2=2. So y=(2 -0)/(2 +0)=1. So arctan(0) + arctan(1) =0 + π/4=π/4. Correct. x=1: A=1-1=0, B=2. Same as above. x=0.5: A=0.25 -0.5=-0.25, B=0.25 -0.5 +2=1.75. y=(1.75 - (-0.25))/(1.75 + (-0.25))=2/1.5=4/3. So arctan(-0.25/1.75) + arctan(4/3). Let me compute tan(arctan(-1/7) + arctan(4/3)):

(-1/7 +4/3)/(1 - (-1/7)(4/3)) = ( ( -3/21 + 28/21 ) ) / (1 + 4/21 ) = (25/21)/(25/21)=1. So yes, sum is π/4. Therefore, arctan(A/B) + arctan( (B - A)/(B + A) ) = π/4. Therefore, arctan(A/B) = π/4 - arctan( (B - A)/(B + A) ). Therefore, K = ∫₀¹ [π/4 - arctan( (B - A)/(B + A) ) ] dx = π/4 - ∫₀¹ arctan( (B - A)/(B + A) ) dx. But B - A = (x² -x +2) - (x² -x) =2. B + A = (x² -x +2) + (x² -x) =2x² -2x +2. So (B - A)/(B + A) =2/(2x² -2x +2)=2/(2(x² -x +1))=1/(x² -x +1). Therefore, K = π/4 - ∫₀¹ arctan(1/(x² -x +1)) dx. But arctan(1/z) = π/2 - arctan(z) if z>0. Since x² -x +1 is always positive (discriminant (-1)^2 -4*1*1= -3 <0), so it's always positive. Therefore, arctan(1/(x² -x +1)) = π/2 - arctan(x² -x +1). Therefore, K = π/4 - ∫₀¹ [π/2 - arctan(x² -x +1)] dx = π/4 - π/2 *1 + ∫₀¹ arctan(x² -x +1) dx = -π/4 + J. 

But we had earlier J = π/4 + K. So substituting K = -π/4 + J into J = π/4 + K gives J = π/4 + (-π/4 + J) → J = J. Hmm, that's a tautology. So this approach doesn't help. Wait, but maybe combining the two equations. We have:

J = π/4 + K

K = -π/4 + J

Substitute K into J:

J = π/4 + (-π/4 + J) → J = J. Which is an identity, so no new information. Hmm. So this approach doesn't help. Maybe need to find another relation.

Alternatively, let's go back to the original integral after integration by parts: J = π/4 - I, where I = ∫₀¹ [x(2x -1)] / [1 + (x² -x +1)^2] dx. Let me try to compute I. Let me consider substitution u = x² -x +1. Then du = (2x -1) dx. Notice that the numerator is x(2x -1) dx. Let me write x(2x -1) dx = x du. So I = ∫ x du / (1 + u²). But we need to express x in terms of u. From u = x² -x +1, we can solve for x. Let me rearrange: x² -x + (1 -u) =0. Quadratic equation: x = [1 ± sqrt(1 -4(1 -u))]/2 = [1 ± sqrt(4u -3)]/2. Hmm, this complicates things. Alternatively, maybe integrate by parts again. Let me try integrating I = ∫ x(2x -1)/[1 + (x² -x +1)^2] dx. Let me set v = x, dw = (2x -1)/[1 + (x² -x +1)^2] dx. Then dv = dx, and w is the integral of dw. But integrating dw would require finding the integral of (2x -1)/[1 + (x² -x +1)^2] dx. Let me check if this is a standard form. Let me set z = x² -x +1. Then dz = (2x -1) dx. So dw = dz / (1 + z²). Therefore, the integral of dw is arctan(z) + C. So w = arctan(x² -x +1). Therefore, integrating by parts, I = v w - ∫ w dv = x arctan(x² -x +1) |₀¹ - ∫₀¹ arctan(x² -x +1) dx. Wait, but this is the same as the original integration by parts! Because the original J = ∫ arctan(...) dx = π/4 - I, and here I = [x arctan(...)]₀¹ - J. Which gives I = π/4 - J. Therefore, substituting back into J = π/4 - I gives J = π/4 - (π/4 - J) → J = π/4 - π/4 + J → 0 =0. Again, a tautology. So this approach doesn't help.

Hmm, so maybe I = π/4 - J, and J = π/4 - I, which gives J = π/4 - (π/4 - J) → J = J. So this doesn't help. So perhaps we need to find another way to compute I.

Let me go back to the integral I = ∫₀¹ [x(2x -1)] / [1 + (x² -x +1)^2] dx. Let me try substitution z = x - 0.5. Then x = z + 0.5, dx = dz. The limits become z = -0.5 to z=0.5. The numerator: (z + 0.5)(2(z + 0.5) -1) = (z + 0.5)(2z +1 -1) = (z + 0.5)(2z) = 2z(z + 0.5) = 2z² + z. The denominator: 1 + ( (z + 0.5)^2 - (z + 0.5) +1 )^2. Let me compute inside the square:

(z + 0.5)^2 - (z + 0.5) +1 = z² + z + 0.25 - z -0.5 +1 = z² -0.25 +1 = z² +0.75. So denominator is 1 + (z² +0.75)^2. So I = ∫_{-0.5}^{0.5} (2z² + z)/[1 + (z² +0.75)^2] dz. As before, the integral of the odd function z over symmetric limits is zero. So I = ∫_{-0.5}^{0.5} 2z² / [1 + (z² +0.75)^2] dz = 2 * ∫_{0}^{0.5} 2z² / [1 + (z² +0.75)^2] dz = 4 ∫_{0}^{0.5} z² / [1 + (z² +0.75)^2] dz. Wait, no. Wait, the integrand is even, so integrating from -0.5 to 0.5 is twice the integral from 0 to 0.5. So I = 2 * ∫_{0}^{0.5} (2z² + z)/[denominator] dz. But since the odd part integrates to zero, it's 2 * ∫_{0}^{0.5} 2z² / denominator dz. So I = 4 ∫_{0}^{0.5} z² / [1 + (z² +0.75)^2] dz. Let me denote this integral as L. So I =4L.

Now, let me focus on computing L = ∫_{0}^{0.5} z² / [1 + (z² +0.75)^2] dz. Let me make substitution t = z. Hmm, not helpful. Let me try substitution u = z² +0.75. Then du/dz = 2z. So z dz = du/2. But the integrand is z² / denominator. Since u = z² +0.75, z² = u -0.75. So L = ∫ [u -0.75]/[1 + u²] * (dz). But dz = du/(2z) = du/(2 sqrt(u -0.75)). So L = ∫ [u -0.75]/[1 + u²] * 1/(2 sqrt(u -0.75)) du = (1/2) ∫ sqrt(u -0.75)/[1 + u²] du. This seems complicated. Let me try another substitution. Let me set v = sqrt(u -0.75). Then u = v² +0.75, du = 2v dv. Then L becomes (1/2) ∫ v / [1 + (v² +0.75)^2] * 2v dv. Wait, no. Let me substitute:

L = (1/2) ∫ sqrt(u -0.75)/(1 + u²) du. With u = v² +0.75, du=2v dv. So sqrt(u -0.75) = v. Therefore, L = (1/2) ∫ v / [1 + (v² +0.75)^2 ] * 2v dv = ∫ v² / [1 + (v² +0.75)^2 ] dv. Hmm, this seems to lead back to a similar integral. Not helpful.

Alternatively, maybe use substitution t = v. Not helpful. Let me try to expand the denominator. (v² +0.75)^2 = v^4 + 1.5v² + 0.5625. So denominator is v^4 +1.5v² +1.5625. Let me see if this factors. Let me check discriminant for quadratic in v²: 1.5^2 -4*1*1.5625=2.25 -6.25= -4. So it doesn't factor. Hmm. Maybe partial fractions? Not sure.

Alternatively, maybe use substitution w = v. Not helpful. Alternatively, consider integrating v² / (v^4 + 1.5v² +1.5625). Let me write denominator as v^4 + 1.5v² +1.5625. Let me see if this can be written as (v² + a)^2 + b. Let me compute (v² + a)^2 = v^4 +2a v² +a². Comparing to denominator: v^4 +1.5v² +1.5625. So 2a=1.5 → a=0.75. Then a²=0.5625. So denominator is (v² +0.75)^2 +1.5625 -0.5625= (v² +0.75)^2 +1. So denominator = (v² +0.75)^2 +1. Therefore, L = ∫ v² / [ (v² +0.75)^2 +1 ] dv. Hmm, maybe substitution y = v² +0.75. Then dy = 2v dv. But the numerator is v² = y -0.75. So L = ∫ (y -0.75)/ (y² +1) * (dv). But dy=2v dv → dv= dy/(2v). But v = sqrt(y -0.75). So dv= dy/(2 sqrt(y -0.75)). Therefore, L = ∫ (y -0.75)/(y² +1) * 1/(2 sqrt(y -0.75)) dy = (1/2) ∫ sqrt(y -0.75)/(y² +1) dy. This seems to lead back to the same integral. Not helpful.

Hmm, this is getting too complicated. Maybe there's a different approach. Let me think back to the original problem. The integral J = ∫₀¹ arctan(x² -x +1) dx. After integration by parts, J = π/4 - I, where I is complicated. But maybe there's a way to express I in terms of J. But earlier attempts didn't work. Alternatively, maybe consider differentiating under the integral sign. Let me define a parameter a, and consider J(a) = ∫₀¹ arctan(a(x² -x +1)) dx. Then compute J'(a) and integrate. But this might not help. Let me try:

J'(a) = ∫₀¹ [ (x² -x +1) / (1 + a²(x² -x +1)^2) ] dx. Not sure if this is easier. For a=1, this is the derivative. But integrating this with respect to a might not be straightforward.

Alternatively, maybe use series expansion of arctan. The arctan(z) can be expanded as a power series for |z| ≤1. But x² -x +1. Let me check the maximum value of x² -x +1 on [0,1]. The function x² -x +1 is a quadratic opening upwards with vertex at x=0.5. At x=0.5, value is (0.25) -0.5 +1=0.75. The minimum is 0.75, and at x=0 or 1, it's 1. So the argument of arctan ranges from 0.75 to1. So the series expansion around z=0.75 or z=1 might converge, but integrating term-by-term might be complicated. Not sure.

Alternatively, maybe use substitution t = x -0.5. Then x = t +0.5, dx=dt. The integral becomes ∫_{-0.5}^{0.5} arctan( (t +0.5)^2 - (t +0.5) +1 ) dt. Simplify inside: t² + t +0.25 -t -0.5 +1 = t² +0.75. So J = ∫_{-0.5}^{0.5} arctan(t² +0.75) dt. Since the integrand is even, J = 2 ∫₀^{0.5} arctan(t² +0.75) dt. Hmm, but this still doesn't help much. Maybe integrate by parts again. Let me set u = arctan(t² +0.75), dv = dt. Then du = [2t] / [1 + (t² +0.75)^2] dt, v = t. So J = 2 [ t arctan(t² +0.75) |₀^{0.5} - ∫₀^{0.5} t * [2t / (1 + (t² +0.75)^2) ] dt ].

Compute boundary terms: at t=0.5, 0.5 arctan(0.25 +0.75)=0.5 arctan(1)=0.5 * π/4=π/8. At t=0, 0. So boundary term is π/8. Then the remaining integral is -2 * ∫₀^{0.5} [2t² / (1 + (t² +0.75)^2) ] dt. Which is -2 * (2 ∫₀^{0.5} t² / denominator dt) = -4L, where L was defined earlier. But J = 2 [ π/8 -4L ] = π/4 -8L. But earlier we had J = π/4 - I, and I =4L. So J = π/4 -4L. But according to this, J = π/4 -8L. Contradiction? Wait, no. Let me check:

Wait, J = 2 [ π/8 - 2 ∫₀^{0.5} t² / denominator dt ] = π/4 -4 ∫₀^{0.5} t² / denominator dt. But I =4L =4 ∫₀^{0.5} t² / denominator dt. So J = π/4 - I. Which matches the previous result. So this doesn't help.

Hmm, I'm stuck here. Maybe I need to accept that the integral I cannot be expressed in terms of elementary functions and look for another approach. Wait, but the problem says to compute the integral analytically. So there must be an exact answer. Maybe I missed a trick earlier.

Let me go back to the identity we had: arctan(x² -x +1) = π/4 + arctan( (x² -x)/(x² -x +2) ). Then J = π/4 + K, where K = ∫₀¹ arctan( (x² -x)/(x² -x +2) ) dx. Then, using the same identity for K. Let me apply the identity to K. Let me set y = (x² -x)/(x² -x +2). Let me compute arctan(y) = π/4 - arctan( (1 - y)/(1 + y) ). Wait, no. Wait, from the previous identity, arctan(a) + arctan(b) = π/4 when ab=1. But in this case, y = (x² -x)/(x² -x +2). Let me compute 1/y = (x² -x +2)/(x² -x). So 1/y =1 + 2/(x² -x). Not sure. Alternatively, maybe use the identity again. Let me see:

If we have arctan(y) = π/4 - arctan( (1 - y)/(1 + y) ). Wait, not sure. Alternatively, let me use the identity as before. Let me set arctan(y) + arctan(z) = π/4. Then z = (1 - y)/(1 + y). Wait, but this is similar to before. Let me check:

If arctan(y) + arctan(z) = π/4, then tan(arctan(y) + arctan(z)) =1. So (y + z)/(1 - yz)=1. Solving for z: y + z =1 - yz → z(1 + y) =1 - y → z=(1 - y)/(1 + y). So yes, arctan(y) + arctan( (1 - y)/(1 + y) )=π/4. Therefore, arctan(y) = π/4 - arctan( (1 - y)/(1 + y) ). Therefore, K = ∫₀¹ [π/4 - arctan( (1 - y)/(1 + y) ) ] dx, where y = (x² -x)/(x² -x +2). So K = π/4 - ∫₀¹ arctan( (1 - y)/(1 + y) ) dx. Let me compute (1 - y)/(1 + y):

1 - y =1 - (x² -x)/(x² -x +2) = [ (x² -x +2) - (x² -x) ] / (x² -x +2) =2/(x² -x +2).

1 + y =1 + (x² -x)/(x² -x +2) = [ (x² -x +2) + (x² -x) ] / (x² -x +2) = (2x² -2x +2)/ (x² -x +2) =2(x² -x +1)/(x² -x +2).

Therefore, (1 - y)/(1 + y) = [2/(x² -x +2)] / [2(x² -x +1)/(x² -x +2)] ] = [2/(x² -x +2)] * [ (x² -x +2)/2(x² -x +1) ) ] =1/(x² -x +1). Therefore, K = π/4 - ∫₀¹ arctan(1/(x² -x +1)) dx. But as before, arctan(1/z) = π/2 - arctan(z) for z>0. So K = π/4 - ∫₀¹ [π/2 - arctan(x² -x +1)] dx = π/4 - π/2 + ∫₀¹ arctan(x² -x +1) dx = -π/4 + J. Therefore, J = π/4 + K = π/4 + (-π/4 + J) → J = J. Again, no help.

This seems to suggest that the integral J is equal to itself, which is a tautology, so this approach doesn't help. Therefore, perhaps the integral cannot be expressed in terms of elementary functions and requires a special function or a clever substitution. Alternatively, maybe there's a substitution that I haven't tried yet.

Let me try to compute I numerically to see if it can be expressed in terms of known constants. But the problem says to compute it analytically first. Alternatively, maybe the integral simplifies to a combination of π and ln terms. Let me consider the integral I = ∫₀¹ [x(2x -1)] / [1 + (x² -x +1)^2] dx. Let me try substitution u = x² -x +1. Then du = (2x -1) dx. Wait, the numerator is x(2x -1) dx. So x(2x -1) dx = x du. But x in terms of u. From u =x² -x +1, we can write x² = u +x -1. So x² -x +1 = u. Wait, not helpful. Alternatively, x = [1 ± sqrt(4u -3)]/2. Hmm, complicated.

Alternatively, let me split the numerator x(2x -1) =2x² -x. Let me write this as 2x² -x = A*(d/dx denominator) + B. The derivative of denominator is 2*(x² -x +1)*(2x -1). So denominator derivative is 2*(x² -x +1)*(2x -1). Let me see:

Let me set 2x² -x = A*2*(x² -x +1)*(2x -1) + B. But this seems complicated. Let me check if this is possible. Let me expand the right-hand side:

A*2*(x² -x +1)*(2x -1) + B = 2A*(2x³ -x² +2x² -x +2x -1) + B = 2A*(2x³ +x² +x -1) + B. But the left-hand side is 2x² -x. So equating coefficients:

For x³: 4A =0 → A=0. Then for x²: 2A*1=0=2x² coefficient is 2. Contradiction. So this approach doesn't work.

Alternatively, maybe write the integrand as a derivative of some function. Let me consider the denominator 1 + (x² -x +1)^2. Let me compute the derivative: 2(x² -x +1)(2x -1). The numerator is x(2x -1). So the numerator is x(2x -1) = [x/(2(x² -x +1))] * derivative of denominator. So the integrand can be written as [x/(2(x² -x +1))] * d/dx [denominator] / denominator. Which is [x/(2(x² -x +1))] * d/dx [denominator] / denominator. This is similar to [x/(2(x² -x +1))] * d/dx [ln(denominator)]. But integrating this would require integrating x/(2(x² -x +1)) * d/dx [ln(denominator)] dx. Not sure.

Alternatively, let me write the integrand as x(2x -1)/[1 + (x² -x +1)^2] = x(2x -1)/denominator. Let me split the fraction into two terms. Let me write x(2x -1) = (2x² -x). Let me try to express this as a combination of the derivative of the denominator and another term. The derivative of denominator is 2(x² -x +1)(2x -1). Let me compute:

Let me write 2x² -x = A*(x² -x +1)(2x -1) + B*(something). Let me see:

Suppose 2x² -x = A*(x² -x +1)(2x -1) + B*(x² -x +1) + C*(2x -1) + D. Let me expand the right-hand side:

A*(2x³ -x² +2x² -x +2x -1) + Bx² -Bx +B + C*2x -C +D.

Simplify:

A*(2x³ +x² +x -1) + Bx² -Bx +B +2Cx -C +D.

Combine like terms:

2A x³ + (A + B) x² + (A -B +2C) x + (-A + B -C +D).

Set equal to left-hand side 2x² -x. Therefore, coefficients:

For x³: 2A =0 → A=0.

For x²: A + B =2 → 0 + B=2 → B=2.

For x: A -B +2C = -1 → 0 -2 +2C =-1 → 2C=1 → C=0.5.

For constant term: -A + B -C +D=0 → 0 +2 -0.5 +D=0 → D= -1.5.

Therefore, 2x² -x =0*(...) +2*(x² -x +1) +0.5*(2x -1) -1.5. Let me verify:

2*(x² -x +1) =2x² -2x +2

0.5*(2x -1)=x -0.5

-1.5

Total:2x² -2x +2 +x -0.5 -1.5=2x² -x +0. Correct. So 2x² -x=2(x² -x +1) +0.5(2x -1) -1.5. Therefore, the integrand becomes [2(x² -x +1) +0.5(2x -1) -1.5]/[1 + (x² -x +1)^2]. Therefore, split into three terms:

I = ∫₀¹ [2(x² -x +1)/denominator +0.5(2x -1)/denominator -1.5/denominator] dx.

Let me handle each term separately:

First term: 2(x² -x +1)/[1 + (x² -x +1)^2]. Let me set u =x² -x +1. Then du=(2x -1)dx. So the first term is 2u/(1 +u²). The integral is ∫ 2u/(1 +u²) du = ln(1 +u²) + C. Evaluated from x=0 to x=1. At x=1, u=1-1 +1=1. At x=0, u=0 -0 +1=1. Wait, both limits? So the first term integral is ln(1 +1²) - ln(1 +1²)=0. So the first term contributes nothing.

Second term:0.5*(2x -1)/denominator. Let me set u =x² -x +1. Then du=(2x -1)dx. So the second term is 0.5*du/(1 +u²). The integral is 0.5 arctan(u) + C. Evaluated from 0 to1. At x=1, u=1. At x=0, u=1. So again, 0.5(arctan(1) - arctan(1))=0. So the second term also contributes nothing.

Third term: -1.5/denominator. So I =0 +0 -1.5 ∫₀¹ 1/[1 + (x² -x +1)^2] dx. Therefore, I = -1.5 ∫₀¹ 1/[1 + (x² -x +1)^2] dx. Let me denote this integral as M = ∫₀¹ 1/[1 + (x² -x +1)^2] dx. So I = -1.5 M.

Now, we need to compute M. Let me try substitution t =x -0.5. Then x =t +0.5, dx=dt. The integral becomes ∫_{-0.5}^{0.5} 1/[1 + (t² +0.75)^2] dt. Since the integrand is even, M=2 ∫₀^{0.5} 1/[1 + (t² +0.75)^2] dt. Let me compute this integral. Let me set u =t. Hmm, not helpful. Let me try substitution u =t² +0.75. Then du=2t dt. But the integrand is 1/(1 +u²). So M=2 ∫_{0.75}^{0.5² +0.75} 1/(1 +u²) * (dt). Wait, but t= sqrt(u -0.75). So dt= du/(2 sqrt(u -0.75)). The limits when t=0, u=0.75; t=0.5, u=0.25 +0.75=1. So M=2 ∫_{0.75}^1 1/(1 +u²) * 1/(2 sqrt(u -0.75)) du = ∫_{0.75}^1 1/(1 +u²) * 1/sqrt(u -0.75) du. This still looks complicated. Let me try substitution v = sqrt(u -0.75). Then u =v² +0.75, du=2v dv. The integral becomes ∫_{0}^{sqrt(0.25)} 1/(1 + (v² +0.75)^2) * 1/v *2v dv = 2 ∫_{0}^{0.5} 1/(1 + (v² +0.75)^2) dv. So M=2 ∫₀^{0.5} 1/[1 + (v² +0.75)^2] dv. Let me denote this as N. So M=2N.

Now, N=∫₀^{0.5} 1/[1 + (v² +0.75)^2] dv. Let me expand the denominator: (v² +0.75)^2 +1= v^4 +1.5v² +0.5625 +1= v^4 +1.5v² +1.5625. Let me check if this can be factored. Let me set v^4 +1.5v² +1.5625= (v² + av +b)(v² -av +b). Multiplying out: v^4 + (2b -a²)v² +b². Comparing coefficients:

2b -a²=1.5

b²=1.5625 → b=1.25 (since b>0)

Then 2*1.25 -a²=1.5 → 2.5 -a²=1.5 → a²=1 → a=1.

Therefore, denominator factors as (v² +v +1.25)(v² -v +1.25). Therefore, N=∫₀^{0.5} 1/[(v² +v +1.25)(v² -v +1.25)] dv. Let me use partial fractions. Let me write:

1/[(v² +v +1.25)(v² -v +1.25)] = (Av +B)/(v² +v +1.25) + (Cv +D)/(v² -v +1.25).

Multiply both sides by the denominator:

1 = (Av +B)(v² -v +1.25) + (Cv +D)(v² +v +1.25).

Expand the right-hand side:

Av(v² -v +1.25) + B(v² -v +1.25) + Cv(v² +v +1.25) + D(v² +v +1.25)

= Av³ -Av² +1.25Av + Bv² -Bv +1.25B + Cv³ +Cv² +1.25Cv +Dv² +Dv +1.25D

Combine like terms:

(A + C)v³ + (-A + B + C + D)v² + (1.25A -B +1.25C + D)v + (1.25B +1.25D).

Set equal to 1. Therefore, coefficients:

For v³: A + C =0.

For v²: -A + B + C + D=0.

For v:1.25A -B +1.25C + D=0.

For constant term:1.25B +1.25D=1.

Now, solve this system:

From A + C=0 → C= -A.

Substitute C= -A into the second equation:

-A + B -A + D=0 → -2A + B + D=0.

Third equation:1.25A -B +1.25*(-A) + D=0 →1.25A -B -1.25A + D=0 → -B + D=0 → D=B.

Fourth equation:1.25B +1.25D=1. Since D=B, this becomes 1.25B +1.25B=1 →2.5B=1 → B=0.4. Therefore, D=0.4.

From the second equation: -2A +0.4 +0.4=0 → -2A +0.8=0 → A=0.4.

Then C= -0.4.

Therefore, the partial fractions are:

(0.4v +0.4)/(v² +v +1.25) + (-0.4v +0.4)/(v² -v +1.25).

So N=∫₀^{0.5} [ (0.4v +0.4)/(v² +v +1.25) + (-0.4v +0.4)/(v² -v +1.25) ] dv.

Let me split this into two integrals:

N=0.4 ∫₀^{0.5} (v +1)/(v² +v +1.25) dv +0.4 ∫₀^{0.5} (-v +1)/(v² -v +1.25) dv.

Let me compute each integral separately.

First integral: I1 = ∫ (v +1)/(v² +v +1.25) dv.

Let me complete the square in the denominator: v² +v +1.25 = (v +0.5)^2 +1. Let me set w =v +0.5. Then dw=dv. When v=0, w=0.5; v=0.5, w=1. The integral becomes:

∫ (w -0.5 +1)/(w² +1) dw = ∫ (w +0.5)/(w² +1) dw = ∫ w/(w² +1) dw +0.5 ∫1/(w² +1) dw.

Integrate:

0.5 ln(w² +1) +0.5 arctan(w) + C.

Evaluated from w=0.5 to w=1:

[0.5 ln(1 +1) +0.5 arctan(1)] - [0.5 ln(0.25 +1) +0.5 arctan(0.5)]

=0.5 ln(2) +0.5*(π/4) -0.5 ln(1.25) -0.5 arctan(0.5).

Second integral: I2 = ∫ (-v +1)/(v² -v +1.25) dv.

Complete the square in the denominator: v² -v +1.25 = (v -0.5)^2 +1. Let me set z =v -0.5. Then dz=dv. When v=0, z=-0.5; v=0.5, z=0. The integral becomes:

∫ (- (z +0.5) +1)/(z² +1) dz = ∫ (-z -0.5 +1)/(z² +1) dz = ∫ (-z +0.5)/(z² +1) dz.

Split into two terms:

-∫ z/(z² +1) dz +0.5 ∫1/(z² +1) dz.

Integrate:

-0.5 ln(z² +1) +0.5 arctan(z) + C.

Evaluated from z=-0.5 to z=0:

[-0.5 ln(0 +1) +0.5 arctan(0)] - [-0.5 ln(0.25 +1) +0.5 arctan(-0.5)]

= [0 +0] - [-0.5 ln(1.25) +0.5*(-arctan(0.5))]

=0.5 ln(1.25) +0.5 arctan(0.5).

Therefore, combining I1 and I2:

N=0.4 [ (0.5 ln2 + π/8 -0.5 ln1.25 -0.5 arctan0.5) + (0.5 ln1.25 +0.5 arctan0.5) ) ].

Simplify inside the brackets:

0.5 ln2 + π/8 -0.5 ln1.25 -0.5 arctan0.5 +0.5 ln1.25 +0.5 arctan0.5 =0.5 ln2 + π/8.

Therefore, N=0.4*(0.5 ln2 + π/8)=0.2 ln2 + π/20.

Therefore, M=2N=0.4 ln2 + π/10.

Then I= -1.5 M= -1.5*(0.4 ln2 + π/10)= -0.6 ln2 - 3π/20.

Therefore, the original integral J=π/4 - I= π/4 - (-0.6 ln2 -3π/20)= π/4 +0.6 ln2 +3π/20.

Convert π/4 to 5/20 and 3π/20 to get total π*(5/20 +3/20)=π*8/20=2π/5.

So J=2π/5 +0.6 ln2.

But 0.6 is 3/5. So J=2π/5 + (3/5) ln2.

Therefore, the exact answer is (2π/5) + (3/5) ln2. Which can be written as (2π +3 ln2)/5.

Now, let's compute the numerical approximation. Compute 2π ≈6.283185307, 3 ln2≈3*0.6931471806≈2.079441542. Sum≈6.283185307 +2.079441542≈8.362626849. Divide by5:≈1.6725253698. Rounded to 10 decimal places:1.6725253698≈1.6725253698.

But let me verify with more precise calculations:

2π =6.283185307179586

3 ln2=3*0.6931471805599453=2.0794415416798357

Sum=6.283185307179586 +2.0794415416798357=8.362626848859422

Divide by5:8.362626848859422 /5=1.6725253697718844

Rounded to 10 decimal places:1.6725253698.

So the numerical approximation is approximately1.6725253698.
</think>

{"answer": "\\frac{2\\pi + 3\\ln 2}{5}", "numerical_answer": "1.6725253698"}