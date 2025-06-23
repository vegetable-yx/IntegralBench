import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the natural logarithm of 2
log_val = mp.log(2)

# Negate the logarithm to get the result
result = -log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))