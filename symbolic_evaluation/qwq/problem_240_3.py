import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the logarithmic part: ln(6 / (3 + 2*sqrt(2)))
sqrt2 = mp.sqrt(2)
denominator = 3 + 2 * sqrt2  # Calculate denominator 3 + 2√2
log_argument = 6 / denominator  # Compute argument for logarithm
log_part = mp.log(log_argument)  # Calculate natural logarithm

# Compute the algebraic part: (sqrt(10) + 3)/2
sqrt10 = mp.sqrt(10)
numerator = sqrt10 + 3  # Calculate numerator sqrt(10) + 3
fraction_part = numerator / 2  # Divide by 2

# Combine both parts for final result
result = log_part - fraction_part

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))