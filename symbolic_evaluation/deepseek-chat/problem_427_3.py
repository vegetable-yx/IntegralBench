import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate sqrt(11)
sqrt_11 = mp.sqrt(11)

# Calculate sqrt(6)
sqrt_6 = mp.sqrt(6)

# Compute 45 * sqrt(11)
term1 = 45 * sqrt_11

# Compute 6 * sqrt(6)
term2 = 6 * sqrt_6

# Combine terms: (45*sqrt(11) - 6*sqrt(6)
numerator = term1 - term2

# Divide by 48 to get final result
result = numerator / 48

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))