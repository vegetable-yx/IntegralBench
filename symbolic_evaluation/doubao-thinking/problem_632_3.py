import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute natural logarithm of 2
log_val = mp.log(2)

# Apply negative sign to get the result
result = -log_val

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))