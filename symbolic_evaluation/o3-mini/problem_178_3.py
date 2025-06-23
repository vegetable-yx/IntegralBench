import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute term1: [ √2 * π * hyp1f2(-1/4; 1/4, 3/2; -1) ] / [8 * (Γ(5/4))^2]
# Using reflection formula: Γ(-1/4) = -√2 * π / Γ(5/4)

# Calculate hypergeometric function for term1
hyp1 = mp.hyp1f2(mp.mpf('-0.25'), [mp.mpf('0.25'), mp.mpf('1.5')], -1)

# Compute gamma(5/4) and its square
gamma_54 = mp.gamma(mp.mpf('1.25'))
gamma_54_sq = gamma_54 * gamma_54

# Numerator: √2 * π * hyp1
num1 = mp.sqrt(2) * mp.pi * hyp1

# Denominator: 8 * gamma_54^2
den1 = 8 * gamma_54_sq

# Term1: num1 / den1
term1 = num1 / den1

# Compute term2: [ Γ(1/4) * hyp1f2(1/4; 3/4, 5/4; -1) ] / [8 * Γ(7/4)]

# Calculate hypergeometric function for term2
hyp2 = mp.hyp1f2(mp.mpf('0.25'), [mp.mpf('0.75'), mp.mpf('1.25')], -1)

# Compute gamma(1/4) and gamma(7/4)
gamma_14 = mp.gamma(mp.mpf('0.25'))
gamma_74 = mp.gamma(mp.mpf('1.75'))

# Numerator: gamma_14 * hyp2
num2 = gamma_14 * hyp2

# Denominator: 8 * gamma_74
den2 = 8 * gamma_74

# Term2: num2 / den2
term2 = num2 / den2

# Final result: term1 + term2
result = term1 + term2

# Print result to 10 decimal places
print(mp.nstr(result, n=10))