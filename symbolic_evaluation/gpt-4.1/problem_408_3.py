import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the natural logarithm of (5/3)
log_val = mp.log(mp.mpf(5)/mp.mpf(3))

# Multiply by 1/8
term1 = mp.mpf(1)/mp.mpf(8) * log_val

# Calculate the constant term: 1/20
term2 = mp.mpf(1)/mp.mpf(20)

# Combine the terms: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))