import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi^4 using intermediate steps
pi_val = mp.pi
pi_squared = pi_val ** 2
pi_fourth = pi_squared ** 2

# Compute the final result by dividing by 144
denominator = 144
result = pi_fourth / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))