import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the natural logarithm of 2
log_argument = mp.mpf(2)
result = mp.log(log_argument)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))