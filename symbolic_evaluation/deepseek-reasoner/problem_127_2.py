import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute mathematical constant e
e_value = mp.e

# Calculate 1/e
reciprocal_e = 1 / e_value

# Compute sum of e and its reciprocal
sum_e_reciprocal = e_value + reciprocal_e

# Subtract 2 from the sum
adjusted_sum = sum_e_reciprocal - 2

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply sqrt(2) with adjusted sum to get final result
result = sqrt2 * adjusted_sum

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))