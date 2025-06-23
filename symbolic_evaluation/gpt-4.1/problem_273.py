import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the first integral: I1 = ∫₀^{π/2} sin³θ arctan(sinθ) dθ
# Using the known closed-form expression: 
# I1 = (π(√2 - 1))/8 - 1/6 + (√2/6) arcsin(1/√3)
term1 = (mp.pi * (mp.sqrt(2) - 1)) / 8
term2 = -1/mp.mpf(6)
term3 = (mp.sqrt(2) / 6) * mp.asin(1/mp.sqrt(3))
I1 = term1 + term2 + term3

# Compute the second integral: I2 = ∫₀^{π/2} ln(1 + sin²θ) dθ
# Using the known closed-form expression: 
# I2 = π ln((1 + √2)/2)
I2 = mp.pi * mp.log((1 + mp.sqrt(2)) / 2)

# Combine the integrals according to the given expression
# result = (1/3)*I1 - π/24 + (1/6)*I2
result = (1/mp.mpf(3)) * I1 - mp.pi/24 + (1/mp.mpf(6)) * I2

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))