import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate components of the expression step by step
sqrt5 = mp.sqrt(5)  # Compute square root of 5
log_arg = 2 + sqrt5  # Argument for the logarithm
log_term = mp.log(log_arg)  # Compute ln(2 + sqrt(5))
combined_terms = log_term + 1 - sqrt5  # Combine terms inside parentheses
result = (mp.pi/2) * combined_terms  # Multiply by pi/2

print(mp.nstr(result, n=10))