import mpmath as mp

# Set the internal decimal precision to 15 to ensure accuracy
mp.dps = 15

# The analytical expression is a simple fraction: 1/2
# Assign the exact value of 1/2 to the result variable
result = mp.mpf(1)/2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))