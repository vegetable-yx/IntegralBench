import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Square the pi value
pi_squared = mp.power(pi_val, 2)

# Divide by 2 to get the final result
result = mp.fdiv(pi_squared, 2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))