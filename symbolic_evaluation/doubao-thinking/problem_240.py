import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the first term: (1/3) * ln(3 + 2√2)
sqrt2 = mp.sqrt(2)
log_arg = 3 + 2 * sqrt2  # Compute argument for logarithm
log_term = (1/3) * mp.log(log_arg)  # Compute logarithmic term

# Calculate the second term: π√2/8
pi_sqrt2 = mp.pi * sqrt2  # Multiply π by √2
pi_term = pi_sqrt2 / 8  # Divide by 8 to get the second term

# Combine both terms
result = log_term - pi_term

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))