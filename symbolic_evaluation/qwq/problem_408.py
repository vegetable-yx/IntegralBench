import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the natural logarithm of 5/3
log_term = mp.log(mp.mpf(5)/3)

# Calculate the constant term 2/5
constant_term = mp.mpf(2)/5

# Compute the difference between the logarithm term and the constant term
numerator = log_term - constant_term

# Divide the result by 8 to get the final value
result = numerator / 8

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))