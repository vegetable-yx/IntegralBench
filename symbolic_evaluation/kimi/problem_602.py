import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi^4
pi4 = mp.pi ** 4

# Divide by 120 to get the result
result = pi4 / 120

# Print result with 10 decimal places
print(mp.nstr(result, n=10))