import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate components of the expression
sqrt5 = mp.sqrt(5)  # Compute square root of 5
log_argument = (1 + sqrt5)/2  # Calculate argument for logarithm
log_term = mp.log(log_argument)  # Compute natural logarithm
fraction_term = sqrt5/8  # Compute second part of the expression

# Combine components for final result
result = (3/4)*log_term - fraction_term

# Print result with 10 decimal places
print(mp.nstr(result, n=10))