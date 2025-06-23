import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the value of pi using mpmath's constant
pi_value = mp.pi

# Compute π divided by 2
pi_over_two = pi_value / 2

# Calculate the final result by subtracting π/2 from 1
result = 1 - pi_over_two

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))