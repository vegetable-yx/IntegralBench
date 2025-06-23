import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Divide π squared by 6
divided = pi_squared / 6

# Subtract 1 to get final result
result = divided - 1

# Print result with 10 decimal places
print(mp.nstr(result, n=10))