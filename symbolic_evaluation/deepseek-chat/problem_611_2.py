import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the expression: ln(2 + sqrt(3))
log_num = mp.log(2 + sqrt3)

# Compute the expression: ln(sqrt(3)) = ln(3)/2
log_denom = mp.log(sqrt3)

# Subtract the two logarithms
result = log_num - log_denom

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))