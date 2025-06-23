import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π squared
pi_squared = mp.power(pi_value, 2)

# Divide by 4 to get the final result
result = pi_squared / 4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))