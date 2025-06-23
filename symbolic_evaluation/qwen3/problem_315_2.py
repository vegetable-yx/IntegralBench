import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^4
pi_val = mp.pi
pi_squared = pi_val ** 2
pi_fourth = pi_squared ** 2

# Compute the denominator 1440
denominator = 1440

# Calculate the final result: -pi^4 / 1440
result = -pi_fourth / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))