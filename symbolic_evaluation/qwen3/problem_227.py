import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi raised to the 5th power
pi_power = mp.power(pi_val, 5)

# Calculate the denominator
denominator = 1440

# Compute the final result
result = pi_power / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))