import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Cube the value of pi
pi_cubed = pi_value ** 3

# Divide the cubed pi by 192 to get the final result
result = pi_cubed / 192

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))