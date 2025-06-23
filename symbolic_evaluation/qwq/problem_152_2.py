import mpmath as mp
mp.dps = 15

# Calculate pi constant using mpmath's high-precision value
pi_value = mp.pi

# Compute the result as pi divided by 2
result = pi_value / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))