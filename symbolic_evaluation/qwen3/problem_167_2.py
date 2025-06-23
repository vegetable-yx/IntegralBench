import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the coefficient (8π)/3
coefficient = mp.mpf(8)/3 * mp.pi

# Calculate the logarithm term ln(3)
log_term = mp.log(3)

# Multiply components to get final result
result = coefficient * log_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))