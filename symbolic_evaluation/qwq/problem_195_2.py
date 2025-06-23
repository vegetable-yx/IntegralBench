import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi/2 using mpmath's constant
pi_half = mp.pi / 2

# Compute the final result by subtracting pi/2 from 2
result = 2 - pi_half

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))