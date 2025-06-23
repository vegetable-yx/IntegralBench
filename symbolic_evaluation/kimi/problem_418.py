import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Compute π²/6 term
term = pi_squared / 6

# Subtract 1 from the calculated term
result = term - 1

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))