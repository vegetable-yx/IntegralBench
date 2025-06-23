import mpmath as mp

# Set internal decimal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Compute the constant value: 1/2
result = mp.mpf(1) / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))