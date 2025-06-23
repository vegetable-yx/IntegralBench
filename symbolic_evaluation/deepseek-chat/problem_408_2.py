import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the natural logarithm of (5/3)
log_val = mp.log(mp.mpf(5)/mp.mpf(3))

# Calculate the constant fraction 2/5
fraction = mp.mpf(2)/mp.mpf(5)

# Subtract the fraction from the logarithm
difference = log_val - fraction

# Multiply by 1/8
result = difference / mp.mpf(8)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))