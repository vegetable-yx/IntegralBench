import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression
sqrt5 = mp.sqrt(5)  # Compute square root of 5
log_arg = (1 + sqrt5) / 2  # Calculate argument for logarithm
log_term = mp.log(log_arg)  # Compute natural logarithm
first_part = (3/2) * log_term  # Multiply by 3/2
second_part = sqrt5 / 4  # Compute sqrt(5)/4 term

# Combine components for final result
result = first_part - second_part

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))