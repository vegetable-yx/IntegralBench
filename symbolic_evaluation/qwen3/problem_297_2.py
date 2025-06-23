import mpmath as mp
mp.dps = 15

# Calculate the fractional coefficient 64/225
numerator = 64
denominator = 225
coefficient = mp.mpf(numerator) / denominator

# Compute π squared using mpmath's pi constant
pi_squared = mp.pi ** 2

# Calculate final result by multiplying components
result = coefficient * pi_squared

print(mp.nstr(result, n=10))