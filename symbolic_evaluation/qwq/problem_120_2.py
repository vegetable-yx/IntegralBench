import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute pi squared
pi_squared = pi_val ** 2

# Square pi squared to get pi^4
pi_fourth = pi_squared ** 2

# Divide by 64 to get the final result
result = pi_fourth / 64

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))