import mpmath as mp
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Compute π^4
pi_power4 = pi_val**4

# Multiply by 7 to get the numerator
numerator = 7 * pi_power4

# Divide by 1440 to get the final result
result = numerator / 1440

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))