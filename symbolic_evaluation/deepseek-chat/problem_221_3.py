import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the constant coefficient: 9/16
numerator = mp.mpf(9)
denominator = mp.mpf(16)
coefficient = numerator / denominator

# Multiply the coefficient by pi to obtain the result
result = coefficient * mp.pi

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))