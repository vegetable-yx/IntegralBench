import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi constant using mpmath
pi_value = mp.pi

# Compute the result as pi divided by 2
result = pi_value / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))