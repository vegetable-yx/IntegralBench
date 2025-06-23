import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi^(5/2)
pi_power = mp.pi ** (5/2)

# Compute the denominator: 27 * pi^(5/2)
denominator = 27 * pi_power

# Calculate the final result: 8192 / denominator
result = 8192 / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))