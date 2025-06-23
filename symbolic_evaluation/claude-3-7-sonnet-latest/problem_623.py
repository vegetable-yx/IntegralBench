import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the natural logarithm of 3/2
log_val = mp.log(mp.mpf(3)/2)

# Multiply by pi to get the final result
result = mp.pi * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))