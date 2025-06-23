import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Calculate the term π²/6
term1 = pi_squared / 6

# Subtract 1 to get the final result
result = term1 - 1

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))