import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute frequently used constant: square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the argument for the first logarithm: 3 + 2*sqrt(2)
log_arg1 = 3 + 2 * sqrt2

# Calculate the argument for the second logarithm: 1 + sqrt(2)
log_arg2 = 1 + sqrt2

# Compute the natural logarithms using mp.log
log1 = mp.log(log_arg1)
log2 = mp.log(log_arg2)

# Calculate term2: (1/sqrt(2)) * ln(3 + 2*sqrt(2))
term2 = (1 / sqrt2) * log1

# Calculate term3: sqrt(2) * ln(1 + sqrt(2))
term3 = sqrt2 * log2

# Combine all terms: 3 - term2 - term3
result = 3 - term2 - term3

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))