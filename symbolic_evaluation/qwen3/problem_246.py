import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerator and denominator
numerator = 2457
denominator = 256

# Compute the coefficient 2457/256
coefficient = mp.mpf(numerator) / mp.mpf(denominator)

# Compute pi squared
pi_squared = mp.pi ** 2

# Calculate the final result
result = coefficient * pi_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))