import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi divided by 2
pi_over_2 = mp.pi / 2

# Compute the final result by subtracting pi/2 from 1
result = 1 - pi_over_2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))