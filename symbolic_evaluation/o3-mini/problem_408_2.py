import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the natural logarithm of (5/3)
log_val = mp.log(mp.mpf(5)/mp.mpf(3))

# Calculate the constant 2/5
const_val = mp.mpf(2)/mp.mpf(5)

# Subtract the constant from the logarithm
diff = log_val - const_val

# Multiply the result by 1/8
result = diff / mp.mpf(8)

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))