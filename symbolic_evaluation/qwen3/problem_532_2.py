import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the pi value
result = pi_value ** 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))