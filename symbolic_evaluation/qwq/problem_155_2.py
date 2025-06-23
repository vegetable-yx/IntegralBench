import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Square the pi value
pi_squared = mp.power(pi_val, 2)

# Divide by 16 to get the final result
result = mp.fdiv(pi_squared, 16)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))