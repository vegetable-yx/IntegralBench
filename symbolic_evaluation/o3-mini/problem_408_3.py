import mpmath as mp

# Set internal decimal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Compute the logarithm of 5/3
log_val = mp.log(mp.mpf(5)/mp.mpf(3))

# Compute the constant fraction 2/5
fraction = mp.mpf(2)/mp.mpf(5)

# Subtract the fraction from the logarithm
diff = log_val - fraction

# Multiply by 1/8
result = diff * mp.mpf(1)/mp.mpf(8)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))