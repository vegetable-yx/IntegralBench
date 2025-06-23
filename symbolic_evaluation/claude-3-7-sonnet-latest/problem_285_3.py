import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi cubed
pi_val = mp.pi
pi_cubed = pi_val ** 3

# Define the denominator
denominator = 48

# Compute the final result: π³/48
result = pi_cubed / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))