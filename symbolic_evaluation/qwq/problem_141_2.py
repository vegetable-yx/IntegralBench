import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sinh(1)
sinh_1 = mp.sinh(1)

# Square the hyperbolic sine value
result = sinh_1 ** 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))