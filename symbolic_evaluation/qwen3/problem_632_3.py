import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 2
ln_2 = mp.log(2)

# Compute the negative of ln(2)
result = -ln_2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))