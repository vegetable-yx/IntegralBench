import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Compute the value of the analytical expression: 1/2
result = mp.mpf(1) / mp.mpf(2)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))