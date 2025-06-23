import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate natural logarithm of 2
log2 = mp.log(2)

# Square the logarithm value
log2_squared = log2 ** 2

# Multiply by 1/2 to get final result
result = 0.5 * log2_squared

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))