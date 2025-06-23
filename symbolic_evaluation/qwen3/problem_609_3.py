import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the value of pi using mpmath's constant
pi_value = mp.pi

# Compute pi divided by 2
half_pi = pi_value / 2

# Calculate the final result by subtracting half_pi from 1
result = 1 - half_pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))