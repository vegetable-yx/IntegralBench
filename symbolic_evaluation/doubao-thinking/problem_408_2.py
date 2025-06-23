import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the natural logarithm of 5/3
log_term = mp.log(mp.mpf(5)/3)

# Calculate the constant fraction 2/5
fraction_part = mp.mpf(2)/5

# Combine the components and multiply by 1/8
result = (log_term - fraction_part) * mp.mpf(1)/8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))