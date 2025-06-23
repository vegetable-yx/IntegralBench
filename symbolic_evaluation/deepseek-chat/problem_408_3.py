import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the logarithm term: ln(5/3)
log_term = mp.log(mp.mpf(5)/mp.mpf(3))

# Calculate the constant fraction: 2/5
constant_term = mp.mpf(2)/mp.mpf(5)

# Compute the difference: ln(5/3) - 2/5
difference = log_term - constant_term

# Multiply by 1/8 to get the final result
result = difference * (mp.mpf(1)/mp.mpf(8))

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))