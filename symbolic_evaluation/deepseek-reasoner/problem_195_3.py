import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi divided by 2
pi_over_2 = pi_val / 2

# Subtract pi/2 from 2
result = 2 - pi_over_2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))