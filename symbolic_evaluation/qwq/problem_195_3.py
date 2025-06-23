import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the constant term
constant_term = mp.mpf(2)

# Calculate pi/2 with high precision
pi_half = mp.pi / 2

# Compute the final result
result = constant_term - pi_half

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))