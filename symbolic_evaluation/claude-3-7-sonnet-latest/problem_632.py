import mpmath as mp

# Set internal decimal places to 15 for precision
mp.dps = 15

# Calculate natural logarithm of 2
log_value = mp.log(2)

# Apply negative sign to the logarithm
result = -log_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))