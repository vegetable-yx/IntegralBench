import mpmath as mp

# Set internal decimal precision to 15 to ensure 10 decimal places in output
mp.dps = 15

# Compute the fraction 5/6
result = mp.mpf(5) / mp.mpf(6)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))