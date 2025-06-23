import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Divide π squared by 6 to get the first term
term1 = pi_squared / 6

# Subtract 1 to obtain the final result
result = term1 - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))