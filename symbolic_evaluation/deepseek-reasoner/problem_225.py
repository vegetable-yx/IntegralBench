import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π^4
pi_squared = mp.pi ** 2
pi_fourth = pi_squared ** 2

# Compute numerator (7 * π^4)
numerator = 7 * pi_fourth

# Divide by 120 to get final result
result = numerator / 120

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))