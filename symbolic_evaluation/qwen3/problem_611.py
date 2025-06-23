import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the first term: ln(2 + sqrt(3))
log_numerator = mp.log(2 + sqrt3)

# Compute the second term: ln(sqrt(3))
log_denominator = mp.log(sqrt3)

# Subtract the two results
result = log_numerator - log_denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))