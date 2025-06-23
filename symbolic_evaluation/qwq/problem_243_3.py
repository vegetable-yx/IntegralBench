import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi raised to the fourth power
pi_power4 = pi_val**4

# Divide by 128 to get the final result
result = pi_power4 / 128

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))