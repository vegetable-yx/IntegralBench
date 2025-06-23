import mpmath as mp
mp.dps = 15

# Calculate pi^4 using mpmath's constant
pi_power = mp.pi ** 4

# Define the denominator
denominator = 1152

# Compute the final result by division
result = pi_power / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))