import mpmath as mp
mp.dps = 15

# Calculate π using mpmath's high-precision constant
pi_val = mp.pi

# Compute π^4
pi_power4 = pi_val ** 4

# Multiply by 3 to get the numerator
numerator = 3 * pi_power4

# Divide by 256 to get the final result
result = numerator / 256

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))