import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Compute the argument for the second logarithm
inner_arg = (1 + sqrt5) / 2

# Calculate logarithm of the inner argument
log_inner = mp.log(inner_arg)

# Multiply sqrt5 with the computed logarithm
sqrt5_log_part = sqrt5 * log_inner

# Combine all terms in the numerator
numerator = -1 + 2*ln2 + sqrt5_log_part

# Divide by 4 to get the final result
result = numerator / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))