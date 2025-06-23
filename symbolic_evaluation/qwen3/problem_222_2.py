import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate 3 times pi using mpmath's constant
pi_value = mp.pi
result = 3 * pi_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))