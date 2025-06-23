import mpmath as mp
mp.dps = 15

# Calculate pi constant using mpmath
pi_value = mp.pi

# Multiply by -3 to get the final result
result = -3 * pi_value

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))