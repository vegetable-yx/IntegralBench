import mpmath as mp

# Set the internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the square root of 30
sqrt_30 = mp.sqrt(30)

# Compute the coefficient (11 + 2*sqrt(30))
coeff = 11 + 2 * sqrt_30

# Compute pi squared
pi_sq = mp.pi ** 2

# Multiply the coefficient by pi squared
numerator = coeff * pi_sq

# Divide by 32 to get the final result
result = numerator / 32

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))